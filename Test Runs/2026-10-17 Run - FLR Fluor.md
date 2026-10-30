# Company Run — Fluor Corporation (NYSE: FLR) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run, unattended overnight cycle of 2026-10-17, under the canonical brief `Screens/_daily/_dispatch_brief.md`
with its one stated departure: the lines of evidence were derived by the analyst from the FY2025 10-K (Items 1, 1A and 7), not
written by the dispatcher. The lines chosen are listed under STEP 0. Working folder: `Test Runs/_research 2026-10-17 FLR/`
(scripts and their outputs tracked; raw filings in the gitignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (58466b23): `PORTFOLIO.md` read for this ticker only; not held.*

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $46.95 (close 2026-10-16, as printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $.01 par, **133,741,067** shares as of 2026-07-31
  (10-Q for the quarter to 2026-06-30, filed 2026-08-07, accession `0001124198-26-000071`; `python Screens/cover_shares.py FLR`).
  Check against issued less treasury: the 10-Q balance sheet gives 135,564,463 shares "issued and outstanding" at 2026-06-30;
  repurchased shares are cancelled, so there is no treasury count (10-Q, same accession; the FY2025 10-K says the repurchased shares
  were "repurchased and canceled"). The gap of 1.8 million shares between 2026-06-30 and 2026-07-31 is consistent with the stated
  programme ("still targeting $1.4 billion" of repurchases for 2026, Exhibit 99.1 to the 8-K of 2026-08-07, accession
  `0001124198-26-000074`). No 8-K or prospectus after the 10-Q changes the count (submissions list read 2026-10-17: the last filings
  are that 8-K and the 10-Q). **For the per-share arithmetic below the 2026-06-30 count is used, because net cash is taken at that
  date; the cover count is shown beside it.**
- **Market cap:** $6,279M at the cover count; $6,365M at the 2026-06-30 count.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16 (issuing authority,
  as fetched by `tools/run.py` through `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-17, accession `0001124198-26-000007` (Items 1, 1A, 3, 5, 7, 7A; notes on contingencies, contract assets,
    RUPO); 10-K/A filed 2026-03-02, accession `0001124198-26-000025` (adds NuScale's statements under Rule 3-09; nothing else changed).
  - 10-Q for the quarter to 2026-06-30, filed 2026-08-07, accession `0001124198-26-000071` (statements, liquidity, contingencies,
    subsequent events).
  - Proxy (DEF 14A) filed 2026-03-12, accession `0001104659-26-027053` (pay design, incentive definitions, summary compensation table).
  - 8-Ks: 2026-04-23, accession `0001124198-26-000051` (NuScale sale completed); 2026-08-07, accession `0001124198-26-000074`, Exhibit
    99.1 (second-quarter release, guidance).
  - The cycle: 10-Ks FY2019 (filed 2020-09-25 after an NT 10-K, accession `0001628280-20-013900`), FY2020 (`0001628280-21-003360`),
    FY2021 (`0001628280-22-003231`), FY2022 (`0001628280-23-004139`), FY2023 (`0001628280-24-005451`), FY2024 (`0001628280-25-005924`);
    and the SEC company-facts transcription of the 10-K figures 2015 to 2025 (accessions printed in the research folder's outputs).
  - NuScale Power's own filed operating cash flow 2021 to 2024 (company facts, CIK 1822966; 10-K accession `0001822966-23-000059`
    for 2021 and 2022, `0001822966-24-000039` for 2023, 10-Q `0001822966-24-000144` for the nine months of 2024).
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 of $(387)M, printed by `tools/run.py` from the
  XBRL, equals the "OPERATING CASH FLOW" line of the cash-flow table in Item 7 of the FY2025 10-K (`0001124198-26-000007`); and
  shareholders' equity at 2025-12-31 of $3,244M (XBRL) equals the December 31, 2025 column of the 10-Q balance sheet
  (`0001124198-26-000071`).
- `python tools/run.py FLR` **arithmetic lines only** (Part VII): OCF 2023/2024/2025 = 212 / 828 / (387); SBC 48 / 31 / 30; capex
  106 / 164 / 50; D&A 74 / 73 / 68; distributions to minority partners 53 / 14 / 64 (financing section, flagged by the tool as an
  alternate, used below as a real cost); ten balance-sheet year-ends 2019 to 2025. The tool's three-year means and yields are not used:
  the window and the recasting are Q7's (below), and its printed rules, ids and floor are v4 material and are ignored.
- **The lines of evidence chosen (the brief's departure), and where from.** From Item 1: the three segments and their markets; the
  contract mix (81% of backlog reimbursable at 2025-12-31); the named competitors; customer concentration (U.S. government 17% of
  2025 revenue, one Urban Solutions customer 15%). From Item 1A: cyclicality and dependence on new awards; lump-sum overrun risk;
  "Intense competition"; client payment risk; joint-venture partner risk; the credit facility's collateral trigger; litigation and
  claims. From Item 7: segment revenue, profit and margin 2023 to 2025; awards and backlog; the Santos judgment; NuScale's
  deconsolidation and sale; Stork's divestiture; cash flow, buybacks, debt, letters of credit and guarantees. The standing lines
  are covered as follows: segments and margins over the cycle (2019 to 2025 from four 10-Ks, consolidated 2015 to 2025);
  customers and suppliers (Item 1, 1A); pricing through the last inflation (Item 1A and MD&A on lump-sum cost growth, 2022 to 2025);
  acquisitions and divestitures and their goodwill (Stork bought 2016, goodwill $532M at 2016-12-31, sold 2024 to 2025; AMECO sold;
  NuScale sold); debt and leases (2029 converts, 2028 notes, credit facility; leases not read, see "What I could not get"); buybacks
  and their prices; stock pay; litigation and investigations (2019 to 2023 SEC and DOJ, restatement, class actions old and new).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own Fluor "if the market closed for five years" **[M1997-109]**, which
for a contractor means owning the stream of fees and the stream of claims that its backlog throws off, not the quotation. "the market is there to serve you and not to instruct you"
**[M2006-077]**: the price has moved with NuScale (a fair-value gain of $2,221M booked in 2024 and the
stake sold for about $2.43 billion, 8-K `0001124198-26-000051`), and none of that tells what the contracting business earns. Who is paid
to tell you: "you do not get impartial advice from Wall Street" **[M2020-037]**, and the company features "Adjusted EBITDA" and "adjusted EPS" in its release headline and gives guidance on
the first (Exhibit 99.1, `0001124198-26-000074`), so the reading starts from the GAAP and cash statements. The analyst's habit: look
for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) FY2025 revenue was cut by
a $643M reversal for the Santos judgment on a project completed in 2015, and the class of legacy claims is recurring (Sadara, Barrick,
NTTA, Kuwait; FY2023 and FY2025 10-Ks); (2) the FY2019 10-K was filed seven months late with a restatement of 2016 to 2018 and
material weaknesses, one of them that "Former leaders of our Energy & Chemicals segment caused pressure to be applied on the
individuals charged with accounting and finance responsibilities in a manner intended to present overly optimistic forecasts"
(FY2019 10-K, `0001628280-20-013900`); (3) the SEC settled with a $15M civil penalty in September 2023 (FY2023 10-K,
`0001628280-24-005451`); (4) the company's own competition risk factor reports "a continuing influx of non-traditional competitors
offering below-market pricing while accepting greater risk" (FY2025 10-K); (5) new awards fell from $19,528M (2023) to $15,123M (2024)
to $11,956M (2025) and backlog from $28,484M to $25,536M (FY2025 10-K). For the business: 81% of backlog is reimbursable, and the
balance sheet now holds net cash.

## THE STANDING RULE
Owning a part-interest in Fluor bought for cash, unlevered and sized so that a total loss could be borne, puts the buyer at no risk of
ruin; the rule binds the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**,
and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this run sizes or finances a purchase.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; the product may stay opaque so long as one understands "the economic dynamics of the
  industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **What Fluor sells, from Item 1 (FY2025 10-K, `0001124198-26-000007`).** Engineering, procurement, construction and project
  management, and operations and maintenance, sold to clients' capital programmes in three segments: Urban Solutions (advanced
  technologies and manufacturing including data centers and semiconductors, life sciences, mining and metals, infrastructure, staffing,
  plant services); Energy Solutions (oil and gas, fuels, chemicals, LNG, power); Mission Solutions (DOE and NNSA site management and
  remediation, military logistics, FEMA). Two contract types: reimbursable, where "the client reimburses us based upon negotiated rates
  and fees", and lump-sum or guaranteed maximum, where the firm must "predetermine the work to be performed, the project execution
  schedule and all costs associated with the work based on incomplete information". 81% of 2025 year-end backlog was reimbursable.
  Revenue is recognised on the cost-to-cost percentage of completion with estimate changes taken on a "cumulative catch-up basis".
- **The key variables, and whether they are foreseeable**: "trying to identify the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**. Two decide the economics: (1) the volume of awards, which
  follows clients' capital spending, "The award and timing of projects is unpredictable and driven by our clients" (Item 1A); (2) the
  margin kept between the price or fee and the cost of execution, which the filer calls exposed to "Evolving estimates related to
  productivity, scheduling estimates or future economic conditions" (Item 1A) and which has been cut, year after year, by
  project charges and old claims (Santos 2025; infrastructure cost growth 2022, 2023, 2025; the 2019 charges and restatement).
  Neither is predictable year to year. The economics that both produce are foreseeable in kind: a contractor with little fixed capital,
  paid fees on other people's capital programmes, competing against a long list of rivals the 10-K names, earning thin margins that
  are periodically wiped out by execution losses and claims. That is a fix on the "competitive position" and on the shape of the
  "earning power" **[M2012-065]**, even though the level in any year is not foreseeable.
- **Do the past statements tell me the future ones?** "the financial statements will tell me the information that’s useful to me in
  making a judgment about what the future financial statements are going to look like" **[M2008-033]**. For the shape, yes: ten years of filings show margins between
  -5.4% and 2.8% of revenue on the operating line (company facts, 2017 to 2025) and the same causes of loss recurring; for the
  level, no. The accounts themselves are construction-in-progress accounts, of which the rows say "anything where you’ve got construction in progress or
  progress payment-type things — there’s so many ways you can cheat in accounting" **[M2013-086]**; that is carried to Q4.
- **Routing.** Not a fast-technology business; not a bank; not a holding company. The parts (three segments) are each contracting
  businesses of the same economic kind; the by-parts reading belongs to Q2.
- **Contrary evidence on this question, written down** ("write it down in the first 30 minutes" **[M1997-127]**): the doubt row says "if you have doubts about something being
  into your circle of competence, it isn’t" **[M2002-092]**, and of the level of earnings the row says "If something is not very predictable, forget it." **[M1998-044]**. The analyst's
  reading: the doubt is about how much the business will earn, not about whether its economic dynamics can be understood; what can be
  foreseen is that it will remain a bidder among many on clients' projects, and whether that position protects any return is the
  castle question, which the framework asks at Q2. This placement is recorded as unclear under "What in the framework was wrong or
  unclear".
- **VERDICT: IN.** The economic dynamics of an EPC contractor can be understood from the filings, "I understand the economic dynamics of the industry" **[M2011-014]**, and the
  competitive position and the shape of the earning power can be fixed, "what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the unpredictability of the yearly level is
  carried to Q2 and Q7.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now" **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (business of parts, Q2 CONVENTION: a part decides at more than half of five-year operating profit, else the largest).
Segment profit as filed, latest vintage, USD millions (2021 and 2022 from the FY2023 10-K `0001628280-24-005451`, restated there for the
move of Plant & Facility Services into Urban Solutions; 2023 to 2025 from the FY2025 10-K `0001124198-26-000007`):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share of the three | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Urban Solutions | 41 | 17 | 268 | 304 | 205 | 835 | 36.9% | EPC and staffing in life sciences, advanced manufacturing, mining, infrastructure | **yes (largest)** |
| Energy Solutions | 250 | 301 | 381 | 256 | (414) | 774 | 34.2% | EPC in oil and gas, chemicals, LNG, power | read as well (see note) |
| Mission Solutions | 155 | 136 | 116 | 153 | 94 | 654 | 28.9% | DOE/NNSA site management and remediation, military logistics, FEMA | no |
| Other (NuScale to Oct 2024, Stork, AMECO) | (31) | (27) | (228) | (78) | 6 | (358) | n/a | divested or sold | no |

No part carries more than half; the largest, Urban Solutions, decides. Note: Energy Solutions' 2025 figure carries the $643M Santos
reversal; with it excluded Energy would be the largest part (1,417). The Santos judgment is a real cost of the Energy business (a court
judgment on its own 2015 work), so the filed figure stands; but both parts are EPC contracting on clients' capital programmes and the
castle tests below are read for both, so the close does not turn on which of the two decides.

**The castle tests, each with its filing fact (FY2025 10-K `0001124198-26-000007` unless stated).**
1. *Key factors*: "What are the key factors? And how permanent are they?" **[M1995-038]**. The filer's own list of strengths is safety, a global execution platform,
   "Excellence in Execution", market diversity, client relationships, risk management, sustainability. Each is a claim every named
   rival can make; none is a reason the client must come to Fluor rather than to the next bidder, and the results below do not show
   any of them protecting a return.
2. *Would it stand without the lord?* The margin on each job depends on estimating and executing that job: "we may not be able to
   recover cost overruns, which may cause us to lose money" (Item 1). This is the business where "you have to stay smart"
   **[M1995-040]**; "the poor business is one that can only succeed, or even survive, with great management" **[M1996-037]**. The
   2019 charges, the restatement of 2016 to 2018, and the infrastructure cost growth of 2022, 2023 and 2025 are the record of what
   happens when execution slips.
3. *The money test*: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]**. The filer answers it: "We have seen a continuing influx of non-traditional competitors offering
   below-market pricing while accepting greater risk. Competition places downward pressure on our contract prices and profit margins"
   (Item 1A). Attackers with money are already entering. These are the industries "that are just never going to have barriers to
   entry" **[M2012-106]**; and "one competitor is frequently enough to ruin a business" **[M2012-108]**.
4. *Pricing power through the last inflation*: "the agony they go through in determining whether a price increase can be sustained"
   **[M2005-020]**; "the businesses with strong competitive positions manage to pass through increases in raw material costs" **[M2005-017]**. On lump-sum work Fluor carried the cost rises:
   2025 "cost growth on 3 infrastructure projects for subcontracted design errors, price escalation and schedule impacts"; $255M of
   backlog in "legacy projects in a loss position" with about $212M of "estimated unfunded losses" at 2025-12-31 ($702M and $237M a year
   earlier). The response has been to move risk to the client (81% reimbursable), not to raise price; some inflation was recovered by
   contract term ("inflation-adjusted variable consideration on certain downstream projects", FY2023 10-K). A business that passes cost
   through only where the contract already says so shows no pricing power of its own.
5. *Unit volume*: "we want a lot more unit cases sold" **[M1999-054]**; read here as awards and backlog: total new awards $19,528M (2023), $15,123M (2024), $11,956M (2025);
   Energy Solutions awards $6,871M, $3,246M, $1,421M; backlog from $28,484M to $25,536M during 2025.
6. *The low-cost position*: "being the low-cost producer is all-important" **[L2000-017]**. In a field where "the low-cost producer can put you out of business"
   **[M1997-010]**, Fluor's operating margin is the lowest of the four filers compared in 8 of the 9 years 2017 to 2025 (competitor row
   below). Margin on revenue is not cost per unit, but in a field selling the same hours and the same procurement on the same bids, the
   firm that keeps least of each revenue dollar over nine years is not the low-cost operator. "The figures are available."
   **[M2009-059]**.
7. *The brand in the customer's mind*. The filer says awards are lost on "price, a client's perception of our ability to perform and/or
   perceived technology advantages held by others" (Item 1A). Reputation lets it bid; nothing in the filings shows clients asking for
   Fluor by name at a higher price.
8. *Would the customer still choose it over the low bid?* "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. On lump-sum work, "we may not be selected for the work if
   our bid is higher than the competition" (Item 1); on government task orders, "We face rigorous competition and significant pricing
   pressures in order to win these task orders" (Item 1A); on reimbursable work the fee is "negotiated". The customer buys on the bid,
   the condition the row describes in its own field: "price competition in insurance is usually fierce" **[L2004-003]**.
9. *Ask the competitors*: "which one would it be and why?" **[M1999-130]**. Not done: no interviews are on the public record. The rivals' filings are read instead (row
   below).
10. *Widening or narrowing*: "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Narrowing on the filed evidence: awards and backlog falling (test 5); the business has been
    shrunk by sales (AMECO, Stork, the Mexico joint venture sold in July 2026 for $175M, 10-Q `0001124198-26-000071`); revenue went
    from $19,037M (2016) to $15,503M (2025), and about $8 billion of the 2025 figure was "at-cost revenue" (53% of revenue) carried
    "without meaningful markup" (Item 7).
11. *What could destroy it*: "destroy, or modify, or reduce the economic strengths" **[M2000-014]**. One court judgment on a project finished ten years earlier took $643M of revenue and
    $642M of cash in 2025 (Santos: the contract's liability cap of about AUD 236M was found not to apply); performance guarantees are
    "estimated to be $14 billion" (Item 7).

**The competitor row.** The 10-K names, among others, AECOM, Amentum, Bechtel, Black & Veatch, Burns & McDonnell, BWXT, EMCOR,
Jacobs, KBR, Kiewit, Parsons, Turner, V2X and Zachry, and abroad ACS, Balfour Beatty, Chiyoda, Exyte, Hatch, JGC, Petrofac,
AtkinsRéalis, Technip Energies, Wood and Worley. **Named rivals that do not file with the SEC (flagged):** Bechtel, Black & Veatch,
Burns & McDonnell, Kiewit, Turner, Zachry (private) and the eleven international companies. **Chosen, three named SEC filers:** KBR,
Jacobs and AECOM, the named filers whose work spans, as Fluor's does, energy and chemicals engineering, infrastructure and government
programmes (the choice among named filers is the analyst's). Same metric, operating income over revenue, from each filer's 10-K figures
as transcribed in SEC company facts (latest vintage; fiscal years end in September for Jacobs and AECOM; KBR's 2024 and 2025 years end
on 2025-01-03 and 2026-01-02); **XBRL transcription, not checked line by line against the rivals' statements**:

| FY | FLR | KBR | Jacobs | AECOM |
|---|---|---|---|---|
| 2017 | 1.4% | 6.3% | 2.4% | 3.6% |
| 2018 | 2.7% | 9.5% | 2.6% | 2.8% |
| 2019 | -5.4% | 6.4% | 3.2% | 2.9% |
| 2020 | -1.5% | 1.0% | 4.0% | 2.9% |
| 2021 | -1.9% | 3.1% | 4.9% | 4.7% |
| 2022 | 1.5% | 5.2% | 5.5% | 4.9% |
| 2023 | 0.9% | 6.5% | 6.2% | 2.3% |
| 2024 | 2.8% | 8.5% | 6.0% | 5.1% |
| 2025 | -2.4% | 10.0% | 7.2% | 6.4% |
| **nine years, aggregate** | **-0.1%** | **6.4%** | **4.6%** | **4.0%** |

Accessions: FLR `0001628280-20-013900` to `0001124198-26-000007`; KBR `0001357615-20-000034` to `0001357615-26-000051`; Jacobs
`0000052988-19-000069` to `0001628280-25-053316`; AECOM `0001104659-19-063367` to `0000868857-25-000013` (full lists in
`comp_summary_output.txt`). Fluor is lowest in every year but 2018.

**The field's returns over the last full cycle, judged in words** (Q2 CONVENTION: no figure). The three rivals earned modest single-digit
margins on revenue over the nine years; whether those protect excellent returns on their tangible capital is not settled here (their
equity is largely purchased goodwill). Fluor's own return over the same span is the finding: nine years of operating income summing to
less than nothing on about $140 billion of revenue, and net earnings attributable to Fluor over 2016 to 2025 of $589M in total, which
becomes a loss of about $1,442M once the NuScale gains of 2024 ($1,729M after tax) and 2025 ($302M after tax) are removed (MD&A
tables, FY2025 10-K; company facts). Equity fell from $3,125M (2016) to $1,030M (2020) and was rebuilt only by the NuScale mark (see
AFTER THE STOP, Q4).

**Mission Solutions (not deciding).** The filer claims "a tier 1 position" at DOE and NNSA; its margins were 2.9% to 5.9% (2020 to
2025) and its government work is re-competed, with funding that "may even be eliminated" (Item 1A). As a non-deciding part it would be
carried at no growth; it is inside the whole-company computation below.

- **A castle shown open on the evidence closes OUT.** The deciding part, and Energy Solutions with it, sells on the bid in a field the
  filer itself describes as entered by competitors "offering below-market pricing", with "downward pressure on our contract prices and
  profit margins"; it is not the low-cost operator, keeping the least of each revenue dollar among the four filers compared in eight of
  nine years; it shows no pricing power through the last inflation; and its volume is falling. The rows rule out the business whose customers
  do not care from whom they buy, "most insureds don't care from whom they buy" **[L2004-003]**, the high-cost producer in a commodity
  field, "a company must lower its costs to competitive levels or face extinction" **[L1994-035]**, and the business whose rival sets its price, "whatever he
  charged for gas was my price" **[M2012-109]**. A price cannot reopen it: "What you can’t do is turn any investment into a good deal by
  paying little" **[M2019-015]**.
- **VERDICT: OUT.** The castle is open on the filed evidence; "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
  No moat protects any return, let alone "excellent returns on invested capital" **[L2007-004]**. The file closes here. Q3 to Q12:
  NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 and are written under AFTER THE STOP, Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP, Q5; any later run that reaches Q5 must answer them.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, Q6 (the buyback prices against the computed range are written there as facts, not weighed).

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**, as Part VII
(The owner's price) asks of a file closed before Q7.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, Q9.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business on the rows' named list is carried on: the businesses are engineering, construction, government site
management and staffing.)

---
## COMPUTATION, NOT A CLEARANCE
*Operator rule 3: valuation arithmetic after a closing STOP. It carries no entry language, decides nothing, and does not reopen Q2. The
reporting figures are the owner's (a reporting convention, not a rule). Scripts and outputs: `owner_cash.py`, `owner_cash_output.txt`,
`value.py`, `value_output.txt` in the research folder. Note for the self-audit: these scripts were run while the filings were being
gathered, before the Q2 section was written; their outputs were headed as computation and did not enter the Q2 reasoning.*

**Owner cash after every real cost** (operator rule 5; never a net-income proxy), USD millions, from the filed cash-flow statements:
operating cash flow, less capital spending, less stock pay (a real cost added back inside OCF), less distributions paid to minority
partners (cash that leaves Fluor's owners). Two recastings, both stated:
- **NuScale removed (core).** NuScale was consolidated until October 2024 and its own operating cash outflow sat inside Fluor's OCF:
  $(99)M 2021, $(149)M 2022, $(183)M 2023, $(82)M nine months of 2024 (NuScale's filings, accessions in Step 0). NuScale was an
  investment, sold for about $2.43 billion (8-K `0001124198-26-000051`) whose proceeds are in today's net cash; its burn is added back
  so that it is not charged twice. NuScale's stock pay inside Fluor's consolidated figure was not separated (small; see What I could
  not get).
- **All-equity basis (central, Q7 On what the floor is earned).** Net interest income is removed after tax so that the cash earning it
  is counted once, in net debt. **CONVENTION of this run:** the US statutory rate of 21% is applied to net interest; rationale: the
  company's effective rate swung from 39% to 103% on items unrelated to interest, and no filing states the tax on the interest line.

| year | OCF | owner cash, literal | core | core, all-equity | core, all-equity, Santos added back | OC / revenue (core, all-equity) |
|---|---|---|---|---|---|---|
| 2016 | 706 | 372 | 372 | 414 | 414 | 2.17% |
| 2017 | 602 | 231 | 231 | 263 | 263 | 1.77% |
| 2018 | 162 | (155) | (155) | (123) | (123) | -0.65% |
| 2019 | 219 | (32) | (32) | (23) | (23) | -0.15% |
| 2020 | 186 | 28 | 28 | 64 | 64 | 0.41% |
| 2021 | 25 | (191) | (92) | (34) | (34) | -0.24% |
| 2022 | 31 | (123) | 26 | (2) | (2) | -0.01% |
| 2023 | 212 | 5 | 188 | 56 | 56 | 0.36% |
| 2024 | 828 | 619 | 701 | 583 | 583 | 3.57% |
| 2025 | (387) | (531) | (531) | (584) | 58 | -3.77% |

Means, core, all-equity: **literal window 2021 to 2025: $3.6M**; ten years 2016 to 2025: **$61.3M**; the cycle 2017 to 2024 (the year
after the 2016 high to the 2024 high): $97.9M; the window with the Santos payment added back: $132.0M. With net joint-venture funding
deducted as well (investments less returns of capital; $256M in 2025, of which $158M funded "a proportionately consolidated loss
project", FY2025 10-K), the window mean is $(87.2)M.

**Q7's range convention applied in full.**
- *The PG four.* Growth measured on aggregate owner cash, not per share; all capital spending deducted (the depreciation variant: capex
  ran below D&A in 2023 to 2025, $106M/$74M, $164M/$73M, $50M/$68M per `tools/run.py`, so the variant changes little); zero nominal
  growth after year ten; a price above the top of the range closes OUT through the floor.
- *(a) Cycles.* The last year of the window, 2025, is aberrational on the filer's own description: results "significantly impacted by a
  judgment on the long completed Santos project" (FY2025 10-K, Item 7). The base is therefore taken over the full cycle. **CONVENTION of
  this run:** the ten years 2016 to 2025 are the cycle base (central); rationale: the owner-cash series runs from a high (2016) through a
  trough (2018 to 2022) to a high (2024) and a new low (2025), and the ten years hold the whole swing without choosing which loss year
  to leave out; the 2017 to 2024 high-to-high span and the literal window are shown beside it.
- *(b) Decline.* The owner-cash series changes sign repeatedly, so its compound rate between end years is meaningless; between the first
  and second halves of the ten years it falls from $119M to $3.6M a year, a rate (about -50% a year) that is also meaningless on a
  series that crosses zero. By (b) the range would then be the no-growth case alone. **CONVENTION of this run:** the decline is carried
  as the bottom at the business's own sales growth, -2.26% a year (revenue $19,037M in 2016 to $15,503M in 2025, company facts);
  rationale: the business is shrinking on the filed record, (b) says a decline makes the bottom, and sales is the nearest filed series
  that does not cross zero.
- *(c) Acquisitions.* None in the window. Businesses sold (AMECO, Stork, the China fabrication yard, the Mexico joint venture) are not
  credited as owner cash: **CONVENTION of this run**, rationale: (c) nets sales against purchases, and with no purchases a sale is a
  shrinking of the business, not a cash yield; their cash is inside net cash. No signed, unclosed deal at the price date (the China yard
  sale closed in 2026 with a $124M gain, 10-Q). Not a serial acquirer.
- *(d) Working capital* is inside OCF and so counted; the 2025 working-capital release on "several large projects" is part of that
  year's figure.
- *(e) Growth spending.* The filings do not separate maintenance from growth capital spending (2025 capex "primarily related to
  investments in IT", 2024 "improvements to our new office lease in Houston"); the all-spending case is therefore central, said so.
- *(f) The cap.* Not engaged: the growth carried is negative. The highest share of revenue earned as owner cash in the years read was
  3.57% (2024).
- *Tax.* Owner cash is after the company's own tax as paid (inside OCF). No carryforward or credit that runs out inside ten years was
  priced (the effective rate was above statutory in each of 2023 to 2025, 75%, 103% and 39%, FY2025 10-K); not applicable.
- *Net debt* (all-equity basis, latest filed balance sheet 2026-06-30, 10-Q `0001124198-26-000071`): cash $2,923M plus marketable
  securities $120M less long-term debt $1,072M, plus the subsequent event the 10-Q itself states, the July 2026 sale of the Mexico
  joint venture for $175M less the $33M tax funded in August 2026: **net cash $2,113M** ($15.59 a share). Operating leases left out, and
  said so. Of the cash, $320M and $26M of securities relate to consolidated VIEs and are "not available for our general operations";
  excluding them, net cash would be $1,767M (shown, not used).

**The floor, tested first** (Q7 CONVENTION of 2026-10-10). Enterprise value at the price: $46.95 x 135.564M shares = $6,365M, less net
cash $2,113M = **$4,252M**. To earn about ten percent at no growth, owner cash before interest would need to be about $425M a year; to be
worth the price even at the 5.43% sovereign, about $231M. The cases: ten-year base $61.3M (1.44% on EV), cycle 2017 to 2024 $97.9M
(2.30%), window with Santos added back $132.0M (3.10%), literal window $3.6M (0.08%); with any growth case lower still. **No case in the
range earns the floor at the price.** Had Q7 been reached it would have closed OUT on the floor; the width test does not arise.

**(a) THE VALUE RANGE** (Q7's construction; central figure on the all-equity basis, net cash added back per share, 135.564M shares at
2026-06-30): **$22.55 to $23.91 a share, against a price of $46.95.** Bottom: the ten-year base declining at the sales rate for ten years,
then flat, at 5.43%. Top: the ten-year base at no growth. Beside it: the literal window, $16.00 to $16.08; the 2017 to 2024 cycle base,
$26.70 to $28.89; the window with the Santos payment added back, $30.57 to $33.52. At the cover count (133.741M) the central range would
be $22.86 to $24.24. The price sits above the top of every case.

**(b) THE FAIR PRICE** (Part VII: each end case valued at ten percent instead of the sovereign, the two averaged), after the company's own
tax, no conversion: **$19.79 a share on the all-equity basis (central)** (no-growth end $20.11, decline end $19.47). **Equity-only figure,
beside: $5.05 a share** (owner cash after interest, ten-year core mean $73.6M, valued at ten percent: no-growth $5.43, decline $4.67;
no net cash added, because the cash's interest is inside that owner-cash figure). The equity-only figure values $3.0 billion of cash and
securities only through its after-tax interest income capitalised at ten percent, which is why it is far below the central figure; it
never decides alone (Q7, On what the floor is earned). Beside the central figure: on the 2017 to 2024 cycle base, $22.30; on the window
with Santos added back, $24.64; on the literal window, $15.83. No other price figure is reported.

---
## THE BOX
**OUT, at Q2 (the castle is open on the filed evidence), integrity facts recorded, not judged.** Computed beneath the stop, not a
clearance: value range $22.55 to $23.91 a share (all-equity, ten-year cycle base) against $46.95; no case earns the floor; fair price
$19.79 (all-equity), $5.05 equity-only beside. Q11 belongs to the holding review, not to a purchase run.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source ("write it down in the first 30 minutes" **[M1997-127]**); written down, not weighed; no verdict; the box
unchanged (operator rule 2).*

**Q3 (capital).** Capital spending $50M to $283M a year over 2016 to 2025 on revenue of $13.7 billion to $19.0 billion; PP&E $446M at
2026-06-30. Working capital: accounts receivable $1,027M and contract assets $1,440M against accounts payable $1,762M and contract
liabilities $541M at 2026-06-30 (10-Q); client advances only $14M at 2025-12-31 (FY2025 10-K). Joint-venture funding: $278M invested
in 2025, including $158M "on a proportionately consolidated loss project for an infrastructure joint venture" and $33M for "a legal
settlement payment"; $101M in the first half of 2026. Claims: $214M of revenue recognised for claims at 2025-12-31 ($244M a year
earlier); "up to $105 million" of back charges that may be disputed.

**Q4 (the accounts). The balance sheets, read in Step 0**, "balance sheets over an 8 or 10 year period before I even look at the income
account" **[M2025-032]** (USD millions; company facts and
`tools/run.py` ten-year table; 2026-06-30 from the 10-Q):

| year-end | assets | equity | cash + securities | goodwill | long-term debt | retained earnings |
|---|---|---|---|---|---|---|
| 2016 | 9,216 | 3,125 | 1,961 | 532 | 1,518 | 3,582 |
| 2017 | 9,328 | 3,342 | 1,965 | 565 | 1,592 | 3,655 |
| 2018 | 8,883 | 2,834 | 1,980 | 467 | 1,662 | 3,294 |
| 2019 | 7,967 | 1,488 | 2,005 | 508 | 1,652 | 1,701 |
| 2020 | 7,310 | 1,030 | 2,222 | 207 | 1,701 | 1,250 |
| 2021 | 7,089 | 1,393 | 2,336 | 249 | 1,174 | 791 |
| 2022 | 6,827 | 1,786 | 2,624 | 206 | 978 | 896 |
| 2023 | 6,973 | 1,940 | 2,588 | 206 | 1,158 | 979 |
| 2024 | 9,143 | 3,949 | 2,959 | 199 | 1,104 | 3,124 |
| 2025 | 8,236 | 3,244 | 2,194 | - | 1,070 | 3,064 |
| 2026-06-30 | 7,536 | 2,686 | 3,043 | - | 1,072 | 2,978 |

What moved and why: retained earnings fell by $2.9 billion from 2017 to 2021 (the 2019 charges and restatement, losses in 2020 and
2021); equity fell to $1,030M; the goodwill bought with Stork in 2016 ($532M) was impaired and then sold away; the recovery of equity in
2024 came from the fair-value mark on NuScale ($2,221M gain booked in 2024; the stake has since been sold for cash, so the cash now on the
balance sheet is the realised form of that mark); equity then fell again in 2025 to 2026 as $1.57 billion of shares were bought back
(2025 and first half of 2026). Cash has stayed near $2 billion to $3 billion throughout, part of it inside joint ventures and VIEs
($328M at 2025-12-31, "not necessarily readily available"). What the figures cannot say: the size of claims and estimates inside
contract assets, the subject of the 2019 restatement.
The restatement: the FY2019 10-K (filed 2020-09-25 after an NT 10-K, `0001628280-20-013900`) restated 2016, 2017 and 2018 and the
interim periods of 2018 and 2019, and reported material weaknesses, one in the Energy & Chemicals segment where "Former leaders of our
Energy & Chemicals segment caused pressure to be applied on the individuals charged with accounting and finance responsibilities in a
manner intended to present overly optimistic forecasts", which "in certain instances [...] gave rise to an override of our project
controls on a project and resulted in errors in our financial statements due to unsupported forecasted estimates". Construction in
progress is the accounting the rows name as one where "there’s so many ways you can cheat" **[M2013-086]**.
Featured figures: the release headline gives "Adjusted EBITDA" and "adjusted EPS" and the company gives and revises adjusted-EBITDA
guidance ("narrowing its 2026 adjusted EBITDA guidance from $525 – $560 million to $500 – $525 million", Exhibit 99.1,
`0001124198-26-000074`); the 10-K features non-GAAP "Total segment profit" and "adjusted net revenue". Under the framework these are
recorded at Q4 as a weighing against and carried to Q5 (an adjusted figure featured "makes us nervous" **[L2016-006]**; guidance, "the scourge of
earnings" **[L2019-006]**); here they are recorded only. Stock pay $19M to
$48M a year (2016 to 2025). Effective tax rate 75% (2023), 103% (2024), 39% (2025).

**Q5 (the people). Integrity facts, recorded, not judged.**
- SEC investigation announced February 2020 into the second-quarter 2019 charges; DOJ subpoenas April 2020 and January 2022. "In May
  2023, the DOJ advised that it had closed its investigation and does not intend to bring charges. In September 2023, we entered into a
  settlement agreement with the SEC resolving the investigation and agreed to pay a civil penalty of $15 million." (FY2023 10-K,
  `0001628280-24-005451`).
- The restatement and the Energy & Chemicals "pressure" material weakness (Q4 above). The current chief executive, James R. Breuer
  (chief executive since May 2025, with the company since 1993), was "President, Downstream — Energy & Chemicals from 2019 to 2021"
  (FY2025 10-K, executive officers). The filings read make no finding about him; the fact of tenure is recorded only because a later run
  reaching Q5 must read it with the rest.
- Securities class action filed 2018 (class period August 2013 to February 2020), dismissed except for one 2015 statement about a
  gas-fired power contract, settled and approved November 2022 (FY2022 10-K, `0001628280-23-004139`); eleven derivative actions settled
  2023 (FY2023 10-K).
- New securities class action filed September 2025 over statements made from February to July 2025 "concerning market conditions,
  rising costs on three infrastructure projects and the effectiveness of our risk mitigation strategies"; four derivative actions and a
  books-and-records demand followed (FY2025 10-K). In February 2026 NuScale shareholders sued NuScale, two NuScale executives and Fluor;
  the July 2026 amended complaint added "two current Fluor employees who are former NuScale directors" (10-Q `0001124198-26-000071`).
- Guidance and an adjusted figure featured (Q4 above); under the framework these are judged at Q5 with the rest, and "If you’ve got
  doubts, forget it." **[M2013-088]** governs that later reading.

**Q6 (the money and the owners).**
- Buybacks: "Since we restarted the program in the fourth quarter of 2024, a total of 38 million shares have been purchased for $1.7
  billion through June 2026" (10-Q), an average of about $44.7; 2025, 18 million shares for $754M (about $41.9); first half of 2026, 17
  million for $816M (about $48.0); second quarter of 2026 at an average of $48.74 (10-Q, Part II). The programme names no price: "at such
  time and in amounts that we deem appropriate" (FY2025 10-K, Item 5). Against the computed range above (bottom $22.55), every reported
  average price paid sits above the bottom; under the framework's buyback convention that would weigh against at Q6, since value is "entirely purchase-price dependent" **[L2016-002]**;
  recorded, not weighed.
- NuScale: total investment $570M, sales of about $2.43 billion since September 2025 (8-K `0001124198-26-000051`); federal and state
  tax of $357M paid in 2026 "primarily related to the 2025 conversion of our shares in NuScale" (10-Q).
- Dividends: none since April 2020 (FY2025 10-K, Item 5).
- Pay (DEF 14A `0001104659-26-027053`): the 2025 incentive definitions of EBITDA exclude "significant litigation and regulatory costs and
  settlements or associated damages in excess of $10 million", marked as applicable in 2025 (the year of the Santos judgment); the chief
  executive's 2025 total compensation was $6,873,013, including $1,330,300 of non-equity incentive pay, in a year in which net earnings
  attributable to Fluor were a loss of $51M; long-term awards weighted 70% on annual EBT goals averaged over three years and 30% on
  relative TSR; a supplemental clawback was adopted in February 2026; the pay ratio was 97 to 1. Under the framework Part B would read
  these against "heads I win, tails you lose" **[L1994-020]**; recorded, not weighed.
- 2029 convertible notes (1.125%, conversion price $45.37, capped calls to $68.48); the stock traded above the conversion price in the
  second quarter of 2026, adding 872,024 shares to diluted shares (10-Q).

**Q9 (debt and exposures).** Long-term debt $1,072M (2028 notes and the 2029 converts) against cash and securities of $3,043M at
2026-06-30. The $2.2 billion credit facility (undrawn) "will require us to provide collateral to secure the facility should we be
downgraded to BB by S&P and Ba2 by Moody's, which is a one notch downgrade from both agencies' current ratings"; covenants include
debt-to-capitalisation at most 0.60 and minimum liquidity of $1.1 billion (FY2025 10-K, Item 7). Letters of credit $424M committed and
$918M uncommitted, including $347M for two lump-sum projects in Kuwait "substantially complete except for the resolution of unapproved
change orders and extension of time claims"; performance guarantees "estimated to be $14 billion". Santos: appeal hearing scheduled for
July 2026, insurer coverage dispute under a standstill (FY2025 10-K; the 10-Q reports the appeal hearing commenced). Joint and several
liability on venture contracts (Item 1A).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `3b4ce064`); written question by question; committed after each (Step 0 to Q1
      `2dac5292`; Q2 `e1741f77`; the rest in the final commit). The first write replaced the template's later headings with Step 0 to
      Q1; the remaining headings were restored from the template in this final section.
- [x] Dispatched: the brief allowed per-question pathspec commits of the run file and research folder only; the lock is the
      dispatching session's; the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination declared:** (1) a directory
      listing of `Test Runs/` filtered for today's date (made to check that this run's folder did not yet exist) showed the names
      `2026-10-17 Run - AMTM Amentum.md`, `2026-10-17 Run - ARCAY Arcadis.md` and their research folders; (2) the session's opening git
      context showed recent commit subjects about the AMTM run (its box, a figure share for its Global Engineering Solutions part, its
      competitor names). Neither file was opened. Amentum is a rival the 10-K names; it was not chosen for the competitor row, and nothing
      from those subjects was used. (3) The memory index loaded with the session names queue counts and "57 gate-clearers"; not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in that row (check script
      `check_ids.py`, output `check_ids_output.txt`); no E-id. Every filing fact carries its accession; the competitor figures are flagged
      as XBRL transcription.
- [x] The order was kept; Q2 closed the run OUT; nothing after it is a clearance. **Declared:** the owner-cash and value scripts were run
      while the filings were being gathered, before the Q2 section was written (their outputs are headed as computation); they did not
      enter the Q2 reasoning, which rests on Items 1, 1A and 7 and the competitor row.
- [x] Owner cash after every real cost (stock pay, all capital spending, distributions to minority partners), never a net-income proxy;
      the sovereign from the US Treasury par curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (Foundations; Q1); facts for later questions under AFTER THE STOP, with the integrity flag
      in the box line.
- [x] No point-in-time anchor; no row dated after an anchor issue arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text was ignored.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the reply to the dispatcher).

## WHAT I COULD NOT GET
NuScale's stock pay inside Fluor's consolidated stock pay (not separated; small against the gap to the floor). NuScale's operating cash
before 2021 (Fluor funded it then; left inside owner cash). Operating leases (not read; left out of net debt as the convention allows).
The rivals' figures were not checked against their filed statements line by line (XBRL transcription). No scuttlebutt (test 9 of Q2).
Cash and payments of proportionately consolidated joint ventures beyond what the 10-K states.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a contractor.** Q1 asks for "a reasonable fix on about what the earning power and competitive position will look
like" **[M2012-065]**, and the doubt row closes on any doubt, "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**; a contractor's yearly earnings level is not predictable
(the filer says awards are "unpredictable"), yet its economic dynamics, and the absence of a moat, are plain. The text does not say
whether an unpredictable level with a foreseeable shape is a Q1 TOO HARD or a Q1 IN that Q2 then closes; this run read it as IN and let
Q2 decide, on M2011-014's "Is there ease of entry?". Two analysts could split here (Q1 TOO HARD (NATURE) against Q2 OUT), with the same
practical result but different boxes and re-look rules. (2) **Q7 (b) on a series that crosses zero.** (b) says that where halves are
meaningless "the range is the no-growth case alone"; it does not say whether a decline visible in another filed series (sales) may set
the bottom. This run carried sales decline as the bottom as a CONVENTION of the run; the text should say. (3) **Q7 (c) with sales and no
purchases.** "Cash paid for businesses, net of businesses sold" read literally would credit divestiture proceeds (AMECO, Stork, China
yard, Mexico joint venture) as owner cash in a shrinking business; this run excluded them and counted their cash in net cash. (4)
**Consolidated investee burn.** Neither Q4 nor Q7 says how to treat the operating losses of a consolidated investee later sold (NuScale);
the equity-method paragraph covers the reverse case only. (5) **The equity-only figure with large net cash.** Valuing owner cash after
interest at ten percent capitalises the cash at its interest yield ($5.05 against $19.79 here); the convention says the figure never
decides alone, but a reader of the two figures side by side may misread the gap. (6) **The template** asks for the balance sheets "in Step
0 if the file closes before Q4" but gives Step 0 no slot for them; they are written under AFTER THE STOP, Q4, with a note that they
were read in Step 0.
