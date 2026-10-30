
*Wave 7 name 36 of 218 (line 36 of `Screens/_daily/_wave7_order.txt`; 35 lines in `_wave7_done.txt` at claim, the last being CAH). No `*Run - NATH*.md` existed in `Test Runs/` at claim.*

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## THE FACT THAT CHANGES WHAT THE QUOTE IS: A LIVE CASH MERGER, BY THE LICENSEE

**The screen row's `deal_note` is blank and the brief said to check anyway. A deal is live.** On
2026-01-20 Nathan's signed an Agreement and Plan of Merger with **Smithfield Foods, Inc.** (and
Boardwalk Merger Sub Inc.) at **$102.00 per share in cash** (8-K Item 1.01 filed 2026-01-21, accession
`0001104659-26-005233`, merger agreement as Exhibit 2.1; PREM14A 2026-03-06 `0001104659-26-024713`;
**DEFM14A filed 2026-09-24, accession `0001104659-26-110393`, accepted 20:05:13Z, i.e. 16:05 EDT, after
that day's close**). **Smithfield is the counterparty of Nathan's largest contract**: *"Since March 2014,
we have held an exclusive license to manufacture, distribute, market and sell "Nathan's Famous" branded
hot dogs, sausages, corned beef and certain other ancillary products through retail outlets in the U.S.
and Canada and Sam's Clubs in Mexico. The license is scheduled to expire in March 2032."* (Smithfield
10-K FY2025, accession `0000091388-26-000014`). **The licensee is buying the licensor.** What the
DEFM14A says, read:
- **HSR**: filed 2026-01-23, *"the applicable waiting period expired at 11:59 p.m., Eastern Time, on
  February 23, 2026."*
- **CFIUS** (Smithfield is about 87% owned by WH Group of Hong Kong, per its own 10-K): Declaration
  2026-01-23, Notice 2026-06-08, and *"CFIUS Clearance was obtained on September 17, 2026."* **No 8-K
  announced the clearance**: the submissions index shows nothing between the GAMCO 13D/A of 2026-08-31 and
  the DEFM14A. **The first public statement of it is the DEFM14A, filed after the 2026-09-24 close**, so the
  close used below predates it.
- **Special meeting 2026-10-23**, record date 2026-09-22 (4,097,661 shares entitled to vote). **A Voting
  Agreement binds the directors and certain holders, about 29.9%**; directors and executive officers own
  about 31.0%; Howard M. Lorber alone 989,841 shares, 24.2% (13D/A No. 14, `0001104659-26-005238`);
  GAMCO/Gabelli about 10.8% (13D/A of 2026-08-31, `0000807249-26-000078`).
- **End Date** 2026-06-22, automatically extended to 2026-10-20 for the CFIUS and HSR conditions; the
  termination right is not available *"to either party until five business days after the completion of
  the Stockholders' Meeting"* where those conditions were satisfied before the End Date, which the CFIUS
  date says they were. Company termination fee **$10,581,814**; Parent fee **$7,407,270** on a CFIUS
  turndown, conditional on Nathan's electing to extend the Smithfield licence four years to **2036-03-02**.
  **The price was cut from $103.50 to $102.00** in January 2026 after Smithfield's diligence found *"an
  approximate $20 million gap in its valuation of the Company related to certain matters identified in
  Parent's due diligence findings"* (DEFM14A, Background; carried to Q3 beneath the close).
- **The dividend stops**: *"After the payment of the June 2026 Regular Cash Dividend, the Company is no
  longer permitted to declare and pay any further dividends under the Merger Agreement."* (10-K MD&A).

**What this does, per the ROKU precedent of 2026-09-12:** it excuses no gate. Q1-Q4 are about the
business and are run on the filings in order. It changes **what the price is**: $94.29 against $102.00 in
cash, **the price is 92.4% of the consideration**, a merger spread on a transaction whose last regulatory
condition had been met a week earlier but was not yet public at that close. **Whoever buys at $94.29 is
underwriting the vote and the closing, not the hot dog.** That trade is an arbitrage, the corpus's
*parking place* category **[E2-74]**, and this framework has nothing to say about it.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a forecast **[E4-15, E3-32]**:
- rate **5.47 %** · date **09/24/2026** (the newest row when struck on 2026-09-25) · source (issuing
  authority) **US Treasury daily par yield curve, 30 Yr**, `home.treasury.gov` daily-treasury-rates CSV for
  2026, struck fresh and saved raw as `Test Runs/_research 2026-09-25 NATH/treasury_2026.csv`; neighbouring
  row 5.40 (09/23). `python tools/run.py NATH` printed the same rate and date. **FRED not used.**
