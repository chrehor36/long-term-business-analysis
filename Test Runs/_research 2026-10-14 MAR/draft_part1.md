**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md` with the brief's one stated departure: the
lines of evidence and the competitors were chosen by the analyst from the latest 10-K's Item 1, Item 1A and Item 7, and are
named below with the reason for each choice.

**Lines of evidence chosen from the 10-K for FY2025** (accession 0001048286-26-000007, filed 2026-02-10), and why:
1. **The fee stream and its sources** (Item 1, "Franchised, Licensed, and Other Properties", "Company-Operated
   Properties"; Item 7, "Fee Revenues"): franchise royalties "typically range from four to seven percent of room revenues",
   base and incentive management fees, and co-branded credit card fees. This is what the castle protects; Q1, Q2, Q3.
2. **Marriott Bonvoy and the co-brand cards** (Item 1, "Loyalty and Credit Card Programs"; Item 1A, the Loyalty Program
   risk): "approximately 75 percent of our U.S. hotel room nights and approximately 68 percent of our global hotel room
   nights were booked by Loyalty Program members". The filer's own candidate for the moat; Q2.
3. **The competition for hotel owners and what it costs** (Item 1, "Competition"; Item 1A, "Our growth strategy depends upon
   attracting hotel owners..." and "Premature termination of our agreements..."; Item 7, contract acquisition costs and
   contract investment amortization). The place to hunt for the castle being paid for rather than owned; Q2, Q3.
4. **Intermediaries and alternative lodging** (Item 1, "Competition", naming Airbnb, Vrbo, Expedia.com, Booking.com and
   others; Item 1A, "Changes in the way hotel rooms are booked..." and the AI risk). What could destroy or reduce the
   castle; Q2 test 11.
5. **The cycle** (Item 1A, economic conditions; Item 7, RevPAR tables; the 2020 and 2021 10-Ks). Sets the cycle base at
   Q7 and tests the castle in a downturn.
6. **The balance sheet and the returns to owners** (Item 7, "Liquidity and Capital Resources", debt, share repurchases and
   dividends; Item 5). Debt-funded buybacks and a stockholders' deficit; Q4, Q6, Q9.
7. **The Starwood Data Security Incident** (Item 1A; Note 7). The one matter in the filing that bears on the people; Q5.

**Competitors.** The 10-K names "Hilton, IHG Hotels & Resorts, Hyatt, Wyndham Hotels & Resorts, Accor, Choice Hotels, Best
Western Hotels & Resorts, and others", and Airbnb, Vrbo and the online travel platforms. The first three named that file
with the SEC are used: **Hilton** (10-K), **IHG** (Form 20-F) and **Hyatt** (10-K). Named rivals that do not file with the SEC:
**Accor** and **Best Western** (flagged). Wyndham and Choice file but are fourth and sixth in the 10-K's order and are not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $371.50 (close 2026-10-13; aggregator quote printed by `tools/run.py`, flagged per operator rule 5; live quote
  only).
- **Shares by class** from the latest filing's cover: Class A Common Stock 260,766,288 (10-Q for the quarter ended
  2026-06-30, cover as of 2026-07-27, accession 0001048286-26-000035; `python Screens/cover_shares.py MAR`). One class; no
  preferred outstanding (10-K Note on stockholders' equity: "no preferred stock outstanding"). **Check against issued less
  treasury:** 265,864,771 outstanding at 2025-12-31 (10-K); 264,984,554 at 2026-01-31 (10-K Item 5); the 10-Q states
  repurchases of 6.2 million shares year-to-date through 2026-07-29, which with share issuance under the stock plans
  reconciles to the cover count. No 8-K after the 10-Q changes the count (the 8-Ks of 2026-08-13 and 2026-09-24 are a note
  issue and the revolver amendment).
- **Market cap:** $96,875M (260.766M x $371.50).
- **Sovereign for the earnings currency (USD):** 5.56%, US Treasury daily par yield curve, 30-year, 10/13/2026 (`python
  tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-10, 0001048286-26-000007): Items 1, 1A, 1C, 2, 3, 5, 7,
  7A, the statements and Notes 3, 7 and 9; 10-Ks FY2019 (0001628280-20-002376), FY2020 (0001628280-21-002433), FY2021
  (0001628280-22-002666), FY2022 (0001628280-23-003485), FY2023 (0001628280-24-004372), FY2024 (0001628280-25-004818) for
  the cash-flow statements, the MD&A cash and capital-spending paragraphs and the acquisition notes; 10-Q Q2 2026 (filed
  2026-08-03, 0001048286-26-000035): statements, debt note, Item 2 repurchases; proxy DEF 14A filed 2026-03-27
  (0001140361-26-011590): CD&A, Summary Compensation Table, director pay, beneficial ownership; 8-K 2026-08-03
  (0001048286-26-000033, exhibit 99 earnings release); 8-K 2026-09-24 (0001193125-26-401051, revolver amendment).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $3,212M in the
  filed Consolidated Statement of Cash Flows (10-K page 38) against $3,212M in the tagged data printed by `tools/run.py`.
  Agrees.
