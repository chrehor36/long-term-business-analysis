# Company Run — Walmart Inc. (NASDAQ: WMT) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule that forbids opening
`PORTFOLIO.md`. The analyst does not know whether the operator holds this name. **Contamination declared:** (1) the
directory listing of `Test Runs/` filtered on the ticker showed that an earlier run file for this name exists, dated
2026-09-06; it was not opened, and its box is not known to this analyst. (2) The v5 ledger itself carries rows that
name Walmart (the speakers' 2002 "You can certainly understand Walmart" **[M2002-092]**, the 2012 remarks on its low
gross margins **[M2012-051]**, and the narrated omission of not buying Walmart stock in the 1990s **[M2003-047]**,
**[M2004-039]**, **[L2014-045]**). They are corpus, not run history; they are cited where they bear and are treated as
the speakers' view in their year, to be tested against today's filings, not as a verdict on today's company. (3) The
analyst's general memory of Walmart (largest US retailer, a three-for-one split in 2024, a listing move to Nasdaq, a
change of chief executive in early 2026) predates the run and is set aside; every fact below is from a filing read today.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$105.07** (close 2026-10-05, the quote `tools/run.py` fetches; **aggregator, live quote only, flagged**
  under operator rule 5).
- **Shares by class** from the latest filing's cover: **7,933,746,241** common, one class (10-Q for the quarter ended
  2026-07-31, filed 2026-08-28, accession `0000104169-26-000154`, cover as of 2026-08-26;
  `python Screens/cover_shares.py WMT`). The balance-sheet share tag `tools/run.py` lists (3,418M, as of 2012) is stale
  and pre-split and is not used.
- **Market cap:** 7,933.7M × $105.07 = **$833.6B**.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR (CIK 104169):
  - 10-K for fiscal 2026 (year ended 2026-01-31), filed 2026-03-13, accession `0000104169-26-000055`.
  - 10-Q for the quarter ended 2026-07-31, filed 2026-08-28, accession `0000104169-26-000154`.
  - DEF 14A for the 2026 annual meeting, filed 2026-04-23, accession `0001193125-26-173673`.
  - 8-K of 2026-08-20, accession `0000104169-26-000145`, Ex. 99.1 (Q2 FY2027 earnings release); 8-K of 2026-02-19,
    accession `0000104169-26-000032`, Ex. 99.1 (Q4 FY2026 release).
  - 8-Ks of 2026-01-08 (`0000104169-26-000008`, a director appointed) and 2026-01-16 (`0000104169-26-000023`, the
    International CEO's departure and the executive changes under the incoming CEO, John Furner).
  - For the history: 10-K FY2023, `0000104169-23-000020`; 10-K FY2021, `0000104169-21-000033`; annual report FY2017
    (Ex. 13 of `0000104169-17-000021`), each used where cited.
- **One figure cross-checked against the filed statement:** operating cash flow FY2026 **$41,565M** and payments for
  property and equipment **$26,642M** on the filed Consolidated Statement of Cash Flows (`0000104169-26-000055`) agree
  with `tools/run.py`'s XBRL lines; the 10-K's own free-cash-flow table gives **$14,923M**, which is 41,565 − 26,642.
- `python tools/run.py WMT`, arithmetic lines only (its "OE" labels, yields and rule text are not used; Part VII),
  saved at `Test Runs/_research 2026-10-06 WMT/run_py_output.txt`. The owner-cash recast is done at Q4 from the filed
  statements (`Test Runs/_research 2026-10-06 WMT/owner_cash.py`), not from these lines:

  | FY end | OCF | SBC | D&A | capex |
  |---|---|---|---|---|
  | 2024-01-31 | 35,726 | 2,093 | 11,853 | 20,606 |
  | 2025-01-31 | 36,443 | 2,769 | 12,973 | 23,783 |
  | 2026-01-31 | 41,565 | 3,603 | 14,203 | 26,642 |

  ($ millions.) Known defects checked: run.py's "other capital payments" (finance-lease principal and dividends to
  minority partners) are real and are deducted in the recast; SBC FY2026 includes a **$0.7B** one-off charge on the
  modification of PhonePe's options (10-K Note 3 and Note 11), kept in as a real cost (paid in a subsidiary's shares).

## THE FOUNDATIONS (not a gate)
Four foundations bear on this name. **A share is a business:** would one be content to own Walmart "if the market closed
for five years" **[M1997-109]**; for a retailer that is a question about whether its customers still come, in stores and
online, ten years out, not about the quote. **The market serves:** at $833.6B the quotation tells "prices" and nothing
else **[M2006-077]**; steering by it would assume "that the stock market knows more than you do" **[M2003-046]**. **Who is
paid to tell you:** the company issues quarterly and annual guidance on an adjusted basis (8-K Ex. 99.1,
`0000104169-26-000145`: "issues guidance for Q3; raises outlook for FY27"), which the speakers call a corrosive habit
**[L2000-039]**, **[M2016-002]**; it is weighed at Q4 and Q6, not here. **No macro enters** **[M2000-094]**: the tariff
regime, the IEEPA tariff refunds of the second quarter and the consumer cycle are read only as properties of the
business, what counts being "the average profitability of the business over time and how strong its competitive mode
is" **[M2015-016]**. The index fork **[M2008-055]** is assumed passed, the operator being the professional the questions
are written for. **The analyst's habits:** the worst anchor is "your previous conclusion" **[M2016-054]**, and the
speakers' own conclusion on this company is in the ledger ("You can certainly understand Walmart" **[M2002-092]**); it is
treated as their 2002 reading, to be re-tested, not inherited.

**Contrary evidence, written down as found** **[M1997-127]**, looking for "what’s wrong" and "what you’re missing"
**[M2025-013]**, in the order met:
1. Capital spending has risen from **$10.3B** (FY2021) to **$26.6B** (FY2026) while operating income rose from **$22.5B**
   to **$29.8B** (10-Ks `0000104169-21-000033`, `0000104169-26-000055`). Owner cash after all capital spending was **$23.7B**
   in FY2021 and **$10.0B** in FY2026 (`owner_cash.py`). The business is earning more and handing the owner less; the
   question is whether that is growth spending that will pay or the price of standing still (Q3).
2. Return on investment, the company's own measure, fell from 15.5% to 15.1% in FY2026 "primarily due to an increase in
   average invested capital due to higher purchases of property and equipment" (10-K MD&A, `0000104169-26-000055`).
3. Retail is the field the speakers name for the illusion of understanding: "it’s easy to sort of think you understand
   retail, and then subsequently find out you don’t" **[M2014-052]**; and "In retailing, to coast is to fail."
   **[L1995-008]**.