- FX: **not required.** International revenue was $3,443K of $162,063K in FY2026 (2.1%); the licences, the
  Branded Product Program and the restaurants are US-dollar businesses. USD sovereign.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2026-03-29, filed 2026-06-09, accession `0001437749-26-019923`**
    (`nath20260329_10k.htm`). Read: cover; Item 1 whole (the three channels, the Licensing Program with the
    Smithfield terms, Provisions and Supplies, Competition, Trademarks, Seasonality); Item 1A whole; MD&A
    whole (results by line, the EBITDA and Adjusted EBITDA reconciliation, liquidity, the Credit Agreement,
    repurchases, dividends); the statements of earnings, changes in stockholders' deficit and cash flows
    with every reconciliation line; Notes A, B (policies), I (segments), J (debt), K (leases), L (stock
    plans, benefit plans), M (commitments), N (merger), O.
  - **10-K/A filed 2026-07-24, accession `0001104659-26-086491`** (Part III; carried beneath the close).
  - **10-Q for the quarter ended 2026-06-28, filed 2026-08-07, accession `0001437749-26-026427`** (cover,
    MD&A, debt note, EBITDA reconciliation).
  - **Earlier 10-Ks, FY2010-FY2025, sixteen documents downloaded from EDGAR** (accessions listed at the end
    of Q1), read for the licensing history (the SMG agreement at *"royalties ranging between 3% and 5% of
    sales"* to March 2014; John Morrell & Co., Smithfield's subsidiary, from March 2014 at 10.8%), the
    royalty-and-volume sentences of every year's MD&A, the debt-funded special dividends and the notes.
  - **8-K of 2026-01-21 with Exhibits 2.1, 2.2, 10.1, 10.2 and 99.1; the DEFM14A of 2026-09-24**; the 8-K
    earnings releases of 2025-06-10, 2025-08-08, 2025-11-06, 2026-02-05, 2026-06-09 and 2026-08-07 (on disk);
    the DEF 14A of 2025-07-25 (`0001104659-25-070823`).
  - **Smithfield Foods 10-K FY2025, accession `0000091388-26-000014`**, for the licensee's own brands, its
    competitor list and its Packaged Meats segment.
- **figure cross-checked against the filed statement: FY2026 net cash provided by operating activities,
  $18,234K**, rebuilt from its own lines: net income 20,020 + D&A 925 + amortisation of debt issuance costs
  70 + share-based compensation 1,132 + credit-loss provision 129 − deferred taxes 88 = 22,188 (the MD&A's
  *"other non-cash operating items of $2,168,000"* is 22,188 − 20,020; ties); working capital: receivables
  −5,906, inventories +330, prepaid +64, other assets +28, lease assets and liabilities −193, payables and
  accruals +2,238, deferred franchise fees −305, other liabilities −210 = −3,954 (the MD&A's *"changes in
  other operating assets and liabilities of $3,954,000"*; ties); **total 18,234. Ties.** The XBRL pull
  (`xbrl_out.txt`, `vintage="newest"`) carries the same $18.234M.
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked.**

**THE PRICE AND THE CAP** *(struck by this run)*
- **Share count, quoted from the cover of the 10-Q for the quarter ended 2026-06-28, accession
  `0001437749-26-026427`, the latest periodic filing:** *"At August 3, 2026, an aggregate of 4,097,661 shares
  of the registrant's common stock, par value of $.01, were outstanding."* **One class**: Section 12(b)
  registers the common stock alone; the balance sheet shows *"Common stock, $ .01 par value; 30,000,000
  shares authorized"* and no preferred. The DEFM14A's record-date count (2026-09-22) is the same 4,097,661.
  `python Screens/cover_shares.py NATH` returned the same document, accession and count.
- **Price $94.29** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint, raw
  response `price_raw.json`; 49,500 shares traded). Two-year closing range in the pull **$76.79 to
  $115.75**; $92.73 on 2026-01-20 before the announcement, $100.79 the day after, $97.94 on the CFIUS date,
  $94.29 on 2026-09-24.
- **cap = close × shares**, `close` never `adjclose`: $94.29 × 4,097,661 = **$386.4M.** At the deal price
  the shares are $418.0M. The screen's $403M is an earlier price on a similar count.
- **The balance sheet beside the cap:** Term Loan **$47.8M** at 2026-06-28 (unsecured Citibank facility,
  SOFR + 1.40%, maturing 2029-07-10; covenants a fixed charge ratio and net leverage not above 3.00x;
  *"certain Change of Control events constitute an Event of Default"*, and *"the Buyer at the Effective Time
  shall pay all outstanding obligations under the Credit Facility"*); cash $24.4M at 2026-03-29; total
  stockholders' **deficit $(14.2)M** at 2026-03-29, the residue of the debt-funded distributions below.

**THE PERIMETER, read before any question.**
- **Acquisitions: none found.** No acquisition line appears in any cash-flow statement FY2010-FY2026 read;
  Arthur Treacher's is an owned trademark carried as a small amortising intangible.
- **Two debt-funded recapitalisations and a third special dividend from cash:**
  1. **March 2015**: *"On March 10, 2015, the Company completed an offering of $135.0 million aggregate
     principal amount of 10.000% Senior Secured Notes due 2020 (the "Notes"). The Company used the net
     proceeds of the Notes offering to pay a special dividend of $25.00 per share (approximately $116.1
     million)"* (10-K FY2015, `0001437749-15-012185`).
  2. **November 2017**: $150.0M of 6.625% Senior Secured Notes due 2025, used to redeem the 2020 notes
     (*"paid a call premium of $6,750,000"*) and toward *"a special $5.00 per share cash dividend"* ($20.9M,
     paid January 2018; *"Nathan's also funded the majority of the special dividend through its existing
     cash"*) (10-K FY2018, `0001437749-18-011457`).
  3. The 2025 notes were bought down to $60M and refinanced on **2024-07-10** by the **$60M unsecured Term
     Loan**; **December 2025, a $2.50 special dividend** from cash (FY2026 dividends paid $18,403K including
     four regular $0.50 quarters).
- **Buybacks**: the sixth plan, 1,101,884 shares for about $39.0M; 5,289,515 shares in treasury at a cost
  of $86.7M; none in FY2025-26, and the merger agreement forbids them.
- **Regular dividend** from June 2018 ($0.25 a quarter, later $0.50), stopped by the merger agreement after
  June 2026.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words.** Nathan's owns a 110-year-old hot dog brand and makes money from it
  three ways.
  1. **It rents the name to a meat packer.** Smithfield makes, sells, prices and promotes Nathan's packaged
     hot dogs in US supermarkets and club stores and pays Nathan's **10.8% of net sales** monthly, *"subject
     to minimum annual guaranteed royalties"*, under an agreement that runs to **March 2032**. Nathan's
     supplies no plant, no sales force, no retail pricing. Smithfield's royalties were **$33,589K in FY2026**
     ($31,893K retail plus $1,696K foodservice), **20.7% of revenue** and *"approximately 90%"* of licence
     revenue. Smaller licences (Lamb Weston fries to July 2028, Solina spices, pickles, snacks) bring the
     licence line to $37,417K. **The Product Licensing segment earned $37,234K of operating income: 84.4% of
     the three operating segments' $44,136K in FY2026 (79.6% in FY2025).**
  2. **It sells hot dogs to foodservice (the Branded Product Program).** Nathan's buys hot dogs, mostly from
     Smithfield, and resells them to distributors and operators (stadiums, cinemas, amusement parks, chains).
     **$105,768K of revenue, 65% of the total, at a segment gross margin of 6.1% (FY2026) and 10.2%
     (FY2025)**, with beef 80-90% of cost of sales and prices set by *"sales agreements with our Branded
     Product Program customers that are correlated to our cost of beef and beef trimmings"*; five customers
     are about 80% of the segment. Segment operating income $4,285K.
  3. **It runs four restaurants (Coney Island among them) and franchises 221 more plus 476 virtual
     kitchens**, taking 5.5% royalties on franchised sales. Restaurant segment operating income $2,617K. The
     system shrank from 230 to 221 in FY2026 (23 opened, 32 closed).
  - Corporate costs of $14,034K (including $3,210K of merger fees in FY2026) sit against the three.
- **The scarce input this business controls:** the **Nathan's Famous trademarks** (registered in the US and
  in over 80 jurisdictions) and the recipe and spice formulation (*"Through this agreement, we control the
  manufacture of all "Nathan's Famous" branded hot dogs"*, of the Solina spice licence). The plants, the
  retail customers, the retail price and the promotions belong to the licensee.
- **Will the fundamentals look broadly the same in ten years?** The mechanism does not change: a royalty on
  packaged sales, a margin on foodservice resale, a franchise royalty. **The contract does**: the Smithfield
  licence expires in March 2032, inside the ten years, and if the merger closes the licensee owns the
  licensor. Whether the brand keeps its rent at the next renewal is Q2's question, not a failure of
  understanding.
- **What I cannot see from Nathan's own filings**: the retail product's price, promotion and shelf, which
  are Smithfield's decisions. That is Q2's evidence problem and is stated there, not a reason to close Q1.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — relatively simple and stable in
  character and legible from the filings **[E3-31]**.

*Earlier 10-Ks read (EDGAR primary documents): FY2025 `0001437749-25-019916`, FY2024 `0001437749-24-020013`,
FY2023 `0001437749-23-016924`, FY2022 `0001437749-22-014727`, FY2021 `0001437749-21-014536`, FY2020
`0001437749-20-012966`, FY2019 `0001437749-19-012012`, FY2018 `0001437749-18-011457`, FY2017
`0001437749-17-011019`, FY2016 `0001437749-16-033631`, FY2015 `0001437749-15-012185`, FY2014
`0001437749-14-011106`, FY2013 `0001437749-13-007587`, FY2012 `0001437749-12-005931`, FY2011
`0001144204-11-034784`, FY2010 `0001144204-10-032962`.*
