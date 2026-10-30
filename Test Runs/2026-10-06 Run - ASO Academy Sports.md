# Company Run — Academy Sports and Outdoors, Inc. (NASDAQ: ASO) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched blind: `PORTFOLIO.md`, the holding
reviews, the resume-state files, the run queue and the prepped reading list were not opened, so whether the operator
holds ASO is unknown to this analyst.

**CONTAMINATION DECLARED.** A directory listing of `Test Runs/` showed file names only, none opened: an earlier run on this
name, `2026-07-16 Run - Consumer & Leisure 6-pack (HOG THO PRKS BYD ASO SBH).md` (pre-v4.1, binds nothing; its verdict
was not seen), and the names of the 2026-10-05 runs and research passes of other companies (among them BOOT Boot Barn and
CALY Callaway Golf). The commit subjects shown at session start named PTEN and BTU v5 runs closing OUT at Q2 (coal and
drilling); no retailer verdict was seen. `tools/run.py` prints v4 material; only its arithmetic lines were read (Part VII).

**Analyst's incentive line** (operator rule 9): none known. The analyst holds no position and was asked to hunt hardest
for the evidence against the business.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $51.98 (close 2026-10-05; `tools/run.py`; aggregator quote, live price only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **61,578,891** as of
  2026-09-02 (Form 10-Q for the quarter ended 2026-08-01, filed 2026-09-09, accession `0001817358-26-000149`;
  `python Screens/cover_shares.py ASO`). Balance-sheet count 62,028,664 at 2026-08-01, the difference being
  repurchases after the quarter end. No other class; no preferred issued.
- **Market cap:** $51.98 × 61.579M = **$3,201M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2025 (year ended 2026-01-31), filed 2026-03-17, accession `0001817358-26-000031`: Item 1, Item 1A
    (competition, vendors, firearms, leases), Item 7 in full, balance sheet.
  - 10-Q for the quarter ended 2026-08-01, filed 2026-09-09, accession `0001817358-26-000149`: income statement,
    balance sheet, debt note, the IEEPA tariff-refund note, buybacks.
  - 8-K of 2026-09-09 with the second-quarter release (Exhibit 99.1), accession `0001817358-26-000146`: guidance and
    the non-GAAP reconciliation.
  - DEF 14A filed 2026-04-21, accession `0001817358-26-000063`: bonus and equity plan design, the 2025 payouts,
    the Summary Compensation Table, ownership.
  - IPO prospectus (424B4) filed 2020-10-02, accession `0001193125-20-262578`: the five-year table FY2015 to FY2019.
  - 10-Ks for fiscal 2020 (`0001817358-21-000059`), 2021 (`0001817358-22-000039`), 2022 (`0001817358-23-000062`),
    2023 (`0001817358-24-000042`) and 2024 (`0001817358-25-000027`): results tables and comparable-sales sentences.
  - Competitors: Dick's Sporting Goods 10-Ks for fiscal 2019 (five-year table, `0001089063-20-000014`), 2021
    (`0001089063-22-000031`), 2022 (`0001089063-23-000023`), 2023 (`0001089063-24-000037`), 2024
    (`0001089063-25-000012`) and 2025 (`0001089063-26-000007`); Hibbett 10-K XBRL facts FY2014 to FY2023
    (accessions `0001017480-15-000006` to `0001017480-24-000043`, transcription).
- **One figure cross-checked against the filed statement:** fiscal 2025 net cash from operating activities,
  $434,798 thousand in the 10-K's cash-flow summary (`0001817358-26-000031`), equals the 434.8 that `tools/run.py`
  read from the XBRL. Net sales $6,053,414 thousand likewise agree.
- **`tools/run.py ASO` arithmetic lines only** (saved at `Test Runs/_research 2026-10-06 ASO/run_py_output.txt`):
  owner cash = operating cash flow less stock pay less capital spending, with the depreciation variant beside it;
  the cash-flow lines below were rechecked against the XBRL company facts and extended to five years.

| Fiscal year (ended) | OCF | Stock pay | Capex | D&A | Owner cash, all capex | Owner cash, D&A basis |
|---|---|---|---|---|---|---|
| FY2021 (2022-01-29) | 673.3 | 39.3 | 75.8 | 105.3 | 558.2 | 528.7 |
| FY2022 (2023-01-28) | 552.0 | 21.2 | 108.3 | 106.8 | 422.5 | 424.0 |
| FY2023 (2024-02-03, 53 weeks) | 535.8 | 24.4 | 207.8 | 110.9 | 303.6 | 400.5 |
| FY2024 (2025-02-01) | 528.1 | 26.6 | 199.6 | 118.1 | 301.9 | 383.4 |
| FY2025 (2026-01-31) | 434.8 | 21.2 | 212.7 | 122.9 | 200.9 | 290.7 |
| **five-year mean** | | | | | **357.4** | **405.5** |

USD millions. Owner cash is after cash interest (about $35M a year since FY2023) and after cash tax. FY2021 stock pay
includes a $24.9M vesting charge set off by KKR's May 2021 sale. FY2025 operating cash carries two distortions in
opposite directions: a $118.7M working-capital outflow from inventory bought early ahead of tariffs, and cash tax of only
$37.8M against a $109.3M provision, because of deferred taxes from the 2025 tax act (10-K MD&A). Sale-leaseback proceeds
(in investing) are not netted against capex: they turn owned stores into rent, which is already inside operating cash.

**Maintenance capital, as far as the filing allows a judgment.** The 10-K splits capex: new stores $119.9M, corporate,
e-commerce and IT $41.3M, existing stores and distribution centres $51.5M in FY2025; the non-new-store total was $107.4M
(FY2023), $91.9M (FY2024) and $92.8M (FY2025), against D&A of $110.9M, $118.1M and $122.9M. Maintenance therefore sits
at or a little below depreciation; the D&A basis is taken as the maintenance case and the all-capex basis as the
convention's central input.

### The balance sheets, eight to ten years of them, read before the income account
Read first, as the framework asks: "balance sheets over an 8 or 10 year period before I even look at the income
account" **[M2025-032]**. The file closes at Q2, so the reading is done here (template, Q4 note).

| Year-end | Cash | Inventory | Total assets | Funded debt | Equity | Goodwill + trade name | Lease liabilities |
|---|---|---|---|---|---|---|---|
| FY2015 (2016-01-30) | 52 | 1,028 | 3,257 | 1,699 | 689 | n/r | pre-ASC 842 |
| FY2016 (2017-01-28) | 55 | 1,091 | 3,258 | 1,681 | 756 | n/r | pre-ASC 842 |
| FY2017 (2018-02-03) | 31 | 1,223 | 3,323 | 1,675 | 833 | n/r | pre-ASC 842 |
| FY2018 (2019-02-02) | 76 | 1,134 | 3,239 | 1,625 | 857 | n/r | pre-ASC 842 |
| FY2019 (2020-02-01) | 149 | 1,100 | 4,331 | 1,463 | 988 | 1,439 | on balance sheet |
| FY2020 (2021-01-30) | 378 | 990 | 4,384 | 785 | 1,112 | 1,439 | 1,230 |
| FY2021 (2022-01-29) | 486 | 1,172 | 4,585 | 687 | 1,467 | 1,439 | 1,161 |
| FY2022 (2023-01-28) | 337 | 1,284 | 4,595 | 587 | 1,628 | 1,440 | 1,181 |
| FY2023 (2024-02-03) | 348 | 1,194 | 4,677 | 488 | 1,955 | 1,440 | 1,209 |
| FY2024 (2025-02-01) | 289 | 1,309 | 4,901 | 486 | 2,004 | 1,441 | 1,301 |
| FY2025 (2026-01-31) | 330 | 1,504 | 5,277 | 484 | 2,171 | 1,442 | 1,409 |
| Q2 FY2026 (2026-08-01) | 298 | 1,657 | 5,508 | 494 | 2,178 | 1,442 | 1,475 |

USD millions. FY2015 to FY2019 from the IPO prospectus's balance-sheet data (`0001193125-20-262578`; "Total debt, net of
deferred loan costs"); FY2019 to FY2025 from the 10-Ks via `tools/run.py`; the last row from the 10-Q. n/r = not read
for those years (not in the prospectus summary table).

**What the balance sheets say.**
- **The KKR leverage was paid down by the pandemic, not by the business before it.** Funded debt barely moved from
  FY2015 to FY2018 ($1,699M to $1,625M) while equity crept up from $689M to $857M. The prospectus records that in 2019
  the company bought $147.7M of its own term loan in the open market for $104.6M, about 71 cents on the dollar; lenders
  were pricing the pre-pandemic business as a credit at risk. The debt fell by $678M in the single pandemic year
  (FY2019 to FY2020) and to $484M by FY2025. Since May 2026 it is one $500M issue of 5.875% senior secured notes due
  2031 plus an undrawn $1.0B asset-based revolver due 2031 (10-Q note 4). No maturity before 2031.
- **Goodwill and the trade name ($862M and about $580M) are the 2011 buyout's purchase accounting and have never been
  written down**, including through four years of falling comparable sales; they are 66% of FY2025 equity. Tangible
  equity at FY2025 is about $729M.
- **Inventory has outrun sales since the unwind.** Inventory to sales: 22.1% (FY2015), 22.8% (FY2019), 17.3% (FY2021),
  20.1% (FY2022), 19.4% (FY2023), 22.1% (FY2024), 24.8% (FY2025). The filer attributes FY2025's rise to tariff
  pull-forward. Payables carry much of it ($638M at FY2025 year-end; $752M at 2026-08-01).
- **Retained earnings rose from $987M (FY2020) to $1,914M (FY2025) but have stalled since** ($1,919M at 2026-08-01
  after $190.6M of half-year net income), because the buybacks are charged against them.
- **The real fixed obligation is the leases, not the notes:** lease liabilities $1,475M at 2026-08-01, undiscounted
  operating lease payments $2,368M (10-K, FY2025), cash rent $245M in FY2025, store leases of 15 to 20 years that
  "we generally cannot cancel" (10-K Item 1A).
- What the balance sheets cannot say: whether the post-2021 margin is the business's own or the industry's. That is Q2.

---
## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**? Only if
I knew where its earnings would sit, which is the castle question. Margin of safety: "with pencil and paper, it’s too
close to think about" **[M1996-084]**; the computation below is within a few percent
of the price at its central case, which is the pencil case. The analyst's habits: contrary evidence is written down "in
the first 30 minutes" **[M1997-127]**, and scuttlebutt here is the competitors' own filings, read "to possibly reject
your original hypothesis." **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]** (evidence *for* the business, against this run's closing view):
1. Gross margin rose from 29.6% (FY2019) to 34.8% (FY2025) and operating margin from 3.7% to 8.5%, and has held at
   8.5% to 13.4% for five years after the boom (10-Ks).
2. Academy sold more per square foot than Dick's before the pandemic: $264 in FY2019 (prospectus) against about $209
   for Dick's ($8,751M on 41.8M square feet, DKS FY2019 five-year table). Munger names this as a retailer's scale
   advantage: "a retailer that just has huge advantages in terms of buying cheaper and enjoying higher sales per square
   foot." **[M1995-039]**.
3. New-store sales are growing: 68 stores opened since 2022; the 47 open a year or more average about $13M of sales;
   new stores "comp positive mid single digits" (8-K release 2026-09-09).
4. Vendor access improved: the Jordan Brand was added in the first quarter of 2025 (10-Q), and the 10-K says "we
   receive favorable product allocations from leading suppliers."
5. Rivals left the field: the prospectus says e-commerce disruption "played a role in shutting down some of our peers";
   Hibbett was taken private (its XBRL stops at FY2023).
6. First-half FY2026 comparable sales turned positive (+1.1%), the first positive half since FY2021 (10-Q).
7. Retail's Q1 warning cut the other way for a time: Academy had operated since 1938 and survived the decade that closed
   several rivals.

## THE STANDING RULE
Owning ASO for cash, at a size that a total loss would not touch what the buyer needs, puts the buyer at no risk of
ruin; the rule binds the buyer's financing: "borrowed money has no place in the investor's tool kit" **[L2014-005]**;
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. No purchase is
made in any case (the file closes at Q2).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**, where understanding is "a reasonable fix on
  about what the earning power and competitive position will look like in five or 10 years." **[M2012-065]**.
- **What it does.** Buys branded and private-label goods from about 1,500 vendors and sells them in 322 large leased
  stores (average 70,000 square feet) in 21 southern and midwestern states, 117 of them in Texas, plus e-commerce at
  11.7% of merchandise sales; outdoors 31%, apparel 27%, sports and recreation 22%, footwear 20% of FY2025 sales;
  national brands about 78% of merchandise sales, 19 private brands about 22%; firearms about 6% of sales; no brand over
  about 12% (10-K Item 1). No fast-moving technology; the product is simple and the change that matters is in where
  the customer buys, not in what.
- **The key variables**, "trying to identify the key variables in that particular business, and evaluating how
  predictable they were first" **[M1998-044]**. They are (1) comparable transactions, (2) gross margin, (3) vendor
  allocation of the wanted brands, (4) new-store productivity. Each can be read from the filings; (1) and (2) are what Q2
  tests.
- **Do the past statements tell me the future ones?** **[M2008-033]** Not reliably: the FY2015 to FY2019 statements
  (operating margin 2.7% to 5.4%) said nothing of FY2021 (13.4%), and the speakers' own warning is about this kind of
  business: "many retailing businesses I can think of" with "I’m not sure I’d know where we would stand in the
  competitive pecking order five or 10 years from now." **[M1996-062]**; "it’s easy to sort of think you understand
  retail, and then subsequently find out you don’t" **[M2014-052]**.
- **Routing.** This is not the fast-technology case that closes at Q1 ("it won’t make it through the filter."
  **[M1998-008]**); it is a castle question: where Academy stands against its rivals, which the filings and the rivals'
  filings can test. The doubt is recorded, not hidden: "if you have doubts about something being into your circle of
  competence, it isn’t." **[M2002-092]**. Taken here as a doubt about the castle, not about what the business is; had
  it been taken as a doubt about the circle, the file would close at Q1 TOO HARD and the box would still not be IN.
- **VERDICT: IN, narrowly.** The business is plain and its key variables can be named and read; whether they hold is
  Q2's question **[M2012-065]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "How much do they depend on the genius of the lord in the
castle?" **[M1995-038]**.

- **Unit volume and share of mind.** The speakers measure the place in the mind by units: "We measure it by unit cases
  sold" **[M1999-054]**. Academy's comparable transactions: down 8.2% (FY2022), down 6.3% (FY2024), down 4.2% (FY2025),
  down 3.6% in the first half of FY2026 and 5.3% in its second quarter; FY2023 comparable sales fell 6.5% (10-Ks
  `0001817358-23-000062`, `-25-000027`, `-26-000031`; 10-Q). Average ticket rose each time; the customers did not.
  Private-brand reach fell from about 60% of customers buying an owned-brand item (2019, prospectus) to about 53%
  (2025, 10-K).
- **Is the moat widening or narrowing?** "whether it’s likely to widen further or shrink on you" **[M1999-108]**. The
  competitor row (below) is the answer: over the eleven fiscal years FY2015 to FY2025 Academy's comparable sales rose
  about **3% in total** (nominal, so a real decline), while Dick's rose about **61%**, each compounded from its own 10-Ks.
  Before the pandemic Academy's comps fell four years running (FY2016 to FY2019: −3.4%, −5.2%, −2.5%, −0.7%) while
  Dick's were mixed (+3.5%, −0.3%, −3.2%, +3.7%); after the boom Academy fell four years running (−6.4%, −6.5%, −5.1%,
  −1.5%) while Dick's rose in three of four (−0.5%, +2.4%, +5.2%, +4.5%). "We have found in a long life that one
  competitor is frequently enough to ruin a business." **[M2012-108]**.
