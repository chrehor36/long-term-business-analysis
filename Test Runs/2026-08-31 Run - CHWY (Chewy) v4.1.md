# Company Run — Chewy, Inc. (CHWY) — 2026-08-31
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**PROVENANCE, declared first: this is an OPERATOR-REQUESTED name, not screen-sourced.**
It would never surface on this project's screen. The frozen v3b statute gate is
`worst5_NI / cap ≥ max(DGS30, 4%)`, with `worst5 < 0` failing outright. Chewy's worst net
income in the five-year window is **−$75.2M (FY2021)**, an automatic fail. On the most
generous recent five-year cut the worst year is **$39.6M (FY2023)**, which is **0.42%** of
the current $9.52bn capitalisation against a 5.19% requirement. **The screen would reject
it by an order of magnitude.** Said plainly at the top, per operator instruction.

**AGAINST THE STATED MANDATE, also declared first: Chewy pays no dividend.** The
operator's roughly $2,750 of taxable capital is earmarked for a dividend payer that
compounds. The FY2025 10-K, verbatim: *"We have never declared or paid any cash dividends
on our capital stock, and we do not currently intend to pay any cash dividends for the
foreseeable future."* And in the risk factors: *"stockholders must rely on sales of their
Class A common stock **after price appreciation as the only way to realize any future
gains** on their investment."* Chewy's entire return of capital is repurchases, $950M of
which went **directly to the controlling shareholder** rather than to the market (Q3
below). **The company itself says the only return available here is the one the mandate
excludes.** On the mandate alone this name is disqualified before any gate opens.

**POSITION NOTE:** the operator holds **no Chewy position**. This is a fresh entry run,
Q1 to Q5 in hard sequence, stopping at the first non-IN. Q6 is answered regardless
(pre-committed yardsticks, bands, catalysts). There is no [E2-28] hold read because
nothing is held.

**BIAS WARNING, entered before any evidence was weighed (operator rule 9).** Chewy is a
well-liked consumer brand with an emotionally sticky product and a widely-repeated
narrative that Autoship is a moat. The iron prescription **[E4-51]** binds this run: the
bear case is stated better than the bears state it, at Q2 and again at Q4. The
counter-discipline binds too. An analyst who rejects a name *looks* rigorous, so the bull
facts are stated in full and are not shaded: share taken from a shrinking Petco every
year, three straight years of gross-margin expansion, a genuinely capital-free growth
model, no debt, and real owner earnings for the first time in the company's life.

Analyst inputs beyond the filings: `Test Runs/_research 2026-08-26/CHWY competitor row
(WOOF-AMZN-FRPT, WMT-TGT context).md` (the Q2 row, committed alongside this file) and
`Test Runs/2026-08-30 Run - COST (Costco) v4.1.md` (format precedent only).

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** [E4-15, E3-32]:
- rate **5.19%** · date **2026-08-27** (latest observation) · fetched 2026-08-31 ·
  source: **FRED `fredgraph.csv?id=DGS30`, 30-Year Treasury Constant Maturity**, saved as
  `Test Runs/_research 2026-08-26/CHWY_DGS30_2026-08-31.csv` (12,924 rows, 1977-02-15 to
  2026-08-27). FRED lags the intraday quote by a day or two. Immaterial, and known.
- Chewy earns and reports in **USD**. Item 7A: *"We have operations principally within the
  U.S. and therefore have only minimal foreign currency exposure."* No FX, no ADR ratio.
- *Route note.* `tools/run.py` and `tools/sources.py` could not reach FRED or Yahoo from
  this machine (python `urllib` returned `RemoteDisconnected`); `curl` reached both. The
  run.py arithmetic was **reproduced locally, formula for formula** (owner-earnings band,
  implied-growth engine, points-over-sovereign engine) with the curl-fetched inputs passed
  in. No tool file was edited. Same numbers, sooner, which is the only test a tool has to
  pass here.

**Price and market capitalisation. THE DUAL-CLASS CHECK, done explicitly:**
- Price **$23.26**, close **2026-08-28**, Yahoo Finance chart API. **Aggregator, live
  quote only, flagged.** A second source was attempted (Stooq) and was blocked by a
  JavaScript browser-verification wall. One aggregator, flagged, per protocol.
- **Chewy is dual class.** Class A (NYSE: CHWY, one vote) and Class B (unlisted, **ten
  votes**) carry **identical economic rights**. The 10-K states that holders of both
  classes *"are entitled to share equally, on a per share basis, in dividends and other
  distributions"* and share ratably on liquidation, and EPS is computed on the combined
  count under the two-class method.
- **Total economic shares, from the newest filed cover page (10-Q, as of 2026-06-03):**
  Class A **232,945,978** plus Class B **176,478,229** equals **409,424,207**.
- **Market cap = 409,424,207 × $23.26 = $9,523.2M.**
- **The trap, avoided and shown.** Class A alone × $23.26 is **$5,418M**, a **43%
  understatement** of the capitalisation. That error would have turned a 1.8%
  owner-earnings yield into 3.2% and materially mis-ranked the name. The RMR run was
  nearly wrecked by exactly this, and the check is now standing procedure.
- Cross-check against a second filed count: the **10-K cover, 2026-03-18** gives Class A
  240,198,735 plus Class B 176,478,229, or 416,676,964, which is $9,692M. The two filed
  counts differ by 1.8% (Q1 buybacks and RSU vesting between the dates). **The newer count
  is used.** Every conclusion below is invariant across both.
- Third cross-check, from the 10-K cover itself: aggregate market value held by
  **non-affiliates** at 2025-08-01 was *"approximately $8.0 billion"* at $35.91, implying
  roughly 222.8M non-affiliate shares against roughly 415M outstanding, so affiliates held
  about 46%. That is consistent with the proxy's 43.2%. The dual-class arithmetic
  reconciles three ways.

**The filing was read**, not tagged data [E3-27]:
- [x] MD&A (key financial and operating data; all three non-GAAP reconciliations; results
  of operations; liquidity; cash flows; ABL; share repurchase activity; future
  acquisitions; critical accounting estimates)
- [x] cash-flow statement including its detail lines (SBC, D&A, non-cash lease expense,
  deferred taxes, every working-capital line, capex, repurchases, tax withholdings)
- [x] footnotes (Note 1 description of business and the BC Partners Transactions; Note 2
  policies, vendor rebates and **supplier concentration**; Note 4 property and equipment;
  Note 5 intangibles; **Note 6 Commitments and Contingencies, Legal Matters**; Note 7 Debt;
  **Note 8 Leases** with the full maturity table; Note 9 Stockholders' Equity with the
  **Class B conversion history**; Note 10 share-based compensation; Note 12 Income Taxes;
  Note 14 related-party transactions)
- documents:
  - **Form 10-K FY2025 (52 weeks ended 2026-02-01), filed 2026-03-25, accession
    0001766502-26-000034**, primary document `chwy-20260201.htm`, US GAAP, USD.
  - **Form 10-Q Q1 FY2026 (13 weeks ended 2026-05-03), filed 2026-06-10, accession
    0001628280-26-042060**, for freshness and for the two acquisitions.
  - Form 10-K FY2024, accession **0001766502-25-000014**, and FY2022, accession
    **0001766502-23-000011**, for the multi-year active-customer and NSPAC series only.
  - **DEF 14A filed 2026-05-22, accession 0001140361-26-022529**: sponsor ownership, board
    composition, executive compensation.
  - **Form 8-K furnished 2026-04-28, accession 0001193125-26-187308** and its **Exhibit
    99.2 Settlement Notice**, covering the derivative action against the controlling
    stockholder. Read in full. It is the single most important Q3 document in the set.
  - Form 8-K 2026-02-24 (accession 0001193125-26-065612) and 2026-01-20 (accession
    0001193125-26-015958), covering CFO and CTO changes.
  - Earnings-release exhibits 99.1 for FY2024 Q4 (0001766502-25-000013), FY2025 Q4
    (0001766502-26-000033) and Q1 FY2026 (0001628280-26-042058).
