# Company Run: Magnitude International Ltd (Nasdaq: MAGH, trading halted), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
a8e969b5).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (dcba990d): not held; `PORTFOLIO.md` has no line for MAGH, Magnitude International, Herlin or Elec Power.*

**Dispatch.** Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with one stated departure: the lines of
evidence were not written by the dispatcher; I derived them from the 20-F's Item 4 (business overview, competitive landscape,
customers, contracts and pricing model), Item 3.D (risk factors on tendering, pricing, customer concentration, competition,
backlog and the trading suspension) and Item 5 (results, liquidity and cash flows). The lines chosen: (1) how work is won
and priced; (2) who the customers are and how concentrated; (3) who the rivals are and on what they compete; (4) what the
margins and returns have been, year by year, against the field's; (5) what the balance sheet and the cash say; (6) the
IPO, its proceeds and the trading suspension.

**Contamination, declared and not used.** (a) The session's opening git status listed recent commit subjects of a run on a
different company, MAGN Magnera, including its box ("OUT at Q2"); a different business, not used. (b) A directory listing
I ran of `Test Runs/` for today's date showed the file names of other companies' runs of 2026-10-17 (ALFVY, AMTM, ARCAY,
BCKIY, BLGO, CDNL, CHYCY, FER, FLR, HLEO, KGHI, LGN, MAGN, MEC, MPTI, MTRX, SHIM, TSSI, TTEK) and no MAGH file; none was
opened. (c) The git status also showed research-folder names of other runs (AYI, ARCB). (d) The session's memory index
carries lines about the queue and the count of gate-clearers; nothing in it names this company. No position, no holding
review, no other run on this name, under any former name, was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** US$6.76, the last trade, 2025-12-04 (Yahoo Finance chart API, an aggregator, flagged per operator rule 5).
  **The price is stale and no market exists for it:** the SEC suspended trading from 2025-12-05 through 2025-12-18 and
  Nasdaq halted the shares on 2025-12-19; the halt stands (6-K 2025-12-10, accession 0001493152-25-027002; 6-K 2026-08-05,
  accession 0001493152-26-036115). The aggregator carries US$6.76 with zero volume every day since. The same series shows the
  path into the suspension: IPO at US$4.00 (424B4 2025-08-12), US$1.48 on 2025-08-15, US$1.37 on 2025-11-11, then
  US$6.76 on 2025-12-04 on volume of 2.3 million shares (aggregator, flagged).
- **Shares by class:** 35,000,000 ordinary shares, one class (20-F for the year to 2026-04-30, filed 2026-09-17, accession
  0001493152-26-043050: "As of the date of this Annual Report, the Company had 35,000,000 Ordinary Shares issued and
  outstanding"; `python Screens/cover_shares.py MAGH` returns the same 35,000,000 from that filing). Check: 33,350,000
  shares before the IPO (the weighted count for FY2024 and FY2025, giving effect to the 1:40 split and the share surrenders
  of 2025-05-27) plus 1,650,000 new shares sold in the IPO (20-F, Corporate History) = 35,000,000. No treasury shares found.
  No 6-K after the 20-F changes the count (6-K 2026-09-18, accession 0001493152-26-043266, concerns the Nasdaq notices only).
- **Market cap:** 35,000,000 x US$6.76 = US$236.6M. At the filing's own convenience rate (revenue S$19,050,555 =
  US$14,955,688, so S$1 = US$0.78505 and US$1 = S$1.2738), **S$301.4M**. Both on a price that cannot be traded.
