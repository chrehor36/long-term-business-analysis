# Company Run: ScanSource, Inc. (NASDAQ: SCSC), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch.

**POSITION NOTE, declared before any verdict:** not checked. The brief's blind rule forbids opening `PORTFOLIO.md`, so
whether the operator holds SCSC is unknown to this analyst. Working folder: `Test Runs/_research 2026-10-05 SCSC/`
(fetched filings, their text, and the scripts `fetch.py`, `h2t.py`, `hist.py`, `peers.py`, `value.py`, `ids.py`).

**CONTAMINATION, declared.** Before any work the session context showed (a) the subjects of the last five commits, three of
them v5 purchase runs of other companies dated 2026-10-05 (ADNT, MBC, AMR), each closing OUT at Q2 and each reporting a
fair price and a cheap price about half of it; (b) the untracked file name `Test Runs/2026-10-05 Run - KSS Kohls.md`
in the git status (name only, not opened); (c) the project map and the memory index (no SCSC fact in either); (d) at the end of the run, a `git status` check of
this run's own footprint listed other sessions' untracked names (runs of LKQ and SLVM dated 2026-10-05, and research
folders of other tickers), names only, none opened, seen after the verdict was written. No file
about SCSC in `Test Runs/` was opened, nor any file on the blind list. The commit subjects are named because they show
a pattern (Q2 OUT, cheap at half of fair) that this run could copy; the verdict below rests on the SCSC filings, and the
cheap-price rule chosen here is confessed as this run's own CONVENTION in the computation block.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $61.01 (2026-10-05, `tools/run.py`, aggregator live quote, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock, no par value, **20,142,812** as of
  2026-08-17 (10-K for FY ended 2026-06-30, filed 2026-08-20, accession `0000918965-26-000044`;
  `python Screens/cover_shares.py SCSC`). Balance-sheet count 20,161,911 at 2026-06-30 (same filing).