- **Figure cross-checked against the filed statement: FY2025 net cash provided by
  operating activities $691.6M.** Identical in three independent places in the document
  (the Key Financial and Operating Data table, the Free Cash Flow reconciliation, and the
  audited Consolidated Statements of Cash Flows line "Net cash provided by operating
  activities | 691.6"), and restated in the MD&A prose: *"Net cash provided by operating
  activities was $691.6 million for Fiscal Year 2025."* Second figure cross-checked:
  **net sales $12,601.5M**, identical in the metrics table, the income statement and the
  segment note.
- **52/53-week flag: FY2024 (ended 2025-02-02) was a 53-WEEK year.** The company
  quantifies it: *"Excluding net sales of $226.6 million in the 53rd week for Fiscal Year
  2024, net sales for Fiscal Year 2025 increased by $966.8 million, or 8.3%."* FY2021,
  FY2022, FY2023 and FY2025 were 52 weeks. Flagged wherever it bears below, and the
  owner-earnings table carries a weeks column.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? [E3-31]

- **Unit economics in my own words, without management's language.** Chewy buys pet food,
  litter, medicine and toys, almost all of it made by other companies, and ships it out of
  17 leased warehouses to 21.5 million American households, most of them on a standing
  repeat order. Each active customer spends **$591 a year** and leaves Chewy **$176 of
  gross profit**. Out of that $176, Chewy spends about **$39 on advertising** to find and
  keep that customer and roughly **$125 on warehouses, delivery, customer service and
  overhead**, leaving about **$12 of operating profit per customer per year**. Suppliers
  finance the goods: payables of $1,221.4M against inventories of $864.8M is **141%
  coverage**, and the cash conversion cycle is **negative 8.3 days**. Growth therefore
  needs almost no capital, and capex was **$129.2M, one percent of sales**. Two genuine
  engines sit beyond plain retailing. First, a licensed **pharmacy**: Chewy says it
  operates *"the #1 pet pharmacy in America"* and has roughly 20,000 vet practices, about
  50% of U.S. clinics, on its PracticeHub platform. Second, **sponsored advertising sold
  back to the brands whose goods it ships**, which the 10-K names as a driver of
  gross-margin expansion but does not size.
- **The scarce input this business controls.** Not the products: 4,000 brands, roughly
  190,000 SKUs, and **three vendors alone are 39% of net sales**. Not the delivery, which
  is bought from carriers. What Chewy controls is the **standing order**. 84.4% of net
  sales now arrive through Autoship, which is a payment instrument on file, a shipping
  cadence and a reordering habit. Second and smaller, the **pharmacy licences and
  vet-channel integration**, which are genuinely hard to assemble.
- **Will the fundamentals look broadly the same in ten years?** Yes in character. People
  will feed pets, and a meaningful share of that will ship to the door. The *character* is
  simple and stable [E3-31]. What is not stable is who does the shipping, and that is a Q2
  question rather than a Q1 one.
- **VERDICT: [x] IN.** The money-making is legible in one paragraph and the arithmetic
  reconciles from the filed statements. What is in doubt is not comprehension.

## Q2 — IS IT A FRANCHISE? [E3-03]

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by
> its customers to have **no close substitute** and; (3) is not subject to price
> regulation." — **[E3-03]**, 1991 letter

- Needed or desired **[x]**. 21.5M households buy, most on standing order, and the product
  category is non-discretionary.
- **No close substitute: [ ] FAILS, on the issuer's own words.** The FY2025 10-K's
  competition paragraph, verbatim: *"We face competition from the websites of our
  competitors such as other online retailers, online sales for omnichannel retailers,
  **our suppliers' own websites**, and traditional brick and mortar retailers as well as
  those in the veterinary channel. Some of the principal competitive factors influencing
  our business are **price**, product selection and availability, fast and reliable
  delivery, and customer service."* Price is listed **first**. The goods are third-party
  branded and physically identical at Amazon, Walmart, Target, Petco and the
  manufacturers' own direct sites. A 40-pound bag of Purina Pro Plan bought at Chewy is
  the same bag.
- Not price-regulated **[x]**.
- **Must the moat be continuously rebuilt? [E4-04], scoped by [E5-23].** The honest answer
  sits in between, and it is drifting toward rebuild. Advertising and marketing ran
  **6.7%, then 6.8%, then 6.5%** of net sales across FY2023 to FY2025. That was $824.9M
  last year, **$38.68 per active customer against $176.02 of gross profit**, and it has not
  fallen as a share of sales while the customer base grew. Coca-Cola's advertising defends
  the *same* trademark [E5-23, E3-49]. Chewy's advertising largely **re-buys** customers
  into a habit that any competitor's promotion can interrupt. This is not the
  depleting-asset class [E4-04] excludes, but it is not the clean maintenance case either.
- **Does success depend on a great manager? [E4-23] Mayo test, recorded here at Q2 where
  the corpus puts it.** Partially, and that is a **moat defect**. At a **2.02% operating
  margin** a 100bp execution error erases half the profit, and there is no membership
  annuity, no prepaid fee and no toll. This is [E3-38]'s own named class: *"For a retailer,
  hiring that nephew would be an express ticket to bankruptcy."* It is the opposite of
  [E5-18]'s *"capacity to stand"* mismanagement.

**Primary moat metric, filing-sourced, and its trend. BOTH SERIES [E4-55].**

| Fiscal year | Active customers (M) | y/y | NSPAC | y/y | Autoship % of sales | Gross margin |
|---|---|---|---|---|---|---|
| FY2020 | 19.206 | | $372 | | 68.4% | |
| FY2021 | **20.663** (peak) | +7.6% | $430 | +15.6% | 70.2% | |
| FY2022 | 20.405 | **−1.2%** | $495 | +15.1% | 73.0% | |
| FY2023 | 20.083 | **−1.6%** | $555 | +11.9% | 76.2% | 28.4% |
| FY2024 (53 wks) | 20.514 | +2.1% | $578 | +4.1% | 79.2% | 29.2% |
| FY2025 | **21.327** | +4.0% | $591 | **+2.2%** | 83.3% | 29.8% |
| Q1 FY2026 | 21.497 | +3.6% | $597 | +2.4% | 84.4% | 30.1% |

**The units read [E4-55].** The physical series **peaked in FY2021, fell for two
consecutive years, and did not regain the peak until FY2025, four years later**. Across
those years dollar revenue never fell, because NSPAC rose 15.6%, then 15.1%, then 11.9%.
That is precisely the pattern the corpus says to read as *"a serious reverse, not likely
to disappear in some 'bounce back' effect."* It **has** now bounced back, with units at
+4.0% and +3.6%, but the two engines have swapped: the price-and-mix engine has decayed
from +15% to +2%, and units are doing the work. **The COVID distortion is named [E4-41]:**
FY2020 and FY2021 carried a pet-adoption boom and FY2022 and FY2023 are its normalisation,
so any growth rate drawn across those endpoints is the [E4-38] calculated-endpoint artifact
and is not used here.

**[E2-44] two-characteristic test: scores 1 of 2.**
1. *Raise price with demand flat?* **No filed evidence, in seven years of filings.** Gross
   margin did widen 140bp in three years, and the 10-K attributes it to *"growth in
   sponsored ads and margin growth across our consumables business"*, meaning advertising
   fees charged back to the brands plus mix into pharmacy. That is not a price rise.
   **[E4-37] agony test: a business that lists price first among its competitive factors
   and names its own suppliers' websites as competitors is at the agony end of that scale.**
2. *Grow dollar volume with only minor additional capital?* **Yes, emphatically.** Capex is
   1.03% of sales and net operating capital employed is **negative $651.9M**, because
   suppliers and accrued liabilities fund the whole working balance. This is a real and
   unusual strength and it is not diminished below.
- **[E3-33] untapped pricing power, scoped by [E5-28]:** claiming that class claims
  near-monopoly. Chewy is not one. **The class is not claimed, and nothing below rests on
  it.**

**[E3-46] the second question about the business is a number.** Return on capital employed
is not measurable in the usual way here, because the denominator is negative. On the gross
operating asset base that does exist (PP&E $552.3M plus inventories $864.8M plus
right-of-use assets $467.9M, or $1,885.0M), operating income of $254.3M is **13.5%
pre-tax**. Respectable. Not the *"very high returns on capital employed"* [E3-46] asks
about in the best businesses, and achieved only after fifteen years and $12.6bn of revenue.

**[E5-35] Kirkland, run in reverse.** Buffett's passage is about the retailer's own brand
taking power from the national brands. Chewy is the retailer. It has run private brands
for a decade (Frisco in 2016, American Journey, Tylee's, Vibeful in 2022, Get Real in 2025)
and **discloses no private-brand share of sales in any filed year**. Meanwhile its **three
largest vendors have been 39% of net sales for three consecutive years** (Note 2,
verbatim). Costco names Kirkland and sizes it; Petco lists six owned brands across roughly
1,400 stores. A decade of non-disclosure is itself the reading: **the retailer's own brand
is not yet where the economics live.** The premium margin in this category sits with the
manufacturer. Freshpet earns **40.8% gross and 6.87% operating** on $1.1bn, three times
Chewy's operating margin.

**THE COMPETITOR ROW [E3-28]**, built and committed as `Test Runs/_research 2026-08-26/
CHWY competitor row (WOOF-AMZN-FRPT, WMT-TGT context).md`, accessions in the row file.
Chewy's and Petco's fiscal years end **one day apart** (2026-02-01 vs 2026-01-31).

| Metric | **CHWY** FY2025 | **WOOF** FY2025 | **FRPT** FY2025 | **AMZN** FY2025 |
|---|---|---|---|---|
| Net sales | **$12,601.5M** | $5,961.5M | $1,102.0M | $716,924M |
| Growth | +6.2% (+8.3% ex 53rd wk) | **−2.5%** (comps −1.6%) | +13.0% | +12.4% |
| Gross margin | 29.8% (+60bp) | 38.7% (services-incl.) | **40.8%** | n/d |
| **Operating margin** | **2.02%** | **2.02%** | **6.87%** | 11.2% (NA seg 6.95%) |
| Net income | $222.8M | $9.1M | $139.1M | $77,670M |
| Operating cash flow | $691.6M | $314.1M | $160.6M | not pulled |
| Share-based comp | **$297.9M** | $32.6M | $13.9M | not pulled |
| SBC ÷ net income | **134%** | 358% | 10% | not pulled |
| Capex ÷ sales | **1.03%** | 2.13% | 13.45% | not pulled |
| Funded debt | **zero** | $1,488.5M | ~zero | not pulled |
| OE proxy (OCF − SBC − (c)) | **$264M** | $85M .. $154M | −$2M .. $60M | not pulled |

Context, unsegmented: **Walmart** FY ended 2026-01-31, revenue $713,163M, operating margin
4.18%. **Target**, revenue $104,780M, operating margin 4.88%.

- **Peers named: 3 filing-sourced direct competitors plus 2 context filers.** The industry
  does not have Buffett's eight public pure-plays. Named as fetchable if the file is ever
  re-opened: Central Garden & Pet, and Colgate (Hill's, segmented). Not fetchable:
  PetSmart (private, and **controlled by BC Partners, Chewy's own controlling
  shareholder**, see Q3), Nestlé Purina, Mars.
- **THE AMAZON GAP, recorded honestly.** Amazon's FY2025 10-K contains **zero occurrences
  of "pet food", "pet supplies", "pet products", " pets" or "Pet "**, checked mechanically
  over the full converted document, which returns 10 hits for "Prime" and 2 for "grocery",
  so the conversion is sound. Pet is not separable at any level of Amazon's, Walmart's or
  Target's disclosure. Per the absence-claim rule this is stated as *no pet-category
  disclosure found*, and it is **not UNRESEARCHED**, because there is no document to fetch
  and there never will be. **The single most important cell in this row is permanently
  unfillable**, which is itself a finding about a moat claim that depends on measuring the
  attacker.
- **[E2-45] attacker's test.** With ample capital and skilled personnel I would be Amazon,
  and Amazon already is: its **North America segment alone** is 34x Chewy's revenue at
  **3.4x Chewy's operating margin**, with a denser network, an existing subscribe-and-save
  mechanic and the identical bags. The one genuinely hard-to-copy asset is the regulated
  **pharmacy and vet workflow**, and pet health and specialty was $1,980.5M, **15.7% of
  sales, +11.8%**. Growing. Not yet the business.
- **What the row gives Chewy, stated in full and not shaded.** It is winning. It grew 6.2%
  while Petco shrank 2.5% and comped negative 1.6%. It carries no funded debt while Petco
  carries $1.49bn. It produced more owner earnings in one year ($264M) than Petco and
  Freshpet combined. It grows on a hundredth of its revenue in capex. **On operating
  quality Chewy is the best business in this row.**
- **What the row takes away.** After fifteen years and $12.6bn of revenue, Chewy's
  operating margin is **2.02%, identical to two decimal places to that of the shrinking,
  leveraged, store-based competitor it is beating.** The share gain has not converted into
  an owner's return. [E3-62]'s second step asks *"how much is going to stay home and how
  much is just going to flow through to the customer"*, and the filed answer, for fifteen
  years, is **flow through**.
- **Row limit stated [E3-61]:** the row shows position, not conduct.

- Class: **[x] NARROW.** Real, and located precisely: the standing order plus the
  pharmacy and vet channel. · Direction: **MIXED.** Widening on gross margin, Autoship
  share, units and share of category. Flat to narrowing on the two that decide ownership,
  namely realised pricing power (NSPAC growth from 15.6% down to 2.2%) and the share of
  sales spent to keep the customers (advertising flat at roughly 6.5%).
- **VERDICT: [x] OUT.** Under **[E3-03]** a franchise is one its customers believe has **no
  close substitute**, and Chewy's own filing says the opposite: identical third-party
  goods, competition from its own suppliers' websites, and **price named first** among
  competitive factors. The **[E2-44]** two-characteristic test scores 1 of 2, with
  capital-free growth yes and pricing power no, across seven years of filings containing no
  instance of a price increase pushed through. The **[E4-37]** agony metric reads agony.
  The **[E4-55]** physical series went backwards for two years while dollars rose, and the
  price-and-mix engine that hid it has now decayed to +2%. The **[E2-45]** attack is not
  hypothetical: it is run daily by the best-capitalised retailer on earth, whose exposure
  cannot be measured from any filing that will ever exist. And **[E5-35]** run in reverse
  says the retailer's own brand has not taken the economics, because three vendors have
  been 39% of sales for three years and private-brand share has never been disclosed.

  What remains is exactly what the 1991 letter calls the other thing: **a business, not a
  franchise.** *"a business, unlike a franchise, can be killed by poor management"*
  **[E3-43]**. And a genuinely good one: growing, debt-free, capital-light, and
  out-executing every public peer. It is simply not the class this framework buys, and the
  corpus is explicit that most names should end here: *"about a dozen truly good decisions
  — that would be about one every five years"* **[E5-13]**. **The entry run stops at Q2.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN, Q2 OUT. The hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
**Everything below is FOR THE RECORD**, because the operator tasked this run with the SBC
arithmetic, the sponsor's conduct, the owner-earnings range and the floor, and because Q6
is written regardless. **Every valuation figure below sits under operator rule 3's header.
Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless.
Q3 can stop a run, never start one **[E2-37, E2-38, E3-39]**.*

**STEP 1 — THE WEIGHT CASE, declared first.**
- [x] **Daily execution [E3-38]. TICKED. Q3 would be a BINARY GATE and no price
  compensates [E3-29, E5-35].** Chewy is a retailer, the corpus's own named example, and at
  a 2.02% operating margin the leverage of daily execution on the owner's result is
  extreme. A 100bp cost slip erases half the profit. There is no membership annuity to
  absorb a stumble.
- [ ] Control [E1-16]. No. This is a marketable minority stake and exit exists at any time.
- [ ] Leverage [E3-29]. No funded debt, ABL undrawn, net cash. **But note the amplifier
  that the three determinants do not capture.** Chewy is an NYSE **"controlled company"**,
  exempt from the majority-independent-board and independent-committee requirements, with
  **BC Partners holding roughly 43.2% of the economics and roughly 88.4% of the votes**
  (DEF 14A, record date 2026). **Seven directors are BC Partners partners or employees on
  the proxy's own bios:** Svider (Chairman of BC Partners, **and** Chairperson of Chewy's
  board **and** Chairperson of both its Compensation and its Nominating and Corporate
  Governance Committees), Ahmed, Castelli, Chang, Bigand, Leland and Sibenac. **Four of
  them, Svider, Ahmed, Chang and Bigand, also sit on the board of PetSmart**, a direct
  competitor also controlled by BC Partners, with Svider its Non-Executive Chairman since
  2015. Chang also sits on **PetLab** ("a pet supplements company") and Castelli on **Pug
  Holdco** ("a pet products brand"). All of it is disclosed, and disclosure is the right
  treatment. It is recorded because the competitor row cannot include PetSmart's numbers
  while Chewy's own control group can see both sets. **The minority holder cannot outvote
  anything, ever.** That does not tick [E1-16], whose control test is about *you* owning
  the whole thing, but it changes what "no price compensates" is protecting against.

**Honesty. The binary [E5-16], filings-based, each matter dated to when it became public.**
The sweep, named: FY2025 10-K Note 6 (Legal Matters, incorporated by Item 3), read in full;
the FY2024 10-K's equivalent; the Q1 FY2026 10-Q; every 8-K since 2024-01-01; the 2026
DEF 14A; and the derivative-settlement exhibits.

**What the 10-K's Legal Matters note says, in its entirety of substance:** *"Various legal
claims arise from time to time in the normal course of business… The Company does not
believe that the ultimate resolution of any matters to which it is presently a party will
have a material adverse effect."* **No matter is named. Not one.**

**What was actually pending, and is not in any periodic report:**

> **Gilbert v. BC Partners LLP, et al., C.A. No. 2024-1165-KSJM (Del. Ch.)**, a
> consolidated **stockholder derivative action** naming as defendants BC Partners LLP,
> BC Partners Advisers LP, BC Partners Holdings Limited, CIE Management IX Limited, Argos
> Holdings GP LLC, Argos Holdings L.P., Citrus Intermediate Holdings L.P., Citrus
> Intermediate Topco LLC, Buddy Chester Sub LLC, and directors **Raymond Svider, Sumit
> Singh, Fahim Ahmed, Mathieu Bigand, Marco Castelli, Michael Chang, David Leland, Lisa
> Sibenac, Martin H. Nesbitt and James A. Star**. The Complaint *"asserts derivative claims
> against Defendants alleging that they breached their fiduciary duties by causing Chewy to
> enter into an unfair transaction that prioritized BC Partners' interests over those of
> Chewy and its minority stockholders"*, and specifically that the sponsors *"breached
> their fiduciary duties as Chewy's controlling stockholders by causing Chewy to enter into
> the Downstream Merger on terms that were not entirely fair to Chewy"* (the 2023-10-30
> reorganisation under which Chewy assumed $1.9bn of BC Partners affiliates' tax
> obligations). A **Special Litigation Committee** was formed. Settled by Stipulation dated
> **2026-04-06** for a **cash payment of $29,500,000 to Chewy**, with the Court's scheduling
> order on 2026-04-14 and the settlement hearing set for 2026-06-23. Defendants deny
> wrongdoing. Source: 8-K furnished **2026-04-28, accession 0001193125-26-187308**,
> Exhibits 99.1 and 99.2, read in full.

**How this is scored, precisely, and not more harshly than the record supports:**
- It is **not** a proven [E5-16] integrity failure. It settled without admission, and the
  corpus is explicit that *"penalty size is not seriousness, in either direction"* and that
  the failure that counts is *"they didn't act when they learned"* **[E5-22]**. Here the
  board formed a Special Litigation Committee, the SLC negotiated, and **$29.5M came back
  into the company**. Acting is evidenced. Per the worked TJX precedent, an unadmitted
  civil matter is not the binary.
- It **is** a first-order **[E2-26] half-owner failure.** *"Our guideline is to tell you the
  business facts that we would want to know if our positions were reversed."* Two
  successive annual reports (FY2024 filed 2025-03-26 and FY2025 filed 2026-03-25) carry a
  Legal Matters note that names nothing, while a derivative suit against the controlling
  stockholder and the CEO over a $1.9bn related-party reorganisation was pending. **And the
  Q1 FY2026 10-Q, filed 2026-06-10, covering the very quarter in which the stipulation was
  signed, the court order entered and the 8-K furnished, does not mention it either.**
  $29.5M is 13% of FY2025 net income and 27% of that quarter's operating cash flow. It was
  disclosed, via an 8-K **furnished** under Item 7.01, the lightest channel and expressly
  *"not deemed filed"*, plus a court-ordered notice on the IR website. It was not disclosed
  in the documents an owner reads. That is the exact distinction [E2-26] is drawn on, and
  it fails.
- **[E2-68] conduct across an information asymmetry** is the sharpest available read, and
  it reads unfavourably. Where the company held the information advantage about its own
  controlling shareholder, the disclosure went to the lightest available channel.

**Second honesty item, dated 2026-05-22 (DEF 14A).** The prior year's Summary Compensation
Table *"inadvertently omitted $66,877 related to security charges and $354,552 related to
automobile charges for Mr. Singh in Fiscal Year 2024"*, with the full FY2024 amounts
disclosed on correction as **$1,074,319 of security charges and $779,025 of automobile
charges**. The correction was made voluntarily and prominently. Per **[E2-69]**, judge
deviations by *direction*: a company correcting its own understated perquisite disclosure
is moving **toward** candor, and it is scored that way. The quantum is recorded.

**Third item, disclosed and clean.** The CEO's spouse, **Aseemita Malhotra**, is President
of Healthcare, with FY2025 cash compensation of $1,245,871 plus equity, disclosed in full
with the methodology stated. Related-party employment, fully disclosed. No finding.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E2-52, E3-50, E2-57, E3-53].**
- [ ] **weak accounting.** Not fired. SBC is expensed in full and prominently ($297.9M on
  the cash-flow statement, $311.2M including related taxes, footnoted on the *first*
  metrics table). No defined-benefit pension exists (401(k) only), so no fanciful
  assumption is possible. Deloitte issued unqualified opinions on the statements and on
  ICFR, and the critical audit matter is **vendor rebates**, which is the right one to flag
  in this business.