- **Sovereign for the earnings currency (SGD):** **2.62%**, the 50-year Singapore Government Securities benchmark (issue
  NC22300W, 3.000% coupon, maturing 2072-08-01), bid yield at the close of 2026-10-16, from the Monetary Authority of
  Singapore, "Singapore Government Securities - Benchmarks, Closing Levels" (eservices.mas.gov.sg, Daily SGS Prices),
  read 2026-10-17. The longest maturity MAS publishes. (The 30-year benchmark, NA24300E, stood at 2.41% the same day.)
  `tools/sources.py` covers USD, JPY and EUR only, so the figure was taken from the issuing authority by hand.
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0002046117:
  - 20-F for the year to 2026-04-30, filed 2026-09-17, accession **0001493152-26-043050** (Items 3.D, 4, 5, 6, 7, 14, 15, and
    the audited statements for FY2024 to FY2026, auditor WWC, P.C., opinion dated 2026-09-17).
  - 20-F for the year to 2025-04-30, filed 2025-09-15, accession 0001493152-25-013424, and its 20-F/A filed 2026-03-03,
    accession 0001493152-26-008628 (the amendment added the disclosure-controls conclusion, the cybersecurity item and the
    officer certifications the original omitted; SEC CORRESP of 2026-03-03, accession 0001493152-26-008682, and of 2026-03-06,
    accession 0001493152-26-009050).
  - 424B4 prospectus of 2025-08-12, accession 0001641172-25-023166 (audited FY2023 and FY2024 statements; use of proceeds).
  - 6-Ks: 2025-08-14 (0001641172-25-023712), 2025-12-10 (0001493152-25-027002), 2026-04-30 (0001493152-26-019717, interim
    statements to 2025-10-31), 2026-08-05 (0001493152-26-036115), 2026-09-18 (0001493152-26-043266); NT 20-F of 2026-08-31
    (0001493152-26-040731).
  - **One figure cross-checked against the filed statement:** revenue for FY2024, S$24,201,834, is the same in the audited
    income statement of the 424B4 (accession 0001641172-25-023166, F-4) and in the audited income statement of the 2026 20-F
    (accession 0001493152-26-043050, F-4); net profit for FY2024, S$2,007,469, likewise agrees in both.
- `python tools/run.py MAGH`: **returned nothing usable** ("no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.";
  output kept at `Test Runs/_research 2026-10-17 MAGH/run_py_out.txt`). The tool does not read this IFRS 20-F filer. Every
  figure below is taken by hand from the filed statements named above, and said so.
- **The years the filings carry.** Audited statements exist for FY2023 to FY2026 (years to 30 April): income and cash flow
  for four years, balance sheets at four year-ends (2023-04-30 to 2026-04-30). Only one figure reaches further back: the
  provision for onerous contracts of S$1,967,826 at 2022-05-01 (424B4, provision note). Eight to ten years of balance
  sheets **[M2025-032]** do not exist on the public record; the company was private until 2025.

**Owner cash by year, taken from the filed cash-flow statements (S$; all-equity basis, before interest; COMPUTATION after
the Q2 STOP, written here because it was gathered here):**

| Year to 30 April | Operating cash flow (after tax and working capital, before interest) | Capital spending | Lease principal | Owner cash | Finance costs | After interest |
|---|---|---|---|---|---|---|
| FY2023 | 996,128 | (15,548) | (86,879) | 893,701 | (47,363) | 846,338 |
| FY2024 | 609,817 | (31,381) | (31,906) | 546,530 | (68,167) | 478,363 |
| FY2025 | (926,041) | (19,472), with 4,000 of disposals | (36,587) | (978,100) | (90,715) | (1,068,815) |
| FY2026 | (1,912,623) | (28,874) | (47,611) | (1,989,108) | (143,062) | (2,132,170) |
| Four-year average | | | | **(381,744)** | | **(469,071)** |

Sources: 424B4 (0001641172-25-023166) F-6 for FY2023 and FY2024; 20-F 2026 (0001493152-26-043050) F-6 for FY2025 and
FY2026. Excluded as not operating: the keyman life policy bought in FY2024 (S$92,177), the loans to third parties of FY2026
(S$1,783,320), IPO costs. Depreciation ran S$118,896, S$102,990, S$85,684 and S$55,875 against capital spending of
S$15,548 to S$31,381: spending below depreciation in every year. No stock pay found in any year. Interest is added back
inside operating cash by the filer and paid within financing, so operating cash is before interest.

## THE FOUNDATIONS (not a gate)
Two bear hardest. A share is a business: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**; here the market has in fact been closed to this stock since December 2025, and the only question left is the
business, an electrical subcontractor with about S$5M of equity after its IPO. And the market serves and does not instruct
**[M2006-077]**: the last quotation, US$6.76, was set in three weeks of a fourfold rise that ended in an SEC suspension; it
"just tells us prices" **[M2006-077]**, and here not even a price at which anyone can deal. Margin of safety, "if you have to
actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**, is carried to Q7 if the file gets
there. **Contrary evidence, written down as found** **[M1997-127]**: (1) the trading suspension and Nasdaq's delisting
determination under IM-5101-4 (potential third-party misconduct), which the company says involved no finding of wrongdoing
by it (6-K 2026-08-05); (2) FY2026: revenue up 24% to S$19.1M but a loss from operations of S$2.2M and operating cash outflow
of S$1.9M; (3) US$1.4M of the IPO money lent unsecured to two unnamed third parties (20-F 2026, note 8); (4) S$1.6M of
dividends declared to the controlling shareholder in FY2025 against profit of S$42,980 (20-F 2026, statement of changes in
equity); (5) a gross margin that fell from 15.9% in FY2024 to 10.5% in FY2026. All five were found before any verdict.