- **Market cap:** $1,228.9M (20.143M x $61.01).
- **Sovereign for the earnings currency (USD, 97% of sales in the United States):** **5.63%**, US Treasury daily par
  yield curve, 30-year, 2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026 (filed 2026-08-20, `0000918965-26-000044`): Item 1, Item 1A, Item 5,
  Item 7 in full, the auditor's reports, the four statements, notes 1 and 16. 10-Q for the quarter to 2026-03-31
  (`0000918965-26-000028`, fetched, consulted only for the quarter's buybacks). Proxy DEF 14A filed 2025-10-23
  (`0001193125-25-248757`): leadership, ownership, incentive metrics. 8-Ks: 2025-10-16 auditor change
  (`0001193125-25-241443`), 2025-12-19 new credit agreement (`0001193125-25-327081`), 2026-08-20 MicroAge purchase
  agreement and results (`0000918965-26-000043`), 2026-09-02 MicroAge closing (`0001193125-26-379371`), 2026-03-12,
  2026-05-29, 2026-08-17 officer and director changes. History: 10-Ks FY2008 (`0001193125-08-186801`), FY2011
  (`0001193125-11-235318`), FY2014 (`0000918965-14-000019`), FY2017 (`0000918965-17-000022`), FY2019
  (`0000918965-19-000020`), FY2020 (`0000918965-20-000023`), FY2021 (`0000918965-21-000022`), FY2023
  (`0000918965-23-000023`); the FY2006 10-K/A restatement (`0001193125-07-137091`) and the 2006-2007 8-Ks on the option
  review (`0001181431-06-062750`, `0001193125-07-085868`, `0001193125-07-115672`, `0001193125-07-141881`).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2026 $123,131K on the
  filed cash-flow statement (`0000918965-26-000044`) against `tools/run.py` 123.1. Agrees. Also net sales FY2026
  $3,226,062K on the filed income statement against the XBRL series 3,226.1. Agrees.
- `python tools/run.py SCSC`, arithmetic lines only (Part VII; its rules, ids and verdicts are not read). Owner cash
  after every real cost, OCF less stock pay less capital spending, USD millions, from the filed statements (FY2017 to
  FY2020 as first filed, which include the Europe and Latin America businesses later sold):

| FY (June) | OCF | stock pay | capex | owner cash, capex basis | D&A | owner cash, D&A basis |
|---|---|---|---|---|---|---|
| 2017 | 94.9 | 6.6 | 8.8 | 79.5 | 25.0 | 63.3 |
| 2018 | 27.9 | 6.5 | 8.2 | 13.2 | 37.5 | -16.1 |
| 2019 | -27.1 | 6.1 | 7.2 | -40.4 | 36.6 | -69.8 |
| 2020 | 182.0 | 5.5 | 6.4 | 170.1 | 35.3 | 141.2 |
| 2021 | 116.8 | 8.0 | 2.4 | 106.4 | 33.5 | 75.3 |
| 2022 | -124.4 | 11.7 | 6.8 | -142.9 | 29.9 | -166.0 |
| 2023 | -35.8 | 11.2 | 10.0 | -57.0 | 28.6 | -75.6 |
| 2024 | 371.6 | 9.5 | 8.6 | 353.5 | 28.0 | 334.1 |
| 2025 | 112.3 | 11.1 | 8.3 | 92.9 | 30.2 | 71.1 |
| 2026 | 123.1 | 14.1 | 9.3 | 99.7 | 23.6 | 85.4 |

  Five-year average FY2022 to FY2026: **69.3** (capex basis), **49.8** (D&A basis); `tools/run.py` prints 69.3 and 49.8.
  Ten-year average FY2017 to FY2026: 67.5 (capex basis). Capex runs $8M to $10M against D&A of $24M to $37M; most of
  the D&A is amortization of purchased intangibles ($16.7M of $23.6M in FY2026), so the capex basis is the nearer to
  the maintenance need for property, and management guides FY2027 capex to "$8.0 million to $12.0 million, primarily
  for IT and warehouse investments" (10-K FY2026, Liquidity). Acquisitions are a further use of cash outside these
  columns: $83.8M (FY2017, Intelisys at closing, plus earn-outs later), $143.8M (FY2018), $32.2M, $48.9M, $56.7M
  (FY2025), $18.2M (FY2026), and MicroAge, $220.5M paid in cash on 2026-09-01 with about $225M borrowed under the
  revolver (8-K `0001193125-26-379371`). Intelisys earn-out payments of $41.4M (financing) and $5.5M (operating) in
  FY2021 (10-K FY2023 cash-flow statement).
- **The cycle inside the five-year window.** A distributor's operating cash moves with receivables, inventory and
  payables. Net working capital (receivables plus inventory less payables, XBRL, first filed) was $404M at June 2021,
  $630M at June 2022, $820M at June 2023, $506M at June 2024, $521M at June 2025 and $539M at June 2026 (the filing's
  own figure, $538.8M). Sales were $3,150.8M in FY2021 and $3,226.1M in FY2026. So the window absorbed about $135M of
  working capital on sales growth of 0.47% a year: June 2021 was a low point (payables $635M against receivables $569M),
  and the window's two negative years and its one very large year (FY2024, $353.5M, the inventory release) are the
  cycle, not the business. The whole-cycle variant in the computation block below is built for that reason.

### The balance sheets first, ten year-ends (read in Step 0 because the file closes before Q4)
From `tools/run.py`'s ten-year table (first-filed XBRL) checked against the FY2026 and FY2020 filed statements, USD millions:

| June | assets | equity | goodwill | intangibles | cash | receivables | inventory | debt on face | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 1,718 | 837 | 201 | 102 | 56 | 637 | 531 | 97 | 849 |
| 2019 | 2,067 | 914 | 320 | 128 | 24 | 655 | 697 | 356 | 940 |
| 2020 | 1,692 | 678 | 214 | 122 | 29 | 443 | 455 | 219 | 747 |
| 2023 | 2,068 | 905 | 217 | 68 | 36 | 753 | 758 | 330 | 937 |
| 2024 | 1,779 | 924 | 206 | 38 | 185 | 582 | 513 | 144 | 1,014 |
| 2026 | 1,932 | 911 | 245 | 64 | 88 | 770 | 522 | 101 | 1,018 |

What the figures say **[M2025-032]** ("balance sheets over an 8 or 10 year period before I even look at the income account"):
- **Equity did not grow.** $837M in 2017, $911M in 2026, while net income summed about $384M over FY2017 to FY2026.
  The difference went to buybacks (about $318M over the ten years, $204M of it in FY2025 and FY2026), the FY2020 loss
  of $192.7M (goodwill impairment of $119.0M in the barcode, networking and security unit, and a $113.4M net loss from the
  discontinued operations being sold; FY2020 10-K `0000918965-20-000023`), and a translation loss now carried at $107.4M in accumulated other comprehensive loss
  (Brazilian real). Ten years of retained profit left the owners' book capital where it was.
- **Goodwill came back.** $201M in 2017, $320M at the 2019 peak, $214M after the 2020 impairment and the sale of
  Europe and Latin America, $245M in 2026 after the Resourcive, Advantix and other purchases; MicroAge will add more.
  The FY2026 auditor's critical audit matter is the Specialty Technology Solutions goodwill: the 10-K says the fair
  value of that unit "exceeded its carrying value by 2%" (Critical Accounting Policies, `0000918965-26-000044`).
- **Working capital is the capital.** Receivables and inventory ($1,292M) are two-thirds of assets; payables ($753M)
  fund most of them. Days sales outstanding 73 at June 2026 against 70 a year earlier (10-K, Liquidity); the
  receivable allowance is $26.6M. The filer says "As we grow and compete for business, our typical payment terms tend
  to get longer, increasing our credit risk" (Item 1A).
- **Debt was used and repaid with the cycle**: $356M at June 2019 at the inventory peak, $101M at June 2026, and about
  $326M again after the MicroAge borrowing in September 2026 (101 plus about 225). The new facility (December 2025,
  PNC agent) is a $400M revolver and a $100M term loan, secured by substantially all domestic assets, with a 3.50 to 1
  leverage covenant and a 3.00 to 1 interest-coverage covenant (8-K `0001193125-25-327081`).
- **What they cannot say:** the balance sheet does not show the supplier terms on which the whole structure rests
  (rebates, price protection, stock rotation, 30-day termination); those are in Item 1 and are read at Q2.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and for a distributor that means content to own a spread between what Zebra and Cisco charge and what
resellers pay, financed by working capital. The market serves and does not instruct: "It just tells us prices."
**[M2006-077]**; the stock's 85% five-year total return (Item 5 chart, $100 to $185) is not evidence about the business.
Margin of safety: "it’s too close to think about" if it needs pencil and paper **[M1996-084]**. The analyst's habits
govern this run: write contrary evidence down at once **[M1997-127]** ("write it down in the first 30 minutes"), state the
other side's case "better than they can" **[M2016-055]**, and read the competitors and the record "to possibly reject
your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]** (in the order found; "contrary" means against the
business, since the hypothesis to refute is that it has a castle):
1. Item 1A, FY2026: "As a result of intense price competition in our industry, our gross margins and our operating
   profit margins historically have been narrow, and we expect them to continue to be narrow in the future." The FY2011
   10-K says the same: "we have significant price competition that results in narrow gross profit and operating profit
   margins" (`0001193125-11-235318`).