- **Who sets the price.** The filer says it in its own risk factors: "if our competitors reduce their prices, it may be
  difficult for us to reach our net sales goals without reducing our prices", and "The ability of consumers to compare
  prices on a real-time basis through the use of smartphones, apps, and digital technology puts additional pressure on
  us to maintain competitive prices" (10-K Item 1A). That is the condition the speakers would not own: "whatever he
  charged for gas was my price." **[M2012-109]**; "he determined our profit, because we looked at his price every day."
  **[M2023-079]**.
- **The brand in the customer's mind, and who owns it.** 78% of merchandise sales are other companies' brands. The
  speakers' test is whether the trust sits with the retailer or the product: "to the extent that people trust Costco or
  Walmart more than they [...] trust the brand, then the value of having the brand moves over to the retailer from the
  product itself." **[M2001-090]**. Here it runs the other way: the brands decide the allocation ("brand name
  merchandise that is in high demand may be allocated by brand name vendors based upon the vendors’ internal criterion
  which is beyond our control"), sell around the retailer ("vendors increasingly sell their products directly to
  customers"), and are under no long-term contract ("We generally do not have long-term written contracts with our
  suppliers") (10-K Item 1A). The Jordan Brand arrived in 2025 at the vendor's choice and can leave the same way.
- **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the low
  bid." **[M2017-009]**. Academy's own positioning is the value bid, "a value-based assortment" (10-K Item 1) priced against the same
  Nike, Yeti and Carhartt sold by Dick's, Walmart, Amazon and the brands' own sites; the customer can switch on a
  phone in the aisle, by the filer's own account. Of the commodity seller the speakers say "most insureds don't care from
  whom they buy." **[L2004-003]**.