## THE STANDING RULE
The buyer's conduct, not the target's: nothing here requires borrowing, collateral or a call the buyer cannot meet; a
purchase would be of unlevered shares, so the rule is not engaged by the financing **[M2012-081]**, **[L2023-005]**. One
thing it does engage: shares halted since December 2025 and facing delisting cannot be sold, so whatever is put in must be
money the buyer can leave locked up indefinitely; "We are never going to risk what we have and need for what we don’t have
and don’t need." **[M2012-081]**. No ruin to the buyer from the target's own debts, since a shareholder's loss is capped at
the price paid.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filing.** Two Singapore operating subsidiaries, Herlin (founded 2012-03-23) and BNL (2012-11-05),
  held through a BVI intermediate, Elec Power Ltd, under a holding company the 20-F says is "incorporated in the Cayman
  Islands" (20-F 2026, accession 0001493152-26-043050, Corporate History and Holding Company Structure; the brief called it a
  British Virgin Islands company; the filing's own words are used here). They install electrical systems as a subcontractor:
  greenfield installation for new residential and mixed developments (60.5%, 63.3% and 77.1% of revenue in FY2024 to FY2026)
  and brownfield additions and alterations (33.6%, 14.5%, 16.9%), private sector 100%, 76.7% and 63.9% of revenue. Revenue
  S$21.9M, S$24.2M, S$15.4M and S$19.1M in FY2023 to FY2026. Backlog S$85.0M at 2026-04-30 (20-F 2026, Item 4).
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**. The
  key variables **[M1998-044]**, from the filing: (1) the volume of Singapore building work let to electrical subcontractors;
  (2) the mark-up the company can win in tenders against other contractors; (3) its labour and material costs (it uses
  subcontracted labour and foreign workers); (4) its dependence on a handful of main contractors; (5) its BCA grade, which
  caps the size of public contracts it may tender for (L5: up to S$16 million a project; it aims for L6). None is a technology
  forecast. "I never would understand the chemistry of it, but I — but that’s not necessarily vital. What is important is that I
  understand the economic dynamics of the industry." **[M2011-014]**: the economic dynamics here are stated plainly in the
  filing itself, a cost-plus-mark-up tender business with no recurring contracts.
- **Would the insiders write it down?** **[M2000-105]** Yes, in substance: the filing writes down how the business prices,
  wins and loses work, and what moves its margins (20-F 2026, Item 3.D and Item 4, Contracts and Pricing Model). What cannot be
  foreseen is which tenders it wins in a given year, which moves the size of the earnings, not the kind of business.
- **Is it important and knowable?** **[M2006-076]** The deciding matter, whether anything protects the margins, is knowable
  from the filings and is the subject of Q2.
- **Routing.** Not a fast-changing industry, not a financial institution, not a black box. Seeing the industry is not enough
  **[M2012-065]**; here what is foreseeable about the company's own position is exactly what Q2 must judge.
- **Doubt test** **[M2002-092]**: I have no doubt that I understand how this business makes and loses money; the doubts I have
  are about whether it can keep making it, which is Q2's question, and about the people and the stock, which are Q5's.
- **VERDICT: IN.** The economics of a Singapore electrical subcontractor that wins every contract by competitive tender can
  be foreseen in kind ten years out **[M2000-037]**, **[M2012-065]**, **[M2011-014]**; the filing states the variables
  **[M1998-044]**. Passed to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]** The filing was read for the castle the company itself claims. Its "Competitive
Strengths" are five: a track record of over 13 years; safety and quality certifications; an experienced management; "strong
and stable relationships with our customers"; and stable relationships with suppliers (20-F 2026, accession
0001493152-26-043050, Item 4). No cost advantage, brand, patent, licence monopoly or contract right is claimed.