- [ ] unintelligible footnotes. Not fired. The notes are short, plain and legible, and the
  Class B conversion history is laid out transaction by transaction with dates and share
  counts, which is unusually good disclosure.
- [x] **EBITDA and adjusted-earnings promotion [E4-29]. FIRED, and it is the central
  finding of this run.** The corpus: *"Trumpeting EBITDA … is a particularly pernicious
  practice"*, and *"To say 'stock-based compensation' is not an expense is even more
  cavalier"* **[E5-06]**. Chewy's Key Financial and Operating Data table leads with
  **Adjusted EBITDA $719.2M**, **adjusted net income $540.5M**, **adjusted diluted EPS
  $1.27** and **free cash flow $562.4M**, every one of which adds back the **$311.2M of
  share-based compensation and related taxes** that is 134% of GAAP net income. The CEO's
  own results quote leads with *"$719 million of adjusted EBITDA… record free cash flow of
  $562 million"*, not with the $222.8M the owners actually earned. The reconciliations are
  complete and honest and nothing is hidden, but the **promoted** measure is the one that
  deletes the largest real expense in the business. Quantified in full at Q4.
- [x] **serial share issuance [E5-15]. FIRED in substance, though not in the classic
  form.** Chewy does not sell shares to the public. It issues them to employees, at scale.
  **12.5M RSUs were granted in FY2025** at a $34.15 average, plus 1.2M PRSUs. The 2024
  Omnibus Plan authorises up to **83.1M shares, or 20.3% of shares outstanding**. And
  **$510.2M of already-granted, unrecognised compensation** ($478.8M RSU plus $31.4M PRSU)
  is committed ahead. Share count: 425.4M (FY2022), 431.8M (FY2023), 413.6M (FY2024),
  **415.1M (FY2025, up)**, 409.85M (Q1 FY2026). **In FY2025 the company spent $262.5M on
  buybacks and the share count still rose by 1.5M.** The repurchase is not retiring
  capital, it is offsetting issuance, and in FY2025 it did not even do that.