- `python tools/run.py MAR`, arithmetic lines only (Part VII): OCF 3,170 / 2,749 / 3,212, SBC 205 / 237 / 236, capital and
  technology expenditures 452 / 750 / 604 for 2023 / 2024 / 2025, all agreeing with the filed statements. **Two printed
  lines rejected:** (1) the "capex alt" column doubles 2023 and 2024 because the filer's single line "Capital and technology
  expenditures" carries the tag PaymentsToAcquireProductiveAssets, which the tool read as a second payment; the filed
  statement has one line; (2) the tool's D&A column (348 / 383 / 458) is not the filed line, which is 436 / 492 / 599
  "including depreciation and amortization classified in reimbursed expenses". The tool's three-year and five-year owner
  earnings means are not used; owner cash is built below from the filed statements (Q4, Q7).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and for a hotel franchisor that turns on the fee stream ten years out, not on the quotation. The market serves
and does not instruct: "It just tells us prices." **[M2006-077]**; the price has roughly doubled the cash yield it offered
at no time in the window read, and that is a fact about the price, not the business. Margin of safety: if the decision
needs pencil and paper, "it’s too close to think about" **[M1996-084]**. Who is paid to tell you: the filer's own releases
feature "Adjusted EBITDA" and guidance, and its pay plans run on them (Q4, Q5, Q6); "you do not get impartial advice from
Wall Street" **[M2020-037]** applies to the issuer's own presentation as well. The analyst's habits: look "for what’s wrong in
things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) contract acquisition costs paid to
hotel owners rose from $195M (2019) to $434M (2025) in operating cash flow, and the contract investment amortization netted
out of fee revenue rose from $62M to $135M (10-K FY2019 and FY2025 statements): the company is paying more to win and keep
owners; (2) Hilton's system grew 5.65% a year from 2019 to 2025 against Marriott's 4.32% (rivals' 10-Ks); (3) stockholders'
deficit of $(3,771)M at 2025-12-31 and $(4,525)M at 2026-06-30, debt up from $8,506M (2016) to $16,915M (2026-06-30), the
buybacks financed in part by borrowing; (4) in 2020 operating income fell to $84M (10-K FY2022); (5) the price, $371.50, is
far above any value the filed cash supports at the long government rate (Q7).

## THE STANDING RULE
The buyer's conduct, not the target's: the rule forbids buying with borrowed money or so sized that a fall forces a sale,
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has
no place in the investor's tool kit" **[L2014-005]**. Nothing in this name requires the buyer to break it; the target's own
debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular business,
  and evaluating how predictable they were first" **[M1998-044]**.
- **What the business is, from Item 1.** A fee collector on other people's hotels: it owns or leases "less than one percent
  of our system"; 9,805 properties and 1,779,936 rooms at year-end 2025; 7,644 franchised, licensed and other properties and
  2,017 company-operated; franchise royalties "typically range from four to seven percent of room revenues"; management
  agreements "generally for initial periods of 20 to 30 years"; franchise terms "generally for periods of 10 to 25 years".
  Gross fee revenues $5,438M in 2025: franchise fees $3,325M (which include co-branded credit card fees), base management
  fees $1,322M, incentive management fees $791M. Cost reimbursement revenue of $19,204M is a pass-through, "not designed to
  impact our economics, either positively or negatively" (Item 7).
- **The key variables, and whether they are foreseeable.** (1) Rooms in the system: 1,380,921 at year-end 2019 (10-K FY2020)
  to 1,779,936 at year-end 2025, 4.32% a year, with a pipeline of nearly 610,000 rooms, 43% under construction (Item 7); the
  filer guides 4.5 to 5.0 percent net rooms growth for 2026. (2) RevPAR, cyclical: worldwide systemwide RevPAR rose 2.0% in
  2025; in 2020 the whole fee base fell from $3,823M (2019) to $1,683M, and recovered to $4,078M by 2022 (10-K FY2022).
  (3) The fee rate on room revenue, set by contracts of 10 to 30 years. (4) What owners must be paid to sign: contract
  acquisition costs. (5) Credit card and other brand fees. The first and third are contractual and slow; the second is the
  business cycle, which the speakers do not forecast and which averages out over a cycle; the fourth and fifth are the open
  questions and are Q2's. "do I understand enough about this business so that the financial statements will tell me the
  information that’s useful" **[M2008-033]**: yes, the statements separate fees, pass-through reimbursements, owned hotels and
  the loyalty liability.
- **Is the forecast about customers or about technology?** About travellers and hotel owners, the kind of forecast "in terms
  of consumer behavior and threats to a business" **[M2023-030]**, **[M2017-019]**. Technology enters as a threat to the
  distribution (online intermediaries, search, AI, Item 1A), which is a castle question (Q2, test 11), not a change in what
  the business sells. Would the insiders write it down **[M2000-105]**? They do: the filer publishes a net rooms growth
  expectation and a pipeline, and its rivals do the same in their own filings.
- **The doubt test.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
  doubt that exists is about the price paid to owners and the intermediaries, not about whether the economics can be pictured:
  ten years out the business is still a share of room revenue across a system larger than today's, in a downturn smaller for a
  year or two. That is a castle question, sent to Q2 by the routing.
- **Routing.** Not a bank or derivatives book (the notes receivable are $151M at 2025-12-31). Not a holding company. The
  four reportable segments are read at Q2 as parts.
- **VERDICT: IN.** The ten-year economics can be pictured from the filings: a contractual fee stream on a slowly growing
  system, cyclical in RevPAR **[M2012-065]**, **[M2000-037]**, **[M1998-044]**.