2. Item 1: Cisco and Zebra each above 10% of net sales; the Cisco US and Brazil agreements and the Zebra EVM agreement
   may be terminated by either party "upon 30 days' notice"; supplier agreements generally run "Short-term periods,
   subject to periodic renewal, and termination rights by either party without cause upon 30 to 120 days' notice".
3. Item 1A: channel partners buy on purchase orders and "can choose to purchase from other sources, such as from
   competing distributor or directly from the supplier"; "Competition has increased for our sales units as broad-line
   and other value-added distributors have entered into the specialty technology markets."
4. Item 1A: price protection and stock rotation "are becoming less standard, subject to change, limited in scope".
5. Critical accounting policies: the Specialty Technology Solutions unit, 97% of sales, carries a fair value only 2%
   above its book value by management's own discounted-cash-flow test; the same unit took a $119.0M goodwill
   impairment in FY2020.
6. FY2020 10-K: the Europe, UK and Latin America (ex-Brazil) distribution businesses were sold because they were
   "performing below management's expectations" and the company "did not have sufficient scale" there.
7. Operating income kept per dollar of gross profit fell from 41% (FY2011) to 23% (FY2026) (XBRL, first filed); see Q2.
8. 2006-2007: a Special Committee found four annual grants between 1997 and 2001 whose dates "probably were selected
   with the benefit of hindsight", up to seventeen hiring or promotion grants that raised the same question, and a
   pattern to 2002 of choosing between two closing prices "often being consistent with selection of the lower price";
   it "did not conclude that current senior management [...] engaged in intentional misconduct"; the CEO then and now,
   Michael Baur, was among those who "voluntarily offered appropriate remediation" (10-K/A `0001193125-07-137091`;
   8-K `0001193125-07-085868`). NASDAQ delisting notices followed the late filings (8-K `0001193125-07-115672`).
   Q5 is not reached; the fact is recorded, not judged.
9. Proxy 2025: the annual incentive pays on "consolidated adjusted EBITDA" and free-cash-flow conversion, and the
   performance shares on "Adjusted ROIC", which the 10-K defines as adjusted EBITDA (stock pay added back) over invested
   capital. Q4 and Q6 are not reached; recorded, not judged.
10. 8-K 2025-10-16: Grant Thornton (auditor since 2014) dismissed after a competitive process, no disagreements reported,
    Deloitte appointed. Recorded, not judged.

Evidence for the business, written down beside it so the case is stated fairly **[M2016-055]**: the Intelisys agency
(net revenue $101.1M at a 98.6% gross margin, operating income $28.6M, 28% of segment operating income, on supplier
billings of about $2.88B that the filer calls annual recurring revenue); about 25,000 channel partners and about 500
suppliers, no partner above 10% of sales; specialist services (key injection for payment terminals, configuration) that
a broad-line distributor must build to compete; owner cash positive in seven of ten years and positive in total.