**The castle tests, each with its filing fact.**
1. **The money test.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]**. The field, in the filing's words: "competitive and relatively fragmented. As of April 30, 2026, there were
   over 2,200 contractors registered with the BCA under the ME05 (electrical engineering) workhead, of which only approximately
   6.4% and 4.5% were of Grade L5 and Grade L6, respectively. Apart from competition from local contractors, there is also
   competition from many large international players mainly from China and India." (20-F 2026, Item 4). On those percentages,
   roughly 140 contractors hold Grade L5 and roughly 100 hold Grade L6, the grade above the company's. The grade is the only
   barrier the filing names, and it is bought with "financial, management & development and track record requirements" and
   qualified staff, which the company itself plans to meet by the end of 2026 (20-F 2026, Business Objectives). A rival with
   money and a few years can do the same. "there are some industries that are just never going to have barriers to entry"
   **[M2012-106]**.
2. **Pricing power and the agony before a rise** **[M2005-020]**. The company does not raise prices; it bids. "If we perceive
   keen competition on a particular project, we may submit a more competitive tender price with a lower mark-up margin, thereby
   reducing profitability." and "we may have to agree to a contract price that is lower than our proposed tender price and/or
   offer more favorable terms to our customers." (20-F 2026, Item 3.D). Pricing model: "a cost estimate plus mark-up pricing
   model" (Item 4).
3. **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the low bid"
   **[M2017-009]**. Here it is exactly that question: "we derived all of our revenue from contracts awarded through a competitive
   tender process and the contracts are not recurring in nature" (FY2024 to FY2026; the 424B4 says the same of FY2023 and
   FY2024); "Our existing customers are not under any contractual obligation to give us the first right for any future projects
   [...] We have to go through a new tender process with them for each new project." (20-F 2026, Item 3.D). The insurer's
   failing answer fits word for word: "most insureds don't care from whom they buy." **[L2004-003]**.
4. **Service as the escape from the commodity class.** The filing says the field competes "on market position, industry
   reputation, track record, relationship with project owners, main contractors and industry professionals [...] and financial
   standing" (Item 4), and its tender success rate was about 60%, 70% and 70% in FY2024 to FY2026. Reputation qualifies a
   bidder; it does not let it charge more, by the filing's own account of how prices are set (test 2). The rows' own limit on
   the service escape: "there will be a number of companies that provide good services. So that does not distinguish us from a
   great many competitors. Having the low cost is crucial." **[M2000-146]**.
5. **The low-cost position, the commodity field's one exception.** "commodity businesses have risk unless you’re the low-cost
   producer" **[M1997-010]**; "Another way to prosper in a commodity-type business is to be the low-cost operator."
   **[L2004-007]**. The filing claims no cost advantage and states none (its five strengths, above). It subcontracts
   "labor-intensive installation work" "to minimize our fixed costs" (Item 4, Vendors), which any rival can do. Its own record
   shows contracts priced below their cost: a provision for onerous contracts of S$1,967,826 stood at 2022-05-01, "in respect of
   remaining expected losses arising from non-cancellable construction contracts where the expected total contract costs exceed
   the total contract sum" (424B4, accession 0001641172-25-023166, provision note), on revenue of about S$22M a year. Its gross
   margin moved 12.1%, 15.9%, 15.5% and 10.5% in FY2023 to FY2026. No evidence of a low-cost position was found, and the returns
   (below) show none at work.
6. **Who sets the price.** "whatever he charged for gas was my price." **[M2012-109]**; "he determined our profit, because we
   looked at his price every day." **[M2023-079]**. In a sealed tender the rival's bid sets the price the company must beat:
   "If we [...] fail to provide a competitive bid as compared to our competitors, our potential customer may turn to our
   competitors." and "we may face keen competition and significant downward pricing pressure, thereby reducing our profit
   margins" (20-F 2026, Item 3.D).
7. **The customer's power.** The customers are main contractors and some developers. Top five customers: 87.9%, 85.5%, 76.7%
   and 82.5% of revenue in FY2023 to FY2026; the largest alone 70.4%, 52.2%, 30.6% and 23.4% (424B4 and 20-F 2026). No
   long-term contract with any of them (Item 4, Customers). Payment terms are the customer's: progress payments within 35 days
   of invoice, 5% retention held for 12 to 18 months after completion, performance bonds of 5% to 10% backed by cash or
   guarantees on about a third of projects, and start-up costs carried by the company for the first three to six months (Item 4,
   Contracts and Pricing Model).
8. **Would it stand without the lord?** "if a business requires a superstar to produce great results, the business itself cannot
   be deemed great." **[L2007-006]**. Every bid's final price is "signed off by our CEO" (Item 4, Tender submission); the bank
   borrowings are "secured by a personal guarantee from Mr. Lim and a pledge of the keyman life insurance policy on the life of
   Mr. Lim" (Item 5, Bank Indebtedness). The business leans on one man's relationships and credit, not on a standing advantage.