- [x] **metric-switching [E2-49]. FIRED, as a prompt to read.** The Q1 FY2026 10-Q states:
  *"Beginning in the first quarter of 2026, Adjusted net income excludes transaction-related
  costs prospectively."* The exclusion was widened in the same quarter the company closed
  **SmartPak ($175M)** and announced **Modern Animal ($400M)**, so the new exclusion is for
  costs the company had just begun to incur at scale. [E2-49] demands *"pre-set,
  long-lived and small bullseyes"*, and a definition widened concurrently with the activity
  it excludes is the pattern the flag exists for. It was disclosed plainly and
  prospectively, which is the mitigating half. Recorded, not escalated.
- [ ] **trumpeted earnings projections [E4-22, E3-48].** **Cannot be scored from the filed
  record, and that is itself the finding.** Chewy **does** guide. The FY2024 Q4 release
  quotes the CEO: *"Topline growth and profitability exceeded the high-end of our guidance
  ranges for both the fourth quarter and full year 2024."* But **no numeric guidance table
  appears in any of the three earnings-release exhibits examined** (FY2024 Q4, FY2025 Q4,
  Q1 FY2026), because guidance is given on the call and in IR materials that are not filed.
  [E3-48]'s prescribed action is to *"pull the company's own past guidance and set it
  against outturn"*, and the artifact that would do it is the **quarterly earnings-call
  transcript or IR shareholder letter**, which is not an SEC filing and is not on the
  citation shelf. Named as a document, not guessed at. **[E5-30]** is noted: a guidance
  culture is a ratchet, and this one is live.
- [ ] filed-figure tells [E4-30]. **Not fired, and the reason is disclosed.** Cash taxes
  are far below the book provision (FY2025: roughly $14M of operating cash tax and $23.3M
  in total against $263.3M of pretax income and a $40.5M provision), which is the shape
  [E4-30] warns about. The filing explains it: net operating loss carryforwards from a
  decade of losses, R&D credits, and **tax deductions on share-based compensation**, with
  the effective-rate note saying so directly. Reported growth is not unnaturally smooth
  (net income went $39.6M, then $392.7M, then $222.8M). Neither tell fires.
- [ ] dividends funded by issuance [E2-52]. Not applicable. **No dividend has ever been
  paid.**
- [ ] except-for [E2-57]. Partially. Severance ($6.3M), transaction costs ($13.2M) and the
  valuation-allowance release are each quantified at every line, which is the passing form.
  But SBC excluded from **four** different headline measures, every year, forever, is the
  *"except for"* the corpus excises: *"you must count the runs scored against you in all
  nine innings."*
- [ ] restructuring charge [E3-53]. None of consequence. Severance was $6.3M in FY2025 and
  $14.4M in FY2023, disclosed and small.
- [ ] stock-price targeting [E3-50]. No finding in the filed record.

**STEP 3 — THE PRIMARY TEST [E2-01], with its scope carve-outs applied honestly.**
Balance sheet first [E5-27]. Equity ran −$55.0M (FY2020), −$39.6M, $160.3M, $510.3M,
$261.5M, then **$497.9M** (FY2025), against an **accumulated deficit of $1,360.1M** and
$950M of buybacks in two years. **The [E2-01] denominator is not usable here, and the
corpus says so itself.** [E2-47] carves out mis-stated asset values and unusual capital
structures, and [E2-43] directs the analyst to **unleveraged net tangible assets**, which
for Chewy is **negative** (net operating capital employed of −$651.9M). A ROE of 58.7%
(FY2025) or 101.8% (FY2024) is an artifact of a residual denominator, not a measure of
managerial performance, and is **not** reported as a pass.
- **The substitute, disclosed as a judgment.** Operating income of $254.3M on the $1,885.0M
  of gross operating assets that actually exist is **13.5% pre-tax**, on a business that
  also enjoys $2.3bn of interest-free supplier and accrued funding. It is rising, having
  been negative two years ago. Adequate. Not exceptional.
- **The half-owner test [E2-26]: FAILS**, on the derivative action above. On the operating
  disclosure it passes well: both key metrics are defined precisely, filed quarterly, and
  the unflattering ones (the FY2022 and FY2023 active-customer declines) were published
  without softening. The failure is specific, and it is on the sponsor.

**The institutional imperative [E2-30], scored, all four:**
- [ ] resists change in current direction. No. The company has repeatedly extended
  (pharmacy 2018, telehealth 2020, insurance 2022, clinics 2024, equine 2026).
- [x] **projects and acquisitions materialise to soak up available funds. FIRED.** In the
  first four months of FY2026 Chewy spent **$175M on SmartPak (equine)** and **$400M on
  Modern Animal (a veterinary clinic platform)**, a total of **$575M: 1.02x the entire
  FY2025 "free cash flow" it advertises, and 2.2x the framework's owner earnings**, plus
  $200M of buybacks, taking cash from $860.1M to $485.2M at the quarter end **before** the
  $400M Modern Animal payment cleared. This is the [E3-40] loss-of-focus vector to watch:
  capital moving out of a capital-free e-commerce model into leased, staffed, physical
  clinics. Not a verdict. A prompt, and a Q6 tripwire.
- [ ] staff studies for the leader's craving. Not observable from filings.
- [x] **peer behaviour mindlessly imitated. FIRED, on the adjusted-metric suite.** Every
  headline measure Chewy promotes is the standard e-commerce and PE-sponsored template:
  adjusted EBITDA, adjusted net income, adjusted EPS, free cash flow before SBC. Costco, in
  the same industry and with the same auditor class, publishes **zero** adjusted metrics.
  The practice is a choice.

**Capital allocation. The two buyback conditions [E5-08, E4-31, E5-24, E2-51]:**
- (1) **Ample funds for operations and liquidity? Yes at FY2025 year-end, materially
  tighter now.** Cash went $860.1M, then $485.2M at 2026-05-03, then to roughly **$120M
  pro-forma** after the $400M Modern Animal payment on 2026-05-21, against an undrawn
  $783.1M ABL that [E5-39] says may not be counted: *"we will never be dependent on the
  kindness of strangers."*