## THE STANDING RULE
Owning SCSC bought with the buyer's own money, unlevered, puts the buyer at no risk of ruin; the rule binds the buyer's
financing and sizing, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**,
and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this run asks the buyer to borrow.

---
## Q1. CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
"the first question is, can I understand it?" **[M1995-051]**; understanding is "a reasonable fix on about what the
earning power and competitive position will look like in five or 10 years" **[M2012-065]**, which needs the economic
dynamics and not the product: "I understand the economic dynamics of the industry" **[M2011-014]**.

- **What the business is, from the filing.** Specialty Technology Solutions ($3,124.9M of $3,226.1M sales FY2026):
  buys barcode scanners, mobile computers, label printers, POS terminals, payment terminals, cameras, switches and phones
  from about 500 makers (Zebra and Cisco each above 10% of sales) and resells them on credit to about 25,000 resellers
  in the United States and Brazil, from a 741,000 square foot warehouse in Southaven, Mississippi, plus Brazilian
  sites. Gross margin 10.8%, operating margin 2.4%. Intelisys & Advisory ($101.1M): an agency that places telecom,
  connectivity and cloud contracts for independent advisors with more than 200 carriers and cloud providers and keeps
  part of the commission; gross margin 98.6%, operating margin 28.3% (10-K FY2026, MD&A and note 16,
  `0000918965-26-000044`).