4. The Q2 FY2027 operating income rose 28.8%, of which a large part was **$2.9B** of one-off IEEPA tariff refunds
   booked as a reduction to cost of sales (10-Q Note on tariffs, `0000104169-26-000154`); the "adjusted operating income"
   of the release does not remove it, though the release says so in words ("which includes the impact of tariff refunds
   received"). A reader of the adjusted line alone would be misled; the company states the item.

## THE STANDING RULE
Owning a share of Walmart bought with cash, unlevered and sized so that a fall of half would not force a sale, puts the
buyer at no risk of ruin; the rule binds the buyer's financing, not the target: "We are never going to risk what we have
and need for what we don’t have and don’t need." **[M2012-081]**; borrowed money "has no place in the investor's tool
kit" **[L2014-005]**. Nothing in this name requires the buyer to give an option, post collateral or borrow
**[L2014-024]**. **Clear**, on the assumption of cash purchase.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it:** "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years", knowing "how the industry will develop and where the company will stand within the
industry" **[M2012-065]**; the key variables named and judged for predictability **[M1998-044]**.

**What the business is, from the 10-K (`0000104169-26-000055`).** Net sales **$706.4B** in FY2026 in three segments:
Walmart U.S. **$483.0B** (4,611 stores; grocery **$285.5B**, general merchandise $115.1B, health and wellness $69.5B,
other $12.9B), Walmart International **$130.4B** (Mexico and Central America $52.5B, China $24.6B, Canada $23.7B, other
$29.6B, the other including Flipkart and PhonePe in India), Sam's Club U.S. **$93.0B** (601 clubs). Segment operating
income FY2026: Walmart U.S. **$25.2B**, International **$5.1B**, Sam's Club **$2.4B**, against **$29.8B** consolidated after
corporate costs (segment note and MD&A). The two U.S. segments carry about 84% of segment operating income. eCommerce is
inside the same segments: Walmart U.S. eCommerce net sales **$99.6B** (FY2024 $65.4B), mostly "store-fulfilled pickup
and delivery" (MD&A).

**The key variables, and how predictable they are.**
1. *Unit volume and transactions in the U.S.:* comparable sales +4.3% (FY2026), +4.8% (FY2025), +5.5% (FY2024),
   "driven by growth in average ticket and transactions, and also reflected growth in unit volumes" (MD&A). The goods are
   mostly groceries and health products, bought every week; what people will buy in ten years is a forecast about
   consumer behaviour, the kind the rows say can be projected **[M2023-030]**, **[M2017-019]**, not about technology.
2. *The price gap and the cost gap:* the stated model is EDLP and EDLC, "control expenses so our cost savings can be
   passed along to our customers" (Item 1, Competition). Gross profit rate 24.2%, operating expense rate 20.9%, operating
   margin 4.2% (FY2026). These ratios have moved by tenths of a point a year (MD&A, three years), which is the stability
   a ten-year picture needs.
3. *Capital per dollar of sales:* capital spending **$26.6B** against D&A **$14.2B** in FY2026 (cash-flow statement); the
   company says the majority goes to "automation such as eCommerce, supply chain and store and club investments" (MD&A,
   Capital Allocation). Whether that spending earns its keep is Q3; that it can be read from the statements is a Q1 fact
   **[M2008-033]**.
4. *The newer income lines* (advertising, Walmart+ membership, marketplace): membership fee revenue **$4.4B** (Note 1);
   advertising is named as a higher-margin driver but is not broken out as a line in the 10-K. Smaller and less
   foreseeable; they ride on the traffic of 1. and do not change the ten-year picture of it.

**Contrary evidence for Q1, written down as found** **[M1997-127]**: the filer itself calls the landscape "highly
competitive and rapidly evolving", naming "emerging agentic shopping tools and platforms" and "more rapid development of AI
capabilities and agentic tools by these competitors" (Item 1A, `0000104169-26-000055`); the new chief executive's first
reorganisation release says "As AI rapidly reshapes retail" (8-K Ex. 99.2, `0000104169-26-000023`). Change is the enemy
of the forecast **[M1999-063]**. Against it: the change named is in how the order is placed and delivered, while what
is bought (groceries, health products, household goods) and the economics that decide who wins (the lowest delivered
cost, store density within reach of the customer) are the same variables as before; Walmart U.S. eCommerce grew from
$65.4B to $99.6B in two years inside the same segment margin (5.0% to 5.2%), which is the record of a change absorbed,
not of a forecast lost. The rows' warning is about retail itself: "it’s easy to sort of think you understand retail, and
then subsequently find out you don’t" **[M2014-052]**.

**The parts.** By the holding-company CONVENTION (Q1), each part that matters is read. The U.S. stores and clubs are the
earnings. International is about 16% of segment operating income; within it Flipkart and PhonePe (India) are not reported
separately, and an Indian eCommerce and payments field is one whose winners cannot be named **[M2012-067]**. The doubt
rule says doubt means outside **[M2002-092]**; here the doubtful part is a minority of the earnings and does not decide
where the whole will be in ten years, so it is carried to Q3 and Q6 as a question of capital poured in, not as a reason the
whole cannot be foreseen. The country risk is priced, not passed **[M2006-021]**. This is a judgment and is labelled as
one; a reader who weighs the India investment as mattering would close here TOO HARD.

**Would the insiders write it down?** **[M2000-105]**. A ten-year forecast of Walmart U.S.'s grocery volume, price gap and
margin is the kind of forecast a grocery executive would write down; a ten-year forecast of Flipkart's economics is not.
The speakers placed this company inside the circle in so many words, "You can certainly understand Walmart"
**[M2002-092]**; that is a 2002 reading, and the 2026 filings above were read to test it, not to inherit it **[M2016-054]**.

- **VERDICT: IN.** The ten-year economics of the U.S. stores and clubs, which carry the earnings, can be foreseen within a
  model of "how far off we can be" **[M2011-084]**: weekly purchases of essentials at the lowest delivered cost. The Indian
  part is outside the perimeter and is carried forward as a capital question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. Walmart sells goods every rival
also sells; the castle, if there is one, is not a product but a cost position. The rows' route through a commodity field
is exactly this: "Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**;
"when a company is selling a product with commodity-like economic characteristics, being the low-cost producer is
all-important." **[L2000-017]**. So the tests are read for the low-cost position first.

**The castle tests, each with its filing fact.**
1. *Key factors and their permanence:* the stated model is EDLP and EDLC (Item 1, `0000104169-26-000055`). The reasons a
   household buys groceries and household goods from the cheapest nearby seller are the See's kind of reasons, unchanged
   for decades **[M1995-038]**. Low prices on "something that’s essential to people" is "a very good business usually"
   **[M2004-091]**; "if you can offer somebody a good product cheaper than the other guy then everybody practically has to
   buy it." **[M2024-013]**.
2. *Would it stand without the lord?* Retail is the rows' named counter-case: "In retailing, to coast is to fail."
   **[L1995-008]**; it is a business where "you have to stay smart" **[M1995-040]**. Walmart changed chief executive on
   2026-02-01 (8-K `0000104169-26-000023`: John Furner, "32 years with Walmart", promoted from inside with four other
   internal appointments). The castle is a system and a culture "very, very difficult to copy" **[M2009-038]**, not one
   genius; but it is a castle that must be worked every day. Weighs against the castle's permanence, not for it.
3. *The money test:* the attacker with money exists and is named in the rows: "in retail, there are a lot of people that
   would aim that silver bullet at Jeff" **[M2017-022]**. Amazon's North America segment had net sales of **$426.3B**
   (+10%) and operating income of **$29.6B** in 2025 (10-K 2025, Note 10, `0001018724-26-000004`), larger in profit than
   Walmart U.S. (**$25.2B**). Over the same years Walmart U.S. comparable sales rose 5.5%, 4.8%, 4.3% and its eCommerce
   sales went from $65.4B to $99.6B (FY2024 to FY2026, 10-K). A $100 billion attacker "would not have the faintest idea"
   how to displace it **[M1997-103]**? The evidence is that the best-funded attacker in history has grown beside it for
   twenty years without displacing it, and that the weaker store chains (below) are the ones losing.
4. *Pricing power and the agony before a rise:* not the castle here, and the rows say the low-cost operator should not
   want it: "Our goal, however, is not to widen our profit margin but rather to enlarge the price advantage we offer
   customers." **[L1996-016]**. The filings show that conduct: the FY2025 gross margin rise came from "managing prices
   aligned to our competitive historic price gaps" (MD&A); the **$2.9B** of IEEPA tariff refunds in Q2 FY2027 were
   largely "invested into customer-focused initiatives during the current quarter, primarily through price investment"
   (10-Q MD&A, `0000104169-26-000154`), the Costco duty to pass cost advantages on **[M2011-063]**.
5. *Unit volume and share of mind:* "approximately 270 million customers and members visit more than 10,750 stores and
   numerous eCommerce websites in 19 countries" each week (8-K Ex. 99.1, `0000104169-26-000008`); FY2026 comparable sales
   "reflected growth in unit volumes and strength in all merchandise categories", transactions up (MD&A). Volume is the
   evidence the place in the mind holds **[M1999-054]**.
6. *The low-cost position:* "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**. The
   evidence is in the competitor row below: Walmart U.S. earns 5.2% on sales at a 27.5% gross margin, the general-merchandise
   rival (Target) 4.9% on a 27.9% gross margin while its sales shrink, the conventional grocer (Kroger) 1.3%; the warehouse
   club (Costco, and Walmart's own Sam's Club at 11.3% gross margin and 2.6% operating margin) runs a narrower, lower-cost
   model. The cost is measured against the competitor, not in absolute terms **[M2001-013]**, **[M2009-059]**; a tough
   market "helps the low-cost operator" **[L1997-021]**.
7. *The brand:* the brand is the promise of the low price **[M2008-075]**; the rows name Walmart among the retailers to
   which brand value "moves over" from the product **[M2001-090]**, and in 2019 among the retailers that "gained some
   power" **[M2019-014]**.
8. *Would the customer still choose it over the low bid?* Walmart is the low bid; this test is the one a commodity seller
   fails **[L2004-003]** unless it is the lowest-cost seller, which is test 6.
9. *Ask the competitors:* not done by interview; the public record's answer is test 3 and the competitor row.
10. *Widening or narrowing?* **[M1999-108]**, **[L2005-010]**. Narrowing over ten years in margin: Walmart U.S. earned
    **$17.7B on $307.8B** of sales (5.8%) in FY2017 and **$21.3B** (7.4% on about $288B) in FY2015 (annual report FY2017,
    Ex. 13 of `0000104169-17-000021`), against **$25.2B on $483.0B** (5.2%) in FY2026. The margin was spent on wages, price
    and the eCommerce build. Widening in the last three years on the volume and channel evidence: Walmart U.S. segment
    margin 5.0%, 5.2%, 5.2% (FY2024 to FY2026), eCommerce up by half, and the two store-based rivals' sales or margins
    falling. Read together: the castle held its walls by spending, and on the latest evidence the spending is now buying
    share rather than only replacing what was lost. Whether that is a "moat that must be continuously rebuilt"
    **[L2007-005]** or the daily widening of **[L2005-010]** is the judgment the rows say no test separates.
11. *What could destroy it, five to fifteen years out?* **[M2000-014]**. Named in the filing: "emerging agentic shopping
    tools and platforms" that sit between the customer and the store (Item 1A), which would move the customer's choice
    from the store to an intermediary, as the brands once lost it to the retailers **[M2001-090]**; Amazon's delivery
    network; and labour cost in a business with "very high labor content" (2.1 million associates), though its product
    cannot be "shipped in from abroad" in the sense of **[M2007-116]** (the store is the local service). "one competitor is
    frequently enough to ruin a business" **[M2012-108]**; twenty years of Amazon has not done it.

**The competitor row** (latest fiscal year; each from the company's own 10-K; companyfacts XBRL and the filed statements,
`Test Runs/_research 2026-10-06 WMT/competitors_output.txt`):

| company | year | net sales | gross margin | operating margin | sales growth | source |
|---|---|---|---|---|---|---|
| Walmart U.S. (segment) | FY to 2026-01-31 | $483.0B | 27.5% | 5.2% | +4.4% | 10-K `0000104169-26-000055` |
| Walmart consolidated | FY to 2026-01-31 | $706.4B | 24.2% | 4.2% | +4.7% | same |
| Target | FY to 2026-01-31 | $104.8B | 27.9% | 4.9% | −1.7% | 10-K `0000027419-26-000016` |
| Kroger | FY to 2026-01-31 | $147.6B (revenue) | not computed (cost tag differs) | 1.3% | +0.4% | 10-K `0001104659-26-037723` |
| Costco | FY to 2025-08-31 | $275.2B (revenue) | 12.8% | 3.8% | +8.2% | 10-K `0000909832-25-000101` |
| Amazon North America (segment) | CY2025 | $426.3B | n/a (segment) | 6.9% | +10.0% | 10-K `0001018724-26-000004` |

Target's and Kroger's margins are as filed and may carry one-off charges not read here; Costco's fiscal 2026 10-K was not
yet filed on the run date. Walmart's gross margin is on net sales (10-K MD&A); Target's is revenue less cost of sales.

**Contrary evidence for Q2, written down as found** **[M1997-127]**: Amazon North America earns more operating income
than Walmart U.S. on less revenue and grows more than twice as fast; Walmart U.S.'s margin is lower than it was ten years
ago; the attacker is the one the rows themselves point the silver bullet at **[M2017-022]**. A castle whose strongest
attacker is gaining in absolute terms is not a castle that is "impossible" to cross; it is a castle that is being held.

- **VERDICT: IN.** The castle is the low-cost position in weekly essentials, the rows' named route through a commodity field
  **[L2004-007]**, **[M2018-043]**, held against the best-funded attacker for twenty years, with volume, transactions and
  digital sales rising and the store-based rivals losing ground on the latest filings. It is not shown open (no OUT), and
  its future can be judged as a low-cost operator's that "must pursue an unrelenting foot-to-the-floor strategy"
  **[L2004-007]** (no TOO HARD). It is a castle that must be worked, not one that stands by itself **[L1995-008]**; that
  weighs on how sure the cash is (Q7), not on whether it exists.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**; of growth, "whether
that’s good or bad depends on what we earn on that incremental" capital **[M2001-019]**.

**Return on the capital actually needed** **[M2010-090]**, on tangible assets **[M2011-060]**
(`Test Runs/_research 2026-10-06 WMT/return_on_capital.py`; net tangible operating capital = total assets less cash,
goodwill, accounts payable, accrued liabilities and accrued taxes, from the filed balance sheets, accessions in the
script; FY2021 is left out because it carried Asda and Seiyu as held for sale):

| FY | net tangible operating capital | operating income | pre-tax return | after about 24% tax |
|---|---|---|---|---|
| 2022 | $118.9B | $25.9B | 21.8% | 16.6% |
| 2023 | $120.8B | $20.4B | 16.9% | 12.9% |
| 2024 | $128.8B | $27.0B | 21.0% | 15.9% |
| 2025 | $134.4B | $29.3B | 21.8% | 16.6% |
| 2026 | $150.4B | $29.8B | 19.8% | 15.1% |

The company's own ROI, on a broader capital base, is 15.1% (FY2026) and 15.5% (FY2025), and was 15.2% in FY2017 (annual
report FY2017, `0000104169-17-000021`): flat across a decade. A 4.2% margin works only because the capital turns fast
**[M2017-096]**: sales of $706B on about $150B of net tangible operating capital, the suppliers financing $63B of it
through payables. The rows ask whether a high return comes from a cyclical peak, a monopoly or leverage **[L1994-009]**:
none of the three (the return holds across FY2022 to FY2026, the field is open, and the return is measured before debt).

**Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending FY2026 **$26.6B** against
depreciation and amortization **$14.2B** (cash-flow statement). The company's own split (MD&A, Capital Allocation,
`0000104169-26-000055`): U.S. "supply chain, customer-facing initiatives, technology and other" **$16.5B**, store and club
remodels **$5.6B**, new stores and clubs **$1.4B**, International **$3.2B**. The U.S. store count and square footage did not
grow (4,615 to 4,611 stores, 699M to 699M square feet, FY2024 to FY2026), so almost none of the spending is new floor
space; it is automation, delivery and technology inside the same footprint. **The maintenance guess, stated:** about the
depreciation charge, **$14B** a year, since depreciation "is not inappropriate in most companies to use as a proxy for
required capital expenditures" **[M1998-127]**; the remaining **$12B or so** is the spending the company calls growth. The
guess could be wrong in the direction the rows warn of: where the automation is what keeps the price gap against Amazon,
it is the "compulsory reinvestment just in order to stand still" **[M1997-016]**, **[M1998-128]**, and depreciation then
understates the real cost **[M2015-049]**, **[L2023-009]**.

**What the added capital has earned.** From FY2022 to FY2026 net tangible operating capital rose **$31.4B** and operating
income **$3.9B** (12.3% pre-tax on the increment); from FY2023 to FY2026 the same comparison gives **$29.6B** and **$9.4B**
(31.8%). The answer depends on the base year **[L2005-003]**: FY2022 was a peak and FY2023 a trough (the inventory
markdowns of 2022). The five-year mean return on the whole base, 20.3% pre-tax, is about what the increment earned in the
middle of that span. Meanwhile owner cash after all capital spending was **$9.0B** (FY2022) and **$10.0B** (FY2026)
(`owner_cash.py`), so the owner has so far received almost none of the added earnings; they went back into the business.
Rising earnings alone prove nothing: "We just put way more capital into the business" **[M2023-081]**.