- **The low-cost position.** The exception in a commodity field is the low-cost operator, and the high-cost one "must
  lower its costs to competitive levels or face extinction." **[L1994-035]**. No evidence Academy holds the title:
  its operating margin over FY2015 to FY2024 averaged about 7.2% against Dick's 8.5% (below); its SG&A ran 25.9% of sales
  in FY2019 and 26.3% in FY2025 (10-Ks) against Dick's 24.8% in FY2019 (DKS five-year table). Higher sales per square
  foot (contrary evidence 2) did not turn into lower costs or higher margins.
- **Would it stand without the lord?** The speakers answer for retail in general: "In retailing, to coast is to fail."
  and "Your competitor is always copying and then topping whatever you do." **[L1995-008]**; "For a retailer, hiring that
  nephew would be an express ticket to bankruptcy." **[L1995-009]**; "Buying a retailer without good management is like
  buying the Eiffel Tower without an elevator." **[L1995-006]**. The record shows it: under KKR's ownership and the
  previous management the comparable business shrank for four years and the term loan traded near 71 cents.
- **The attacker with money** **[M2011-015]**: could a well-funded rival take Texas? The attackers are already inside:
  Dick's (House of Sport and Field House formats, now with Foot Locker), Walmart, Amazon, Bass Pro and the brands' own
  stores. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