- **The key variables and whether they are foreseeable.** For the distribution part: the gross margin the makers allow
  (rebates, price protection), the operating cost per dollar of gross profit, and the working capital per dollar of
  sales. These have been stable in kind for fifteen years of filings and the filer forecasts them itself: margins
  "historically have been narrow, and we expect them to continue to be narrow in the future" (Item 1A FY2026; the same
  in FY2011, `0001193125-11-235318`). Test 5 asks whether the insiders would write the forecast down **[M2000-105]**
  ("they would not want to put down on paper their predictions"): here they do, every year, and TD SYNNEX writes the
  same of its own business ("we expect them to continue to be low in the future", 10-K FY2025, `0001628280-26-003598`).
  Test 3, do past statements tell me the future ones **[M2008-033]** ("the financial statements will tell me the
  information that’s useful to me"): for the distribution part, yes; the products change, the spread and the capital do not.
- **Routing.** Fast technology change: the products churn (communications moved from premises to cloud; Avaya and HP
  Poly are on the supplier list) and the filer lists "Disruptive technology" as a risk, but the economics that decide
  the value are the distributor's spread and capital, which the change has not moved in fifteen years. This is not the
  case the filter row names, where "it won’t make it through the filter" **[M1998-008]** because future technology hides
  the ten-year economics: what product change does to a middleman's spread is already in the record. Not a bank. Not a
  holding company.
- **The doubt, stated.** Intelisys's ten-year economics turn on whether carriers keep paying agency commissions at
  today's rates and whether advisors stay with one technology services distributor; that is less foreseeable than the
  distribution spread. The doubt rule is "if you have doubts about something being into your circle of competence, it
  isn’t." **[M2002-092]**, and the speakers name the trap of a business it is "easy to sort of think you understand"
  **[M2014-052]**. I hold that the doubt is about one part's growth, not about whether the whole's economics can be
  read: the part that carries 97% of sales and 72% of segment operating income is read from its own forecast, and Q2 can
  be answered on it. A second analyst could send the Intelisys doubt to Q1 TOO HARD; I record the call.
- **VERDICT: IN.** The distribution economics are understood in the speakers' sense, from the filer's own repeated
  forecast **[M2012-065]**, **[M2011-014]**, **[M2000-105]**; the Intelisys doubt is carried to Q2.

## Q2. WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**, asked knowing "most moats aren’t worth a damn" **[M1995-038]** and
that "competitors will repeatedly assault any business "castle" that is earning high returns" **[L2007-004]**.

**The competitor row** (same metrics, each company's own 10-K filings via XBRL, first-filed values: operating income
over gross profit, and pre-tax operating income over year-end shareholders' equity, means over the years available.
Revenue is booked gross by some and net by others, so margins on sales are not compared across firms):

| company | years | operating income / gross profit, mean | operating income / equity, mean (pre-tax) | latest 10-K accession |
|---|---|---|---|---|
| ScanSource (SCSC) | FY2011-FY2026 (16) | **23.6%** (41% in FY2011, 23% in FY2026) | **10.7%** | `0000918965-26-000044` |
| TD SYNNEX (SNX) | FY2011-FY2025 (15) | 31.5% | 17.4% | `0001628280-26-003598` |
| Arrow (ARW) | FY2015-FY2025 (11) | 27.9% | 19.8% | `0001104659-26-012765` |
| Avnet (AVT) | FY2011-FY2026 (16) | 22.4% | 14.3% | `0001104659-26-096346` |
| ePlus (PLUS) | FY2013-FY2026 (14) | 27.8% | 20.9% | `0001140361-26-023171` |
| Climb Global (CLMB) | FY2011-FY2025 (15) | 29.1% | 22.5% | `0001437749-26-006072` |

(SCSC's FY2011 to FY2019 values include the Europe and Latin America businesses sold in 2020-2021; equity includes
goodwill for every firm; Arrow's gross profit is tagged only from FY2015; the script is `peers.py` in the working folder.)

SCSC's own operating margin on sales (first filed; FY2016 to FY2019 are the continuing operations as restated in the
FY2020 10-K, `0000918965-20-000023`): FY2011 4.24%, FY2014 4.18%, FY2016 2.86%, FY2017 2.78%, FY2018 2.18%, FY2019
2.92%, FY2020 -2.13% (1.82% before the $120.5M impairment), FY2021 1.95%, FY2022 3.46%, FY2023 3.59%, FY2024 2.77%,
FY2025 2.80%, FY2026 3.06%. Gross margin rose over the same years (10.3% in FY2011 to 13.6% in FY2026) because the
Intelisys commissions are booked net at a 98.6% gross margin; operating cost rose faster, and the share of gross profit
kept as operating income fell by nearly half. By segment, gross margin in the hardware lines: Worldwide Barcode,
Networking & Security 9.8% (FY2019) and 8.6% (FY2020), Worldwide Communications & Services 16.6% and 18.3%
(FY2020 10-K); Specialty Technology Solutions 9.9% (FY2022), 9.6% (FY2023) (`0000918965-23-000023`), 10.6% (FY2025),
10.8% (FY2026). The segments were redrawn three times in the span, so no single segment series runs fifteen years.

The castle tests, each with its filing fact:
1. **The money test.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The attack is not
   hypothetical; the filer reports it under way: "Competition has increased for our sales units as broad-line and
   other value-added distributors have entered into the specialty technology markets. Such competition could result in
   price reductions, reduced margins and loss of our market share" (Item 1A FY2026), and names Ingram Micro and TD
   SYNNEX as competitors "in most geographic areas" (Item 1). The makers can go around it: partners "can choose to
   purchase from other sources, such as from competing distributor or directly from the supplier" (Item 1A). A
   well-funded attacker can take this business, and two are already in it. The answer is yes.
2. **Pricing power, and the agony before a rise.** "a prayer session before you raise your prices a penny"
   **[M2005-020]**. Price is the first-named basis of competition ("We compete on the basis of price, product and
   service availability", Item 1A), and the price it can charge is set between the makers' terms and the rival
   distributors' quotes: makers "have the ability to make adverse changes in their sales terms and conditions, such as
   reducing the level of purchase discounts and rebates", and "We have no guaranteed price or delivery agreements with
   our suppliers" (Item 1A). The fifteen-year operating margin record shows no span in which the spread widened.
   "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit, because we looked at his price
   every day" **[M2023-079]**.
3. **Unit volume and share of mind.** Sales were $2,886.9M in FY2016 (continuing) and $3,226.1M in FY2026, about 1.1% a
   year nominal; $3,249.8M in FY2019 and $3,226.1M in FY2026, flat over seven years. Share of mind belongs to the
   makers: the reseller asks for a Zebra scanner or a Cisco switch, not for ScanSource. "the brand is our protection
   against the intermediaries making all the money" **[M2019-041]**: the brand here is the maker's, and ScanSource is
   the intermediary it protects against.
4. **The low-cost position.** "Another way to prosper in a commodity-type business is to be the low-cost operator."
   **[L2004-007]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. On the row
   above SCSC keeps the second-lowest share of its gross profit of the six and earns the lowest pre-tax return on
   equity of the six over fifteen years; it exited Europe and Latin America because it "did not have sufficient scale"
   there (FY2020 10-K). It is not the low-cost operator, and "the guy with the lower cost comes in and kills you"
   **[M2001-013]**.
5. **The brand in the customer's mind.** None that the filing claims for itself: "We do not believe that our operations
   are dependent upon any of our marks" (Item 1, Trade and Service Marks).
6. **Would the customer still choose it over the low bid?** See's passed because "it wouldn’t be a question of people
   buying candy for the low bid" **[M2017-009]**. Here it is that question: transactions "generally are performed on a
   purchase order basis rather than under long term supply agreements" (Item 1A), and the filer says that "To remain
   competitive, we may be forced to offer more credit or extend payment terms". The reseller's position toward a
   distributor of another firm's product is the insured's: "most insureds don't care from whom they buy" **[L2004-003]**.
7. **Ask the competitors.** "which one would it be and why?" **[M1999-130]**. No interview is on the public record; their
   filings speak for the field. TD SYNNEX: "As a result of significant price competition in the IT products and services
   industry, our gross margins are low, and we expect them to continue to be low in the future" (`0001628280-26-003598`).
   Climb: "There is significant competition within each market segment and geography served that creates pricing
   pressure" (`0001437749-26-006072`). Avnet: "pricing and product selection and availability must remain competitive"
   (`0001104659-26-096346`). The field describes itself as a commodity field.
8. **Widening or narrowing.** "the competitive position of each of our businesses grows either weaker or stronger"
   **[L2005-010]**. The evidence is narrowing: operating income per dollar of gross profit 41% in FY2011, 40% in FY2014,
   about 23% in FY2024 to FY2026; the exit from Europe and Latin America in 2019 to 2021; the $119.0M impairment of the
   barcode, networking and security goodwill in FY2020; the present 2% headroom in the same unit's goodwill test; and
   price protection and stock rotation that "are becoming less standard". The newspaper letter's phrase fits, a
   franchise that "has lost still another notch" **[L1995-023]**, except that here the first notch was thin.
9. **What could destroy, modify or reduce it.** "destroy, or modify, or reduce the economic strengths" **[M2000-014]**:
   a 30-day notice from Cisco or Zebra; a cut in rebates; a maker selling direct; a broad-line distributor pricing the
   specialty lines to win share. "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**The other side's case, stated as strongly as I can** **[M2016-055]**. ScanSource has survived since 1992 as a
specialist, which says resellers value its technical help, configuration and payment-terminal key injection, and makers
value its reach into 25,000 small resellers they cannot serve themselves. Its return on the capital it actually needs is
better than its return on book equity, because a third of book equity is goodwill and intangibles (pre-tax operating
income of $98.6M on equity less goodwill and intangibles of about $602M is about 16%). Intelisys is a two-sided agency
whose 98.6% gross margin and $2.88B of billings look like a toll. And the margins, though narrow, have stayed positive in
every year but the impairment year. All true. None of it is a reason the castle will stand that the filer itself does
not deny: the specialist services are being copied by the broad-liners the filer says have entered; the makers keep the
right to leave on 30 days; and Intelisys, the one part with a toll's margin, earned $30.6M, $27.2M and $28.6M of
operating income in FY2024 to FY2026 (note 16), flat, against named rivals (Avant, Telarus), and is the smaller part.
Its quality does not change the answer for the whole, which is mainly the distribution business.

**Why OUT and not TOO HARD.** The castle's future is not unknown here; the filer describes an open field, the case of
"anything you do, your competitors can copy" **[M1996-017]**, of industries "just never going to have barriers to
entry" **[M2012-106]**, where "the improvement you get one day, your competitor gets the next day" **[M2004-053]** and
"average is not going to go away, either" **[M2000-072]**. The framework sends a castle shown to be open to OUT, and
lists among what Q2 rules out the business whose price a competitor sets, the customer who buys on the low bid, and the
high-cost producer in a commodity field (Q2, What it rules OUT). A lower price does not reopen it: "What you can’t do is
turn any investment into a good deal by paying little" **[M2019-015]**; marginal businesses bought cheap "are the wrong
foundation on which to build a large and enduring enterprise" **[L2014-009]**.

- **VERDICT: OUT.** The castle is shown open on the filing's own evidence and on fifteen years of competitor-relative
  returns **[M1995-038]**, **[M2011-015]**, **[M2005-020]**, **[M2012-109]**, **[L2004-007]**, **[L2005-010]**; the box is
  "out" among "in, out, and too hard" **[M2006-013]**. The run closes here. Q3 to Q12 are NOT REACHED.

## Q3. HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (Q2 closed OUT).

## Q4. DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion.
NOT REACHED. The ten balance sheets were read in Step 0, as the template asks when the file closes before Q4. Facts
met on the way and not judged: the 10-K's own return measure, "Adjusted ROIC", is adjusted EBITDA (stock pay, interest,
taxes, depreciation and amortization added back) over average equity plus funded debt (MD&A, Non-GAAP); the proxy pays
the annual incentive on "consolidated adjusted EBITDA" (DEF 14A `0001193125-25-248757`); the auditor changed in October
2025 after a competitive process with no reported disagreement.

## Q5. WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts met and not judged: Michael Baur has been President or CEO since December 1992 and Chair since
February 2019, owning 416,613 shares (1.9%) on 2025-10-03 (proxy); the 2006-2007 option review and restatement are
recorded in the foundations' contrary-evidence list, item 8.

## Q6. WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts met: never a dividend; buybacks of $97.5M in FY2026 (2,420,668 shares, about $40.29 each) and $106.5M
in FY2025 under a $300M authorization with no stated price limit (Item 5); MicroAge bought for $220.5M cash, borrowed,
on 2026-09-01. The buyback prices are set against the computed range below, as a computation only.

## Q7 to Q12
NOT REACHED. Q7, Q8 and Q9 arithmetic is reported below, at the owner's request, as a computation that clears nothing.

---
## COMPUTATION - NOT A CLEARANCE
*(Operator rule 3. The file closed OUT at Q2; nothing below is a judgment of value for buying, and no entry language
applies. The heading's dash is a hyphen because this file carries no em dash outside verbatim quotes.)*

**(a) VALUE RANGE by the Q7 convention** (Part VI, Q7: five-year average owner cash after every real cost, carried at the
growth shown for ten years, then no nominal growth, discounted at the long government rate; "What is the risk-free
interest rate (which we consider to be the yield on long-term U.S. bonds)?" **[L2000-021]**). Rate 5.63%. Shares 20.143M.
Script: `value.py` in the working folder.
- **Growth shown.** The convention measures growth on aggregate owner cash; here the five-year series starts negative
  (-$142.9M in FY2022), so no rate can be measured on it. CONVENTION of this run: the growth shown is taken from sales
  over the same years, FY2021 $3,150.8M to FY2026 $3,226.1M, **0.47% a year**, never above it. (A second reading, this
  five-year average of $69.3M against the prior five years' $65.8M, gives about 1% a year; shown in the script, not used.)
- **Convention range, capex basis** (owner cash $69.3M): no growth **$61.11**, shown growth **$63.43** a share. Top to
  bottom 1.04 to 1, narrow. The price, $61.01, sits at the bottom, 100% of the no-growth value.
- **D&A variant** (owner cash $49.8M): $43.94 to $45.60.
- **Under the convention's closes** (had Q7 been reached): narrow range, price inside or just below it, so "not a
  screamer" and OUT; "It should scream at you." **[M2009-005]**; "it’s too close to think about" **[M1996-084]**.
- **Whole-cycle variant, because the window holds the cycle's extremes** (FY2022 -$142.9M, FY2024 +$353.5M, and a net
  working-capital build of about $135M on almost no sales growth, from an abnormally low June 2021 base). Built from the
  filed cash-flow statements: operating cash before the filed changes in operating assets and liabilities, FY2022 to
  FY2026, $137.9M, $129.8M, $106.8M, $124.7M, $128.8M (average $125.6M); less stock pay (average $11.5M), capex ($8.6M)
  and the provision for doubtful accounts ($5.4M, a real credit cost that the pre-working-capital figure adds back) =
  **$100.1M**; less the working capital that 0.47% growth needs at the June 2026 intensity (net working capital 16.7% of
  sales) = $2.5M, giving **$97.6M** before acquisitions; less acquisitions averaged over the same five years ($74.9M / 5 =
  $15.0M) = **$82.6M** after them. Values: before acquisitions $86.06 (no growth) to $89.32 (shown growth); after
  acquisitions **$72.85 to $75.61**. Confessed: this variant rests on operating cash before working-capital changes,
  which is net income plus the non-cash lines; it is shown beside the convention range, not in place of it, so that
  operator rule 5's bar on a net-income proxy is not crossed by the range itself. Under it the price is 81% to 84% of the
  after-acquisition value: a discount that needs a pencil, not one that screams.
- **MicroAge** ($220.5M, paid after the window with about $225M borrowed) is carried at what was paid: value got taken
  equal to value given, neither added nor subtracted. CONVENTION of this run; the target's earnings were not read.

**(b) FAIR PRICE** (the price at or below which the central case clears the floor, the CONVENTION of about ten percent
pre-tax, from "at least 10% pre-tax returns" **[L2002-020]** and "there’s just a point at which we drop out of the
game" **[M2003-149]**). Tax treatment: owner cash is after the company's own income tax (cash taxes paid $28.9M in
FY2026); it is grossed up at the FY2026 effective rate of 24.0% to set it against a pre-tax floor; the expected
pre-tax return is the pre-tax owner-cash yield plus the shown growth of 0.47%.
- **Central case: the whole-cycle variant after acquisitions** ($82.6M after tax, $108.7M pre-tax): clears 10% at a
  market value of $1,141M, **$56.63 a share**. The convention case ($69.3M, $91.2M pre-tax) clears it at **$47.51**.
  The whole-cycle case before acquisitions clears it at $66.89. At $61.01 the expected pre-tax return is about 7.9%
  (convention) or 9.3% (central), below the floor in both.

**(c) CHEAP PRICE** (below which no pencil is needed). Rule, a CONVENTION of this run: half the central fair price, a
two-to-one margin, the "big discount from that present value" **[M1997-126]** made wide enough that the answer would
"scream" **[M2009-005]**, and wider than for a business whose future is surer, since "the more volatile the business is
[...] the larger the margin of safety" **[M1997-080]**: **$28.31 a share**. (Contamination declared above: other runs'
commit subjects show the same two-to-one ratio.) A cheap price does not reopen Q2 **[M2019-015]**.

**Q8 as arithmetic.** At $61.01 the convention owner cash yields 5.64% after the company's tax, against the 30-year
Treasury at 5.63%: the buyer would be paid the bond's rate for owning a business whose filer expects its margins to stay
narrow. **Q6 as arithmetic.** FY2026 buybacks at about $40.29 a share sit below the bottom of the convention range
($61.11), so by the Q6 convention they would be read by what they did; not judged. **Q9 as arithmetic.** Debt about
$326M after the MicroAge borrowing against FY2026 operating income of $98.6M and interest expense of $6.6M; the
facility's covenants are 3.50 to 1 leverage and 3.00 to 1 interest coverage; secured on substantially all domestic assets.

---
## THE BOX
**OUT, at Q2.** The castle is shown open: the filer forecasts narrow margins "as a result of intense price competition",
reports broad-line distributors entering its specialty markets, holds its two largest supplier lines (Cisco, Zebra) on
non-exclusive agreements terminable on 30 days' notice, sells on purchase orders to resellers who can buy from rivals or
the makers, and over fifteen years earned the lowest pre-tax return on equity of six distributors (10.7%) while the
share of gross profit it keeps fell from 41% to 23%. Not TOO HARD: the field's future is described, not unknown. No
research pass is owed. For the record, as computation only: convention range $61.11 to $63.43, whole-cycle $72.85 to
$75.61, fair $56.63 (convention $47.51), cheap $28.31, against $61.01.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written section by section (Step 0 and the foundations, then Q1 and Q2,
      then the rest), but after the reading was done, not question by question as each closed. **Not committed**: the
      brief forbids commits; the write-early commit rule was not applied.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, below); every filing fact has its
      accession; numbers carry a filing, a row, or a CONVENTION label.
- [x] The order was kept; Q2 was the first STOP that failed and closed the run; Q3 to Q12 are NOT REACHED; all value
      arithmetic sits under COMPUTATION - NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less capex), never a net-income proxy, for the convention
      range. The whole-cycle variant uses operating cash before working-capital changes and is labelled a variant, with
      that dependence confessed. Sovereign from the Treasury. The price is an aggregator quote, flagged.