9. **Ask the competitors.** The 20-F names no competitor; "large international players mainly from China and India" are not
   named. No rival's view is on the public record.
10. **Widening or narrowing** **[M1999-108]**. Narrowing on the filer's own figures: FY2026 revenue rose 24% while gross margin
    fell from 15.5% to 10.5%; the largest-customer share fell from 70.4% to 23.4% in four years, a wider customer list but not
    better terms.
11. **What could destroy it** **[M2000-014]**. A Singapore building downturn, a lost main contractor, a fixed-price contract that
    runs over (the 2022 onerous contracts), foreign competitors bidding lower.

**The competitor row.** *CONVENTION of this run: the 20-F names no rival, so the field comparators are the two SEC filers found
by an EDGAR full-text search for the company's own registration vocabulary ("workhead", "registered with the BCA") that sell
construction trades in Singapore to main contractors and public owners on tender: FBS Global Ltd (FBGL) and SKK Holdings Ltd
(SKK). Rationale: the brief allows rivals of the run's choosing when the filing names none, and these share the regulator, the
customer and the way work is won; neither is an electrical contractor, so they show the field's economics, not the trade's.
A third search hit, Wang & Lee Group (Hong Kong electrical works), was not read: a different market, and it shows no ticker.*

| Company (filing) | Year | Revenue | Gross margin | Operating margin |
|---|---|---|---|---|
| Magnitude (424B4 0001641172-25-023166; 20-F 0001493152-26-043050), years to 30 April, S$ | FY2023 | 21.86M | 12.1% | 3.6% (helped by the use of the 2022 onerous provision) |
| | FY2024 | 24.20M | 15.9% | 8.4% |
| | FY2025 | 15.36M | 15.5% | 0.5% |
| | FY2026 | 19.05M | 10.5% | -11.6% (-2.2% before the S$1.79M rise in administrative costs the filer calls one-time) |
| FBS Global (20-F 2026-04-30, 0001493152-26-020758), years to 31 December, S$ | 2023 | 21.81M | 12.1% | -0.2% |
| | 2024 | 13.85M | 9.0% | -7.0% |
| | 2025 | 25.86M | 10.2% | -7.5% |
| SKK Holdings (20-F 2026-04-10, 0001493152-26-016229), years to 31 December, US$ | 2023 | 9.66M | 28.4% | 3.4% |
| | 2024 | 11.11M | 36.2% | 4.6% |
| | 2025 | 12.95M | 25.1% | -19.6% (-1.0% before stock pay of US$2.4M) |