- (2) **Repurchases at a material discount to conservatively calculated IV? THE RECORD IS
  THE ANSWER, AND IT IS NOT GOOD.** Every dollar of the pre-2026 programme was paid
  **directly to the controlling shareholder**, at prices set alongside its own exits:

  | date | counterparty | shares | price | $ |
  |---|---|---|---|---|
  | 2024-06-26 | **Buddy Chester Sub LLC (Sponsors)** | 17,550,000 | **$28.49** | $500.0M |
  | 2024-09-18 | **Buddy Chester Sub LLC** | 10,204,081 | **$29.40** | $300.0M |
  | 2024-12-09 | **Buddy Chester Sub LLC** | 1,596,424 | **$31.32** | $50.0M |
  | 2025-06-20 | **Buddy Chester Sub LLC** | 2,395,210 | **$41.75** | $100.0M |
  | FY2025 open market | market | 4,453,622 | ~$35.21 avg | $156.8M |
  | Q1 FY2026 open market | market | 7,599,226 | ~$26.32 avg | $200.0M |

  **$950.0M, or 68% of the $1,405.3M of repurchases made in the company's history, went to
  the seller who controls the board, at $28.49 to $41.75, against a market price today of
  $23.26. Every one is under water: the largest by 18%, the last by 44%.** Each was
  executed *concurrently with* a secondary offering in which the same seller was also
  selling to the public (424B7s filed 2024-09-20, 2024-12-11 and 2024-12-13, and
  2025-06-23 and 2025-06-24). **[E5-24]'s first law**, *"what is smart at one price is dumb
  at another"*, and **[E4-31]'s third condition** are both engaged, and **[E2-51]** cuts
  the other way here: the tell is not a refusal to repurchase but a *pattern* of
  repurchasing from one informed, controlling, exiting holder. This is a **live CAPITAL
  ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: it rests on this run's
  own IV range, management knows the business far better than I do, and *"many CEOs never
  stop believing their stock is cheap"* **[E5-08]**. **The flag binds position size, never
  the discount rate**, which is moot here since Q2 already closed entry.
- **Retention test [E3-54].** Retained capital over the five filed years produced a share
  price of $23.26 against a $28.49 to $41.75 range at which the company itself bought. On
  the corpus's dollar-of-market-value-per-dollar-retained test, the five-year rolling read
  is **negative**, though the window is dominated by a market de-rating rather than by
  operating failure. Stated both ways, and not leaned on.
- **[E3-58] delegation and [E2-56] the Pro-Am effect.** Not assessable segment by segment,
  because Chewy reports **one** reportable segment. The pharmacy, clinic, insurance and
  advertising ventures are not separately sized anywhere in the filing. **This is a named
  disclosure gap**, and it is the reason the [E2-56] test cannot be run: *"Their marvelous
  core businesses camouflage repeated failures in capital allocation elsewhere."* Whether
  that is happening at Chewy is **not determinable from the filed record.**
- **Executive churn, recorded.** CFO Mario Marte, then David Reeder, then William Billings
  as interim principal financial officer, then **Christopher Deppe, appointed 2026-02-23**.
  CTO Satish Mehta notified retirement on 2026-01-13. The 8-K states Billings' removal
  *"was not a result of any disagreement with the Company on any matter related to its
  operations, policies, practices, financial disclosures, or accounting."* Three CFOs in
  roughly two years, in a business whose weight case is daily execution. A fact, recorded.

**THE GUARDRAIL, checked before writing the verdict.**
- [x] Nothing in this Q3 is used to **promote** the name. Q2 is OUT and stays OUT, and a
  strong or weak Q3 cannot repair it [E2-37, E2-38, E3-39].
- [x] The **key-person and execution dependence was recorded at Q2** as a moat defect
  [E4-23], not here as a compliment or a criticism of any person.
- [x] No excisable-cancer case is argued [E2-35, E2-36]. The manager is not the plan.

- **VERDICT (for the record): [ ] IN. This gate would NOT have been written IN for entry.**
  It is a **BINARY GATE** by the declared weight case, and three flags are live and
  converge in one direction: adjusted-metric promotion that deletes the largest real
  expense [E4-29], continuous issuance to employees against a 20.3% plan authorisation
  [E5-15], and $950M of buybacks paid to the controlling seller at prices 22% to 79% above
  today's [E5-08, E5-24]. **[E4-52]'s lollapalooza rule applies: flags that converge are
  not a sum of prompts but one reinforcing system**, and the system here points the same
  way. The reported economics of this company are presented in a currency (SBC-adjusted) in
  which the controlling shareholder was paid out in cash. Set beside a Legal Matters note
  that names nothing while its own control group was in Chancery, the **[E2-26] half-owner
  test fails**, and a failed half-owner test on a gated business is not an IN.
  *Per [E5-17] this is the absence or presence of found disqualifiers, not a finding about
  anyone's character. The derivative action settled without admission and the board did act
  [E5-22]. Q3 stops runs, it never starts them, and it is not what stopped this one.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings, the one number [E2-23]
Convention applied: multi-year mean of **(OCF − SBC) − (c)**, capex band displayed, both
windows shown [E2-42, E4-25]. All figures in $M, from the filed cash-flow statements.
FY2021 and FY2022 come from XBRL cross-checked to the FY2022 and FY2024 10-K statements;
FY2023 to FY2025 are read directly off the FY2025 10-K.

| FY | fiscal year end | weeks | OCF | SBC | D&A | capex | NI | OE lo | OE hi |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 2022-01-30 | 52 | 191.7 | 77.8 | 55.3 | 183.2 | −75.2 | **−69.3** | 58.6 |
| 2022 | 2023-01-29 | 52 | 349.8 | 158.1 | 83.4 | 230.3 | 49.9 | **−38.6** | 108.3 |
| 2023 | 2024-01-28 | 52 | 486.2 | 239.1 | 109.7 | 143.3 | 39.6 | 103.8 | 137.4 |
| 2024 | 2025-02-02 | **53** | 596.3 | 306.4 | 114.6 | 143.8 | 392.7 | 146.1 | 175.3 |
| 2025 | 2026-02-01 | 52 | 691.6 | 297.9 | 129.3 | 129.2 | 222.8 | **264.4** | 264.5 |

- **Long-window mean (5-yr, FY2021 to FY2025, the corpus default [E2-42]): $81.3M .. $148.8M**
- **Short-window mean (3-yr, FY2023 to FY2025): $171.4M .. $192.4M**
- **Spread, conservative end: +110.9%** (3-yr above 5-yr). Enormous, far past the 15%
  display threshold. **The spread is part of the range [E4-25]**, carried, not resolved.
- **Combined range (window spread × capex band): $81M to $192M**, a 2.4x span end to end.
- **Is the range too wide to reach a conclusion [E4-25]?** It would be, for a *ranking*. It
  is not, for the question actually asked. **The yield is 0.85% to 2.02% at every point
  inside the range against a 5.19% sovereign, and the pre-tax expectancy is 3.5% to 6.1% at
  every point including the most generous growth assumption.** The verdict is invariant
  across the whole range, so no [E4-25] close is forced. The width is reported, not buried.
- **The width is also a Q4 finding in its own right [E5-11], and the distorted years are
  named.** First, **FY2021 and FY2022 have negative owner earnings at the conservative
  end**, because the company was still building fulfilment capacity (capex of $183.2M and
  $230.3M, since halved) while SBC was ramping. Second, **FY2024 was 53 weeks** (+$226.6M
  of net sales) and carried a **$241.0M income-tax benefit** from the release of the U.S.
  federal valuation allowance, which is why GAAP net income of $392.7M that year is not an
  earnings number. Third, FY2025 is the first year in which capex ($129.2M) and D&A
  ($129.3M) essentially coincide, which is why the FY2025 band collapses to a point.
  **[E3-55] scope check:** this is *not* the benign volatility case. The mechanism here is
  a business changing shape (a build-out ending, an expense category ramping), not a
  certain endgame with a bouncing annual figure.
- **Maintenance capex, the DISCLOSED JUDGMENT.** This is the **[E2-41] 95% class, not the
  [E5-20] capital-intensive exception.** Nothing in the filing says depreciation
  understates renewal. There are no rails, no fleet, no owned real estate. **Every
  fulfilment centre, office and clinic is leased**, so the renewal obligation shows up as
  rent inside operating expenses rather than as capex, and the operating-lease liability
  ($556.8M present value, $837.9M of undiscounted payments) is on the balance sheet. Capex
  is 1.03% of sales and has *fallen* three years running (183.2, 230.3, 143.3, 143.8,
  129.2) while sales grew. **Judgment, disclosed: (c) is approximately D&A, that is
  roughly $130M on the FY2025 base, so the D&A end of the band is the honest one here**,
  and the band is narrow because the two have converged. The D&A end is not taken as free
  money either: 25 vet clinics, up from 8 two years ago, plus the Modern Animal platform
  will raise the renewal burden, and the growth capex embedded in the recent years is real.
  **Judged owner earnings: 5-yr roughly $130M to $149M; 3-yr roughly $185M to $192M.** The
  full computed band is carried everywhere below.
- **Working-capital increment [E2-23].** The source's own carve-out is favourable here.
  Chewy's cash conversion cycle is **negative 8.3 days** (DIO 35.7, DPO 50.4, DSO 6.4) and
  payables cover inventories 141%. **Unit growth releases working capital rather than
  consuming it**, and the OCF line nets it in any case, which is why this convention uses
  OCF.