**The growth arithmetic and its caps.** Operating income grew **5.8%** a year FY2021 to FY2026; aggregate owner cash after
all capital spending grew **2.8%** a year FY2022 to FY2026; on the depreciation basis it grew **18.4%** a year over the same
endpoints, a figure made by the FY2022 working-capital trough (operating cash flow $24.2B that year against $36.1B the year
before) and rejected as a picked base year **[L2005-003]**. A business with $706B of sales growing about 5% nominal cannot
compound owner cash much faster than its sales for long without the margin doubling; the cap for Q7 is the operating-income
rate, about 6%, and it is not run past the discount rate **[M2003-120]**.

**The second-best business, as the rows grade it** **[M1998-081]**, **[L2007-010]**: Walmart is not the business that
"gives you more and more money every year without putting up anything"; it is the second kind, which grows by putting up
more at a return that has so far held at about 20% pre-tax on the whole, "unattractive unless the cash they consume gets to
earn a reasonable return" **[M2012-057]**.

- **WEIGHS: UNDECIDED.** FOR: about 20% pre-tax (15% after tax) on the tangible capital the business needs, held for five
  years and, on the company's own measure, for ten **[M2010-090]**. AGAINST: capital spending has nearly doubled against a
  flat store base while the owner's cash has not grown, and whether the $12B above depreciation is growth or the price of
  standing still against Amazon is not shown by the filings **[M1997-016]**, **[M2023-081]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py` transcription of the
first-filed XBRL, accessions in `run_py_output.txt`; the FY2026 column checked line by line against the filed balance
sheet in `0000104169-26-000055`: total assets $284,668M, cash $10,727M, receivables $11,172M, inventories $58,851M, goodwill
$28,735M, long-term debt $34,624M, retained earnings $104,774M, Walmart shareholders' equity $99,617M, all agree).

| year-end | assets | equity | cash | receivables | inventory | goodwill | LT debt | retained |
|---|---|---|---|---|---|---|---|---|
| 2017-01-31 | 198,825 | 77,798 | 6,867 | 5,835 | 43,046 | 17,037 | 36,015 | 89,354 |
| 2019-01-31 | 219,295 | 72,496 | 7,722 | 6,283 | 44,269 | 31,181 | 43,520 | 80,785 |
| 2021-01-31 | 252,496 | 80,925 | 17,741 | 6,516 | 44,949 | 28,983 | 41,194 | 88,763 |
| 2023-01-31 | 243,197 | 76,693 | 8,625 | 7,933 | 56,576 | 28,174 | 34,649 | 83,135 |
| 2026-01-31 | 284,668 | 99,617 | 10,727 | 11,172 | 58,851 | 28,735 | 34,624 | 104,774 |

($ millions; the intervening years are in the research file.) What moved, and what it says:
- **Equity against goodwill.** Goodwill jumped from $17.0B to $31.2B in FY2019 (the Flipkart purchase of 2018) and has sat
  near $28.7B since; equity was lower in FY2023 ($76.7B) than in FY2017 ($77.8B) and is $99.6B now. Tangible equity grew
  slowly because the earnings went out: retained earnings were $89.4B in FY2017 and $104.8B in FY2026, while the company
  earned and paid away the rest in dividends and repurchases (Q6).
- **Inventory against sales.** $43.0B on $481.3B of net sales (8.9%, FY2017, annual report `0000104169-17-000021`) against
  $58.9B on $706.4B (8.3%, FY2026). The jump to $56.5B in FY2022 was the 2022 overstock, worked off in FY2023 with the
  markdowns that took operating income to $20.4B; it has not recurred. Inventory is turning slightly faster than ten years
  ago, the opposite of the tell **[M1995-064]**.
- **Receivables** doubled ($5.8B to $11.2B; 1.2% to 1.6% of sales), consistent with the pharmacy, advertising and
  marketplace lines the MD&A names; small against the whole.
- **Prepaid and other** $4.0B (FY2025) and $4.1B (FY2026), not building **[M1995-064]**.
- **Debt.** Long-term debt $36.0B (FY2017) and $34.6B (FY2026), with a hump to $43.5B after the Flipkart purchase. Debt on
  the face of the balance sheet $39.4B to $44.8B; short-term borrowings rose from $3.1B to $6.6B in FY2026 (Q9).
- **What the figures do not say** **[M2025-032]**: the $63.1B of payables that finance the inventory are a promise to
  suppliers, not equity; the leases ($14.8B operating and $6.1B finance right-of-use assets) are store obligations under
  another name (Q9).

**The income account and the real costs.**
- *Depreciation:* $14.2B, against capital spending of $26.6B; "almost always true costs" **[L2015-004]**, **[R1996-023]**.
  The owner-cash figure deducts all capital spending (Step 0, Q7), with the depreciation variant beside it.
- *Stock pay:* $3.6B (FY2026), $2.8B, $2.1B, $1.6B (FY2023), $1.2B (FY2022) (Note 11 of each 10-K): it has trebled in four
  years, partly the PhonePe modification ($0.7B). It is deducted in full **[L2015-003]**, **[L2021-003]**.
- *The recurring "one-time":* business reorganization charges in FY2023 ($0.8B), FY2025 ($0.26B), FY2026 ($0.15B) and the
  first half of FY2027 ($0.18B); legal charges every few years (opioid settlements $3.3B in FY2023; "certain legal matters"
  $0.29B FY2026, $0.44B in Q2 FY2025). They are in the GAAP figures and in operating cash flow, and are kept in the earnings
  used here **[L2016-007]**, **[M1999-023]**, **[L1998-031]**.
- *Cash taxes:* FY2026 operating cash flow was helped by $2.3B of deferred taxes, the 100% bonus depreciation of the
  OBBB Act ("decreased cash taxes paid in fiscal 2026 and may change the timing", MD&A). A timing benefit, not earning
  power; the five-year mean in Q7 dilutes it.
- *Investment gains:* net income swings with marks on equity investments ($2.0B gain FY2026, $3.2B loss FY2024); ignored
  for earning power **[L2010-017]**, **[M2011-003]**.
- *EBITDA in the filer's mouth:* no instance found in the FY2026 10-K, the two earnings releases or the proxy (text search
  "EBITDA" over all four). The company's own cash measure, "free cash flow", is operating cash less capital spending and is
  said by the company not to deduct debt service or acquisitions (MD&A) **[L2000-036]**.

**The tells.**
- *Predictions:* the company issues quarterly and annual guidance and in Q2 FY2027 "raises outlook for FY27" (8-K Ex. 99.1,
  `0000104169-26-000145`). Predicting growth rates is "both deceptive and dangerous" **[L2000-037]**, and the rows grow
  "incredulous if they consistently reach their declared targets" **[L2002-041]**. Whether Walmart consistently reaches its
  guidance was not measured in this run (the guidance-against-actual record over several years was not assembled); the
  habit of predicting is established, the habit of always making the number is not.
- *Adjusted earnings featured:* both releases lead with "Adjusted EPS". The FY2026 adjustments to operating income were
  $1.16B on $29.8B (PhonePe stock pay $0.72B, legal $0.29B, reorganization $0.15B; 8-K Ex. 99.1, `0000104169-26-000032`);
  the recurring reorganization charge and a stock-pay charge are the kinds of cost the rows say not to wave away
  **[L2016-006]**. Against it: the regular $2.9B of stock pay is not removed; good items are removed as well as bad (the
  opioid derivative-settlement proceeds of FY2025, investment gains); and the Q2 FY2027 tariff-refund gain, the largest
  unusual item of the year, was left *in* the adjusted figure and described in words, which flatters the adjusted line but
  hides nothing.
- *Clear speech:* the 10-K MD&A states each driver in plain terms, including the ones against the company (the $0.9B rise
  in self-insured liability claims, the depreciation from the capital programme) **[M1994-018]**.

**Is it confusion or suspicion?** No. The accounts reconcile, the cash-flow statement matches the company's own free-cash
figure, the balance sheet shows no account building against sales, and the adjusted figures sit within 4% of GAAP with
both directions disclosed. Guidance is a habit; adjusted EPS featured is a second tell in form. Under the two-tell
CONVENTION (Q4) the second tell is required before suspicion; it is present here only in a mild form, and the run does not
read the CONVENTION as making suspicion automatic once two tells are counted (see WHAT IN THE FRAMEWORK WAS WRONG OR
UNCLEAR). The decisive row is the purpose test: "people don’t obfuscate with numbers, usually, without a purpose"
**[M2003-029]**; nothing here is obscured.

**The recast for Q7** (`owner_cash.py`; $ millions; owner cash = operating cash flow − stock pay − all capital spending −
finance-lease principal − dividends to minority partners; the D&A variant replaces capital spending with D&A):

| FY | OCF | capex | SBC | D&A | owner cash, capex basis | owner cash, D&A basis |
|---|---|---|---|---|---|---|
| 2022 | 24,181 | 13,106 | 1,163 | 10,658 | 8,950 | 11,398 |
| 2023 | 28,841 | 16,857 | 1,578 | 10,945 | 9,399 | 15,311 |
| 2024 | 35,726 | 20,606 | 2,093 | 11,853 | 11,209 | 19,962 |
| 2025 | 36,443 | 23,783 | 2,769 | 12,973 | 8,407 | 19,217 |
| 2026 | 41,565 | 26,642 | 3,603 | 14,203 | 9,990 | 22,429 |
| **five-year mean** | | | | | **9,591** | **17,663** |

- **VERDICT on confusion: IN** (the accounts can be read; no suspicion established). **WEIGHS AGAINST, mildly:** guidance
  and adjusted EPS featured **[L2000-039]**, **[L2016-006]**, and a "one-time" reorganization charge in FY2023, FY2025, FY2026
  and the first half of FY2027 (FY2024 not checked). The owner-cash mean of **$9.6B** a year (capex basis) against regular after-tax earnings of about $22B
  (net income attributable FY2026 $21.9B, of which $2.0B was investment gains) is the measure of how much of what is
  earned the business keeps.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet **[M2007-081]**; the yardsticks and the reading tests carry the
weight here.

**The people.** President and CEO **John Furner** since 2026-02-01, 51, at Walmart 32 years, CEO of Walmart U.S. from
November 2019 to February 2026 (10-K, Executive Officers, `0000104169-26-000055`; 8-K `0000104169-26-000023`). Chairman
**Greg Penner**, a member of the Walton family by marriage; the Walton family, through Walton Enterprises, LLC and the
Walton Family Holdings Trust, holds **3,516,197,849** shares, **44.11%** of the class (DEF 14A, Stock Ownership,
`0001193125-26-173673`). The chairman and chief executive roles are separate; eight of eleven nominees are independent;
the board "has not determined the independence of Greg Penner or Steuart Walton" (DEF 14A).

**The first yardstick: the record against the hand dealt** **[M1994-008]**. Furner ran Walmart U.S. through the years in
which its operating income went from **$19.1B** (FY2021) to **$25.2B** (FY2026) and its eCommerce sales reached **$99.6B**,
against the attacker named at Q2 (10-Ks `0000104169-21-000033`, `0000104169-26-000055`). That is a .350 record in the
major leagues **[M2005-039]**, **[M1996-038]**, made in the job the castle depends on. The hand also includes the
international record before him: Asda (U.K.) and Seiyu (Japan) carried as held for sale in the FY2021 10-K and since
sold, and the Flipkart purchase whose return is not disclosed (Q6).

**The second yardstick: how they treat the owners** **[M1994-009]**. The proxy (DEF 14A `0001193125-26-173673`):
- CEO pay FY2026 (Doug McMillon, the outgoing CEO) **$29,240,930**: salary $1.5M, stock awards $21.1M, cash incentive
  $4.0M, above-market deferred-compensation earnings and pension value $2.2M, other $0.4M (Summary Compensation table).
  Ratio to the median associate **958:1** (median $30,520).
- About **82%** of the CEO's target pay rests on "operating income, sales, and ROI"; the long-term performance equity (about
  68% of target) on sales and ROI, measured "on a constant currency basis" and excluding "certain items" (CD&A). The
  committee says it does not use total shareholder return because these metrics "can be impacted by our executives". Pay
  tied "to what is actually under the reasonable control of the person" **[M2003-019]** and with a capital element
  (ROI) **[M2009-081]**: these weigh for. The "certain items" excluded are a doorway for the adjusted figures of Q4.
- No hedging; no unapproved pledging; stock ownership guidelines; a clawback policy (DEF 14A, governance highlights).
- Related-person payments FY2026: about **$2.2M** of fees from entities in which Walton family members have interests,
  described as "immaterial, ordinary-course" (DEF 14A, Related Person Transactions).

**Integrity: the tells the rows name, applied on doubt** **[M2013-088]**.
- *Conduct the filings disclose* (10-K Note 9): opioid dispensing claims settled with all 50 states, a pending DOJ civil
  suit on controlled-substance dispensing, a False Claims Act action; a settlement with the FTC and states over the pay and
  practices of the Spark Driver platform; grand-jury subpoenas on consumer-fraud prevention in money-transfer services;
  antitrust matters in Mexico and India; and an Indian foreign-investment notice to Flipkart. Written down as found
  **[M1997-127]**. The speakers met the same question of this company in 2012 and drew the line between "an occasional
  glitch" in a company "as big as Walmart" and one "fundamentally dishonorable" **[M2012-052]**; the worry is "that it’s
  material and nothing gets done about it" **[M2012-053]**. The matters are of the first kind on the record read: they
  arise in the field among 2.1 million associates, they are disclosed in full in the filing, and they were settled rather
  than fought to the end. None reaches the chief executive or the board in the documents read. The front-page test
  **[M2016-033]** is failed by some of these matters at the level of practice; it is not failed by the management's own
  conduct on what was read.
- *Reports that dance* **[M1995-111]**: none found. The 10-K states the bad drivers in plain words (Q4).
- *Too good to be true; stock price fixation:* the release language ("Our business model is only getting stronger and more
  durable", CFO, 8-K Ex. 99.1 `0000104169-26-000145`) is promotional but not false on the figures.
- *How they talk about mistakes* **[L2024-003]**: a text search for "mistake", "we were wrong", "fell short" and
  "disappoint" in the FY2026 10-K and the two releases found no instance. There is no chairman's letter in the filings read.
  Weighs against, mildly: the owners are told what happened, not what was misjudged **[M1998-036]**.

**Love of the business.** A 32-year insider promoted with four other internal appointees, each with decades at the company
(8-K `0000104169-26-000023`), and a controlling family that has kept 44% for two generations: the people at the top are
attached to this business, not passing through it **[M2000-098]**. The test cannot be run further from outside.

**Ability as a weight on value** **[M1999-104]**. Retail is the business where "Buying a retailer without good management
is like buying the Eiffel Tower without an elevator" **[L1995-006]**; Walmart is not a business "an idiot can run"
**[M1996-037]**. The bench and the succession were visible before the change (**[M2014-059]**, **[L2011-001]**): the
successor came from running the largest segment.

- **VERDICT on integrity: IN** (no doubt reaches the management on the documents read; the disclosed legal matters are
  carried as contrary evidence, of the kind **[M2012-052]** distinguishes from dishonour). **Ability WEIGHS FOR**: a long,
  measured record in the job that matters, against the strongest attacker in the field **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**; the two
factors are the wise employment of the cash flows and the channelling of rewards to the owners **[L1993-020]**.

### Part A: the money
**Where the money went, FY2022 to FY2026** (cash-flow statements, 10-Ks `0000104169-23-000020` and
`0000104169-26-000055`; $ billions): net income attributable to Walmart **82.2** (13.7, 11.7, 15.5, 19.4, 21.9); dividends
paid **32.6**; repurchases **35.1** (9.8, 9.9, 2.8, 4.5, 8.1); earnings kept on the books **14.5**. In cash, capital
spending above depreciation was **40.4** over the same five years, financed from operating cash and a little debt.

**The retention test** **[R1995-009]**, **[M1998-110]**, read in market value and against intrinsic value **[R2009-002]**.
The market leg passes by a wide margin: the market value of the shares held by non-affiliates was **$182.9B** on 2020-07-31
and **$391.7B** on 2025-07-31 (10-K covers, `0000104169-21-000033`, `0000104169-26-000055`) while about $14.5B was kept; but
at a price the Q7 range puts at four times value the market leg alone misleads **[R2009-002]**. The intrinsic leg: operating income rose
$3.9B (FY2022 to FY2026) to $9.4B (FY2023 to FY2026) on about $30B of added net tangible capital (Q3), about 12% to 32%
pre-tax on the increment depending on the base year. At the middle of that span a dollar kept in the U.S. business is worth
more than a dollar at the bond rate; the test passes for the U.S. stores, by judgment and not by a margin that needs no
pencil.

**Abroad the record is worse.** Walmart International carries total assets of **$86.1B** for operating income of **$5.1B**
(FY2026 segment note), about 6% pre-tax, against Walmart U.S. at $25.2B on $165.6B. Asda was sold in February 2021 "for
net consideration of $9.6 billion" with a pre-tax loss of **$5.5B** in FY2021 (10-K FY2023 MD&A, `0000104169-23-000020`).
In FY2024 the company paid **$3.5B** to buy out Flipkart minority holders and settle a PhonePe liability (10-K FY2026 Note 3);
Flipkart's own return is not disclosed. The capital sent outside the U.S. over the last decade has earned far less than the
capital kept at home **[M2007-031]**.

**Buybacks** **[L1999-023]**, **[L2011-003]**. The programme names no price: repurchases depend on "current cash needs,
capacity for leverage, cost of borrowings, our results of operations and the market price of our common stock" (10-Q,
`0000104169-26-000154`), a new **$30B** authorization was announced with the Q4 release (8-K Ex. 99.1, `0000104169-26-000032`).
Prices paid: **$104.48** to **$116.69** a share in the last quarter of FY2026 (10-K Item 5); **$5.1B** at an average of
**$120.71** in the first half of FY2027 against **$92.03** a year earlier (10-Q). The 10-Q does say purchases were larger
"during the first quarter of fiscal 2026" because of "opportunistic prices", which is a sign of price sensitivity. Under the
CONVENTION (Q6), a programme with no stated price is read by the prices paid against the bottom of the Q7 range: the bottom
is **$21.36** a share (Q7), and every price paid in the period is four to six times it. **Weighs against** **[L2016-002]**,
**[L1999-028]**.

**Issuance and deals.** No all-stock deal by an undervalued acquirer (the one STOP, **[L2009-019]**); the large purchases were
for cash (Flipkart 2018; Vizio, part of the $1.9B "payments for business acquisitions" of FY2025, cash-flow statement). Not a
serial issuer: shares outstanding fell from 8,080M (FY2023 start) to 7,969M (FY2026 end) (statement of shareholders'
equity) **[L2014-015]**. Value given against value got on Flipkart cannot be judged from the filings **[M1995-001]**.

**Dividends.** $0.99 a share for FY2027 (Note 12), about 1% of the price; raised every year in the statements read. Not
paid by a ratio rule that the filings state.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**: sales, operating income and ROI, with ROI carrying the capital
  charge a capital-heavy business needs **[M2009-081]** (DEF 14A, Q5). Against: the metrics exclude "certain items" and are
  computed in constant currency, so the paid-on figure is an adjusted one; and $29.2M at 958:1 is large, though "the real
  sin is having a mediocre manager" and not the size of the number **[M2007-006]**.
- **The board and the owners.** The Walton family's **44.11%** is the "huge and true ownership interest" the rows want on a
  board **[L2002-033]**, held for two generations; the chairman is family and the chief executive is not, so the hard case
  of a mediocre chief executive who also chairs **[L2014-026]** does not arise. A controlling owner also means the minority
  owner rides on the family's choices.
- **The owners told:** quarterly and annual earnings guidance is given (Q4); the speakers call forecasting earnings
  destructive **[M2022-054]**. Weighs against.

- **Part A WEIGHS AGAINST**: the U.S. reinvestment passes the retention test by judgment, but the capital sent abroad has
  earned little, and the buybacks are made without a stated price at four to six times the bottom of the Q7 range
  **[L2016-002]**, **[L2011-003]**.
- **Part B WEIGHS FOR, narrowly**: pay on controllable metrics with a capital charge and a family that owns 44% **[M2003-019]**,
  **[L2002-033]**, against adjusted pay metrics and guidance **[M2022-054]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[R1996-018]**, as a range **[L2000-024]**,
**[L1999-027]**. Construction by the CONVENTION (Q7, with the four PG specifics); arithmetic in
`Test Runs/_research 2026-10-06 WMT/value_range.py` and its output file.

- **Cash input:** five-year mean of owner cash after every real cost, FY2022 to FY2026, **$9,591M** (capex basis, Q4); the
  depreciation variant is **$17,663M**. The maintenance judgment (Q3): about the depreciation charge, so the variant is
  what owner cash would be if all spending above depreciation were optional and stopped. It is shown beside, not used for
  the range, because the filings do not show that the spending above depreciation can stop without the castle losing
  ground (Q3).
- **Growth shown,** on aggregate owner cash (capex basis), FY2022 to FY2026: $8,950M to $9,990M, **2.8% a year**. Q3's cap
  is the operating-income growth of about 5.8%; the shown rate sits below it and is used. The depreciation-basis rate of
  18.4% is rejected as a base-year artefact **[L2005-003]**, **[M1999-067]**.
- **Ten years, then no growth** (zero nominal), discounted throughout at **5.66%** **[M1996-025]**.

| case | value | per share | expected return at $105.07 (after tax / pre-tax) | price that earns the floor |
|---|---|---|---|---|
| capex basis, no growth (**bottom**) | $169.5B | **$21.36** | 1.15% / 1.52% | $15.99 |
| capex basis, 2.8% shown (**top**) | $211.5B | **$26.66** | 1.49% / 1.97% | $19.67 |
| capex basis, 5.8% (the Q3 cap, shown for scale) | $268.3B | $33.82 | 1.94% / 2.57% | $24.61 |
| D&A variant, no growth | $312.1B | $39.33 | 2.12% / 2.80% | $29.45 |
| D&A variant, 5.8% | $494.1B | $62.28 | 3.48% / 4.60% | $45.32 |
| D&A basis, 18.4% (rejected) | $1,322.5B | $166.70 | 8.17% / 10.81% | $116.13 |

(Pre-tax is the after-tax return divided by one less the FY2026 effective tax rate of 24.4%; the floor is about 10% pre-tax,
7.56% on after-tax owner cash. COMPUTATION — the expected returns assume the price is paid for the stated cash stream.)

- **Value range: $21.36 to $26.66 a share against $105.07.** Width 1.25 to 1, well inside the three-to-one CONVENTION, so the
  range is narrow enough to conclude from **[L2000-025]**. Even the depreciation variant carried at the Q3 cap ($62.28) is
  below the price.
- **The price against the range.** The price is about four times the top of the range. At $105.07 the expected return is
  **1.2% to 1.5% a year after tax** (1.5% to 2.0% pre-tax) across the range; the price implies owner cash (capex basis)
  growing about **20%** a year for ten years at the bond rate and about **25%** a year to earn the floor, against 2.8% shown
  and about 6% for operating income. Only the rejected 18.4% case reaches the price. Under the CONVENTION's fourth specific,
  a price above the top of the range closes OUT through the floor: "there’s just a point at which we drop out of the game"
  **[M2003-149]**, **[L2002-020]**.
- **How sure** **[M1999-104]**: the moat is a worked one (Q2) and the reinvestment need is undecided (Q3); neither moves the
  range enough to matter against a fourfold gap.

**Reported at the owner's request (COMPUTATION — NOT A CLEARANCE, since the file closes at this STOP):**
- **Value range:** $21.36 to $26.66 a share.
- **Fair price** (the price at which the central case, 2.8% shown growth, earns about 10% pre-tax): **about $19.67**; with the
  Q3 cap of 5.8% instead, about $24.61. No price inside the range at the bond rate earns the floor; the fair price sits below
  the bottom of the range.
- **Cheap price** (owner cash with no growth at all earns about 10% pre-tax, so no pencil is needed): **about $16**.
  The price is about 6.6 times the cheap price and 5.3 times the fair price.

- **VERDICT: OUT.** Valued, with a range narrower than three to one, and the price far above its top: the expected return at
  the price (about 1.5% to 2% pre-tax) is below the floor of about ten percent **[M2003-149]**, **[L2002-020]**, and far from a
  price that would "scream" **[M2009-005]**. "You can turn any investment into a bad deal by paying too much" **[M2019-015]**.
  The speakers' own narrated omission on this name was fading on a small rise when the price was below value **[M2003-047]**;
  the gap here is not a small rise but a multiple, and the omission rows do not reach it **[M1997-083]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- **NOT REACHED as a clearance** (the file closed at Q7). Recorded only: the 30-year Treasury at 5.66% beats the 1.2% to 1.5%
  after-tax expected return at the price in every case of the range, so the name would also be "taken out of the filter" by
  the bond **[M1997-089]**. The ranking against holdings was not done (blind rule).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- **NOT REACHED as a clearance**; recorded. Debt on the face of the balance sheet **$44.8B** at FY2026 (short-term borrowings
  $6.6B, long-term debt due within a year $3.5B, long-term debt $34.6B), plus lease obligations of $15.6B operating and
  $6.8B finance (balance sheet, `0000104169-26-000055`); interest paid **$2.8B** against operating income of **$29.8B**
  (cash-flow supplemental and income statement), about ten times **[M1995-104]**. Payables of $63.1B are the larger claim, owed
  to suppliers on terms and turned by the inventory. The three strengths **[L2014-023]**: a large and reliable stream of
  earnings, yes; massive liquid assets, no ($10.7B of cash against $107.5B of current liabilities); no significant near-term
  cash requirements, moderate (the $6.6B of short-term borrowings must roll **[L2010-020]**). Self-insured liability claims
  rose by about $0.9B in FY2026 (MD&A). Weighs neither way decisively for a business of this size; not a ruin case.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- **NOT REACHED.** At a price four times the top of the range the draft would have the buyer do nothing: inaction is the
  default **[M1996-006]**, and the omission rows on this very name concern a price below value **[M2003-047]**, not this one.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- **NOT REACHED.** Not a named business **[M2007-018]**; the legal matters of Q5 would be read under the newspaper test
  **[M2008-011]** if the file were reopened.

---
## THE BOX
**OUT** at **Q7**: value range **$21.36 to $26.66** a share against **$105.07** (2026-10-05 close); expected return at the
price about 1.5% to 2% pre-tax, against a floor of about ten percent **[M2003-149]**. Q1 IN, Q2 IN (the low-cost operator's
castle, worked, not self-standing), Q3 UNDECIDED, Q4 IN on confusion (weighs against mildly), Q5 IN (ability weighs for),
Q6 Part A against, Part B for narrowly. The file reopens only on price: about **$19.67** (fair, the central case at the
floor) and **about $16** (cheap, no growth at the floor), both COMPUTATION, not clearance; or on owner cash after all
capital spending rising well above the $9.6B mean, which would show the spending above depreciation paying the owner.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Commits: Step 0 to standing rule, Q1, Q2, Q3, Q4, Q5, Q6, Q7, this close.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-06 WMT/ids.py --check` against `principle_ledger_v5.csv`
      before each commit); every filing fact has its accession; numbers come from a filing, a script in the research folder,
      or a CONVENTION named where used.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are recorded as NOT REACHED.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal, minority dividends), never
      a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1, Q2, Q5).
