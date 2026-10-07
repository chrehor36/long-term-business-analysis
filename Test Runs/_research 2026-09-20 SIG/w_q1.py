import io, sys
p = "Test Runs/2026-09-20 Run - SIG Signet Jewelers.md"
s = open(p, encoding="utf-8").read()

step0_old = """- rate ____ % · date ____ · source (issuing authority) ____
- FX if the quote and the earnings differ in currency: ____ · ADR ratio, derived: ____

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [ ] MD&A  [ ] cash-flow statement incl. detail lines  [ ] footnotes
- document · date · accession no.: ____
- figure cross-checked against the filed statement (say which): ____"""

step0_new = """- rate **5.34%** · date **09/18/2026** · source **US Treasury daily par yield curve, 30-year
  constant maturity, from the issuing authority (home.treasury.gov), struck this session on
  2026-09-20.** The cached copy was deleted and the file re-fetched before use; no rate was
  inherited from the brief **[E4-15, E3-32]**.
- **FX / multi-currency, disclosed rather than averaged away.** Signet reports in USD and is
  incorporated in Bermuda. The earnings currency is **mixed but overwhelmingly USD**: the
  International reportable segment (UK and Republic of Ireland, H.Samuel and Ernest Jones) had
  Fiscal 2026 total sales of **$410.4 million against $6,813.6 million consolidated, 6.0%**,
  and Peoples (Canada, CAD) was **3%** of consolidated sales. The quote is in USD on the NYSE
  and the reporting currency is USD, so no ADR ratio arises. **The AIG replication's
  multi-currency gap is named here and not closed**: a strictly correct treatment would price
  6% of the earnings against a gilt and 3% against a Canada bond. It is not done, because the
  weight is 9% and the framework's instrument is one sovereign for the earnings currency. The
  reader is given the number rather than shown an average.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: Form 10-K for the 52 weeks ended 2026-01-31 ("Fiscal 2026"), filed 2026-03-19,
  accession `0000832988-26-000055`** (document `sig-20260131.htm`).
- **Newest periodic: Form 10-Q for the 13 and 26 weeks ended 2026-08-01, filed 2026-09-09,
  accession `0000832988-26-000229`** (document `sig-20260801.htm`). **The screen's
  `newest_periodic` of 2026-05-02 is one quarter stale** — the screen was cut 2026-09-02 and
  the Q2 10-Q was filed 2026-09-09. A date, not a defect.
- Also read: **8-K of 2026-09-04, accession `0000832988-26-000227`** (Items 1.01, 2.02, 9.01)
  and its **EX-99.1 earnings release of 2026-09-09**; **8-K of 2026-09-10, accession
  `0000832988-26-000231`** (Item 8.01, the accelerated share repurchase); and the **10-K for
  Fiscal 2019, filed 2019-04-03, accession `0000832988-19-000003`**, pulled for the
  eighteen-year rebuild the screen's `spread_caveat` demands.
- **Figures cross-checked against the filed statements:**
  (1) **Share count.** The 10-Q cover reads **38,317,243 common shares outstanding as of
  2026-09-04**. The face of the balance sheet in the same document reads *"authorized 500
  shares, issued 70.0 shares, 38.7 shares outstanding"* at 2026-08-01, treasury 31.3 shares:
  **70.0 − 31.3 = 38.7**, and the cover count is lower because the company went on buying
  between 2026-08-01 and 2026-09-04. The two agree.
  (2) **Total sales.** The 10-K statement of operations reads **$6,813.6 million** for Fiscal
  2026; the tagged `RevenueFromContractWithCustomerExcludingAssessedTax` for the year ended
  2026-01-31 reads 6,813.6. The tagged figure is a transcription of the filed one, which is
  why the filed one was opened.

**PRICE, SHARES AND CAP — stated once here, used at Q5 only.**
- **Price US$100.38**, close of **2026-09-18**, aggregator (Yahoo via `tools/sources.py`),
  **FLAGGED as an aggregator quote** per operator rule 5.
- **Shares 38,317,243**, from the **cover** of the 10-Q, accession `0000832988-26-000229`.
- **Market cap US$3,846.3 million.** No split; `close`, never `adjclose`.
- **A subsequent event moves the count: the 8-K of 2026-09-10** records a **$125 million
  accelerated share repurchase** with JPMorgan, paid 2026-09-11, **initial delivery of about
  1,023,000 shares** on 2026-09-11, final settlement between 2026-09-25 and 2026-12-02. On the
  initial delivery alone the count is **~37,294,000** and the cap **~US$3,743M**, against
  $125M less cash. **The cover count is used**, because it is the count the rule names and
  because pairing it with the 2026-08-01 balance sheet keeps numerator and denominator on the
  same date."""

