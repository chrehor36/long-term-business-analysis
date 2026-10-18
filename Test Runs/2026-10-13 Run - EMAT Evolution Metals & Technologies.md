# Company Run: Evolution Metals & Technologies Corp. (Nasdaq: EMAT), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 830ab25a). Dispatched blind run
under the brief of 2026-10-13 (operator rule ten). Research folder: `Test Runs/_research 2026-10-13 EMAT/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (EMAT; also searched for Evolution Metals, Welsbach and WTMA); not held.*

**Contamination, declared.** Before any work the session context showed (i) the last five commit subjects of the
repository, all about another company's run (ASTE); (ii) a git status listing naming other research folders (AYI, ARCB) and
daily digest files; (iii) a memory index line describing the queue state in general terms (a count of gate-clearers, "nothing
buyable"), naming no company. None concerns EMAT under this or any former name; none was opened or used. No file on the blind
list was opened, listed or searched. The research folder of this run was the only `Test Runs/` path written or read besides
the template.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.47, close 2026-10-12 (Yahoo chart endpoint through `tools/sources.py price()`; an aggregator, flagged, used
  for the live quote only, operator rule 5). Output kept in `_research 2026-10-13 EMAT/price_sovereign.txt`.
- **Shares, one class (common, $0.0001 par):** 621,800,646 on the cover of the 10-Q for the quarter to 2026-06-30, filed
  2026-08-17, accession 0001213900-26-090427 (`python Screens/cover_shares.py EMAT`). Checked against the balance sheet of the
  same 10-Q: 621,790,646 issued and outstanding at 2026-06-30; no treasury shares shown. Checked against the later prospectus:
  "As of October 2, 2026, we have 627,200,646 shares of our Common Stock outstanding" (424B3 filed 2026-10-09, accession
  0001213900-26-108471). The difference is conversions of the Yorkville debentures (below). **Count used: 627,200,646.**
- **Market cap:** $1.47 x 627,200,646 = **$922M**.
- **Sovereign for the earnings currency:** the reporting currency is USD (operations in Korea, revenue in KRW translated);
  US Treasury daily par yield curve, 30-year, **5.6%** on 2026-10-09 (`python tools/sources.py`, issuing authority).
- **Which history the tagged data carries.** `python tools/run.py EMAT` returned "no overlapping OCF/D&A/capex annual facts.
  UNRESEARCHED." The registrant's XBRL history is the SPAC's (Welsbach Technology Metals Acquisition Corp., a blank check
  company with a trust account); no operating-business series was taken from tagged data. **Every figure in this run is read
  from the filed statements**, not from XBRL.
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-20, accession 0001213900-26-018858: Item 1 (business), Item 1A (risks), Item 7 (MD&A, which
    is the SPAC's), the SPAC's balance sheets.
  - 8-K/A (Amendment No. 2) filed 2026-03-31, accession 0001213900-26-036749, items 2.01 and 9.01: Exhibit 99.2 (audited
    statements of Evolution Metals LLC, the accounting predecessor, FY2025 and the period from inception 2024-02-08), Exhibits
    99.3 and 99.5 (audited statements of KCM Industry and NS World), Exhibits 99.9 to 99.13 (MD&A of EM LLC, KCM, KMMI, NS
    World and Handa Lab for 2025 and 2024), Exhibit 99.7 (pro forma, fetched, scanned only).
  - 10-Q for the quarter to 2026-03-31, filed 2026-05-22, accession 0001213900-26-060654 (fetched; the later 10-Q's six-month
    columns were used in its place).
  - 10-Q for the quarter to 2026-06-30, filed 2026-08-17, accession 0001213900-26-090427: statements, notes 1, 15, 21, MD&A.
  - 8-K filed 2026-05-26, accession 0001213900-26-061113 (item 3.01, Nasdaq notice for the late 10-Q).
  - 8-K filed 2026-09-18, accession 0001213900-26-101116 (items 1.01, 2.03, 3.02: the September Yorkville debentures).
  - 424B3 filed 2026-10-09, accession 0001213900-26-108471 (share count; equity plan; dilution note).
  - The proxy: no proxy of the combined company has been filed; the last proxies on EDGAR are the SPAC's (DEF 14A 2025-12-19,
    0001213900-25-123694, and DEFR14A 2025-12-22), listed, not read, because the file closed at Q1.
- **One figure cross-checked against the filed statement:** revenue of $3,515 thousand for the six months to 2026-06-30 on
  the face of the statement of operations (10-Q 0001213900-26-090427) agrees with the revenue table of the same 10-Q (Korean
  domestic sales $3,386 thousand, export sales $129 thousand, total $3,515 thousand) and with the pro forma note's statement
  that the statements "include revenue of $1.7 million and net loss of $3.1 million and revenue of $3.5 million and net loss of
  $4.8 million" from the operating companies since 2026-01-05.
- **`tools/run.py` arithmetic lines:** none produced (see above). Owner cash is computed by hand from the filed cash-flow
  statements in `_research 2026-10-13 EMAT/compute.py`, under COMPUTATION, NOT A CLEARANCE, after the stop.

**The lines of evidence chosen, and why.** The brief left them to the run. From Item 1: what the company says it owns and
operates against what the operating companies' own statements show, because the 10-K's description is of a plan (a U.S.
campus, 55,000 tonnes a year of magnets "within two years") and the price of $922M can only rest on that plan. From Item 1A:
going concern, financing, competition and China's control of prices. From Item 7 and the 10-Qs: revenue, cash burn, capital
spending, the balance sheet and the financing since closing. The 10-K's own Item 7 is the SPAC's and says nothing of the
operating business, so the 8-K/A exhibits and the 10-Q stand in for it.

**Balance sheets (read here because the file closes before Q4; the template asks for eight to ten years).** Ten years do not
exist for anything that is now EMAT. What exists, read from the filed statements:
- *The SPAC (the registrant), 10-K 0001213900-26-018858:* total assets $12.27M at 2024-12-31 and $6.61M at 2025-12-31, almost
  all "Restricted cash held in trust account" ($12.26M, then $6.46M), against current liabilities of $8.23M and $9.51M. The trust
  shrank by redemptions; the 10-Q says "The Business Combination did not include significant external financing at closing".
- *Evolution Metals LLC, the accounting predecessor (8-K/A Ex. 99.2):* total assets $15.70M at 2024-12-31 and $26.67M at
  2025-12-31, of which cash $2.61M then $11.68M, notes receivable (much of it from related parties and the sponsor) and
  deferred transaction costs ($3.99M, then $9.27M). Liabilities $65.07M then $677.36M, nearly all two non-cash items, the "July
  Investment Agreement Derivative" ($53.2M, then $379.2M) and "CPU Share Allocation Obligations" ($10.2M, then $292.7M): promises
  of shares to the investors who funded the entity with $26.3M of convertible preferred units. Members' deficit $(49.4)M then
  $(650.7)M; accumulated deficit $(677.0)M at 2025-12-31.
- *The combined company, 10-Q 0001213900-26-090427:* at 2026-06-30 total assets $95.08M, of which **goodwill $58.91M**,
  intangibles $6.35M, plant $7.33M, cash $5.25M, receivables $4.86M, inventories $1.50M. Total liabilities $113.94M, of which
  non-trade accounts payable $47.55M (consistent in size with the $48,118,084 the 8-K/A's Ex. 99.9 says EM owes the Korean
  Companies' holders under the "Step 6-D" purchase of EM member units, payable on a raise above $50M or at the third
  anniversary), accrued and other current liabilities $27.41M, borrowings and convertibles about $27.5M. **Total deficit
  $(18.85)M.** Accumulated deficit $(1,131.0)M. The filer states "a net working capital deficit of $78.8 million".
- *The operating companies before acquisition (8-K/A Ex. 99.3, 99.5, MD&A exhibits):* KCM total assets $4.57M (2024) and $3.90M
  (2025) against liabilities $4.28M and $3.76M; NS World total assets $6.84M and $5.58M against current liabilities alone of
  $8.20M and $6.64M. Each of the four companies' MD&A carries a going-concern paragraph.
- *What moved and why:* equity is negative at every date; the one large asset of the combined company is goodwill from buying
  the Korean companies; the liabilities that grew were promises of shares, settled into $1,113M of paid-in capital at closing.
  *What the figures do not say:* the comparative column of the 10-Q gives total assets at 2025-12-31 of $22.49M where the audited
  EM statement gives $26.67M (the gap is about the $4.17M related-party note receivable) and an accumulated deficit of
  $(678.8)M against $(677.0)M; the 10-Q's notes were not read far enough to reconcile it. Recorded under AFTER THE STOP.

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. *A share is a business:* "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**. The business that would remain if the market closed is four small Korean companies with $3.5M of
revenue in six months and an operating loss of $27.8M, financed by convertible debentures that convert at a discount to the
market price; the $922M market value rests on a plan, and value is what the asset produces, "That’s investment. One is from what
somebody else will pay you for it later on, irrespective of what the asset produces, and I call that speculation." **[M2002-078]**.
*The analyst's habits:* the filer's case is a projection (55,000 tonnes a year of U.S. magnet capacity "within two years"), and
the rows do not consult projections: "we’ve never looked at a projection in connection with either a security we’ve bought or a
business we’ve bought" **[M1995-050]**; the record of the projectors is the thing to ask for **[M1995-050]**, and here the record
is the operating companies' own losses. "What do I not know that I need to know?" **[M1999-129]** was asked and is answered at
Q1. **Contrary evidence, written down as found** **[M1997-127]**: (1) the 10-K says the company "owns and operates" battery-grade
sulfates, pCAM, precious and base metals and "U.S.-based hydrometallurgical and pyrometallurgical processing infrastructure",
while the 10-Q says its "operating activities consist of the production and development of rare earth magnet materials and
finished magnet products" and calls the U.S. campus "planned"; (2) going-concern doubt at the combined company and at each
of the four operating companies; (3) cash $5.3M against a working-capital deficit of $78.8M; (4) variable-price convertible
financing (Yorkville, May and September 2026); (5) two late 10-Q notices (NT 10-Q 2026-05-15 and 2026-08-14) and a Nasdaq notice
of 2026-05-21; (6) the July 2026 conversions at $2.14 to $4.59 a share against a price of $1.47 now. For the business: NS World,
the largest operating company, has sold magnetic components since 2013 and grew revenue 5.3% in 2025; the 10-K's history says
magnets were sold to Ford, Hyundai, LG and Samsung from 2008; China's export controls on heavy rare earth magnets are a real
demand for a non-Chinese supplier, as the filer argues.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered, puts no demand for sudden sums on the buyer; the rule bites
only if the purchase were financed or sized so that a total loss could hurt, "We are never going to risk what we have and need
for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**.
The target's own going-concern doubt and convertible debt are its ruin risk, not the buyer's, and belong to Q9 (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** "can I understand it?" **[M1995-051]**, where understanding is "a reasonable probability of being able to
asses where the business will be in 10 years" **[M2000-037]**, "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**.

**What the business is, on the filings.** Two businesses are described, and they differ by orders of magnitude.
- *The business that exists:* four Korean companies acquired on 2026-01-05. Their own 2025 statements (8-K/A 0001213900-26-036749,
  Ex. 99.10 to 99.13): KCM, NdFeB bonded powders, revenue $1,300 thousand (2024: $116 thousand, "resumption of operations"),
  operating loss $809 thousand; KMMI, NdPr block and traction-motor magnets, "revenue from contracts with the customers has not
  yet been occurred", "targeting to initiate commercial operations in the second half of 2026"; NS World, magnetic components for
  automobiles and appliances, revenue $6.4M, operating margin "(-) 5.2%"; Handa Lab, monitoring systems and machine vision, revenue
  $458 thousand, operating margin "(89.6)%". Combined 2025 revenue about $8.2M, every company at an operating loss, every company
  with a going-concern paragraph. Under EMAT, six months to 2026-06-30: revenue $3,515 thousand, gross profit $329 thousand,
  selling, general and administrative expense $28,171 thousand, operating loss $27,842 thousand; 42% of revenue from one customer
  and 19% from another; export sales "all ... to China" (10-Q 0001213900-26-090427, notes and statements).
- *The business the price is paid for:* Evolution Metals LLC "was formed in February 2024 for the purpose of building an
  integrated midstream and downstream critical materials platform"; the plan is to "Develop approximately 55,000 tonnes per year of
  rare earth magnet manufacturing capacity in the United States within two years" and "approximately 78,000 tonnes per year of
  battery-grade carbonates, sulfates, and pCAM in the United States within two years", in a U.S. industrial campus the 10-Q calls
  "planned" (10-K 0001213900-26-018858, Item 1; 10-Q MD&A). The existing Korean magnet plants are of 400 and 260 tonnes a year
  (10-K, "EM&T’s Journey from South Korea to USA"). The plan is about eighty times the capacity that exists, to be financed by a
  company holding $5.3M of cash under going-concern doubt.

**The key variables and whether they are foreseeable** **[M1998-044]**: whether the U.S. campus is financed and built, and at
what cost and dilution; the price of feedstock and of rare earth products, which the filer says China sets ("China controls
pricing, supply growth, and downstream availability", 10-K Item 1); Chinese export policy; customer qualification. None can be
foreseen for ten years from the filings, and the first is the whole case. "If something is not very predictable, forget it."
**[M1998-044]**. The commodity paragraph of Q2 says a commodity price is never by itself a STOP at Q1; it is not the ground here.
The ground is that the business to be valued does not yet exist.

**Do the past statements tell me the future ones?** "do I understand enough about this business so that the financial statements
will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look
like" **[M2008-033]**. No: the predecessor's statements are those of a financing vehicle (no revenue; losses from fair-value changes
in share promises), the SPAC's are a trust account, and the operating companies' are a few million dollars of loss-making sales a
small fraction of the size the plan describes.

**The routing.** The rows name this case in Q1's own list of what it rules OUT: "Start-ups are not our game." **[L2007-015]**;
"I say, “We don’t do startups.”" **[M2008-088]**. The entity whose plan the market prices was formed in February 2024; its operating
companies are small and loss-making; one has never had revenue; the capacity on which any value would rest is unbuilt. The rows
put the uncertainty of new businesses beyond any range: "This kind of uncertainty frequently occurs when new businesses and rapidly
changing industries are under examination. In cases of this sort, any capital commitment must be labeled speculative." **[L2000-026]**.
Seeing growth for an industry does not settle it: "Just because Charlie and I can clearly see dramatic growth ahead for an industry
does not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy."
**[L2009-005]**. The doubt row decides the edge: "if you have doubts about something being into your circle of competence, it isn’t."
**[M2002-092]**. And the decision is made off the figures, without a second pass: "So if you can’t make a decision on something like
PetroChina off the figures, forget about going further" **[M2008-069]**.

**Box, and why OUT rather than TOO HARD.** Q1's text lists start-ups under "What it rules OUT" and sends fast-changing technology
and unnamed winners to TOO HARD. The ground here is the first: the question has been answered against the name on the filings
(the business priced is unbuilt), not left unanswerable for want of reading. The alternative reading, TOO HARD (NATURE) on
**[L2000-026]**, is recorded under "What in the framework was wrong or unclear"; it would change nothing in what follows, since
no case of the computation earns the floor at the price.

**VERDICT: OUT** at Q1, on **[L2007-015]**, **[M2008-088]**, with **[M2000-037]**, **[M1998-044]**, **[M2008-033]**, **[M2002-092]**:
the business the price is paid for is a start-up plan; the business that exists is four small loss-making companies whose
statements do not tell the future ones.

## Q2: WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file).
## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0, as the template asks).
## Q5: WHO RUNS IT? NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7: WHAT IS IT WORTH? NOT REACHED (the owner's figures are computed below under COMPUTATION, NOT A CLEARANCE).
## Q8, Q9, Q10, Q12: NOT REACHED.

---
## THE BOX
**OUT at Q1** (a start-up: the business priced at $922M is a planned U.S. campus some eighty times the capacity that exists; the
business that exists is four small Korean companies with about $8.2M of 2025 revenue, all at an operating loss, under going-concern
doubt). COMPUTATION beneath the stop: no positive value on any case, against $1.47. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; **[M1997-127]**.)*

**Bearing on Q2 (the castle).**
- The 10-K (0001213900-26-018858) names no competitor. Its "Competitive Landscape" speaks of "non-China rare earth magnet producers"
  with "approximately 30,000 tonnes per year of planned manufacturing capacity" and names no company; Santoku, Magnequench and Neo
  Performance Materials appear only as former employers of the engineering staff. **No competitor row could be built from rivals the
  filing names**; none was chosen by the analyst (the brief's rule). Named rivals that do not file: none named.
- Item 1A: competitors that "have significantly more resources", several that "have received substantial funding from government or
  government-related sources", and some may offer "products at zero or negative margins". Item 1: "EM&T believes China controls
  pricing, supply growth, and downstream availability".
- Customer concentration: 42% and 19% of six-month revenue from two customers; export sales, all to China (10-Q 0001213900-26-090427).
- July 2026: a 4-tonne trial shipment of NdPr metal for $555,520 ("Senri NdPr Metal Purchase Arrangement"), with an indicative plan of
  about 12 tonnes a month, "not definitive" (10-Q note 21). The company buys its key input.

**Bearing on Q3 (capital).**
- Capital spending $7.74M in six months against revenue of $3.52M; the plan's capacity is about eighty times what exists, with no
  cost stated in the documents read. The 10-Q: "The Company expects to require additional capital to support its operations and
  growth initiatives."

**Bearing on Q4 (the accounts).**
- Net loss $(452.2)M for six months, of which $(423.6)M is "Change in fair value of financial instruments" (share promises to the
  pre-merger investors, settled into paid-in capital at closing); operating loss $(27.8)M.
- The 10-Q comparative column for 2025-12-31 (total assets $22.49M, accumulated deficit $(678.8)M) does not match the audited EM LLC
  balance sheet in the 8-K/A (total assets $26.67M, accumulated deficit $(677.0)M); not reconciled in the notes read.
- The 10-K's Item 1 and Item 7 describe a company that "owns and operates" nine segments including battery-grade sulfates, pCAM,
  precious and base metals, with "U.S.-based hydrometallurgical and pyrometallurgical processing infrastructure", "allowing the
  Company to continue to operate at commercial scale"; the 10-Q says the operating activities are rare earth magnet materials and
  magnets, reports a single segment, and calls the U.S. expansion "planned". None of the four operating companies' MD&As describes a
  battery or e-waste business.
- Going-concern doubt at the combined company (10-Q note 2) and in each operating company's 2025 MD&A; EM LLC's auditor (UHY LLP)
  included a going-concern paragraph.

**Bearing on Q5 (the people): integrity facts, recorded, not judged.**
- Two late quarterly reports in 2026 (NT 10-Q filed 2026-05-15 and 2026-08-14); Nasdaq notice of non-compliance received 2026-05-21,
  cured 2026-05-26 (8-K 0001213900-26-061113).
- The difference between the 10-K's description of what the company "owns and operates" and the 10-Q's (above).
- The 10-K's language: "EM&T’s mission is to become the U.S. champion", "leveraging technology to dominate the REE supply chain",
  "lower execution risk and within a shorter timeframe than alternative approaches". The rows name the tell, "they usually are people
  that tell you things that are too good to be true" **[M2002-028]**; whether it applies is not judged here.
- Frequent 8-Ks under item 7.01 (Regulation FD): thirteen between 2026-07-07 and 2026-10-09 on the EDGAR index, alongside resale
  registrations (S-1 and 424B3 filings of July to October 2026). Contents not read.
- Related-party flows in the cash-flow statement: "Constructive disbursements to related party" $(1.41)M and "Investor expenses
  incurred on behalf of Company" $2.84M in six months; related-party notes receivable of $4.17M at EM LLC at 2025-12-31.
- At closing "the EM Equityholder received $61,875,098 worth of WTMA Common Stock" (8-K/A Ex. 99.9, step seven); the sole stockholder
  of NewCo is named as William David Wilcox Jr.

**Bearing on Q6 (the money and the owners).**
- Shares issued are the company's main source of money: the predecessor's "primary sources of liquidity have been cash flows from
  issuance of convertible preferred units"; since closing, convertible debentures to YA II PN, Ltd. (Yorkville): $19.4M of proceeds in
  the first half, a $5.8M debenture in July (converted in part at $2.14 to $4.59 a share), and on 2026-09-17 a facility of $30.9M
  principal (first $22.0M issued), convertible at the lower of $5.02 or 95% of the lowest daily VWAP of the prior five trading days,
  subject to a floor (8-K 0001213900-26-101116). The rows' warning on issuance is **[L2014-015]**; not weighed here.
- Equity Incentive Plan: 225,000,000 shares initially available, plus up to 3% of outstanding shares each 1 January to 2035 (424B3
  0001213900-26-108471), against 627.2M shares outstanding.
- The "Step 6-D" obligation of $48,118,084 to the Korean Companies, payable on the earlier of 14 days after a capital raise above $50M
  or the third anniversary (8-K/A Ex. 99.9).

**Bearing on Q9 (the target's own exposures).**
- Cash $5.25M against a working-capital deficit of $78.8M at 2026-06-30 (10-Q note 2); borrowings and convertibles about $27.5M at
  that date, plus $5.2M (July debenture, after conversions) and $22.0M (September debenture) since.
- The September debentures carry an "Amortization Event" (VWAP under the floor price for five of seven trading days, the exchange
  cap reached, or the registration unusable for ten days), after which the company pays one fifth of principal a month plus a 5%
  premium; default interest 18%. A demand for sudden sums sits inside the financing.

## COMPUTATION, NOT A CLEARANCE
*(Operator rule 3. Built by Q7's range convention as far as the filings allow; no entry language. Script and output:
`_research 2026-10-13 EMAT/compute.py`, `compute_output.txt`.)*

**Owner cash after every real cost** (operating cash flow, less capital spending, less stock pay and investor-paid expenses added back
as non-cash, after "all forms of compensation" **[L2021-003]**; never a net-income proxy, operator rule 5), $ thousands:

| period | entity, source | operating cash | capex | stock pay; investor-paid | owner cash | annualized |
|---|---|---|---|---|---|---|
| 2024-02-08 to 2024-12-31 | EM LLC, 8-K/A Ex. 99.2 | (3,138) | 0 | not shown | (3,138) | (3,503) |
| FY2025 | EM LLC, 8-K/A Ex. 99.2 | (8,612) | 0 | not shown | (8,612) | (8,612) |
| 2026-01-01 to 2026-06-30 | EMAT combined, 10-Q 0001213900-26-090427 | (14,818) | (7,736) | (1,947); (2,837) | (27,338) | (54,676) |

The predecessor had no operations; its investing cash went to notes receivable (to the sponsor, related parties and others) and is
left out of owner cash here, said so. Interest paid in the half year: $168 thousand; owner cash before interest, annualized,
$(54,340) thousand.

**The window and its base.** **CONVENTION of this run:** Q7 asks for a five-year average; two and a half years of filed periods
exist, and only the last half-year contains the operating business. The central case is the combined company's own half-year,
annualized; the mean of the three periods, $(22,264) thousand a year, is shown beside. Rationale: the predecessor's periods are a
financing vehicle's, not the business's, and averaging them in would flatter the burn. **Growth:** every period is negative and the
burn grows; a compound rate between negative end years is meaningless, so by Q7's specific (b) **the range is the no-growth case
alone, said so.** Specifics (a), (c) to (f) have nothing to act on (no cycle, no positive base, no maintenance guess the filing allows).

**Net debt** at 2026-06-30: short-term debt $2,625K, related-party short-term debt $1,659K, current long-term debt $1,246K,
convertible promissory notes $2,296K, long-term debt $2,309K and $16K, convertible debentures $17,395K, less cash $5,254K; plus the
subsequent event the 10-Q itself states (the July debenture, $5,225K principal left after conversions, about $5,600K of net
proceeds): **$21,917K**. Beside it, with the non-trade payables that carry the Step 6-D obligation ($47,553K and $461K): $69,931K.
The September debenture ($22.0M) came after the 10-Q and is not in its subsequent-events note; left out and said so.

**(a) VALUE RANGE** (the no-growth case alone; zero growth for ten years and after, at the 30-year Treasury, 5.6%):
- **all-equity basis (central):** $(54,340)K / 0.056 less net debt $21,917K = about $(992)M, **$(1.58) a share**;
- equity-only basis (beside): $(54,676)K / 0.056 = about $(976)M, $(1.56) a share;
- on the three-period mean, beside: $(0.67) a share all-equity, $(0.63) equity-only.
Against the price of **$1.47**. No case is positive; no case earns the floor at the price; the floor test closes OUT before any width
test (Q7, "The floor is tested first"; "there’s just a point at which we drop out of the game" **[M2003-149]**).

**(b) FAIR PRICE** (Part VII: each end case valued at ten percent, the two averaged; here the single case; after the company's own tax,
which is nil, the company having losses and a tax benefit of $51 thousand; no carryforward shelter priced, there being no taxable
profit to shelter):
- **all-equity basis (central): $(0.90) a share**; equity-only basis: **$(0.87) a share**;
- with the Step 6-D payables counted in net debt: $(0.98) all-equity;
- on the three-period mean: $(0.39) all-equity, $(0.35) equity-only.
**No positive fair price exists on any case.** Neither figure is a verdict or entry language.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 830ab25a); written question by question; committed when Q1 closed (59371b11)
      and again at the close.
- [x] Dispatched run: the brief allowed per-question pathspec commits of this file and the research folder; the lock is the
      dispatching session's. The run binds nothing until folded into the register.
- [x] No other run file, holding review, `PORTFOLIO.md`, `Screens/RESUME STATE*`, the queue file or the reading list was opened,
      listed or searched. What the session context showed by accident is declared under contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `_research 2026-10-13 EMAT/check_ids.py`); no E-ids; every filing fact carries its accession.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from the filed cash-flow statements after stock pay, never a net-income proxy; the sovereign from the Treasury;
      the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS); facts for later questions under AFTER THE STOP; the integrity flag
      is in the box line.
- [x] No point-in-time anchor; rows of every year usable.
- [x] `tools/run.py` produced no arithmetic lines; nothing it prints was used.
- [x] `python tools/check_framework.py` run before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **"Start-up" is not defined.** Q1 lists start-ups under what it rules OUT (**[L2007-015]**, **[M2008-088]**), while the rows also
say that "new businesses" make "any capital commitment" speculative **[L2000-026]**, which reads as an inability to value, the TOO
HARD ground of **[M2000-038]**. A SPAC that buys small, old, loss-making operating companies and is priced on an unbuilt plant sits
between the two. This run chose OUT because the text lists start-ups by name under OUT and the question is answered on the filings,
not left open for want of reading; another analyst could defensibly write TOO HARD (NATURE). The box would differ; the computation
and any alert would not. A sentence saying whether a company whose value rests on capacity not yet built is a start-up, whatever the
age of the shell or of its acquired subsidiaries, would settle it. (2) **Q7's five-year window has no rule for a company with less
than five years of the business.** The run confessed its own CONVENTION (the combined company's half-year, annualized, central; the
predecessor's periods beside). De-SPACs and recent mergers need a rule, since the registrant's history (a trust account) and the
predecessor's (a financing vehicle) are not the business. (3) **The template's eight to ten years of balance sheets** cannot be met
for such a company; the run read every balance sheet that exists (SPAC, predecessor, two of the four targets, combined) and said so.
(4) **The brief's competitor rule** ("the rivals the 10-K itself names") returns nothing where the 10-K names none; the run recorded
the absence rather than choose rivals, and Q2 was not reached in any case.