- **Stock compensation subtracted in full [E5-06]. The decisive input, quantified:**

  | | FY2023 | FY2024 | FY2025 |
  |---|---|---|---|
  | Company "free cash flow" (OCF − capex) | $342.9M | $452.5M | **$562.4M** |
  | Company adjusted EBITDA | $368.1M | $570.5M | **$719.2M** |
  | Company adjusted net income | $296.2M | $446.8M | **$540.5M** |
  | GAAP net income | $39.6M | $392.7M | $222.8M |
  | **Framework owner earnings** (OCF − SBC − (c)) | $103.8M .. $137.4M | $146.1M .. $175.3M | **$264.4M** |
  | **GAP: company FCF less framework OE** | **$205.5M** | **$277.2M** | **$298.0M** |

  **The gap IS the share-based compensation, to the dollar** ($297.9M in FY2025). On a
  three-year mean, company-defined free cash flow of **$452.6M** is **2.35x to 2.64x** the
  framework's owner earnings of $171.4M to $192.4M. Every dollar of the difference is
  compensation that was paid, was expensed under GAAP, and diluted the owners, and that
  four separate promoted measures add back.
- **[E3-70]: the reported charge is the FLOOR of the subtraction, not the measure.**
  *"an amount equal to what the company could have realized by publicly selling options of
  like quantity and structure."* Chewy grants **RSUs and PRSUs, not options**, so the
  ASC 718 grant-date fair value is a close proxy for market value and the understatement is
  smaller than in an option programme. Two reasons it is still a floor. First, PRSUs vest
  between **0% and 200% of target** (proxy, verbatim), so realised dilution can exceed the
  charge, and FY2025's short-term incentive certified at **176.86% of target**. Second, the
  economic cost of retaining people is set in *shares*, and at a falling share price the
  share cost of a constant dollar cost rises. See the fourth named death below.
- **The reflexive point, stated plainly because it is the one the market's convention
  hides: FY2025 share-based compensation of $297.9M EXCEEDED that year's owner earnings of
  $264.4M.** For every year in the filed record, the employees' claim on this business has
  been larger than the owners'.
- Look-through earnings [E3-04]: no material equity-method or unconsolidated stakes. Not
  applicable.

### Great, good, or gruesome? [E4-20]
- **[x] GOOD, and the classification is genuinely favourable, which the bear case must
  concede.** The gruesome class is *"grows rapidly, requires significant capital to
  engender the growth, and then earns little or no money."* **Chewy fails the middle clause
  emphatically.** Capex is 1.03% of sales, net operating capital employed is **negative
  $651.9M**, and growth is financed by suppliers. The savings account pays an attractive and
  **rapidly rising** rate: owner earnings went $103.8M, then $146.1M, then $264.4M in three
  years, a 2.5x, on essentially no added capital. Freshpet by contrast spends **13.45% of
  sales** on capex to grow. **[E4-43]: good passes Q4.** It simply ranks below great at Q5.
- **Why it is not *great*.** The rate is high on capital but thin on the business, at 2.02%
  of sales, and it has not compounded into a widening structural advantage in fifteen years
  (Q2). And the whole of it, and more, is currently paid to employees in stock.

### Staying power, score all three [E5-11]
- **(1) Large and reliable stream of earnings: PASS, with a qualifier.** Operating cash flow
  rose in every one of the eight filed years, seven consecutive increases with no down year:
  −$13.4M (FY2018), $46.6M, $132.8M, $191.7M, $349.8M, $486.2M, $596.3M, then **$691.6M**.
  That is a genuinely reliable stream. The qualifier: GAAP net income has been positive for
  only four years and one of those was a tax benefit, and the *owner-earnings* stream has
  been positive for only three.
- **(2) Massive liquid assets: MARGINAL, and it turned inside one half-year.** Cash and
  securities were $878.8M at 2026-02-01, then **$520.1M at 2026-05-03** after $200M of
  buybacks and $174.8M for SmartPak, then **roughly $120M pro-forma** after $400M was paid
  for Modern Animal on 2026-05-21 *"using cash on hand"*, before Q2 generation. Against that
  sits **$783.1M of undrawn ABL capacity**, which **[E5-39]** expressly refuses to count:
  *"We will never be dependent on the kindness of strangers."* On the corpus's own standard
  this leg is **not** a pass at 2026-05-21. It is a pass only if the next two quarters of
  operating cash flow arrive as expected. **That is the exact dependency [E5-11] strength 3
  exists to catch.**
- **(3) No significant near-term cash requirements: PASS.** No funded debt, no maturities,
  no commercial paper. Operating leases run $78.5M (2026), $81.3M, $81.5M, $81.5M, $78.1M,
  and $437.0M thereafter, or $837.9M undiscounted, at a 10.2-year weighted average term and
  an 8.2% discount rate, covered roughly 8.8x by FY2025 operating cash flow. The ABL is
  undrawn and matures 2030-04-01. **Terms read [E3-52]:** the $2,301.6M of current
  liabilities are trade payables and accrued expenses, **covenant-free, undated, supplier-
  and customer-funded**, which is the benign animal rather than covenanted bank debt. The
  contractual near-term requirement is genuinely small. The **discretionary** one, being
  $550M of remaining buyback authorisation plus an acquisition appetite that has spent
  $575M in four months, is not, and it is management's to control.
- **Leverage, named and quantified [E4-16, E3-29].** No ratio ceiling exists in this
  framework and none is used. Funded debt is **zero**, the ABL is undrawn, and total lease
  present value of $556.8M is 0.81x FY2025 operating cash flow. **[E2-54] coverage test:**
  there is no interest, payable or accrued, to cover. This is a genuinely unlevered balance
  sheet and it is the strongest single fact in Q4.
- Jurisdiction [E3-66]: a U.S. filer, Delaware-incorporated, inside the U.S.
  shareholder-protection regime. The derivative action at Q3 is that regime working, which
  is worth saying.

### Name the specific ways THIS business dies [E2-27, E3-24]. Exposure, not experience [E4-40]
**The iron prescription [E4-51]: stated as the bears would state it, then quantified from
filed figures. Base rates come from what the filing shows the business is exposed to, not
from what has recently happened. The FY2025 record year is precisely the "benign loss
history late in a good cycle" that [E4-40] warns is dangerous as a guide.**

1. **The price war Amazon can start whenever it likes (the fast death).** Chewy's entire
   operating income is **$254.3M on $12,601.5M of sales**. A **200 basis point** gross-margin
   concession, two cents on the dollar, roughly one competitive holiday season, costs
   **$252.0M and erases the whole of it.** Chewy cannot answer with its own price cut,
   because it has no second profit pool: no membership fee, no owned brand of scale, no
   AWS. Amazon's North America segment earns 6.95% and does not need pet to be profitable.
   Quantified per [E3-24]: 200bp is $252.0M, or 99% of operating income; 100bp is $126.0M,
   or 50%. **Likelihood: a real possibility** over a decade, and the exposure exists every
   day regardless of whether it has been used.
2. **The three suppliers (the slow squeeze).** *"Sales of products from the Company's three
   largest vendors represented approximately 39%, 39%, and 39% of the Company's net sales."*
   Chewy's recent margin gains come substantially from **sponsored ads sold back to those
   same vendors** and from **vendor rebates**, which Deloitte named as the **critical audit
   matter**. If the top three claw back **100bp** of margin on their 39% of sales, that is
   **$49.1M, or 19% of operating income**; **300bp** is **$147.4M, or 58%**. The brands
   have every incentive, because they are building direct-to-consumer channels that Chewy's
   own filing names as competitors. **Likelihood: a real possibility.**
3. **The customer count stalls again (the repeat).** It has already happened twice in five
   years (FY2022 at −1.2%, FY2023 at −1.6%). NSPAC growth has decayed to +2.2%, so units now
   carry the growth. If actives go flat and NSPAC grows 2%, net sales grow roughly 2% while
   advertising ($824.9M) and SG&A are semi-fixed, and a 2% revenue year against 3% cost
   inflation removes roughly **$130M of operating income, about half.** **Likelihood: a
   real possibility**, and it is the one the filing's own history most supports.
4. **The dilution ratchet: the death that gets *worse* as the stock falls, and the one the
   market's own convention hides.** The employees' claim is set in dollars and paid in
   shares. Replacing $297.9M of annual share-based compensation costs **12.8M shares a year
   at $23.26, or 3.13% of the share count**, against 8.5M at $35 (2.1%) and 6.0M at $50
   (1.5%). **The lower the price goes, the faster the owner is diluted.** Already committed:
   **$510.2M of granted-but-unrecognised compensation** and a plan authorisation of
   **83.1M shares, or 20.3% of shares outstanding**. In FY2025 the company spent $262.5M on
   buybacks and the share count **still rose 1.5M**. **Likelihood: likely.** It is not a
   scenario, it is the current mechanism, and it is why "free cash flow of $562M" and
   "owner earnings of $264M" are not two views of one number.
5. **Capital walking into the clinics (the [E3-40] loss-of-focus death).** $575M was spent
   in four months (SmartPak $175M, Modern Animal $400M), and vet clinics went from 8 to 25
   in two years, against a business whose entire virtue is that it needs no capital. Clinics
   are leased, staffed, licensed, local and slow-returning, and they convert a −$652M
   capital base into a positive one. Cash went $860.1M, then $520.1M, then roughly $120M
   pro-forma across two quarters. Chewy reports **one segment**, so none of these ventures
   can be scored separately: *"marvelous core businesses camouflage repeated failures in
   capital allocation elsewhere"* **[E2-56]**. **Likelihood of a solvency event: a low-level
   possibility**, given no debt and no covenants. **Likelihood of the capital earning less
   than the base business: a real possibility**, and it is unmeasurable from the filed
   record, which is the more serious half.