- [x] No row dated after the anchor is cited (not a point-in-time run; run date 2026-10-06, all rows earlier).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its "OE" windows, yields and growth line were not.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q4's two-tell CONVENTION reads as necessary, not sufficient, and has no size.** "It becomes suspicion [...] only with a
second tell" leaves open whether two tells make suspicion automatic. Walmart issues guidance (the predicting habit) and
leads its releases with adjusted EPS (a second tell in form), but the adjustments are under 4% of operating income, run both
ways and are disclosed; whether the guidance is consistently met was not measured. I read "only with" as necessary and
decided suspicion on the purpose row **[M2003-029]**; another analyst could close Q4 here. The CONVENTION needs a sentence on
whether two tells close the file and whether the size of the waved-away cost counts. (2) **Q7's cash input when capital
spending is twice depreciation.** The CONVENTION deducts all capital spending and shows the depreciation variant beside it,
but does not say what a stated maintenance judgment does to the range. Here the choice moves the bottom of the range from
$21 to $39; it did not decide the box, because both sit far below the price, but for a cheaper growing reinvestor it would.
(3) **Q1's holding-company CONVENTION has no test for "a part that matters".** Walmart International is about 16% of segment
operating income and Flipkart and PhonePe are not reported separately; I carried the Indian part to Q3 and Q6 as a capital
question rather than closing Q1, and said so. (4) **Q6's retention test has no stated way to compute its intrinsic leg**, and
the increment's return here runs from 12% to 32% pre-tax depending on the base year; I judged it at the middle. **Tool
notes:** `tools/run.py` lists a stale pre-split balance-sheet share count (3,418M as of 2012) beside the cover count; it marks
it STALE and does not use it, so no defect in the arithmetic; its owner-earnings columns omit finance-lease principal and
minority dividends in the main table and show them only as alternates, which the recast here corrects from the filings.