assert step0_old in s, "step0 anchor not found"
s = s.replace(step0_old, step0_new)

q1_old = """- Unit economics in my own words, no management language: ____
- The scarce input this business controls: ____
- Will the fundamentals look broadly the same in ten years? ____
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**"""

q1_new = """- **Unit economics in my own words, no management language.** Signet buys finished fine
  jewelry from third-party vendors (five largest suppliers about 22% of purchases, the largest
  about 6%), marks it up a little under two times, and sells it through **2,582 stores** and
  eleven brand websites. On Fiscal 2026's **$6,813.6M** of sales it kept **$2,694.6M** of gross
  margin (**39.5%**) and spent **$2,173.2M** of selling, general and administrative expense
  plus **$555.0M of gross advertising (8.1% of sales)** to get it, leaving **$393.1M of
  operating income, a 5.8% operating margin.** Roughly four dollars in ten survive the goods,
  and about nine-tenths of those four go back out on rent, sales staff and television.
  **Three things sit alongside the merchandise and matter more than their size suggests:**
  (a) **service sales of $803.5M, 11.8% of the total** — repairs, custom design, piercing and
  extended service plans, sold at the moment of a merchandise sale and repeated for the life of
  the item; (b) **$1,277.2M of deferred revenue** at 2026-08-01 ($371.6M current, $905.6M
  non-current), customers' money taken in advance for lifetime repair plans and released into
  income over an estimated redemption period — an interest-free, covenant-free, no-due-date
  liability of the **[E3-52]** kind; and (c) **credit that is not on the balance sheet.**
  Signet sold its prime in-house receivables in Fiscal 2018 and the non-prime in June 2018, and
  now runs the card through Bread (Comenity), with Progressive Leasing and Affirm alongside:
  **$2,306.6M of Fiscal 2026 North America sales, 42.0% of eligible sales, are financed on
  somebody else's balance sheet**, and Signet takes a profit share. The business is **a
  specialty retailer with a small prepaid-service annuity bolted on, and its credit risk is
  rented rather than owned.**
- **The scarce input this business controls.** Honestly, not much that is scarce.
  **Scale in advertising** is the nearest thing: $555.0M a year against a US market the 10-K
  puts at roughly **16,800 jewelry retail stores**, most of them single-location independents,
  in a category the same document calls one where *"much of the merchandise is not branded and
  the purchase cycle can stretch to years"* — exactly the condition under which national brand
  awareness is worth buying. Second, **first-call real estate**: 3,765 thousand net selling
  square feet in North America and the mall and off-mall positions a fifty-year-old chain
  holds. Third, and smallest, **rough-diamond access** — Signet is **a De Beers sightholder
  with contractual allocations** and cuts and polishes in its own Gaborone, Botswana factory.
  None of the three is an asset a competitor cannot buy. The genuinely scarce input has always
  been **a customer who does not know what a diamond costs**, and the company's own risk factor
  says that input is eroding: *"increased price transparency in the market"*.
- **Will the fundamentals look broadly the same in ten years?** The activity will. People will
  still get engaged — **bridal was 49% of merchandise sales in Fiscal 2026** — and somebody
  will still sell them a ring in a mall or on a website. What will not obviously look the same
  is the **price of the central raw material**: the company's own risk factors name *"the
  costs, retail prices, supply and consumer acceptance of, and demand for gem quality
  lab-grown diamonds"*. That is a Q2 and Q4 problem, not a Q1 comprehension problem. The
  business is *"relatively simple and stable in character"* **[E3-31]** in the only sense this
  question asks: I can write down where every dollar comes from and where it goes, from the
  filed statements, without using the company's language.
- **What is NOT simple, recorded here and carried to Q3.** The $1,277.2M deferred-revenue
  balance is released on estimated redemption patterns, and Fiscal 2026 International sales
  were *"favorably impacted by a change in estimate in the product protection plan commissions
  revenue recognized of approximately $15 million"* — earnings created by a change in an
  estimate, which is **[E2-50]**'s *"Where 'earnings' can be created by the stroke of a pen,
  the dishonest will gather"* class. It does not defeat Q1; it tells Q3 where to look.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  *IN. The unit economics fit in one paragraph taken from the filed statements. This is no
  compliment to the business: **[E3-31]** asks only whether I understand it, and **[E4-46]**'s
  five-minute test is met — no amount of further study is needed to know what the company
  does.*"""

assert q1_old in s, "q1 anchor not found"
s = s.replace(q1_old, q1_new)
open(p, "w", encoding="utf-8").write(s)
print("written", len(s))