6. **The shareholder's death that is not the company's.** Named here because it belongs in
   the bear case and it is Q5's finding. On the framework's owner earnings the stock trades
   at **36x FY2025 and 49x to 56x the three-year mean**, and the entire appearance of
   cheapness at 16.9x "free cash flow" rests on adding back item 4.

- **VERDICT (for the record): the business survives every named mechanism.** None touches
  solvency at any plausible severity, because there is no debt to accelerate and no covenant
  to breach. Staying-power leg 2 is **marginal** as of 2026-05-21 and is the item to watch;
  it is a self-inflicted, reversible, management-controlled squeeze rather than a structural
  one. **On the entry question this is moot: Q2 is OUT.**

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**
*Operator protocol rule 3. Q1 to Q4 do not all show IN, because Q2 is OUT. **No figure below
is a valuation opinion offered for action, and no sentence below is entry language.** The
arithmetic is produced because the operator asked for the floor and the SBC gap in numbers.*

**Inputs.** Market cap **$9,523.2M** (409,424,207 total economic shares × $23.26, close
2026-08-28, aggregator, flagged). Sovereign **5.19%** (FRED DGS30, 2026-08-27). Owner
earnings **$81.3M to $148.8M** (5-yr) and **$171.4M to $192.4M** (3-yr). The DCF ran as an
**engine** only. It casts no vote [E3-34].

**1. THE YIELD**
- 5-yr: $81.3M to $148.8M ÷ $9,523.2M = **0.85% .. 1.56%** · sovereign **5.19%**
- 3-yr: $171.4M to $192.4M ÷ $9,523.2M = **1.80% .. 2.02%** · sovereign **5.19%**
- FY2025 alone, the best year ever: $264.4M = **2.78%**
- **For contrast, the same price on the company's own convention.** Free cash flow $562.4M
  is **5.91%**; adjusted net income $540.5M is **5.68%**; adjusted diluted EPS $1.27 is
  **18.3x**. **On the market's convention this stock yields more than the 30-year bond. On
  the corpus's convention it yields a third of it. The entire difference is $298M of stock
  compensation, and the corpus is not ambiguous about which one is right [E5-06, E3-70].**
  That is the single most useful sentence this run produces.

**Multiples at $23.26.** GAAP diluted EPS $0.52 gives **44.7x**. Adjusted diluted EPS $1.27
gives 18.3x. Company free cash flow gives 16.9x. **Framework owner earnings give 36.0x
(FY2025), 49.5x to 55.6x (3-yr mean), and 64x to 117x (5-yr mean).**

**2. WHAT THE PRICE ALREADY ASSUMES**
- Engine: a 10-year fade to a 2.5% terminal, discounted at the **bare sovereign**, with no
  risk premium in the rate [E3-42]. Year-1 owner-earnings growth needed to reproduce the
  $9,523.2M capitalisation is **28.9%** (5-yr conservative), **14.2%** (5-yr D&A end),
  **11.0%** (3-yr conservative) and **8.3%** (3-yr D&A end).
- What the business has actually done: **net sales +6.2% (+8.3% ex the 53rd week), active
  customers +4.0%, net sales per active customer +2.2%.** Owner earnings did grow far
  faster, at 2.5x in three years, but off a base of nearly nothing, as a capex build-out
  ended.
- **[E4-35]'s base rate applies to the 8% to 14% cases:** *"fewer than 10 of the 200 most
  profitable companies… will attain 15% annual growth in earnings-per-share over the next
  20 years."* The price needs Chewy to do, from a 2% operating margin against Amazon, what
  fewer than one in twenty of the best businesses in America manage.
- **The ceiling [E2-63, E4-44]:** *"the value of an asset… cannot over the long term grow
  faster than its earnings do."* There is no multiple-expansion term available above 36x
  owner earnings, and the dilution ratchet (Q4 death 4) subtracts roughly 2% to 3% a year
  from per-share growth before the business grows at all.

**3. WHAT YOU ARE PAID**
- Points over the sovereign, engine at the current price:

  | year-1 growth | 5-yr OE base | 3-yr OE base |
  |---|---|---|
  | 3% | **−1.79 .. −1.05** | −0.80 .. −0.57 |
  | 5% | −1.71 .. −0.89 | −0.62 .. −0.37 |
  | 8% | −1.56 .. −0.63 | −0.32 .. −0.04 |
  | 10% | −1.45 .. −0.44 | −0.11 .. **+0.20** |
  | 15% | −1.15 .. +0.09 | +0.49 .. **+0.87** |

  **Bond-minus for equity risk on every honest input, and bond-plus by less than a point
  only if you grant 10% to 15% compound growth to a 2%-margin retailer facing Amazon.**

**THE FLOOR, before any ranking [E4-28].** *"that's the figure we quit on… whether short
rates are 6 percent or whether short rates are 1 percent."*
- **Honest pre-tax expectancy at $23.26, absolute:** **3.48% to 4.30%** on the five-year
  window and **4.57% to 4.82%** on the three-year window at 5% growth; **3.74% to 4.75%**
  and **5.08% to 5.39%** at 10% growth; **4.04% to 5.28%** and **5.68% to 6.06%** even at
  **15%**.
- **The maximum honest expectancy this name offers, with zero conservatism spent anywhere,
  meaning the best window, the best (c) and 15% year-1 growth, is 6.06%. The floor is 10%.**
- **The floor fails, and it fails by a wide margin at every point in the range. The name is
  not ranked. It is quit on at this price.** The floor does not move with the sovereign
  [E4-28]. *(This is a price statement recorded for completeness. Q2 already closed the file
  on the business.)*

**FLOOR ARITHMETIC: the price at which a 10% expectancy would exist.**

| OE base | at 8% growth | at 10% growth |
|---|---|---|
| 5-yr conservative ($81.3M) | $3.39/sh | $3.67/sh |
| 5-yr D&A end ($148.8M) | $6.21/sh | $6.72/sh |
| 3-yr conservative ($171.4M) | $7.15/sh | $7.74/sh |
| 3-yr D&A end ($192.4M) | **$8.02/sh** | **$8.69/sh** |

**Roughly $3.50 to $8.50 a share**, which is **63% to 85% below the current quote, after
the stock has already fallen roughly 48% from a May-2025 monthly close of about $45**
(aggregator monthly closes, flagged; the filed 10-K cover corroborates the direction, at
$35.91 on 2025-08-01 against $23.26 today). The de-rating that looks dramatic on a chart did
not move this name toward the floor, because the de-rating was priced against a cash-flow
number that includes a $298M add-back.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:**
- **conservative, roughly $4 a share.** Five-year mean owner earnings ($81.3M to $148.8M)
  capitalised at the bare sovereign with zero growth, giving $3.83 to $7.00.
- **judged middle, roughly $8 to $9 a share.** Three-year window, judged (c) at
  approximately D&A, zero growth at the sovereign, giving $8.07 to $9.05.
- **generous, roughly $23 to $31 a share.** Three-year D&A-end owner earnings of $192.4M
  with **8% to 15%** year-1 growth fading to 2.5%, discounted at the **bare** sovereign.
  **Zero conservatism is spent anywhere**: best window, best (c), no risk premium, and
  growth at or above anything the business has delivered.
- **Current price: $23.26.** It sits on the floor of the zero-conservatism case, and at 2.6x
  to 6.1x the conservative case.

**WHICH BAR: [x] Screamer test [E4-01].** Outcome: **price inside the range, so no useful
conclusion from the bar. Move on.** That middle outcome is a finished answer, and it never
overrides the floor, which already closed entry, or Q2, which already closed the file. **No
margin was added on top. Windage count: ONE**, being the conservative end of the
owner-earnings band. The generous end deliberately spends none, which is what makes the
floor finding robust. Certainty is **not** priced in any rate [E3-42]. It was spent at Q1
and once more here, and nowhere else.

- **VERDICT: not applicable, because Q5 did not open for entry.** Recorded as computation.
  Had it opened, the finding would be **BELOW THE FLOOR [E4-28], not ranked.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*No position exists, so there is no [E2-28] hold read to run. Everything below is
pre-committed **now, prior to any act** [E1-02], and converts to watch-list items. The
[E4-51] discipline runs in this direction too: what follows is what would have to be true
for this run's Q2 OUT to be wrong.*

**Thesis-CONFIRMING metrics: what would make the "not a franchise" finding wrong.** Each is
filed quarterly and is a specific, falsifiable number.
- **Net sales per active customer growing faster than pet-food CPI for two consecutive
  years**, which is the direct [E2-44] test. NSPAC growth has run 15.6%, 15.1%, 11.9%,
  4.1%, 2.2%, 2.4%. A re-acceleration above roughly 5% **while active customers also grow**
  would be real evidence of pricing power rather than mix.
- **Active customers above 22.0M** and growing at 4% or better, which is the [E4-55]
  physical series. (21.327M at FY2025; 21.497M at Q1 FY2026.)
- **Autoship above 85% of net sales** with gross margin still widening, so that stickiness
  and margin move together rather than trading off. (83.3% at FY2025; 84.4% at Q1 FY2026.)
- **Gross margin above 31%** with the 10-K attributing it to *pricing*, not to sponsored ads
  and mix.
- **A disclosed private-brand share of sales, at all.** After ten years of private brands the
  number has never been filed. Its first appearance, at any level above roughly 10%, would
  materially change the [E5-35] reading.