- **Ask the competitors.** The silver-bullet question, "get rid of one of your competitors, who would it be?"
  **[M2017-022]**, cannot be put; the competitors' filings answer it indirectly: Dick's grew comparable sales through
  the years Academy's fell, in the same categories (footwear, athletic apparel), while noting its own declines in "outdoor-related categories including
  hunt" (DKS FY2024 10-K), the categories where Academy is heaviest.
- **Fewness of rivals is not the cure.** The margin step-up after 2020 is shared: Dick's gross margin went from 29.2%
  (FY2019) to 35.9% (FY2024) and Hibbett's from 32.4% to 38.2% and back to 33.8% (XBRL). It is an industry condition
  after the exits, not a moat of Academy's own; "you can have only two competitors and they’re still terrible
  businesses" **[M2013-052]**.
- **What could destroy, modify or reduce it** **[M2000-014]**: the brands' direct selling and allocation; the online
  price check; Dick's in Academy's markets; tariffs on private-label goods (the proxy records "private brand tariff
  expenses that exceeded planned tariff costs" in FY2025); firearms rules (about 6% of sales).

**The competitor row** (same metrics, each from its own filings):

| Fiscal year | ASO comps | DKS comps | ASO op. margin | DKS op. margin | HIBB op. margin |
|---|---|---|---|---|---|
| FY2015 | +3.1% | −0.2% | 5.4% | 7.4% | 11.9% |
| FY2016 | −3.4% | +3.5% | 3.1% | 5.7% | 9.9% |
| FY2017 (53 wks) | −5.2% | −0.3% | 3.3% | 5.6% | 5.9% |
| FY2018 | −2.5% | −3.2% | 2.7% | 5.3% | 3.7% |
| FY2019 | −0.7% | +3.7% | 3.7% | 4.3% | 3.0% |
| FY2020 | +16.1% | +9.9% | 7.4% | 7.7% | 6.9% |
| FY2021 | +18.9% | +26.5% | 13.4% | 16.5% | 13.5% |
| FY2022 | −6.4% | −0.5% | 13.2% | 11.8% | 9.9% |
| FY2023 (53 wks) | −6.5% | +2.4% | 11.0% | 9.9% | 7.9% |
| FY2024 | −5.1% | +5.2% | 9.1% | 11.0% | acquired |
| FY2025 | −1.5% | +4.5% (DICK'S business) | 8.5% | 6.4% (Foot Locker inside) | |
| **compounded FY2015–FY2025** | **+3%** | **+61%** | avg FY15–24 **7.2%** | avg FY15–24 **8.5%** | avg FY15–23 **8.1%** |

ASO from the prospectus (FY2015 to FY2019) and its 10-Ks; DKS from its 10-Ks (FY2015 to FY2019 from the FY2019 five-year
table, `0001089063-20-000014`; FY2020 and FY2021 from `0001089063-22-000031`; FY2022 and FY2023 from
`0001089063-24-000037`; FY2024 and FY2025 from `0001089063-26-000007`) and XBRL operating margins; HIBB XBRL only
(transcription, flagged). Definitions differ in detail (both include e-commerce). DKS FY2023 comps were later restated
to +2.6%. **Bass Pro Shops** (with Cabela's) is private and files nothing with the SEC: not read, flagged. **Walmart**
reports no sporting-goods line: not separable, flagged. **Amazon** likewise.

- **The single fact that closes it.** Over FY2015 to FY2025 Academy's comparable sales rose about 3% in total while
  its largest public rival's rose about 61%, each from its own 10-Ks, and Academy's comparable transactions fell in every
  year from FY2022 to FY2025 and again in the first half of FY2026. A castle that loses unit volume to one rival for a
  decade, in goods it does not own and at prices it says rivals set, is shown on the evidence to be open
  **[M1999-108]**, **[M2012-108]**, **[M2012-109]**.
- **Why OUT and not TOO HARD.** TOO HARD is for the castle whose future cannot be judged, the moat seen as "tenuous in
  any way" of which "We don’t know how to valuate that" **[M2000-019]**. Here the judgment is made on the evidence, and it is against:
  "Business history is filled with "Roman Candles," companies whose moats proved illusory and were soon crossed."
  **[L2007-004]**. The rows' three boxes are "three boxes at the company: in, out, and too hard." **[M2006-013]**; a
  castle shown to be open is OUT **[M2011-015]**.
- **VERDICT: OUT** **[M1999-108]**, **[M2012-108]**, **[M2012-109]**, **[M2023-079]**, **[L1995-008]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed OUT). Facts gathered, recorded without a weighing: capex rose from $41M (FY2020) to $213M
(FY2025) with the reopened store programme; new stores cost about $5.0M each in capex in FY2025 ($119.9M for 24 stores)
plus about $0.6M of pre-opening expense, and average about $13M of first-year-plus sales against about $19M for the
chain; the filer's own "ROIC" is computed on EBITDA before rent.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets are read in Step 0. Facts gathered, not weighed: the accounts are not
confusing; the headline Adjusted EPS adds back stock pay, the habit of which the letter says "is the most egregious
example" **[L2015-003]**; the second-quarter 2026 gross margin of 40.4% includes 510 basis points of one-time IEEPA
tariff refunds ($83.7M, booked in cost of goods sold) while the $72.2M paid to the buyer of the refund claims sits below
operating income in "other expense" (10-Q note 10); both are disclosed and Adjusted EBIT starts from net income, so the
payment is inside it.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts gathered: CEO Steve Lawrence since June 2023 (joined 2019 as merchant); CFO Carl Ford since July 2023;
chairman Ken Hicks (former CEO) owns 2.88%; KKR's last shares were sold in the September 2021 secondary (10-K FY2021).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts gathered, not weighed: buybacks of $1,855M for 39.9M shares from FY2021 to mid-2026 at an average of
about $46.47 (FY2021 $38.93, FY2022 $41.12, FY2023 $55.91, FY2024 $56.28, FY2025 $50.62 per the 10-K, first half FY2026
$54.51), under a $700M programme that names no price; by subtraction about 10M shares were issued to employees and
option holders over the same span (5.5M options exercised in FY2021 alone); the bonus pays 45% on net sales and 45% on
Adjusted EBIT, which excludes stock pay, and the committee raised the FY2025 Adjusted EBIT for bonus purposes from
$543.4M to $594.7M by excluding "private brand tariff expenses that exceeded planned tariff costs", lifting that
metric's payout to 80.1% of target (DEF 14A); the 2022 performance units earned their missed portion on a stock-price
test. These would have weighed against at Q6. The row on pay that rewards only the upside calls such plans artful
forms of "heads I win, tails you lose." **[L1994-020]**; the question is not reached.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting request is answered below, in the computation section headed as operator rule 3 requires.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Fact gathered: one $500M note due 2031, undrawn $1.0B revolver due 2031, $1.48B of lease liabilities.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Firearms and ammunition are about 6% of sales; they are not among the businesses the framework names.)

---
## COMPUTATION — NOT A CLEARANCE
*Reporting at the owner's request, not a rule change. The file closed OUT at Q2; nothing below is entry language, and
no figure here reopens the file. The rows' answer to a cheap price on an open castle: "What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**. Script: `Test Runs/_research 2026-10-06 ASO/value.py`.*

**(a) VALUE RANGE, the Q7 convention as written** (five-year average owner cash after every real cost, carried at the
growth shown on aggregate owner cash for ten years, then zero nominal growth, discounted at the 5.66% sovereign):
- All-capex basis: five-year mean $357.4M; growth shown FY2021 to FY2025 is **−22.5% a year** ($558.2M to $200.9M).
  Range **$19.82 (shown-growth end) to $102.55 (no-growth end)** a share, a ratio of 5.2 to 1. By the convention a range
  wider than about three to one closes TOO HARD.
- D&A basis (the depreciation variant the convention asks to show): mean $405.5M, growth shown −13.9% a year; range
  **$40.29 to $116.33**, 2.9 to 1.
- The window's first year is the pandemic peak, so "If either year was aberrational, any calculation of growth will be
  distorted." **[L2005-003]**: the negative growth and the high no-growth end are both artefacts of the boom.

**(a′) WHOLE-CYCLE VARIANT** (CONVENTION of this run, confessed: the window holds the boom and its unwind, so the
cash input is rebuilt from the whole span instead). Operating margin averaged over FY2015 to FY2025, eleven fiscal
years (four declining pre-pandemic years, two boom years, five unwind years): **7.34%** (pre-pandemic FY2015 to FY2019
alone: 3.64%; FY2021 to FY2025: 11.04%). Applied to FY2025 net sales of $6,053M: operating income $444M, less tax at
FY2025's 22.5% effective rate, plus D&A $122.9M, less capex, less after-tax interest ($36.2M × 0.775). Stock pay is
already an expense inside operating income and is not deducted twice; working capital is held flat.
- Whole-cycle owner cash: **$226.6M** with all capex deducted; **$316.4M** with maintenance = D&A.
- Growth shown over the whole span: net sales CAGR FY2015 to FY2025 **2.68%**, almost all of it new stores (209 to 322),
  since comparable sales compounded to about +3% in eleven years.
- Range at the sovereign: all-capex **$65.02 (no growth) to $80.40 (2.68% for ten years)**; D&A basis **$90.79 to
  $112.25**. Ratio 1.24 to 1. The price, $51.98, sits about 20% below the bottom of the all-capex range, which under the
  convention is the OUT case (inside or just below a narrower range), not a screamer.

**(b) FAIR PRICE** (the price at or below which the central case clears the ~10% floor).
- **Central case:** whole-cycle owner cash with maintenance capex = D&A, **$316.4M**, no growth credited (the comparable
  business did not grow in eleven years; growth capex is not deducted, so growth is not credited).
- **Tax treatment:** owner cash is after Academy's own corporate tax and after interest. The 10% is applied to it as the
  owner's return before the owner's own tax, reading the speakers' figure, "at least 10% pre-tax returns" with "after
  corporate tax" the holder's own tax **[L2002-020]**; the floor itself is the framework's CONVENTION from
  **[M2003-149]** and **[L2002-020]**.
- **Floor on equity**, the owner cash being after interest. Check on equity plus net debt: adding back after-tax interest
  ($28.1M) and deducting net debt at 2026-08-01 ($500M notes less $298M cash = $202M; leases excluded because rent is
  inside owner cash) gives $52.71 a share. The two agree within 3%.
- **FAIR PRICE: about $51 a share** ($316.4M ÷ 10% = $3,164M; ÷ 61.579M = **$51.39**), against **$51.98**. At today's
  price the central case returns about 9.9%.
- Sensitivities: all capex deducted, no growth: **$36.80**; all capex with 2.68% growth for ten years then flat, at 10%:
  **$44.18**; the five-year window average, all capex, no growth: **$58.04**.

**(c) CHEAP PRICE** (below which no pencil is needed). **Rule stated (ours):** the price at which the *pre-pandemic*
economics, FY2015 to FY2019 average operating margin of 3.64% on today's sales, maintenance capex = D&A, no growth,
still return the ~10% floor. Below it no forecast that the post-2020 margin lasts is needed: the price is covered by
what the business earned in its four worst modern years. On that rule owner cash is $142.7M and the **CHEAP PRICE is
about $23 a share ($23.17)**, 55% below the price. At $23 the central case would return about 22%. (With all capex
deducted the pre-pandemic economics leave $52.9M, $8.59 a share: before the pandemic the business funded its store
growth with almost nothing over.)

**Against the price:** $51.98 is at the fair price of the central case ($51.39), above every all-capex variant ($36.80 to
$44.18), and more than twice the cheap price ($23.17). It "ought to just kind of scream at you" **[M1996-084]**; it does
not. Buffett's word for the margin is a "big discount from that present value" **[M1997-126]**; there is none here.

**The buybacks against these figures** (for Q6, had it been reached): the average price paid since FY2021, about
$46.47, and every year's average since FY2023 ($50.62 to $56.28) sit at or above the central-case fair price and well
above the all-capex variants, not below a value "conservatively-calculated" **[L1999-023]**.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: comparable sales up about 3% in total over FY2015 to FY2025
against Dick's about 61%, comparable transactions down every year FY2022 to FY2025 and again in the first half of
FY2026, prices set by rivals and the online price check by the filer's own account, and 78% of sales in brands the
vendors own and allocate. Range not reached as a verdict; computation only: whole-cycle value at the sovereign
$65 to $80 (all capex), fair price about $51, cheap price about $23, against $51.98.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written in one pass after the reading, not question by question;
      **not committed**, at the dispatcher's instruction (no commits in this task). Deviation from write-early, declared.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession;
      no number without a row or a filing, except the conventions labelled as such.
- [x] The order was kept; Q2 closed OUT and nothing after it is a clearance; the value figures sit under the heading operator rule 3
      requires and carry no entry language.
- [x] Owner cash after every real cost (operating cash less stock pay less all capex, D&A variant beside it), never a
      net-income proxy (operator rule 5); the whole-cycle variant is built from operating income after tax, D&A, capex
      and interest, and is labelled a CONVENTION of this run. Sovereign from the US Treasury. Price flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (seven items, in the foundations).
- [x] No row dated after the anchor is cited (the run is dated today; not a point-in-time test).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its cash-flow lines were rechecked against the
      XBRL company facts.
- [x] `python tools/check_framework.py` run before reporting (result in the reply to the dispatcher). Fragment check:
      every quoted fragment beside an id was matched against that row by script; no E-ids.
- **Not obtained:** Bass Pro Shops (private, no SEC filings); Walmart's and Amazon's sporting-goods figures (not
  segmented); Academy's goodwill and trade-name balances for FY2015 to FY2018 (not in the prospectus summary); new-store
  four-wall profit (the filer discloses sales per new store, not profit); the identity of the largest vendor (12% of
  purchases, unnamed).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 against Q2 for a retailer.** Q1's list of what it rules OUT names retail as the narrated example of the business
   only believed to be understood **[M2014-052]**, and a 1996 row says of "many retailing businesses" that the pecking
   order five or ten years out is not known **[M1996-062]**, which reads as a Q1 TOO HARD; yet the routing paragraph sends to Q1 only the
   fast-changing industry and leaves the competitive question to Q2. Two analysts could close this name at Q1 TOO HARD
   (NATURE) or at Q2 OUT. I took Q1 IN and decided at Q2, because the evidence against the castle is affirmative and a
   TOO HARD would have hidden it. A line saying which question owns a retailer's place in the pecking order would settle it.
2. **The Q7 convention breaks on a window that starts at a boom.** Carrying the cash forward at the growth the business
   has actually shown gives −22.5% a year here, and the convention caps growth only from above (the Q3 arithmetic, the
   absurdity test). Its two ends ($19.82 and $102.55) are both artefacts of the base year **[L2005-003]**, and the 3:1 test
   then reads TOO HARD for a reason that is about the window, not the business. A floor on the shown-growth input (for
   example, the sales growth shown, or zero) or a whole-cycle rule for windows holding a boom is missing; I added a
   whole-cycle variant and labelled it ours.
3. **The floor's tax basis is not stated.** The convention says about ten percent pre-tax without saying pre whose tax.
   **[L2002-020]** reads as before the holder's corporate tax, so I applied 10% to after-company-tax owner cash; the other
   reading (10% on pre-company-tax cash) would raise the fair price to about $66 and change the answer. The convention
   should say which.
4. **The template's write-early and commit lines conflict with a no-commit dispatch.** Declared above.