- [x] Contrary evidence was written down **[M1997-127]**, in the order found, though transferred to this file after the
      reading rather than within the half hour of finding it.
- [x] Not a point-in-time run; no anchor applies (Part VII).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py`: **PASS** (2026-10-05, with this file in `Test Runs/`). A separate script
      (`check_run.py` in the working folder) found no E-id, every cited M, L and R id in `principle_ledger_v5.csv`
      (47 distinct), all 43 quoted fragments beside an id inside that id's row, and no em dash outside verbatim quotes.
      No commit is made.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Two parts of different quality at Q2.** The framework reads a holding company by its parts at Q1, but gives no rule
at Q2 for a single company whose small part (Intelisys, 3% of sales, 28% of segment operating income, a 98.6% gross
margin) may have a toll's economics while the large part is shown open. I judged the castle on the part that carries
most of the earnings and the capital; another analyst could ask whether the small part alone is a castle, or send its
doubt to Q1 TOO HARD. A sentence is missing on how a minority part with a different castle answer is weighed.
(2) **The Q7 growth input fails for a distributor.** "Growth shown on the aggregate owner cash" cannot be measured when
the five-year series starts negative, which working-capital swings make common in distribution; I used sales growth and
confessed it. (3) **No whole-cycle rule.** The five-year window here holds both ends of an inventory cycle and a $135M
working-capital normalization; the convention has no instruction for it, and the only clean way I found to normalize
working capital (operating cash before working-capital changes) sits close to the net-income proxy that operator rule 5
forbids. The line between "normalizing working capital" and "a net-income proxy" needs to be drawn. (4) **Fair and cheap
prices are not in the framework**; both rules here are this run's conventions, and the cheap rule matches a pattern seen
in other runs' commit subjects. (5) **Operator rule 3's heading contains an em dash** while the operator's standing rule
forbids em dashes; a hyphen was used. (6) **"Ask the competitors"** cannot be run as the rows mean it (an interview);
the competitors' 10-K language was used as their answer, which is weaker evidence than the test asks for.