- **Operating margin sustained above 4%** for a full year. Q1 FY2026 hit 3.8%, the best
  quarter ever, against 2.02% for FY2025. Four percent would put the business past Walmart's
  and would be the first hard evidence that scale is converting into an owner's return.
- **Advertising and marketing falling below 6.0% of net sales** while actives still grow,
  which is the [E4-04] test of whether the customer base has to be re-bought.

**Thesis-BREAKING metrics and thresholds: what would confirm the finding, or make it worse.**
Per [E4-17] and [E3-30], slow to conclude, fast once concluded [E2-40].
- Active customers **declining year over year in any two consecutive quarters**, repeating
  the FY2022 and FY2023 pattern.
- Gross margin **down 50bp or more in any two consecutive quarters**, the price-war
  signature.
- **Share count rising year over year in any fiscal year** while a buyback is running, as it
  did in FY2025, meaning the dilution ratchet is outrunning the repurchase.
- Any further **repurchase from Buddy Chester Sub LLC or the Sponsors at a premium to the
  prevailing market**, or any new related-party transaction with a BC Partners entity
  [E5-24, E4-31].
- Cash and securities **below $250M** at any quarter end with acquisitions still being
  announced, or **any drawing on the ABL**, which is the [E5-39] line.
- Cumulative acquisition spend **above $750M in any twelve months**, or vet clinics above 75,
  which is the [E3-40] loss-of-focus threshold. The corpus's remedy is exit, not engagement
  [E4-24, E4-49].
- Any widening of a non-GAAP definition **following** a deterioration [E2-49], or any
  integrity matter becoming public, on which the [E5-22] test is whether they act when they
  learn rather than the size of the number.
- **The Legal Matters note continuing to name nothing** while a material proceeding is
  pending. The [E2-26] failure repeating is itself a datum.

**Bands: the price at which this file would be re-opened.** Computed from this run's owner
earnings. Both bands move with owner earnings and are recomputed at each 10-K.
- **Full re-run below roughly $9 to $10**, where the three-year judged owner-earnings yield
  reaches the 5.19% sovereign and the honest expectancy approaches the [E4-28] floor.
- **A re-run at any price requires Q2 to be re-argued first**, on the confirming metrics
  above. **Price alone cannot repair a Q2 OUT.** That is the whole point of the hard
  sequence, and the corpus is explicit that cheapness is not the remedy for the class of
  defect found here [E3-29, E5-35]: *"What you can't do is turn any investment into a good
  deal by paying little."*
- **tools/alerts.json candidates, LISTED ONLY, NOT EDITED, per instruction:**
  `CHWY price < 10.00` · `CHWY active customers y/y < 0 (any 10-Q)` · `CHWY gross margin
  < 29.0% (any 10-Q)` · `CHWY total shares (Class A + Class B) up y/y (any 10-K)` ·
  `CHWY cash + securities < 250M (any 10-Q)` · `CHWY new related-party repurchase from
  Sponsors (any 8-K)` · `CHWY FY2026 10-K filed (re-run the OE table and the SBC gap)`.

**Next catalyst dates:**
- **Q2 FY2026 results (13 weeks ended about 2026-08-02): expected around 2026-09-09**, on
  the three-year cadence (2025-09-10, 2024-08-28). This will carry the **Modern Animal
  purchase price allocation** the Q1 10-Q deferred, the post-acquisition cash balance, and
  the first full read on whether staying-power leg 2 recovered.
- **Q3 FY2026 10-Q: around 2026-12-09.**
- **FY2026 10-K: late March 2027**, since the fiscal year ends 2027-01-31. Refresh the
  owner-earnings table, the share count, the SBC gap and both bands.
- **The derivative settlement.** The hearing was set for **2026-06-23**. Whether the $29.5M
  receipt and the settlement appear in the Q2 FY2026 10-Q is a **direct, dated test of the
  [E2-26] finding above**, and it is the single most informative thing to check next.

**Position size, a judgment, stated [E3-45 direction]: zero.** The framework's answer is no
entry. The name fails Q2 on the business, fails the mandate on the dividend, and fails the
[E4-28] floor on the price by a factor of three. Capital goes to rank #1, and a name that
does not clear Q2 is not on the list at all.

- **VERDICT: [x] IN.** The question of what would prove me wrong, and when I would act, is
  answered with pre-committed, filing-sourced, falsifiable yardsticks and dated catalysts.

---
## SELF-AUDIT
- [x] Questions answered in order, stopping at the first non-IN (Q2 OUT). Q3 to Q5 are
  marked FOR THE RECORD, Q5 carries the "COMPUTATION — NOT A CLEARANCE" header per operator
  rule 3, and no entry language appears below the Q2 stop
- [x] No question marked IN carries an "unverified", "general knowledge" or "provisional"
  caveat. Q1 and Q6 are the only IN verdicts and both rest on documents in hand
- [x] No UNRESEARCHED verdict issued. The two unfillable items are named as **permanent
  disclosure limits, not work orders**: Amazon, Walmart and Target pet-category revenue (no
  document exists, and the absence-claim rule wording is used, *no pet-category disclosure
  found*), and Chewy's own numeric guidance record (the artifact is the earnings-call
  transcript or IR shareholder letter, named, not an SEC filing, not on the citation shelf).
  Chewy's private-brand share and sponsored-ads revenue are named as issuer disclosure gaps
- [x] No UNKNOWABLE verdict issued. The owner-earnings range is very wide (a +110.9% window
  spread) but the yield and expectancy verdicts are invariant across the entire combined
  range, so [E4-25] does not force a close. The width is reported and its causes named
- [x] Step 0: the filing was read, covering MD&A, cash-flow detail lines and footnotes, with
  accessions recorded (10-K **0001766502-26-000034**, 10-Q **0001628280-26-042060**, plus
  the FY2024 and FY2022 10-Ks, the DEF 14A, and five 8-K accessions). **OCF $691.6M was
  cross-checked in three places in the filed document plus the MD&A prose, and net sales
  $12,601.5M in three places.** FY2024's **53rd week** is flagged and quantified at $226.6M
- [x] **Dual class handled explicitly.** Total economic shares equal Class A plus Class B,
  or 409,424,207 (10-Q cover, 2026-06-03). The Class-A-only trap is shown and priced at a
  43% capitalisation understatement, and the figure reconciles three ways against the 10-K
  cover count and the non-affiliate market value on the 10-K cover
- [x] Owner earnings on multi-year means, with **both windows stated** (five-year default
  [E2-42], three-year shown). The +110.9% spread is carried as part of the range [E4-25].
  The capex band is displayed with (c) disclosed as a judgment, at approximately D&A, with
  reasons cited from the filing: all property leased, capex at 1.03% of sales and falling,
  and capex approximately equal to D&A in FY2025
- [x] **Stock compensation subtracted in full [E5-06]**, with the reported charge treated as
  the **floor** [E3-70] and the two reasons stated. The gap to every company-promoted
  measure is quantified for three years
- [x] Competitor row filled and committed as a separate file (3 direct peers plus 2 context
  filers, all filing-sourced, with Petco's fiscal year ending one day from Chewy's). The
  moat class is **not** provisional, because the one unfillable cell is unfillable by anyone
- [x] Sovereign is for the earnings currency (USD), from the issuing authority's own series
  (FRED DGS30), dated 2026-08-27, saved to the research folder
- [x] Value stated as a round-number range ($4 conservative, $8 to $9 judged middle, $23 to
  $31 zero-conservatism generous), not a point estimate
- [x] One bar chosen (screamer), not both. **Windage count stated: one**
- [x] Prices dated. A single aggregator was used for the live quote only and is flagged, and
  the second-source attempt and its failure are recorded
- [x] No shared file edited. `PORTFOLIO.md`, `Screens/*`, `tools/*` (including
  `tools/alerts.json`) and `Framework/*` are untouched, and alert candidates are **listed
  only**
- [x] Run committed to git

## REGISTER
- Verdict: **[x] OUT (about the business), at Q2.** Q1 IN, **Q2 OUT**, Q3 to Q5 for the
  record only, Q6 IN. No position exists and no [E2-28] hold read was required.
- One line: **The best-run business in pet retail, and not a franchise. 84% of sales arrive
  on a standing order and share is taken from a shrinking Petco every year, but Chewy sells
  other companies' identical bags (three vendors are 39% of sales), names price first among
  its own competitive factors, has watched net sales per active customer decelerate from
  +15% to +2%, and earns a 2.02% operating margin identical to two decimals to the
  competitor it is beating. The apparent cheapness at 16.9x "free cash flow" is entirely a
  $298M stock-compensation add-back, which on the corpus's own convention turns a 5.91%
  yield into 1.8% to 2.0% against a 5.19% bond, an honest expectancy of 3.5% to 6.1%, and a
  floor price of roughly $3.50 to $8.50 against a $23.26 quote.**
- **Biggest single concern: the dilution ratchet.** FY2025 share-based compensation of
  **$297.9M exceeded that year's owner earnings of $264.4M**. A further $510.2M is already
  granted and unrecognised, the plan authorises 20.3% of the share count, and because the
  claim is fixed in dollars and settled in shares, **every fall in the price accelerates the
  dilution**, at 12.8M shares a year at $23.26 versus 6.0M at $50. In FY2025 the company
  spent $262.5M on buybacks and the share count still rose. Second, and structurally worse:
  **$950M of repurchases, 68% of the $1,405.3M ever spent, were paid directly to the
  controlling shareholder at $28.49 to $41.75**, alongside its own secondary exits, while
  two annual reports and a 10-Q carried a Legal Matters note that named nothing about the
  Chancery derivative action against that same shareholder, settled for **$29.5M** on
  2026-04-06.
