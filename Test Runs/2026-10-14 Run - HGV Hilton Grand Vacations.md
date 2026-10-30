# Company Run: Hilton Grand Vacations Inc. (NYSE: HGV), 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to its dated name before any fetch (commit
`9a53627a`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for HGV or Hilton Grand Vacations).

**Dispatched analyst run.** Working folder `Test Runs/_research 2026-10-14 HGV/` (notes, fetch and check scripts, the
`tools/run.py` and `Screens/cover_shares.py` outputs; raw filings under its gitignored `cache/`).

**Contamination, declared.** (1) Before the first fetch I ran a directory listing of `Test Runs/` filtered for "HGV" or
"Hilton Grand", to make sure the dated path was free; it returned no file name. It was a listing the blind rule forbids, and
it is declared here; nothing was learned from it. (2) The session preface showed recent commit subjects of another
company's run (a hotel franchisor, folded overnight); its verdict words were seen and are not used. (3) A listing of
`Screens/_daily/` showed file names only (digests, logs, the lock); none was opened. No run file, holding review,
`PORTFOLIO.md`, register or reading list was opened.

**The lines of evidence, chosen from the 10-K** (the brief's departure from the canonical brief; derived from Item 1,
Item 1A and Item 7 of the FY2025 10-K): (1) the sales engine: contract sales, tour flow, VPG, the cost of selling and the
construction deferrals (Item 7); (2) the loan book: default rates, the allowance, FICO bands, aging by brand (Item 1,
Item 7, Note 7); (3) the funding: the non-recourse securitizations, the Timeshare Facility, the corporate debt (Item 7,
Note 15); (4) the Hilton license, its fees, exclusivity and termination rights (Item 1); (5) the resort and club
management annuity (segments, Note 22); (6) the acquisitions: Diamond (2021), Bluegreen (2024), Elara (2026) and their
integration costs; (7) capital return: the buybacks and the Apollo sell-down; (8) the risks Item 1A names to the product
itself: the secondary market, exit companies, maintenance fees, limited underwriting; (9) internal control (the 2022 and
2023 material weaknesses).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $35.18 (close 2026-10-13, from `tools/run.py`; an aggregator quote, flagged under operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: 77,724,145 common shares, one class, $0.01 par (10-Q for the quarter
  to 2026-06-30, filed 2026-07-30, accession `0001674168-26-000100`, cover count as of 2026-07-23;
  `python Screens/cover_shares.py HGV`). Checked: the 10-Q balance sheet shows 78,017,947 shares issued and outstanding at
  2026-06-30; shares are retired on repurchase (FY2025 10-K, Item 5: "The shares are retired upon repurchase"), so issued
  equals outstanding and there is no treasury count to deduct; the fall of about 0.29 million from 06-30 to 07-23 is
  July buying. The 8-Ks after the 10-Q (2026-07-30 earnings, accession `0001674168-26-000098`) state no issuance.
- **Market cap:** 35.18 x 77.724 = **$2,734M**.
- **Sovereign for the earnings currency (USD):** **5.56%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-13 (`tools/run.py`, which reads the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-26, accession `0001674168-26-000017` (Items 1, 1A, 5, 7,
  8 with Notes 7 and 22, the auditor's critical audit matters); 10-Q Q2 2026, filed 2026-07-30, accession
  `0001674168-26-000100` (statements, Note 3 the Elara acquisition, Note 19); DEF 14A filed 2026-03-17, accession
  `0001140361-26-009850`; the earlier 10-Ks for the cycle: FY2019 `0001564590-20-008097`, FY2020 `0001564590-21-009825`,
  FY2021 `0000950170-22-002564`, FY2022 `0001628280-23-005817`, FY2023 `0001628280-24-007940`, FY2024
  `0001628280-25-009254`. **One figure cross-checked against the filed statement:** net cash provided by operating
  activities FY2025, $300M on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 74) against 300.0 in
  `tools/run.py`; agrees.
- `python tools/run.py HGV` arithmetic lines only (output in the research folder): OCF 2023 to 2025 312 / 309 / 300;
  stock pay 40 / 47 / 64; capital spending (property plus software) 75 / 126 / 146; D&A 213 / 268 / 273. Five-year
  (2021 to 2025) mean of OCF less stock pay less capital spending: 221.6. The tool's "owner earnings" lines and its yield
  lines are not used as a rule (Part VII, the tooling); owner cash is recast at Q4 below, because this company's operating
  cash flow carries the growth of its consumer loan book, which is funded by non-recourse debt shown under financing.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own HGV "if the market closed for five years"
**[M1997-109]**, and for this name that turns on two things the quotation cannot show, whether timeshare buyers keep
paying and whether the securitization market keeps funding them. Who is paid to tell you bears directly: the product is
sold by a commissioned sales force on a tour, and the company's own MD&A leads with Adjusted EBITDA; "you do not get
impartial advice" where fees ride on one answer **[M2020-037]**, and the seller's projection is not consulted
**[M2011-083]**. No macro view enters. **Contrary evidence, written down as found** **[M1997-127]**: (a) Item 1A says the
underwriting "do[es] not include certain traditional ability-to-pay factors, such as income verification"; (b) owners resell
on the secondary market at prices "typically less than the prices at which we would sell the intervals" (Item 1A), and the
company buys there itself as a "low-cost inventory source"; (c) annual default rates were 4.12% / 4.71% / 5.14% in
2017 to 2019 (FY2019 10-K) and 8.56% / 10.77% / 9.86% in 2023 to 2025 (FY2025 10-K); (d) the allowance on originated
loans is $1,078M against $3,665M gross at 2025-12-31 (Note 7), against $184M on about $1.34B at 2019-12-31 (FY2019 10-K,
critical audit matter); (e) material weaknesses in internal control at 2022-12-31 and 2023-12-31, both since remediated
(Item 1A); (f) club members about 519,000 (2022), 529,000 (2023), 724,000 (2024, with about 200,000 Bluegreen members
acquired), "more than 720,000" (2025): flat after the acquisition; (g) 2025 buybacks of $600M against operating cash flow
of $300M.

## THE STANDING RULE
Owning HGV for cash, unlevered and sized so that a fall of half or more does not force a sale, puts the buyer at no risk
of ruin; borrowed money to buy it would, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**
and leverage "can prevent you from playing out your hand" **[M2004-065]**. The target's own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** "can I understand it?" **[M1995-051]** means "a reasonable fix on about what the earning power
  and competitive position will look like in five or 10 years" **[M2012-065]**. HGV does four things the 10-K separates
  (Item 1): it sells timeshare intervals and points (its own inventory, plus fee-for-service sales for third-party
  developers, 17% of 2025 contract sales, and just-in-time inventory, 9%); it lends to the buyers (67% of 2025 contract
  sales financed; ten-year fully amortizing fixed-rate loans at 2.5% to 25%, weighted 14.7%; gross book $4,314M on about
  182,000 loans); it manages resorts for the owners' associations on cost-plus fees of 10% to 15% and runs the clubs on
  annual dues; and it rents unsold and exchanged inventory. None of it is technology; the product has been sold in the
  same way, by tour, for decades, and the filing calls the business "moderately cyclical".
- **The key variables, and how predictable** **[M1998-044]**: tour flow and VPG (contract sales = tours x VPG); the
  default rate on the loan book; the cost and availability of securitization funding; the Hilton license; the owners'
  willingness to keep paying maintenance fees. Each is reported in the filing, year by year. The variables are not
  invented each year; what can move them is the consumer and the credit market, not a new technology.
- **Do the past statements tell me the future ones?** **[M2008-033]**: largely yes for the management annuity (cost-plus,
  "highly predictable"); less so for the sales line, which ASC 606 construction deferrals swing (net deferral of $368M of
  sales in 2025, $52M in 2024), and for the loan book, where the allowance is an estimate from static pools. Those are Q4
  matters (the accounts), not a bar to understanding what the business does.
- **The lending arm, read under the bank rows.** HGV is a lender for the framework's purposes in one of its parts: it
  carries a $4.3B consumer book and takes credit risk on it, and the speakers' own case of a seller that lends to its
  buyers is read the same way: "it's appropriate to finance a soundly-selected book of interest-bearing receivables
  almost entirely with debt (just as a bank would)" **[L2003-019]**. The bank door asks that both sides be readable
  **[M2002-022]**, the danger being "always on the asset side" **[M2011-022]**. The asset side is readable here: Note 7
  gives the book by brand, by FICO band and by origination year, the aging, the write-offs and the allowance roll-forward;
  there is no derivatives book "on top of it" **[M2005-068]** beyond interest-rate hedges. The liability side is not
  deposits but non-recourse term securitizations (fixed coupons, stated maturities, no recourse to HGV) and a revolving
  warehouse; that funding is wholesale, the kind that "can run pretty fast" **[M2012-012]**, and the right question about
  it is the one asked of a finance company, whether "I can continually fund it" **[M2002-094]**. That is a question of
  exposure (Q9: what is demanded tomorrow morning), not of whether the book can be read. The finance arm is read apart
  from the selling and the management, since "lumping them together [...] impedes analysis" **[L2008-005]**.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn't" **[M2002-092]**. My
  doubts are about the direction of the variables (defaults doubled, margins narrowed), which are Q2 and Q9 questions; I
  have no doubt about what the business is and how it makes and loses money.
- **VERDICT: IN.** The economics can be followed from the filings and the variables are named, reported and not driven by
  technology **[M2012-065]**, **[M1998-044]**; the lending part is a readable book funded by matched non-recourse debt
  **[L2003-019]**, **[M2002-022]**, with the funding question carried to Q9 **[M2002-094]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what's going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**.

**The parts table** (Note 22 and the segment tables of the FY2022, FY2023, FY2024 and FY2025 10-Ks; the filer's only
segment profit measure is segment Adjusted EBITDA, used here because no other segment profit is reported):

| Part | Segment Adj. EBITDA 2021 / 2022 / 2023 / 2024 / 2025 ($M) | Share of the five-year total | Castle | Decides |
|---|---|---|---|---|
| Real estate sales and financing | 537 / 865 / 754 / 802 / 707 = 3,665 | 59% | the Hilton-licensed sales engine and its captive lending | **yes** (more than half) |
| Resort operations and club management | 353 / 463 / 504 / 604 / 620 = 2,544 | 41% | cost-plus management contracts and club dues on a base of about 720,000 members | no |

The file closes on the real estate sales and financing part. The management part's castle is noted: fees of 10% to 15%
over the associations' costs, "highly predictable" (Item 1), profit margin 68.9% / 70.8% / 70.8% in 2023 to 2025 (Item 7).

**The castle tests, on the deciding part.**
1. **Key factors and their permanence** **[M1995-038]**. Three: the Hilton license (exclusive in timeshare until
   2051, extendable; initial term to 2116; 5% of gross revenue; Hilton may end exclusivity if licensed revenue falls under
   67% of revenue, and may terminate on quality failures, Item 1); the owner base (74% of 2025 contract sales were to
   existing owners, 72% in 2024, 70% in 2023, Item 7); and the financing (67% of contract sales financed). The brand is
   not owned; license fee expense rose from $138M (2023) to $214M (2025) as the reduced post-acquisition rates step up
   (Item 1, Item 7).
2. **Would it stand without the lord?** It is a selling business: sales and marketing expense was $1,871M against
   contract sales of $3,314M in 2025 (Item 7). It is one "where you have to stay smart" **[M1995-040]**.
3. **The money test** **[M2011-015]**. The Hilton name cannot be bought; an attacker would need another hotel brand, and
   the brand-affiliated incumbents already hold them (Marriott, Wyndham, Disney). Entry without a brand happens (the
   private developers the 10-K names), and HGV's own growth came by buying two such businesses. The test is passed for
   the Hilton franchise, not for the industry.
4. **Pricing power and the agony** **[M2005-020]**. VPG $3,518 (2019, legacy HGV) to $3,851 (2025): up 9.5% in six
   years. In 2025 sales incentives rose $51M and the provision for loan losses $59M (Item 7). Weak, not absent.
5. **Unit volume and share of mind.** Club members about 519,000 (2022) and 529,000 (2023); about 724,000 (2024)
   with about 200,000 Bluegreen members bought; "more than 720,000" (2025). Net of the purchase the base has not grown
   since 2022. Tour flow 856,676 in 2025, up 2.6% (Item 7).
6. **Low cost**: no evidence either way in the filings read; not claimed.
7. **The brand in the customer's mind** **[M2008-075]**. The Hilton name is the promise and the reason for the call
   transfers and the Honors points (Item 1); it is licensed, and its value is shared with its owner through the fee.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. Against: the same intervals resell on the
   secondary market at prices "typically less than the prices at which we would sell the intervals", and the company
   buys there itself (Item 1A). The developer's price holds through the tour and the financing. For: those who buy pay
   that price, mostly existing owners buying again.
9. **Ask the competitors**: not on the public record.
10. **Widening or narrowing** **[L2005-010]**. Narrowing at HGV on every measure of the deciding part: real estate
    margin 33.5% (2018) and 28.5% (2019) to 21.2% (2025), or about 26% with the 2025 construction deferral added back
    ($202M of deferred profit, Item 7); annual default rate 4.12% / 4.71% / 5.14% (2017 to 2019) to 8.56% / 10.77% /
    9.86% (2023 to 2025), with the weighted FICO at origination unchanged (737 / 741 / 734 in 2023 to 2025); the
    allowance on originated loans 29% of gross ($1,078M of $3,665M, Note 7) against about 14% in 2019 ($184M on about
    $1.34B); HGV-brand unsecuritized loans 121 days or more past due $144M (2024) to $206M (2025, Note 7). Part of this
    is the acquired mix (the Diamond and Bluegreen books carry their own aging, Note 7), which HGV chose; part is the
    consumer, since the main rival raised its reserve in 2024 for "the cumulative impact of inflation on consumers and
    the related impact on year-over-year increases in maintenance fees" and reports 2025 delinquencies "declined from
    those experienced in 2024 and 2023" (VAC FY2025 10-K).
11. **What could destroy it** **[M2000-014]**: a consumer-credit downturn that lifts defaults and shuts the
    securitization market at once; rising maintenance fees (Item 1A); loss of the license; the exit companies and the
    secondary market (Item 1A).

**The competitor row** (the rivals the 10-K names that file: Marriott Vacations Worldwide and Travel + Leisure; the
whole span 2019 to 2025, each company's own definition):

| Metric | HGV | VAC | TNL |
|---|---|---|---|
| VPG, 2019 to 2025 | $3,518 to $3,851 (+9.5%) | $3,574 to $3,794 (+6.2%) | $2,381 to $3,284 (+38%), tours 945k to 734k |
| Development or real estate margin, 2019 to 2025 | 28.5% to 21.2% | 22.7% to 23.0% | not reported in this form |
| Loan-loss provision against sales, 2019 to 2025 | $74M / $1,410M = 5.2% to $422M / $3,314M = 12.7% | estimated remaining default rate 11.62% (2022) to 13.51% (2025) | $479M / $2,355M = 20.3% to $484M / $2,486M = 19.5% |
| Net income, 2019 to 2025 summed | $984M | $467M | $1,954M |
| Stockholders' equity, 2025 year-end | $1,289M (goodwill $1,985M) | $1,993M (goodwill $2,958M) | negative $981M (goodwill $972M) |

Sources: HGV 10-Ks `0001564590-20-008097` and `0001674168-26-000017`; VAC 10-Ks `0001524358-20-000011`,
`0001524358-23-000009`, `0001524358-26-000010`; TNL 10-Ks `0001361658-20-000012`, `0001361658-26-000009`; net income and
equity from each filer's XBRL company facts (the 10-K values). **Named rivals that do not file:** Holiday Inn Club
Vacations, Westgate Resorts and the Berkley Group are not in EDGAR's company ticker list; Disney Vacation Club sits inside
Walt Disney Co., which files but does not report it separately. None used.

**The field's returns over the last full cycle** (2019 peak, 2020 trough, 2021 to 2025; research file
`returns_q2_q3_output.txt`). HGV's pre-tax earnings before corporate interest against net tangible capital (equity plus
corporate debt less cash, goodwill and intangibles; the non-recourse debt left with the receivables it funds): 25.4%
(2019), 22.7% (2021), 33.0% (2022), 31.4% (2023), 19.4% (2024), 23.2% (2025). Against total capital with the purchased
goodwill and intangibles: 23.7% (2019), then 8.4%, 13.6%, 13.7%, 7.5%, 8.5%. VAC and TNL carry little or negative
tangible equity on the same structure (VAC's equity is less than its goodwill; TNL's is negative) and earned $467M and
$1,954M over the seven years. Judged in words: the field's businesses earn good returns on the tangible capital they need,
which is how the business is judged **[M2011-060]**, **[M2010-090]**; what buyers paid for them in acquisitions earns
ordinary returns at HGV and poor ones at VAC, which is a capital-allocation finding for Q3 and Q6, not a finding that the
castle protects only ordinary returns.

**Reading.** The castle is standing: the Hilton franchise cannot be bought, the field has had the same few brand-backed
players for decades, and the tangible capital still earns well. What the evidence shows is narrowing at HGV, worse than
at the main rival on margin, partly bought (the acquired brands) and partly the consumer cycle the rival also reports.
The rows sort a bad stretch by whether the position against the competitors held: "we at least maintained [...] our
competitive superiority. [...] you should view last year's figures as reflecting a cyclical problem, not a secular one"
**[L1995-022]**. HGV still has the highest VPG of the three, its pricing rose more than VAC's and less than TNL's, and its
margin fell where VAC's held. The low-bid test is answered against the product, and "A moat that must be continuously
rebuilt will eventually be no moat at all" **[L2007-005]** describes a business that must sell each year's earnings
again through the tour; the evidence shows that rebuilding getting costlier, not failing. On the other side, the speakers
credit the business whose "customers are mad at you and you're growing" **[M2000-032]**, and HGV's contract sales grew
10.4% in 2025.

- **Contrary evidence, written down** **[M1997-127]**: the default rate doubled with the FICO score unchanged; HGV-brand
  serious delinquencies rose in 2025; the real estate margin fell about seven points over the span while VAC's held;
  members flat since 2022 once the purchase is taken out.
- **VERDICT: IN, narrowly.** The castle stands on the license, the owner base and the returns on tangible capital
  **[M1995-038]**, **[M2011-060]**; the narrowing is real and is carried to Q3, to the bottom of the Q7 range and to Q9
  rather than closing the file, because the position against the rivals has broadly held **[L1995-022]**. Had the
  narrowing shown against the rivals as well, the moat would be "tenuous" and the box TOO HARD **[M2000-019]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, on "the capital
actually needed in the business" **[M2010-090]**, with goodwill set aside for the business and kept for the allocation
**[M2011-060]**.

- **Return on the capital needed.** Pre-tax earnings before corporate interest (after the consumer-financing interest,
  which is the finance arm's cost) against net tangible capital: 42.0% (2018), 25.4% (2019), 22.7% (2021), 33.0% (2022),
  31.4% (2023), 19.4% (2024), 23.2% (2025) (`returns_q2_q3_output.txt`; statements of each year's 10-K). The tangible
  capital is small because the receivables are funded almost entirely by non-recourse debt, which the speakers accept for
  a "soundly-selected book of interest-bearing receivables" **[L2003-019]**; the return is high and falling from the
  2018 level.
- **To stand still.** Three outlays recur. Inventory: VOI inventory spending $182M / $298M / $445M / $369M in 2022 to
  2025, against the cost of inventory relieved by each year's sales of about $263M / $203M / $257M / $257M (cost of VOI
  sales with the construction deferrals and recognitions undone, Item 7 tables); the excess averaged about $79M a year.
  Capital spending on property and software: $97M / $75M / $126M / $146M (cash flow statements), against which the
  10-K says renovations "are necessary to stay competitive" (Item 7). The loan book: the operating cash line for
  timeshare financing receivables was an outflow of $315M (2023), $563M (2024) and $669M (2025); in 2025 about $373M of
  it replaced loans written off (write-offs of $187M originated and $186M acquired, Note 7) and the rest is growth of
  the book, funded that year by $404M of net non-recourse borrowing. "there's your profit sitting in the yard"
  **[M2008-036]** is the risk of this model: the profit on a financed sale arrives over ten years, and about a tenth of
  the book defaults each year.
- **What the added capital earned.** From 2019 to 2025 pre-tax earnings before corporate interest rose $170M (316 to
  486) while total capital rose $4,415M (net tangible capital $849M of it, the rest purchased goodwill and intangibles):
  3.9% pre-tax on the added capital. The additions were mainly purchases: Diamond ($2,029M of debt repaid plus 33.93
  million shares, 2021), Grand Islander ($74M, 2023), Bluegreen ($1,444M net of cash, 2024), Elara ($131M, 2026).
  Organic growth, as the filer reports it on its pro forma revenue (FY2022 and FY2024 10-K pro forma notes against the
  actual figures), was about 1.5% a year from 2022 to 2025. "we're not earning a higher rate of return on capital than we
  were when we started. We just put way more capital into the business" **[M2023-081]** is the shape; here the rate fell.
- **The three grades** **[M1998-081]**: the tangible business is near the second grade (decent returns on the capital
  it needs, financed by the receivables themselves); the capital the owners added in the window went in at a very low
  rate, the third grade's mark **[L2007-010]**.
- **WEIGHS AGAINST.** The capital the business needs earns well **[M2011-060]**, but the capital put in over the window
  earned about 4% pre-tax on what was paid, and organic growth was about 1.5% a year **[M1998-081]**, **[M2023-081]**.
  (The "little or no debt" criterion is applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]** (`tools/run.py` ten-year table, first-filed XBRL, checked against the filed
balance sheets of the FY2019, FY2022 and FY2025 10-Ks and the Q2 2026 10-Q; USD millions):

| Year-end | Total equity | Goodwill | Intangibles | Corporate debt | Non-recourse debt | Cash | Receivables, net | Inventory | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 167 | 0 | 70 | 490 | 694 | 48 | n/r | n/r | 28 |
| 2019 | 570 | 0 | 89 | 828 | 747 | 67 | 1,156 | 558 | 390 |
| 2021 | 1,988 | 1,377 | 1,441 | 2,913 | 1,328 | 432 | n/r | n/r | 357 |
| 2022 | 2,151 | 1,416 | 1,277 | 2,651 | 1,102 | 223 | n/r | n/r | 529 |
| 2024 | 1,895 | 1,985 | 1,787 | 4,601 | 2,318 | 328 | 3,006 | 2,244 | 352 |
| 2025 | 1,440 | 1,985 | 1,670 | 4,545 | 2,716 | 239 | 3,115 | 2,522 | 34 |
| 2026-06-30 | 1,258 | 1,986 | 1,592 | 4,876 | 2,896 | 272 | 3,591 | 2,546 | (101) |

(n/r: not read from the statement for that year in this run.) What moved, and why: equity was built by the Diamond share
issue (2021) and has since been drawn down by buybacks ($272M, $368M, $432M, $600M in 2022 to 2025 and $300M in the first
half of 2026) faster than earnings refilled it, so retained earnings fell from $593M (2023) to a deficit of $101M; the
purchases put $3.6B of goodwill and intangibles on a balance sheet that carried none in 2019; corporate debt rose from
$828M to $4,876M; inventory rose from $558M to $2,546M against contract sales that rose from $1,410M to $3,314M, so
inventory went from about 0.4 to about 0.8 of a year's contract sales. "if some prepaid expense, deferred asset accounts
start building up suspiciously high, and inventories look out of line, you know, with sales [...] you want to look twice"
**[M1995-064]**. Looking twice: the inventory build is explained in the filings (acquired inventory at fair value; $637M
of deferred revenue at 2025-12-31 against sales of units under construction; an inventory pipeline of $14.7B at current
pricing, Item 1), and other assets rose from $410M to $657M in six months of 2026 with an equal deferred-revenue rise
($637M to $864M). Explained, not cleared: the inventory is now a larger claim on the owners' capital than it was.
"what the figures are saying and what they don't say and what they can't say" **[M2025-032]**: the receivables carry a
29% allowance against the originated book, an estimate from static pools; the figures cannot say whether that is enough.

**The real costs.**
- Depreciation and amortization $273M (2025), of which a large part is amortization of purchased intangibles (club
  member relationships, management contracts, trade names); the member relationships deplete as members default and
  leave, so the charge is treated as real here **[R1996-023]**.
- Stock pay $40M / $47M / $64M (2023 to 2025), charged in owner cash **[L2015-003]**.
- Acquisition and integration expense in every year of the window: $106M (2021), $67M, $68M, $237M, $98M (2025), and
  $26M in the first half of 2026: a recurring cost labelled one-time, left in **[L2016-007]**.
- The provision for loan losses ($422M deducted from 2025 sales, Item 7) is real; the defaulted loans' cash never comes.
- Securitizations are booked as secured borrowings with no gain on sale (Note 7), which is the conservative treatment.
- **EBITDA in the filer's own mouth.** The MD&A presents EBITDA, Adjusted EBITDA and Adjusted EBITDA Attributable to
  Stockholders ($950M for 2025 against net income attributable to stockholders of $81M); the earnings release gives
  guidance only in Adjusted EBITDA ($1.185B to $1.225B for 2026, 8-K `0001674168-26-000014`) and the CEO is quoted:
  "finishing in the upper half of our guidance range"; pay is set on "Economic Adjusted EBITDA" ($1,152M for 2025, proxy).
  The rows: EBITDA "utter nonsense" **[M1998-086]**, and "I'll look at that figure when you tell me you'll make all the
  capital expenditures" **[M2003-108]**. The 10-K itself lists EBITDA's limitations and says it "should not be considered
  as discretionary cash available to us" (Item 7).
- **Internal control.** Material weaknesses at 2022-12-31 (Diamond) and 2023-12-31 (IT access over a revenue and
  inventory application), both remediated; unqualified opinion on internal control at 2025-12-31 (Item 1A, Item 8).

**Owner cash, recast** (feeds Q7). OCF less stock pay less all capital spending (property and software), **plus the net
non-recourse borrowing** of the year. **CONVENTION of this run:** the non-recourse debt is treated as the finance arm's
working capital, by extension of Q7's convention on inventory-secured trade finance to receivable-secured non-recourse
debt; rationale: it is secured by the receivables and repaid as they collect, its interest is already charged inside
owner cash (consumer financing interest, in the financing segment), and the speakers keep a finance arm apart from the
operations **[L2008-005]** and fund such a book "almost entirely with debt" **[L2003-019]**; the alternative with the
non-recourse debt counted in net debt is shown beside at Q7. USD millions:

| Year | OCF | Net non-recourse borrowing | Stock pay | Capital spending | Owner cash (equity) | Corporate interest | Owner cash before corporate interest, after tax |
|---|---|---|---|---|---|---|---|
| 2021 | 168 | (95) | 48 | 39 | (14) | 105 | 64.75 |
| 2022 | 747 | (221) | 46 | 97 | 383 | 142 | 489.5 |
| 2023 | 312 | 174 | 40 | 75 | 371 | 178 | 504.5 |
| 2024 | 309 | 259 | 47 | 126 | 395 | 329 | 641.75 |
| 2025 | 300 | 404 | 64 | 146 | 494 | 311 | 727.25 |

(Cash flow statements of the FY2022 and FY2025 10-Ks; the interest shield at 25%, a **CONVENTION of this run**: the 21%
federal statutory rate plus state, which the 2025 reconciliation shows at 12 points that year and the 2023 one at about
4; rationale: a single marginal rate for the add-back, not the year's effective rate. Acquisitions are kept out of
these lines and handled at Q7.)

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The statements can be followed and reconciled; nothing in them
  confuses on a second reading **[M1995-063]**: the construction deferrals and the allowance are tabled, the inventory
  build is explained, the securitizations take no gain. Against: the featured adjusted figure, the guidance and the pay set
  on it, the recurring integration charges, two years of material weakness, and inventory and deferred accounts rising
  faster than sales **[M1995-064]**. Preoccupation with presentation is "a negative" but not "a total exclusionary factor"
  **[M1994-018]**; the habits are carried to Q5. *(The Q4 text also carries the EBITDA count, "about zero" **[M2002-026]**,
  as part of why confusion is a STOP; this run reads it under the 2026-10-06 convention that sends a featured adjusted
  figure to Q5; see "What in the framework was wrong or unclear".)*

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
Mark D. Wang, chief executive since the 2017 spin-off and a director since 2016, a timeshare executive for decades (former
chairman of the industry association, ARDA, 2017 to 2019), owns 1,448,622 shares, 1.8% (proxy `0001140361-26-009850`);
the board has an independent chair, Leonard Potter, since 2017; an Apollo designee left on 2026-07-02 as Apollo's holding
fell (8-K `0001140361-26-027453`).

- **The first yardstick, the record against the hand dealt** **[M1994-008]**. Against the main rival on the same
  structure and the same cycle, HGV earned $984M of net income over 2019 to 2025 to VAC's $467M, and its VPG ended the
  span the highest of the three (Q2). The capital half of the record is weaker: two large purchases whose combined capital
  earns about 8% pre-tax on what was paid (Q3), and a real estate margin that fell where VAC's held.
- **The second yardstick, how they treat their owners.** Candid where it matters: Item 1A states in plain words that the
  underwriting does "not include certain traditional ability-to-pay factors, such as income verification", that resale
  prices undercut the company's, and that two material weaknesses were found; the report tells an owner what he would
  want to know if he owned it all **[M1998-036]**. Against: the habits carried from Q4. The company gives annual
  guidance in Adjusted EBITDA and the chief executive reports "finishing in the upper half of our guidance range"; the
  rows say "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]**, name "the
  scourge of earnings "guidance"" **[L2019-006]**, and are made "nervous" by a management "highlighting "adjusted
  per-share earnings"" **[L2016-006]**; the count for EBITDA talk is "about zero" **[M2002-026]**.
- **Reading the habits with the integrity record** **[M2004-067]**. What the rows fear from the habit is that managers who
  promise to make the numbers "will at some point be tempted to make up the numbers" **[L2002-041]**. The record searched
  for that: no restatement found in the 10-Ks of 2019 to 2025; the allowance has been raised, not released (originated
  allowance $404M at 2022-12-31 to $1,078M at 2025-12-31, Note 7), which is the opposite of the reserve that moves to
  meet a target; the 2023 material weakness concerned access controls over a revenue application and was disclosed and
  remediated. Whether the declared targets are consistently met was not tested: only the FY2025 release was read, and
  it is recorded as one instance of a target met, not as a record. The habit is a preoccupation with presentation, which is "a
  negative" **[M1994-018]**; I find no fact in the filings read that makes it a doubt about honesty.
- **Love of the business.** A career inside one industry, a 1.8% stake held, an independent chair. Stock awards are
  66% of the chief executive's total direct compensation (proxy). The pay's measures are judged at Q6.
- **VERDICT on integrity: IN.** No fact found in the filings read raises a doubt about honesty **[M2013-088]**; the
  candour of Item 1A weighs for **[M1998-036]**; the guidance and EBITDA habits weigh heavily against and are recorded,
  not excused **[L2002-041]**, **[L2016-006]**. **Ability: WEIGHS AGAINST, narrowly**: a better operator than the main
  rival on the same hand **[M1994-008]**, a poor allocator of the capital added in the window (Q3).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **Retention** **[R1995-009]**. No dividend has been paid (Item 5). Net income attributable to stockholders over 2021 to
  2025 was $969M (176, 352, 313, 47, 81); the company spent more than that on its own stock ($1,672M in 2022 to 2025) and
  more again on purchases (Q3), the difference borrowed. The market leg of the test: the share price was $40.71 on the
  Diamond closing date, 2021-08-02 (the FY2021 10-K's consideration table), and is $35.18 now; market value per share
  fell over five years in which every dollar earned was kept or spent on the owners' behalf. The test is failed on its
  market leg; the intrinsic leg is Q7's.
- **Buybacks** **[L1999-023]**, **[L2016-002]**. The programmes state a dollar size and a period ($600M over two years,
  approved 2025-07-29) and no price above which they stop (Item 5). Prices paid: about $40 on average in 2025 ($600M for
  15 million shares, Item 7), $42.30 in the fourth quarter of 2025, about $47 in January and February 2026 (1.9 million
  shares for $89M); the company also bought 933,488 shares (August 2025) and 750,000 shares (June 2026) out of Apollo's
  underwritten sales (8-Ks `0001140361-25-031043`, `0001140361-26-023950`). Funded beyond the year's owner cash: 2025
  buybacks of $600M against equity owner cash of $494M (Q4), and corporate debt rose from $4,545M to $4,876M in the
  first half of 2026 while $300M more was spent. "cash plus sensible borrowing capacity -- beyond the near-term needs of
  the business" **[L1999-023]** is the condition; with corporate debt near nine times 2025 pre-tax earnings before
  corporate interest ($4,876M against $486M), the borrowing capacity used is not slack. *Written back from Q7 (committed with Q7):*
  the bottom of the central Q7 range is $94.23 a share at the government rate; the prices paid (about $40 to $47) sit
  below it, so the programme is read by what it did and is not weighed against for naming no price **[L2016-002]**;
  recorded beside it, those prices are above the fair price of $25.77, the price at which the business earns the floor.
- **Issuance and deals** **[L2014-012]**. Diamond (2021): 33.93 million shares at $40.71 ($1,381M) plus $2,029M of
  Diamond debt repaid in cash; the larger part was cash, so by Q7's definition it is an acquisition, not a merger, and the
  STOP on an all-stock deal in undervalued stock **[L2009-019]** does not apply. The shares given were 28% of the combined
  company; the count has since fallen from 119.9 million (2021-12-31, FY2022 10-K) to 78.0 million (2026-06-30, 10-Q),
  more than the shares issued, bought back at prices close to the issue price. Bluegreen (2024): $1.6B in
  cash including net debt. Elara (2026): $131M for the remaining 75%. No post mortem of either large deal against its
  projections was found in the filings read **[L2014-013]**. Deals financed with debt are judged on an all-equity basis
  **[L2017-004]**, which Q7 does.

**Part B: the pay, the board and the owners.**
- **Pay** **[M2003-019]**, **[M2016-083]**. The annual cash incentive is set 70% on "Economic Adjusted EBITDA" and 30% on
  revenue for most officers; the performance stock units vest on Economic Adjusted EBITDA and contract sales (proxy).
  Economic Adjusted EBITDA was $1,152M for 2025 against net income of $99M. Neither measure carries a charge for the
  capital employed **[L1994-019]**: "a batting average that does not include a cost of capital is a phony batting average"
  **[M1995-010]**; and contract sales reward the volume of sales whether or not the financed buyer later defaults, in a
  year when the provision took 12.7% of contract sales. Chief executive pay 2025: $14,067,191, including $361,616 for
  personal use of the company aircraft (proxy).
- **The board.** An independent chair since 2017 (proxy); the Apollo designation right falling away as Apollo sells.
- **Owners as partners.** Guidance in an adjusted figure (Q4, Q5) is the inversion, read as a test, of "We don't give
  out earnings guidance. We think it's silly." **[M2016-002]**; the 10-K's risk factors are candid.
- **Part A: WEIGHS AGAINST**: the market leg of retention failed, purchases earned about 4% pre-tax on the capital added
  (Q3), buybacks funded partly by debt **[R1995-009]**, **[L1999-023]** (the missing price is not weighed, the prices
  paid sitting below the bottom of the Q7 range **[L2016-002]**; written back with Q7).
  **Part B: WEIGHS AGAINST**: pay on an EBITDA figure and on sales volume, with no capital charge **[M1995-010]**,
  **[M2016-083]**; the independent chair weighs for.

## Q7: WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**, at "the yield on
long-term U.S. bonds" **[L2000-021]**, 5.56%; arithmetic in `q7.py` and `q7_output.txt`.

**The input.** Owner cash as Q4 recasts it, all-equity basis (before corporate interest, after the company's tax, the
finance arm funded by its non-recourse debt under this run's confessed CONVENTION): 64.75 / 489.5 / 504.5 / 641.75 /
727.25 for 2021 to 2025 ($M).

**The specifics, in order.**
- **(a) The base.** 2021 is aberrational on the filer's own description ("Our business has been and continues to be
  adversely impacted by the COVID-19 pandemic", FY2021 10-K, Item 7) and holds only five months of Diamond. A full cycle,
  peak to peak, cannot be built across the two purchases from the filer's own series, so the base is the average of
  2022 to 2025, **$590.75M**, with the literal 2021 to 2025 window, $485.55M, shown beside (this run's reading of (a);
  see the framework section below).
- **(c) Acquisitions.** Cash paid for businesses in the window: $1,592M (2021, Diamond, net of cash acquired), $74M
  (2023), $1,444M (2024, Bluegreen): **$3,110M**, against half of owner cash before purchases over the window, $1,214M.
  Net purchases exceed half: **the serial acquirer's rule applies** and the central figure is the organic pair, purchases
  left out, organic growth as the filer reports it: the pro forma and actual revenue chain 2022 to 2025 (3,835; 3,978;
  pro forma 5,013 to 5,028; 5,047), **1.46% a year**. The default pair is shown beside: purchases deducted ($379.5M a
  year over the base years), total growth of owner cash 2022 to 2025 credited (14.11% a year; the cap check passes,
  year-ten owner cash at 6.3% of sales against the highest share earned, 14.4%). Diamond is classed an acquisition by its
  larger cash part (Q6). Elara (closed 2026-04-29, after the window): no earnings of its own are filed, so it is credited
  at nothing, and its price and assumed debt are already in the 2026-06-30 balance sheet.
- **(d) Working capital** is inside operating cash and counted, including the loan book's growth net of its
  non-recourse funding.
- **(e) Maintenance.** The filing allows one guess: VOI inventory spending above the cost of the inventory relieved by
  each year's sales (Item 7's spending table against cost of VOI sales with the construction deferrals undone): -81 /
  95 / 188 / 112, averaging **$78.5M** a year of growth spending. Capital spending on property and software is kept as
  maintenance, since the 10-K calls the renovations "necessary to stay competitive". Maintenance-only base: $669.25M.
  Charged against the growth it buys (1.46% a year), the growth case is worth less than the maintenance-only no-growth
  case: **the inversion** (growth "can destroy value" **[L2000-023]**): the maintenance-only no-growth case is the top of
  the range and the growth case the bottom.
- **(b) Decline**: not shown on the organic measure. **(f) The cap**: 1.46% is below the discount rate; nothing cut.

**The range** (all-equity, less net debt of **$4,604M**: corporate debt $4,876M less cash $272M at 2026-06-30, 10-Q;
restricted cash and operating leases left out; non-recourse debt treated as the finance arm's working capital, $2,896M,
with the alternative beside; 77.724 million shares):

| Case | Base ($M) | Growth | Value per share at 5.56% | Expected return at $35.18 |
|---|---|---|---|---|
| **Central top: maintenance-only, no growth** | 669.25 | 0% | **$95.63** | **9.12%** |
| **Central bottom: all spending, organic growth** | 590.75 | 1.46% | **$94.23** | **8.92%** |
| Beside: all spending, no growth | 590.75 | 0% | $77.47 | 8.05% |
| Beside: default pair, purchases deducted, total growth | 211.25 | 14.11% | $90.00 | 8.12% |
| Beside: default pair, purchases deducted, no growth | 211.25 | 0% | negative $10.35 | 2.88% |
| Beside: literal window 2021 to 2025, organic growth | 485.55 | 1.46% | $66.90 | 7.37% |
| Beside: non-recourse debt counted in net debt ($7,500M) | 495.44 | 0% to 1.46% | $18.15 to $32.21 | 4.84% (no growth) |

**The floor, tested first** (CONVENTION, about ten percent: "we don't want to buy equities where our real expectancy is
below 10 percent" **[M2003-149]**). No case earns it at the price: the best is 9.12%. Owner cash of about $734M a year
with no growth would be needed to earn ten percent on the market value plus net debt of $7,338M; the four-year base is
$591M and its maintenance-only form $669M; only the single year 2025 ($727M) comes near, and one year does not set the
base **[L2005-003]**. The equity-only figures are higher (owner cash after interest $410.75M, 15.0% on the market value;
expected returns 16.3% to 17.9%) because $4.6B of corporate debt at about 5.7% takes the first claim on an unlevered
yield of about 8% to 9%; the equity-only figure "never decides alone", and the speakers judge deals "on an all-equity
basis" **[L2017-004]**. The interest shield at 21% instead of 25% moves the best case to about 9.25%.

- **Reading.** The range at the government rate sits far above the price ($94 to $96 against $35), but that is the
  leverage speaking: at the price, the whole business offers about 9% on what an owner of all of it would pay, below the
  floor, and the width test does not arise. Even read generously (a single good year, the maintenance guess, a lower tax
  shield) the answer needs a pencil to reach ten percent, which is the close call the rows refuse: "if you really need a
  calculator to figure out that it's — the discount rate is 9.6 percent instead of 9.8 percent — forget about the whole
  exercise" **[M2009-005]**.
- **VERDICT: OUT.** No case earns the floor at the price **[M2003-149]**; on the all-equity basis **[L2017-004]**.

**Fair price (a reporting figure, never a verdict; Part VII):** **$25.77 a share** on the all-equity basis (central
cases at ten percent: maintenance-only no growth $26.87, all-spending organic growth $24.67, averaged, less net debt);
**equity-only $60.64** beside it (owner cash after all interest, the same two cases, no net debt deducted). Both after the
company's own tax. Beside, not reported as fair: the all-spending organic pair $20.72; the default pair negative; the
non-recourse-as-debt reading negative. No cheap price is reported.

*Written back to Q6 (the buyback line), with this commit:* the bottom of the central range is $94.23 a share; the prices
paid in 2025 and early 2026 (about $40 to $47) sit below it, so by the convention the programme is read by what it did and
not weighed against for naming no price **[L2016-002]**; recorded beside it, those prices are above the fair price of
$25.77, so the purchases bought a return below the floor for the continuing owners.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7** (Q1 IN; Q2 IN narrowly; Q3 against; Q4 against, no STOP; Q5 integrity IN, ability against narrowly; Q6
against on both parts). Value range **$94.23 to $95.63 a share** (all-equity basis, organic pair with the maintenance
inversion, at the 5.56% Treasury) against **$35.18**; no case earns the floor of about ten percent at the price on the
all-equity basis (best 9.12%), because $4.6B of corporate debt sits ahead of an unlevered yield of about 8% to 9%. Fair
price $25.77 all-equity, $60.64 equity-only (reporting figures, not verdicts). Not a TOO HARD, so no research pass.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box unchanged (operator rule 2).
- **Q8.** The 30-year Treasury yields 5.56% (2026-10-13). The expected return on the whole business at the price, by the
  Q7 cases, is 8.05% to 9.12%; the equity-only cases 15.0% to 17.9%.
- **Q9.** Corporate debt $4,876M at 2026-06-30 (10-Q), weighted rate 5.691% at 2025-12-31; maturities (Note 15, FY2025
  10-K): term loan A $400M (2028), term loan B $851M (2028; refinanced on 2026-07-17 by a new $850M term loan due
  2033, 8-K `0001140361-26-028827`), notes $850M (2029), revolver $130M drawn (2030; $809M undrawn), term loan B $887M
  (2031), notes $500M (2031), secured notes $900M (2032). Non-recourse debt $2,896M (10-Q): the Timeshare Facility due
  2027 ($615M drawn, $235M undrawn at 2025-12-31) and securitized notes due 2033 to 2044; the securitizations carry
  "portfolio performance requirements related to default, delinquency and recovery rates, which, if not met, would result
  in loss or disruption of cash flow" (Item 1A). Coverage on the speakers' definition, pre-tax earnings over interest
  **[L2012-002]**: ($175M + $311M) / $311M = 1.56 times for 2025; 2.5 times for 2023. Surety commitments $439M; contractual
  obligations $9.4B over 14 years, $1.0B in 2026 (Item 7). For a whole business offered, the "little or no debt"
  criterion **[R1997-001]** would not be met. The loan book defaults at about a tenth a year, and the warehouse must be
  renewed in 2027.
- **Q12.** Facts for the newspaper test **[M2008-011]**: the product is sold on a tour by a commissioned sales force, 67%
  of it financed at a weighted 14.7% under underwriting that does "not include certain traditional ability-to-pay
  factors, such as income verification"; about a tenth of the loan book defaults each year and the defaulting owner's
  interest returns to inventory for resale (Items 1, 1A, 7); exit companies target the acquired Diamond owners (Item 1A).
  None of the businesses Q12 names (casinos, tobacco, distributor-loading schemes, gambling, promotion on a borrowed
  reputation) is this business.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `9a53627a`); written question by question; committed after each
      (Q1 `b96fe649`, Q2 `7b315d7a`, Q3 `2c459b9e`, Q4 `5e831431`, Q5 `65a8418f`, Q6 `bd8cc1e9`, Q7 with the Q6 write-back
      `183f891d`, the close in the final commit).
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits; the lock is the dispatching
      session's (a lock file was seen in `Screens/_daily/` and not opened). Folding into the register is the dispatcher's.
- [ ] The blind rule: **one breach, declared at the top**: a listing of `Test Runs/` filtered for the ticker and name,
      run before the first fetch to check the dated path; it returned nothing. Commit subjects of another company's run were
      seen in the session preface and not used. No run file, holding review, `PORTFOLIO.md`, register or reading list was
      opened.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check.py` in the research folder: no
      E-ids, every M/L/R id in the CSV, every adjacent quotation inside its row); every filing fact carries its accession
      or names its document.
- [x] The order was kept; Q7 was the first STOP that failed; nothing after it is a clearance.
- [x] Owner cash after every real cost (stock pay, all capital spending, the loan losses, the integration costs), never a
      net-income proxy; the sovereign from the Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations, Q2, Q4); the facts for later questions are under AFTER
      THE STOP; no integrity flag is needed, since Q5 was answered.
- [x] Not a point-in-time run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings and yield lines were set aside.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Receivable-secured non-recourse debt has no rule.** Q7's convention covers inventory-secured trade finance only. For
a seller that lends to its buyers and funds the book with non-recourse securitizations, the choice decides everything: as
the finance arm's working capital (this run's confessed CONVENTION, by extension) the fair price is $25.77; counted in
net debt while the loan growth is also charged in operating cash, it is negative, because that reading charges the
receivables' growth without counting the receivables. The run used the first and showed the second; a ruling is owed.
(2) **EBITDA talk sits in two places.** Q4's "Why confusion is a STOP" still carries the count, "about zero"
**[M2002-026]**, and Q4's rules-OUT list still names "managements that talk it", while the 2026-10-06 convention sends a
featured adjusted figure, guidance and the make-the-numbers habit to Q5 as a weighing. A management that guides and pays
on Adjusted EBITDA falls under both; this run followed the later, more specific convention and judged it at Q5. (3)
**Specific (a) and the serial acquirer.** A full cycle cannot be built across two purchases when the organic pair is
central; the run took the window less its aberrational first year and showed the literal window beside. (4) **"Ordinary
returns" names no capital base.** On tangible capital the field earns well; on what buyers paid, ordinarily or poorly. The
run judged the business on tangible capital (**[M2011-060]**) and sent the purchase prices to Q3 and Q6; another analyst
could close Q2 OUT on the other base. (5) **The parts convention says "operating profit"**; HGV reports only segment
Adjusted EBITDA, which was used for want of anything else. (6) **"Organic growth, as the filer reports it"**: HGV reports
pro forma revenue, not organic owner cash; the run chained the pro forma revenue. (7) **The value range at the government
rate misleads under leverage**: the range ($94 to $96) sits nearly three times the price while no case earns the floor;
for a levered business the floor test and the range point in opposite directions, and the reported range invites a
"cheap" reading that the floor refuses. (8) **The maintenance guess for a developer** rests on the cost of VOI sales under
the relative sales value method, which counts on future recoveries of defaulted inventory, so the guess likely overstates
growth spending and so flatters the maintenance-only case; it did not change the box.