**The field's returns over the last full cycle, judged in words** *(CONVENTION of the framework: "ordinary" carries no figure)*.
The filings reach back to the trough of 2022 (Magnitude's contracts then running below cost, the S$1.97M onerous provision), up to
the best year, FY2024, and down again. Over that span the three companies show operating margins from a few percent in good
years to losses in bad ones, and FBS Global lost money in all three of its years. Magnitude's own four filed years add up to
S$689,471 of operating profit on S$80.5M of revenue, under 1%, or about 3% before the FY2026 listing costs; its owner cash over
the same four years sums to a negative S$1.53M (Step 0 table). The high return on capital Magnitude shows in FY2024 (operating
profit of S$2.04M on equity plus borrowings less cash of S$1.73M) rests on a capital base that subcontractors' credit keeps small
(trade and other payables of S$3.8M to S$6.1M at every year-end) and did not turn into cash across the window. These are
ordinary returns or less, and nothing in the filings protects even those: "A truly great business must have an enduring
"moat" that protects excellent returns on invested capital." **[L2007-004]**; "you can have only two competitors and they’re
still terrible businesses" **[M2013-052]**, and here there are over two thousand.

**The parts table.** Not needed: the filer reports one business, electrical installation in Singapore, through two
subsidiaries with the same economics (20-F 2026, Item 4).

**Why this is OUT and not TOO HARD.** The castle is not tenuous or unjudgeable **[M2000-019]**; it is shown open on the
filer's own evidence: every dollar of revenue is won on a competitive tender, the price is cut to win, rivals' bids set it,
the barrier is a registration grade (L5 or above) that some 240 firms already hold on the filing's percentages, no cost advantage is claimed or shown, and the
field earns ordinary returns or less. The framework's list of what Q2 rules OUT names three of these directly: the business
whose price a competitor sets **[M2012-109]**, **[M2023-079]**; the customer who buys on the low bid **[L2004-003]**,
**[M2017-009]**; and the standing castle that protects only ordinary returns **[L2007-004]**, **[M2013-052]**. "If the answer
had been yes, we wouldn’t have done it." **[M2011-015]**. Price does not reopen it: "You can turn any investment into a bad
deal by paying too much. What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** A commodity service sold by tender with no shown low-cost position, in a field earning ordinary returns
  or less **[L2004-003]**, **[M2017-009]**, **[M2012-109]**, **[M1997-010]**, **[L2007-004]**, **[M2011-015]**. The file closes
  here; Q3 to Q12 are NOT REACHED, and every figure below is COMPUTATION, NOT A CLEARANCE.

## Q3 to Q12: NOT REACHED
Closed at the Q2 STOP (operator rule 2). Q3, Q4, Q5, Q6, Q8, Q9, Q10 and Q12 are not answered. Q6's buyback line needs the
bottom of a Q7 range that was not reached as a clearance; no buyback is on record in any case.

## Q7 COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures)
Built by Q7's range convention as far as the filings allow; nothing here is a verdict or entry language (operator rule 3).
- **The window.** Four filed years, FY2023 to FY2026, not five: no earlier audited cash flow is on the public record (Step 0).
  The literal window is the window.
- **Owner cash, all-equity basis (before interest, after the company's tax, all spending deducted, working capital counted):**
  S$893,701, S$546,530, (S$978,100), (S$1,989,108); average **(S$381,744)**. Equity-only (after finance costs): average
  (S$469,071). Depreciation variant beside (depreciation in place of capital spending): average (S$449,787). Maintenance case
  (specific e): capital spending sat below depreciation in every year, so there is no growth spending to separate; all spending
  is maintenance and the central case is the one above.
- **Growth (specifics b and f).** The series changes sign (positive in FY2023 and FY2024, negative in FY2025 and FY2026); the
  halves average S$720,116 and (S$1,483,604), a swing through zero that gives no meaningful rate. By specific (b), the range
  is the **no-growth case alone**, said so. No cap arises.
- **Cycle (specific a).** FY2026 is aberrational on the filer's own description: a S$1,789,292 rise in administrative costs,
  "principally comprising one-time advisory and consultancy fees incurred following the IPO" (20-F 2026, Item 5). FY2023 was
  helped by the use of the 2022 onerous-contract provision. No full cycle can be marked within four years; the variant with the
  FY2026 fees added back is shown beside: FY2026 owner cash (S$199,816), average **S$65,579**.
- **Acquisitions (c):** none in the window. **Working capital (d):** counted, inside operating cash.
- **Net debt at 2026-04-30:** borrowings S$2,034,177 (bank S$1,484,569 plus lease liabilities S$549,608; the filing does not
  split vehicle from property leases, so all are kept in) less cash S$1,139,870 = **S$894,307**. Beside, not in: loans to third
  parties S$1,884,941 (unsecured, to unnamed parties; would make net cash of S$990,634 if counted as cash, worth S$0.05 a share);
  keyman policy S$450,603 (pledged to the bank); dividend payable to Mr. Lim S$600,000 (owed to the controlling shareholder).
- **Rate:** 2.62% (50-year SGS, MAS, 2026-10-16), zero nominal growth after year ten, here from year one.

**VALUE RANGE (all-equity, central):** whole business (S$381,744) / 2.62% = (S$14.57M), less net debt S$0.89M = **(S$15.46M),
(S$0.44) a share, (US$0.35) a share** at US$1 = S$1.2738. A single case, so no width. Beside: the fees-added-back variant,
S$65,579 / 2.62% = S$2.50M less net debt = S$1.61M, **S$0.046 (US$0.036) a share**; equity-only, (S$469,071) / 2.62% =
(S$17.90M), (S$0.51) a share. Against **US$6.76** (the last trade, 2025-12-04, aggregator, untradeable).

**The floor, tested first.** At a market value of S$301.4M plus net debt, every case returns below zero or near it: (0.13%),
0.02% on the fees-added-back variant. A ceiling case outside the convention, shown only to measure the distance (CONVENTION
of this run: rationale, to show no reading of the filings reaches the price): the best year's operating profit, FY2024
S$2,042,793, taxed at Singapore's statutory 17% (S$1,695,518), carried forever at 2.62% = S$64.7M, or **S$1.82 (US$1.43) a
share**, about a fifth of the last price; its return at the price is 0.56%. No case earns the floor of about ten percent
**[M2003-149]**. Had Q2 passed, Q7 would close OUT on the floor.

**FAIR PRICE** (Part VII: each end case valued at ten percent, averaged; one case here): (S$381,744) / 10% = (S$3.82M), less
net debt S$0.89M = (S$4.71M), **negative, (S$0.13) or (US$0.11) a share, all-equity basis (central)**. Equity-only beside:
(S$469,071) / 10% = (S$4.69M), **negative, (S$0.13) or (US$0.11) a share**. Fees-added-back variant: S$65,579 / 10% less net
debt = (S$0.24M), still negative. Company's own tax throughout, no conversion. **No positive price earns the floor on the
filed record.**

## THE BOX
**OUT at Q2** (the castle is open: every contract won by competitive tender at a price rivals' bids set, no low-cost position,
a field earning ordinary returns or less). COMPUTATION, NOT A CLEARANCE: value range (S$0.44) a share (US$0.35), a single
no-growth case, against US$6.76 (last trade 2025-12-04, halted); fair price negative. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**. No verdict on them; the box is unchanged.

**Q3 (capital).** Receivables plus contract assets: S$6.55M, S$5.21M, S$5.65M and S$9.09M at the four year-ends, 30%, 22%,
37% and 48% of the year's revenue. The company carries start-up costs for three to six months, cash-backed performance bonds of
5% to 10% on about a third of projects, and 5% retentions (20-F 2026, Item 4). Capital spending S$15,548 to S$31,381 a year.

**Q4 (the accounts; the balance sheets, four year-ends, all the record holds).** Equity S$140,213 (2023), S$1,949,587 (2024),
S$599,545 (2025), S$4,961,916 (2026, after S$6,664,717 of net IPO proceeds); retained earnings S$1,153,437, S$2,710,906,
S$1,153,886, then accumulated losses of S$1,179,180. Cash S$1.61M, S$1.87M, S$0.76M, S$1.14M. Borrowings S$1.38M, S$1.65M,
S$2.34M, S$2.03M. Trade and other payables S$6.14M, S$3.84M, S$5.33M, S$4.78M. No goodwill or intangibles. What moved: equity
was drawn down by dividends to near nothing before the IPO and refilled by it; receivables and contract assets grew faster than
revenue; S$1.88M of the new money sits in loans to third parties. Other facts: FY2023 profit (S$783,735) was struck after
using S$1,856,344 of the onerous-contract provision, and operating cash before working capital that year was (S$678,668)
(424B4 F-6); a S$398,607 receivable "from a third party" was fully provided by 2025-04-30 and written off in FY2026 (20-F 2026,
note 7 and credit-risk note); income tax of S$253,504 was charged on a pre-tax loss in FY2026, "principally attributable to
expenses that were not deductible for tax purposes, deferred tax assets that were not recognized and adjustments relating to
prior years" (Item 5); the FY2026 administrative rise of S$1,789,292 is called "one-time" by the filer; the FY2025 20-F omitted
the disclosure-controls conclusion, the cybersecurity item and the officer certifications until the SEC asked (CORRESP
2026-03-03 and 2026-03-06; 20-F/A 0001493152-26-008628); the FY2026 20-F was late (NT 20-F 0001493152-26-040731; delay
"attributable to the internal administrative procedures of the Company’s independent registered public accounting firm", 6-K
0001493152-26-043266). Auditor WWC, P.C., since 2024. No adjusted figure or guidance featured was found.

**Q5 (integrity facts, recorded, not judged).**
1. **IPO money lent out.** Net IPO proceeds were estimated at about US$4,952,000 (424B4, Use of Proceeds: 30% acquisitions,
   10% materials, 10% workforce, 15% a bigger head office, 10% a dormitory, 5% systems, the balance working capital). The IPO
   closed on 2025-08-13 (20-F 2026, Corporate History). Loans of US$1,400,000 "unsecured", at 8%, "maturing on August 13, 2026"
   and extended to 2027-08-13, were made to two third parties who are not named (20-F 2026, note 8; cash flow, S$1,783,320 in
   FY2026). Lending is not among the stated uses. Item 14 of the 20-F, which carries the use-of-proceeds report, reads "None."
2. **Dividends to the controlling shareholder ahead of the IPO.** S$450,000 paid in FY2024; in FY2025 Herlin declared
   S$200,000, S$300,000 and S$1,100,000 to Mr. Lim, S$1.6M against FY2025 profit of S$42,980; S$600,000 is still payable and
   "the Company does not expect to repay it in the next 12 months" (20-F 2026, Item 5, Liquidity). Equity fell from S$1.95M to
   S$0.60M in the year before the IPO.
3. **The pre-IPO shareholders.** On 2024-12-27 five entities (Beyond Merchant Limited, KeyStone Builders Group Limited,
   Kingkey Holdings (International) Limited, Canningale Investments Limited, SwiftBuild Solutions Group Limited) subscribed
   for 23.7% of the company for US$9,000 to US$9,800 each; in January and February 2025 Mr. Lim's nominee transferred 2.7%,
   3.0% and 3.4% to three individuals described as "independent third party", two "at par value" and one for US$18,000
   (20-F 2026, Corporate History). Mr. Lim now holds 62.46% (Item 7).
4. **The stock and the regulators.** The shares rose from US$1.37 (2025-11-11) to US$6.76 (2025-12-04) (aggregator); the SEC
   suspended trading from 2025-12-05 to 2025-12-18; Nasdaq halted the shares on 2025-12-19 and on 2026-08-03 determined to
   delist them under IM-5101-4, "based on the potential for one or more third parties to engage in misconduct impacting a
   company’s securities"; the company has appealed, and states that it "has no knowledge of and is not connected to any alleged
   price manipulation activity" and that Nasdaq "has not communicated any finding or determination that the Company engaged in
   any wrongdoing" (6-Ks 0001493152-25-027002 and 0001493152-26-036115).
5. **Who signs.** Every bid price is signed off by the CEO; the bank debt rests on his personal guarantee (Item 4; Item 5).

**Q6 (money and owners).** Dividends above earnings before the IPO (item 2); IPO money lent to third parties (item 1); 30% of
the proceeds earmarked for acquisitions (424B4). No buyback.

**Q9 (debt and exposures).** Bank borrowings S$1.48M at 2.75% to 7.75%, repayable in 1 to 9 years, secured by the CEO's
personal guarantee and the keyman policy; lease liabilities S$0.55M; performance bonds backed by cash or guarantees; S$600,000
dividend payable to the CEO; the shares untradeable while halted and facing delisting.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit a8e969b5); written question by question; Step 0 to Q1 committed
      (624eab22). **Q2 and everything after it were NOT committed by me:** an `index.lock` (created 11:27) held the repository,
      and this environment ends any command that sleeps, so I could not wait between retries. I did not delete the lock. The
      dispatching session commits the two paths, as the brief provides.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatcher's; the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched; what was seen by accident (file names of
      other companies' runs today, commit subjects of the MAGN run, research-folder names) is declared under contamination.
- [x] Every v5 id resolves (`check_run.py` in the research folder: ids exist, quoted fragments beside ids found in their rows,
      no E-ids); every filing fact carries its accession.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance.
- [x] Owner cash from the filed cash-flow statements, never a net-income proxy; the SGD sovereign from MAS, dated; the price
      from an aggregator, flagged and stale.
- [x] Contrary evidence written as found (foundations paragraph); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No point-in-time anchor; not applicable.
- [x] `tools/run.py` produced nothing; no line of it was used.
- [x] `python tools/check_framework.py` run before the end (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q7's range convention assumes five years; a company private until 2025 files four, and the text does not say whether a
four-year window is the window or a TOO HARD (WORK) on the base; I used the four years as the literal window and said so.
(2) Specific (b) sends a series that changes sign to the no-growth case; where that case is negative, the "range" is a single
negative number and the fair price is negative, and the text does not say how a negative value is reported or alerted; I
reported it as negative. (3) The canonical template's Step 0 asks for eight to ten years of balance sheets when the file closes
before Q4; the record holds four, and the template gives no instruction for the shortfall. (4) The protocol's sovereign table
has no SGD row; I took the longest SGS benchmark from MAS. (5) The brief describes the company as a British Virgin Islands
holding company; the 20-F says the Cayman Islands (the BVI company is the intermediate, Elec Power Ltd). (6) Q2's commodity
paragraph is written for dependence on a commodity price and routes an unread cost position to TOO HARD; a commodity *service*
sold by tender is not clearly covered by it. I closed OUT on the "ordinary returns" and "low bid" items of Q2's OUT list rather
than on the cost position, and say so. (7) The price question: a halted, untradeable last quote is still "the price" for the
floor test; the text does not address a market that does not exist.
