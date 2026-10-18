# Company Run — Marriott International, Inc. (Nasdaq: MAR) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for MAR or Marriott).

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
A share is a business: the question is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and for a hotel franchisor that turns on the fee stream ten years out, not on the quotation. The market serves
and does not instruct: "It just tells us prices." **[M2006-077]**; the quotation of $371.50 says what the market asks and nothing
about what the fee stream will be. Margin of safety: if the decision
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

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**; a moat is what "protects excellent returns on invested
capital" **[L2007-004]**.

**The parts table** (section B; segment profit as filed, five years 2021 to 2025; 10-Ks FY2022, FY2023, FY2025; the
filer reported U.S. & Canada and International until FY2023 and four segments after):

| part | segment profit 2021-2025, $M | share | castle | decides |
|---|---|---|---|---|
| U.S. & Canada | 1,394 + 2,446 + 2,724 + 2,640 + 2,679 = 11,883 | 74% | standing (below) | **yes**, more than half |
| International (EMEA, Greater China, APEC; CALA in unallocated from 2023) | 258 + 794 + 1,121 + 978 + 1,011 = 4,162 | 26% | standing, thinner in Greater China | no |

The parts sell the same thing, a brand, a reservation and loyalty system and a management service, under the same brands,
so the castle is read once and checked against the deciding part: "lumping them together [...] impedes analysis"
**[L2008-005]** applies to different economics, and here the economics differ in degree (Greater China RevPAR $76.53
against $132.35 in U.S. & Canada, 2025 systemwide), not in kind.

**The castle tests, each with its filing fact.**
1. **What keeps it standing, and how permanent?** The filer names it: Marriott Bonvoy, "approximately 75 percent of our U.S.
   hotel room nights and approximately 68 percent of our global hotel room nights were booked by Loyalty Program members"
   (Item 1); more than 295 million members at 2026-06-30 (8-K 2026-08-03, exhibit 99); co-branded cards in 11 countries with
   JPMorgan Chase and American Express in the U.S. (Item 1), newly re-signed on long-term terms in 2026 (same exhibit). The
   owner joins because the members book; the members join because the hotels are everywhere: 17 percent of U.S. hotel rooms
   and four percent outside the U.S. (Item 1). It is a scale advantage of the kind Munger names, "advantages of scale"
   **[M1995-039]**, and it is a reason the customer comes that does not change with fashion.
2. **Would it stand without the lord?** Yes. The system ran through the death of its chief executive in 2021 and a change of
   leadership with no visible break in rooms growth (rooms 1,423,044 at year-end 2020, 10-K FY2020, to 1,779,936 at year-end
   2025). "If you have a big enough moat, you don’t need as much management." **[M1999-106]**.
3. **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
   it?" **[M2011-015]**. To rebuild 1.78 million rooms of contracts running 10 to 30 years and a membership of 295 million
   would take decades, not money alone. But the test also shows the castle is shared: Hilton (1,351,351 rooms at year-end
   2025, its 10-K FY2025, 0001585689-26-000007) and IHG (1,026,177 rooms, its 20-F FY2025, 0000858446-26-000010) have built
   the same kind of castle, and "one competitor is frequently enough to ruin a business" **[M2012-108]** is tested against the
   returns, below: the rivals have not ruined each other.
4. **Pricing power and the agony before a rise.** "it’s not a great business when you have to have a prayer session before
   you raise your prices a penny" **[M2005-020]**. With the traveller the price is the hotel owner's, not Marriott's. With the
   owner, Marriott's price is the royalty, "typically range from four to seven percent of room revenues" (Item 1), and that
   rate is not where the agony shows. It shows in what Marriott must pay to sign: contract acquisition costs in operating cash
   flow of $210M (2021), $149M (2022), $221M (2023), $341M (2024), $434M (2025) against gross rooms added of 86,372, 65,376,
   81,281, 123,389 and 99,459 (10-Ks FY2021 to FY2025): about $2,400, $2,300, $2,700, $2,800 and $4,400 a room added. The
   intangible "Contract acquisition costs and other" rose from $2,687M (2019) to $4,129M (2025); the amortization netted from
   fees rose from $62M (2019) to $135M (2025). Item 1A says it plainly: the terms with owners "may be less favorable to us,
   depending on the terms offered by our competitors", and incentive fees are earned at only 32 percent of U.S. & Canada
   managed hotels (Item 7). This is the evidence against: the price of growth is rising.
5. **Unit volume and share of mind.** Rooms grew 4.32% a year 2019 to 2025; the pipeline is nearly 610,000 rooms; deletions
   were 25,643 rooms in 2025 against 1.71 million at the start of the year, about 1.5 percent (Item 7). Members booking direct
   is share of mind in the rows' sense, "It’s share of mind." **[M1997-099]**.
6. **The low-cost position.** For the owner, what Marriott sells is cheaper demand: a loyalty-sourced booking against an
   online-agency commission. The filings do not give the cost comparison; recorded as not measured.
7. **The brand in the customer's mind, and the intermediary.** "the brand has to stand for something in the consumer’s mind"
   **[M2015-038]**; the danger is the one the rows name for retailers, that "the value of having the brand moves over to the
   retailer from the product itself" **[M2001-090]**. Here the intermediaries are Expedia, Booking and the search engines,
   which buy "trademarked online keywords such as “Marriott”" (Item 1A). The loyalty programme is the brand's answer: "the brand
   is our protection against the intermediaries making all the money." **[M2019-041]**. The 68 percent of room nights booked
   by members says the answer is working today.
8. **Would the customer still choose it over the low bid?** Partly. Business and luxury travellers pick by brand and points;
   the select-service traveller often picks by price and location, and the filer says select-service demand was "softer" in
   2025 (Item 7). The owner, the other customer, has a real alternative in Hilton, IHG, Hyatt and the independents.
9. **Ask the competitors.** The 10-K names Hilton first among the chains; Hilton's own record is the strongest rival fact
   (the competitor row below). The rows' silver-bullet question **[M2017-022]** would likely be aimed at Marriott by the others,
   as the largest system; that says where the threat is, not that the castle fails.
10. **Widening or narrowing?** "how wide the moat is and whether it’s likely to widen further or shrink on you" **[M1999-108]**.
    For: fee revenue up from $3,823M (2019) to $5,438M (2025), members up, U.S. market share 17 percent. Against: Hilton's
    rooms grew faster (5.65% against 4.32% a year), and the cost of a room added nearly doubled from 2023 to 2025. Read
    together: the castle is holding its width, and the toll to the owner side is rising.
11. **What could destroy, modify or reduce it, five to fifteen years out?** "destroy, or modify, or reduce the economic
    strengths" **[M2000-014]**. Named by the filer: online intermediaries and search; short-term rentals (Airbnb, Vrbo); AI
    ("if we fail to keep pace with rapidly-evolving technological developments in AI and other emerging technologies, our
    competitive position and business may suffer", Item 1A); owner terminations; data security. None of these was able to
    stop rooms or fees growing through 2019 to 2025. The 2020 test was harder than any of them: fees fell 56% and the system
    kept growing (1,380,921 to 1,423,044 rooms in 2020, 10-K FY2020).

**The competitor row** (each filer's own XBRL, 10-K or 20-F, as filed; owner cash simple = operating cash flow less stock pay
less capital spending less software or intangibles purchased, no acquisition adjustments; scripts `peers.py`):

| metric | Marriott | Hilton | IHG | Hyatt |
|---|---|---|---|---|
| rooms, year-end 2019 to 2025 | 1,380,921 to 1,779,936 (4.32%/yr) | 971,780 to 1,351,351 (5.65%/yr) | 883,563 to 1,026,177 (2.53%/yr) | 372,763 at 2025 (2019 not read) |
| owner cash, avg 2017-19 to avg 2023-25, $M | 1,423 to 2,216 (7.7%/yr) | 863 to 1,648 (11.4%/yr) | 443 to 719 (8.4%/yr) | 88 to 337 (owner of hotels; not comparable) |
| operating income, avg 2017-19 to avg 2023-25, $M | 2,223 to 3,924 (9.9%/yr) | 1,407 to 2,429 (9.5%/yr) | 652 to 1,102 (9.1%/yr) | pre-tax plus interest 970 to 865 |
| operating income / tangible assets (the rows' measure **[M2011-060]**), 2019 and 2025 | 24% (36% before the 2019 reimbursement shortfall of $840M) and 50% | 40% and 43% | on total assets, intangibles not tagged: 15% and 22% | on total assets: 13% and 3% |

Accessions: Hilton 10-K FY2025 0001585689-26-000007 and FY2019 0001585689-20-000013; IHG 20-F FY2025 0000858446-26-000010
and FY2019 0001193125-20-052322; Hyatt 10-K FY2025 0001468174-26-000007. IHG's 2025 purchase of intangibles is not tagged; the
20-F text's $43M of System Fund capital investments is used in its place (flagged). The span is 2017 to 2025, the whole of
both halves of the cycle, never one year.

**The field's returns over the last full cycle.** The three asset-light franchisors earn very high returns on the tangible
capital they need, Marriott 50% and Hilton 43% pre-tax in 2025 on operating income over tangible assets, and grew operating
income about 9 to 10 percent a year across the cycle. That is not an ordinary return; the castle protects "excellent returns"
**[L2007-004]**. The rows' warning that "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**
does not describe this field on its own filings. Hyatt, which still owns hotels, earns far less, which is the evidence that
the return sits in the fee model, not in hotels.

**What the evidence against amounts to.** The castle is shared with Hilton and IHG, Hilton is growing faster, and the toll
paid to owners is rising. That is a castle under the assault the 2007 letter predicts, "competitors will repeatedly assault" it **[L2007-004]**, not one shown
to be filling in: rooms, members, fees and returns all rose over the cycle. It is carried to Q3 (what the added capital earns)
and to Q7 (the growth input).

- **VERDICT: IN.** The deciding part, U.S. & Canada (74% of five-year segment profit), and the whole system stand on a
  loyalty-and-scale castle that has protected excellent returns through a full cycle including 2020 **[M1995-038]**,
  **[L2007-004]**, **[M1999-108]**; the rising cost of signing owners is recorded against it and weighed at Q3 and Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** The rows' measure is "return on tangible assets" **[M2011-060]**, on "the capital
  actually needed in the business" **[M2010-090]**. 2025: operating income $4,141M against tangible assets of $8,297M (total
  assets $27,540M less goodwill $8,907M less intangibles $10,336M, 10-K FY2025 balance sheet): about 50% pre-tax. Counting the
  capitalised payments to owners ("Contract acquisition costs and other", $4,129M) as capital, since they are cash paid to buy
  contracts: $4,141M against $12,426M, about 33%. Against all the capital the owners and lenders have in it, net debt plus
  equity ($16,204M debt less $358M cash plus a $(3,771)M deficit = $12,075M): about 34%. These are "very high returns on
  capital employed over time" **[M1995-047]**, on any of the three bases.
- **Not credited: return on equity.** Equity is negative because the company has bought back more than it earned; "if you
  keep the equity low enough by buying shares back, why, you could make return on equity whatever you want" **[M1998-017]**.
  No return-on-equity figure is used here.
- **Reinvestment to stand still and to grow.** The filer's own guesses at maintenance capital spending: about $200M for 2020
  (10-K FY2019), $220M for 2021 (10-K FY2020), $250M for 2022 (10-K FY2021), $300M for 2023 (10-K FY2022), $250M for 2024
  (10-K FY2023); the FY2024 and FY2025 10-Ks give none. The rows ask for exactly this guess and the spending "beyond that
  maintenance cost" **[M2000-144]**, **[L1999-024]**. Capital and technology spending, acquisitions taken out, averaged $368M
  a year over 2019 to 2025 (`calc.py`), and the filer says the technology part is mostly "expected to be reimbursed over time"
  by owners (10-K FY2025 Item 7). Growth is bought mainly with contract acquisition costs, $1,844M over 2018 to 2025, which
  sit inside operating cash flow.
- **What the added capital earned.** Operating income averaged $2,223M over 2017 to 2019 and $3,924M over 2023 to 2025, up
  $1,701M. Capital put in over 2018 to 2025: capital and technology spending less acquisitions $2,876M, contract acquisition
  costs $1,844M, and acquisitions net of hotel sales $323M ($1,566M of purchases including the Sheraton Phoenix, W Union
  Square, Elegant, City Express, Sheraton Grand Chicago and citizenM, less $1,243M of dispositions): $5,043M gross, before
  depreciation of $3,269M. The added operating income is about 34% of the gross sum put in. "whether that’s good or bad
  depends on what we earn on that incremental $130 million over time" **[M2001-019]**: here it earned well. The grade is the
  rows' best business or close to it, one that "gives you more and more money every year without putting up anything to get
  it, or very little" **[M1998-081]**.
- **The caution the rows require before crediting a high return.** Rule out "a cyclical peak in earnings, a monopolistic
  position, or leverage" **[L1994-009]**. Leverage: the operating return above is before interest and is not leverage-made.
  Cyclical peak: 2025 RevPAR is not at an obvious peak (worldwide up 2.0%), but 2023 to 2025 follow the 2020 to 2021 trough,
  and the five-year window is read on the cycle at Q7. The rising price of signing owners (Q2, test 4) is the trend that would
  lower the incremental return, and it is carried to Q7.
- **The growth arithmetic and its caps.** Fee revenue grew 6.2% a year between the 2017 to 2019 and 2023 to 2025 averages
  and owner cash 7.6% (Q7); both are below the rates the rows call absurd only when carried forever, and Q7 carries nothing
  above the discount rate past year ten.
- **WEIGHS FOR.** The business needs little tangible capital and has earned roughly a third or more pre-tax on what was put
  in over the cycle **[M1995-047]**, **[M2011-060]**, **[M1998-081]**; the rising cost of each room signed is the weight on
  the other side. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (the ten-year table printed by
  `tools/run.py`, read against the filed balance sheets of the 10-Ks listed in Step 0; $M):

  | year-end | assets | goodwill | intangibles | cash | debt (current + long-term, incl. finance leases) | equity | retained earnings |
  |---|---|---|---|---|---|---|---|
  | 2016 | 24,140 | 7,598 | 9,270 | 858 | 8,506 | 5,357 | 6,501 |
  | 2017 | 23,948 | 9,207 | 8,805 | 383 | 8,238 | 3,731 | 7,391 |
  | 2018 | 23,696 | 9,039 | 8,380 | 316 | 9,347 | 2,225 | 8,982 |
  | 2019 | 25,051 | 9,048 | 8,641 | 225 | 10,940 | 703 | 9,644 |
  | 2020 | 24,701 | 9,175 | 8,989 | 877 | 10,376 | 430 | 9,206 |
  | 2021 | 25,553 | 9,073 | 8,926 | 1,393 | 10,138 | 1,414 | 10,305 |
  | 2022 | 24,815 | 8,872 | 8,747 | 507 | 10,064 | 568 | 12,342 |
  | 2023 | 25,674 | 8,886 | 9,190 | 338 | 11,873 | (682) | 14,838 |
  | 2024 | 26,182 | 8,731 | 9,488 | 396 | 14,447 | (2,992) | 16,531 |
  | 2025 | 27,540 | 8,907 | 10,336 | 358 | 16,204 | (3,771) | 18,414 |
  | 2026-06-30 (10-Q) | 28,085 | 8,876 | 10,465 | 462 | 16,915 | (4,525) | 19,458 |

  **What moved, and why.** (1) Equity fell from $5,357M to a $(3,771)M deficit while retained earnings rose by $11.9B:
  treasury stock grew from $(6,460)M at 2016-12-31 (as restated in the 10-K FY2019 equity statement) to $(27,900)M at
  2025-12-31, about $21.4B of repurchases in nine years against cumulative net income of $15.9B (sum of the filed net income
  lines 2017 to 2025) and dividends of about $4.1B; the difference was borrowed (debt up $7.7B) or came from the hotel sales of
  2017 to 2019 ($2.3B of dispositions). (2) Goodwill and brands are the Starwood merger of 2016 and have not moved; no
  impairment, and the 10-K says fair values "significantly exceeded" carrying amounts. (3) The intangible that does move is
  "Contract acquisition costs and other": $2,687M (2019) to $4,129M (2025) to $4,283M (2026-06-30), the capitalised cash paid to
  owners (Q2, test 4). (4) Cash is kept near zero; the company runs on its commercial paper and revolver (current ratio 0.4,
  Item 7). (5) Receivables, $2,909M at 2025-12-31, moved with fees and reimbursements ($1,695M in 2016; gross fees and
  reimbursement revenue both higher), no sign of a build-up out of line with sales. (6) The loyalty liability grew from $4,541M
  (2016) to $7,992M (2025): cash received from card issuers and owners before the stays are given, a float that grows with the
  system. "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**: they cannot say what
  the loyalty liability will cost to settle (the breakage estimate; a one-point change is about $50M, Item 7), and they do not
  say, after 2024, what maintenance spending is.
- **The real costs.** Stock pay ($236M in 2025) is deducted in owner cash; "Stock-based compensation" is "the most egregious
  example" of a real cost waved away **[L2015-003]**, and the speakers' earnings are "a figure calculated after interest, taxes,
  depreciation, amortization and all forms of compensation" **[L2021-003]**. Capital and technology spending ($604M in 2025) is
  deducted in full in the all-spending case. Contract acquisition costs are already inside operating cash flow. Restructuring
  and merger charges recur in small amounts every year (2019 $138M, 2020 $267M, 2024 $77M, 2025 a $2M recovery); they are left
  in the cash figures, not added back. The 2024 cash payment of $300M under a guarantee, which the filer ties to the purchase
  of the Sheraton Grand Chicago, is moved to acquisitions (Q7), as the filer itself describes it.
- **EBITDA in the filer's own mouth.** The earnings release of 2026-08-03 leads with "Adjusted EBITDA totaled $1,592 million",
  "Adjusted diluted EPS" and "Adjusted net income" beside the GAAP figures, and gives a full-year outlook (8-K
  0001048286-26-000033, exhibit 99). The adjusted figures leave out cost reimbursements net and restructuring and impairment
  charges. "The one figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**; "a management that regularly
  attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**;
  guidance is the "scourge of earnings "guidance"" **[L2019-006]**. Under the framework's Q4 paragraph of 2026-10-06 these are
  recorded here as a WEIGHING against and carried to Q5; the accounts themselves present GAAP first and reconcile every
  adjusted figure.
- **What the accounts say of character.** No prepaid or deferred accounts building out of line (prepaid $317M against $294M),
  no reserves moving to make a number, no restatement (the 10-K cover's restatement boxes are unchecked). The large tax swings
  are explained in the filing: 2023's provision of $295M on $3,378M pre-tax was lowered by $228M from an intellectual-property
  restructuring, a $223M valuation-allowance release and a $103M reserve release (10-K FY2023 Item 7); owner cash is built
  from operating cash flow, which carries cash taxes, so the swing does not enter Q7. The pass-through revenue of $19.2B is
  disclosed with its expense line and net; it is large but not confusing. "we can’t afford to use it as a total exclusionary
  factor" **[M1994-018]** describes the adjusted-figure habit; nothing here meets "when the accounting confuses you"
  **[M1995-063]**.
- **The recast earnings for Q7.** Owner cash = operating cash flow less stock pay less capital and technology spending (the
  acquisitions inside it taken out) less net loan advances plus other investing, before acquisitions and dispositions; on the
  all-equity basis the after-tax net interest is added back (Q7, `calc.py`).
- **VERDICT on the accounts: IN** (no confusion, no suspicion raised by the statements) **[M1995-063]**, **[M2025-032]**;
  **WEIGHS AGAINST** on the featured Adjusted EBITDA and the guidance, carried to Q5 **[M1998-086]**, **[L2016-006]**,
  **[L2019-006]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people.** President and CEO Anthony G. Capuano (CEO since 2021; total pay in the Summary Compensation Table $22,970,926
  for 2025 and $21,934,093 for 2024). Chairman David S. Marriott, son of the Chairman Emeritus, a non-executive chairman paid
  a cash fee of $2,250,000 (raised from $2,000,000 in 2025). Lead Independent Director Frederick A. Henderson since 2022. The
  founding family (J.W. Marriott, Jr., Deborah M. Harrison, David S. Marriott) beneficially owns 13.22% after removing double
  counting, 17.57% with the family's other holders (proxy, DEF 14A 0001140361-26-011590).
- **The two yardsticks.** "how well they run the business" and how well "they treat their owners" **[M1994-008]**. Running the
  business: the system grew through the 2020 shock and after (rooms 1,380,921 at year-end 2019 to 1,779,936 at year-end 2025),
  operating income across the cycle grew about as fast as Hilton's and IHG's (Q2, competitor row), and the hand dealt
  includes a merger (Starwood) whose reservation database brought the 2018 breach with it. Treating the owners: the proxy
  test, "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**, is run at Q6, Part B.
- **The tells of dishonesty, searched for in the filings read.**
  - *Reports that dance:* none found. The 10-K's discussion is plain; adverse facts (select-service softness, Greater China,
    the Sonder termination charge, the Data Security Incident) are stated in Item 7 and Note 7.
  - *The Data Security Incident:* unauthorised access to the Starwood reservations database, disclosed in November 2018;
    about 100 lawsuits; final resolutions with the FTC and the attorneys general of 49 states and the District of Columbia in
    2024 including a $52 million payment and "various long-term requirements relating to our data privacy and information
    security programs" (10-K FY2024 Note 7; 10-K FY2025 Item 1C); the UK ICO fine was "reduced to £18.4 million in October
    2020" (10-K FY2021 Item 7). The filings show a failure of security in an acquired system and a resolution reached; they
    show no finding of concealment or false statement. The rows' test of conduct after bad news, "the main problem was they
    didn’t act when they learned about it" **[M2017-005]**, is not met by anything in the filings read.
  - *Related persons:* family entities hold interests in 18 hotels Marriott manages, and two family members' entities in 13
    Marriott-branded hotels; the company also employs family members; all disclosed under a written policy with audit-committee
    approval of categories (proxy, "Transactions with Related Persons"). Recorded as a conflict to watch, not a tell.
  - *The habits carried from Q4:* annual guidance, Adjusted EBITDA and adjusted EPS featured in the releases, and pay that runs
    on Adjusted EBITDA (Q6). The rows read these as "things that they do in public in relation to their investors and the
    promises they make" **[M2004-067]**. The 2023-2025 PSUs paid at 200% of target on 2025 Adjusted EBITDA "above maximum"
    (proxy CD&A): a target beaten, set by a committee, not a reported number made. "we become downright incredulous if they
    consistently reach their declared targets" **[L2002-041]** would bite if the company always met its published outlook; the
    filings read do not show the outlook record, and the habit is weighed, not judged as dishonesty.
- **Love of the business, and after the pay.** A family-founded company whose family still owns 13% and chairs the board
  without an executive title. Buffett proposed the same arrangement for Berkshire, a family member as "non-executive Chairman"
  **[L2014-026]**, as a check on the chief executive. The chief executive's own holding is 269,175 shares (proxy), about
  $100M at the price, against annual pay near $23M.
- **Doubt.** "If you’ve got doubts, forget it." **[M2013-088]**. The doubts I can name are about stewardship (the price paid
  for buybacks, pay on an EBITDA measure, a large non-executive fee, the security failure inherited with Starwood), and they
  are weighed at Q6. I found nothing in the 10-K, the 10-Q, the proxy or the 8-Ks read that is a doubt about honesty.
- **VERDICT on integrity: IN** (no tell of dishonesty in the filings read) **[M1994-008]**, **[M2017-005]**; the Q4 habits
  read and weighed against **[M2004-067]**, **[L2002-041]**. **Ability WEIGHS FOR**: the system and the fee stream grew through
  a full cycle including 2020, at returns matching the best rival **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test.** The company keeps nothing. Over 2017 to 2025 it paid about $4.1B of dividends and bought back about
  $21.4B of stock (net growth of treasury stock) against $15.9B of net income (Q4); debt rose $7.7B. The question the rows ask,
  whether a dollar retained becomes "at least $1 of market value for each $1 retained" **[R1995-009]**, has no retained dollar
  to test. The question that replaces it is the price paid for the stock bought with the earnings and the borrowing.
- **Buybacks.** The rows allow buying with "cash plus sensible borrowing capacity" only when the stock sells "below its
  intrinsic value, conservatively-calculated" **[L1999-023]**; "Continuing shareholders are hurt unless shares are purchased
  below intrinsic value." **[L2011-003]**. The programme is authorised in shares, "no expiration date", with no price named
  (10-K Item 5; 10-Q Item 2), the case **[L2016-002]** describes. Prices paid: 12.1 million shares for $3.3B in 2025, about
  $273 a share (10-K Item 7); fourth quarter 2025 average $284.25 (10-K Item 5); second quarter 2026 average $368.49 (10-Q
  Item 2); 6.2 million shares for $2.2B year-to-date through 2026-07-29, about $355 (10-Q). **The test against the Q7 range,
  run when Q7 was reached (written back here):** the bottom of the Q7 range is $90.30 a share; every price paid in the
  periods read is far above it, so the programme with no stated price weighs against with no exception (the convention under
  Q6, The buyback with no stated price, tested) **[L2016-002]**, **[L1999-023]**.
- **Issuance and deals.** No all-stock acquisition in the window, so the one STOP of Part A **[L2009-019]** does not apply.
  The deals were for cash and small: City Express brand $101M (2023), Sheraton Grand Chicago (about $500M with the guarantee
  settlement, 2024), citizenM $350M (2025), with an earn-out up to $110M (10-K FY2025 Item 7). The Starwood combination of 2016
  lies before the window and is not tested here. Q3 found the capital put in over the cycle earned well.
- **Dividends.** $0.63 then $0.67 a quarter in 2025 (10-K Item 7), "clear, consistent and rational" **[L2012-015]**; no objection.
- **Part A WEIGHS AGAINST**: everything earned and more is spent on the stock at prices far above the bottom of the Q7 range
  **[L2011-003]**, **[M1996-013]**.

**Part B: the pay, the board and the owners** (proxy DEF 14A 0001140361-26-011590).
- **Pay tied to what the person controls?** The annual cash incentive weights "2025 Adjusted EBITDA as the most critical
  financial metric for the Company (weighted 60%)"; the 2025 PSUs pay on "2027 Adjusted EBITDA with a three-year relative
  Total Shareholder Return (TSR) modifier"; the 2023-2025 PSUs settled at 200% of target. The measure leaves out the capital
  the business spends and the interest on the debt that funds the buybacks. "you get what you reward for" **[M2016-083]**:
  a plan on EBITDA rewards EBITDA, which the speakers call "utter nonsense" as a measure of earnings **[M1998-086]**; and a
  measure before interest cannot see the cost of buying stock with borrowed money. The relative TSR modifier ties part of the
  pay to the stock price, which is "totally out of the control of the person whose behavior we would like to affect" **[L1996-018]** only in part, since the modifier is relative.
- **SARs.** The chief executive received $4,125,205 of stock appreciation rights in 2025 (Summary Compensation Table),
  option-like awards at the market price, with no step-up for retained earnings; the rows want the strike no lower than what
  the business would bring if sold **[M2011-067]**.
- **The board.** A family non-executive chairman with a Lead Independent Director; the arrangement the rows themselves
  proposed for Berkshire **[L2014-026]**. The chairman's cash fee of $2,250,000 is large for a non-executive role.
- **Owners as partners.** Anti-hedging and anti-pledging rules for executives, clawbacks, stock-ownership requirements
  (proxy CD&A). The family's 13% stake aligns the board with owners; the related-party hotels (Q5) cut the other way.
- **Part B WEIGHS AGAINST** on the EBITDA-based pay and the SARs **[M2016-083]**, **[M1998-086]**, with the family's ownership
  and the non-executive chair weighing for **[L2014-026]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business" **[R1996-018]**, at the long government rate,
5.56% (Step 0), held as a range: "working with a range of possibilities is the better approach" **[L2000-024]**. The
arithmetic is in `calc.py` (output in `q7_output.txt`), built from the filed cash-flow statements listed in Step 0.

**The cash input (Q4's recast).** Owner cash = operating cash flow less stock pay less capital and technology spending (the
acquisitions inside it removed: Sheraton Phoenix $255M in 2018, W Union Square $206M and Elegant $128M in 2019, Sheraton Grand
Chicago about $200M in 2024) less net loan advances plus other investing; the $300M guarantee settlement of 2024, which the
filer ties to the Chicago purchase, is moved from operating cash to acquisitions. On the all-equity basis (Q7, "On what the
floor is earned") the after-tax net interest is added back, at 24% (CONVENTION of this run: the 2024 and 2025 effective rates,
24.6% and 23.4%, rounded; rationale: the company's own tax, Q7 "Whose tax", and no single statutory rate fits a company taxed
in many countries). Owner cash is after the company's cash taxes, with no conversion. The carryforwards in the tax note ($52M
of credits expiring through 2035; NOLs mostly state and foreign) are too small against $793M of annual tax to price
separately.

| year | OCF | owner cash, after interest | owner cash, all-equity (before interest) | net purchases (acquisitions less hotel sales) | gross fee revenue |
|---|---|---|---|---|---|
| 2017 | 2,227 | 1,839 | 2,029 | (1,418) | 3,295 |
| 2018 | 2,357 | 1,897 | 2,139 | (224) | 3,638 |
| 2019 | 1,685 | 1,153 | 1,433 | (61) | 3,823 |
| 2020 | 1,639 | 1,213 | 1,531 | (260) | 1,683 |
| 2021 | 1,177 | 796 | 1,094 | (12) | 2,694 |
| 2022 | 2,363 | 1,873 | 2,160 | (1) | 4,078 |
| 2023 | 3,170 | 2,530 | 2,937 | 30 | 4,824 |
| 2024 | 2,749 | 2,288 | 2,786 | 510 | 5,170 |
| 2025 | 3,212 | 2,369 | 2,952 | 341 | 5,438 |

**Specific (a), the cycle.** The literal five-year window is 2021 to 2025. Its first year is aberrational on the filer's own
description ("the negative impact COVID-19 had on our cash from operations in 2021 and 2020", 10-K FY2021 Item 7), and the
window also carries the reversal of the $920M card prepayment received in 2020, which "reduced in both 2021 and 2022" the cash
from the card issuers, "until such reductions ended as of year-end 2023" (10-Ks FY2022 and FY2023). The base is therefore the
last full cycle: **2019 to 2025, all-equity owner cash averaging $2,127M** (after interest, $1,746M); the literal window,
$2,386M, is shown beside. **CONVENTION of this run:** the cycle runs from the last pre-trough year (2019) to the latest year
(2025), because no later peak can yet be known and the span takes in both the 2020 prepayment and its reversal; rationale:
spec (a) asks for peak to peak and only one peak is visible. A year being aberrational is the filer's word, as the
specific requires.

**The growth shown.** Spec (a) measures growth between the averages of successive cycles. The earlier cycle cannot be read
on a combined basis, since the Starwood merger closed in 2016. Growth is measured between the three years before the trough
(2017 to 2019, average $1,867M) and the three latest (2023 to 2025, average $2,891M), midpoints six years apart: **7.56% a
year on aggregate owner cash** (not per share, the first PG specific). **CONVENTION of this run** for that substitution;
rationale: the halves either side of the trough are the nearest thing to successive cycles the filings allow. Gross fee
revenue grew 6.20% a year between the same halves. The literal end-year rate 2021 to 2025, 28.2%, is meaningless off a
trough base, "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**,
and is not used.

**Specific (b), decline.** None; growth is positive.

**Specific (c), acquisitions.** Net purchases averaged $78M a year over the cycle and $174M over the literal window; over
2021 to 2025 they were $868M against $11,929M of owner cash before purchases, far below half, so the serial-acquirer rule does
not apply. The default pair is used: purchases deducted in years one to ten with the total growth credited; after year ten
purchases stop with growth, "they get credit for whatever net cash is left every year" **[M1998-080]**. The filer does not report
organic owner-cash growth, so no organic pair is shown. No deal signed and unclosed, and none closed after the window with
earnings to value (the 8-Ks since 2025-06 show note issues, the revolver and officer changes only).

**Specific (d), working capital.** Counted: it is inside operating cash flow, including the growth of the loyalty liability,
a float that rises with the system (the line "Liability for guest loyalty program" added $257M to $535M a year in five of the
seven cycle years and subtracted in 2021 and 2022). Beside the central figure, the range with that float removed.

**Specific (e), growth spending.** The filing allows the maintenance guess: the filer's own figures of about $200M to $300M
a year (10-Ks FY2019 to FY2023; Q3). The central bottom case is owner cash after maintenance only, $250M, against $368M of
average capital and technology spending: $2,127M + $118M = **$2,245M**, at no growth. The growth spending is charged against
the growth it buys in the top case, which uses all spending. Contract acquisition costs, most of them growth spending, stay
deducted in both cases (they sit inside operating cash flow), so the bottom is conservative on that count. The all-spending
no-growth case is shown beside.

**Specific (f), the cap.** Inside ten years the shown rate, 7.56%, is the cap. Carried ten years, owner cash would be 44% of
gross fee revenue grown at its own 6.20%, below the highest share in the filings read (62% in 2017; 91% in the aberrational
2020), so no cut is needed. Nothing above the discount rate is carried after year ten **[M1997-095]**; after year ten the rate
is zero nominal (the PG specific).

**Net debt** (Q7, "On what the floor is earned"): debt $16,915M (current $460M plus long-term $16,455M, finance leases of
$110M included) less cash $462M at 2026-06-30 (10-Q), plus the repurchases the 10-Q states after the quarter (6.2 million shares
for $2.2B year-to-date through 2026-07-29 against $1,819M paid in the half: $381M): **$16,834M**. Operating leases ($879M
non-current liability at 2025-12-31) are left out, as the convention says. The August 2026 note issue refinanced maturities
and does not change net debt.

**Value range** (whole business at 5.56%, less net debt, over 260.766M shares):

| case | cash input | growth | business value, $M | per share |
|---|---|---|---|---|
| **bottom (central): maintenance-only, no growth** | 2,245 | 0% | 40,381 | **$90.30** |
| **top: all spending, purchases deducted, shown growth ten years, then flat** | 2,127 less 78 | 7.56% | 68,939 | **$199.82** |
| beside: all spending, no growth | 2,127 | 0% | 38,261 | $82.17 |
| beside: literal window 2021-2025 (bottom, top) | 2,560 (2,386 plus 424 less 250 of maintenance); 2,386 less 174 of purchases | 0%; 7.56% | | $112.00 to $228.25 |
| beside: loyalty float removed (bottom, top) | | 0%; 7.56% | | $71.25 to $165.07 |
| beside: equity-only basis (owner cash after interest, $1,746M, against the market value; never decides alone) | | | | $128.55 to $216.39 |

**Value range: $90.30 to $199.82 a share against $371.50.** The equity-only range is higher because the cycle's interest
($382M a year after tax on average) is far below what today's $16.8B of net debt costs; it shows the per-share flattery the
all-equity basis is there to remove **[L2017-004]**.

**The floor, tested first.** At $371.50 the business is priced at $113,709M (market value $96,875M plus net debt). The cycle
base is a 1.87% yield on that; 2025's own owner cash is 2.60%. The top case, valued at the price, returns about 3.6% a year
(purchases ignored, which flatters it); the bottom, about 2.0%. To earn ten percent at the price, owner cash would have to grow
about 24% a year for ten years and then hold. No case in the range earns the floor of about ten percent: "there’s just a point
at which we drop out of the game" **[M2003-149]**. The price is above the top of the range, which closes OUT however wide the
range. (The width, 2.2 to one on equity, would not have closed it TOO HARD.)

**The screamer, for the record.** Not approached: the price is 1.86 times the top of the range, the opposite of "It should
scream at you." **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of the long rate,
the two averaged: bottom $22,452M, top $35,161M, average $28,807M, less net debt $16,834M, over 260.766M shares: **$45.91 a
share on the all-equity basis** (central), after the company's own tax. **Equity-only figure beside it: $90.83 a share**
(owner cash after interest, the same construction, against the market value). No cheap price is reported.

**Q6's buyback test, run here and written back at Q6:** every price paid in the periods read ($273 average in 2025, $284.25 in
the fourth quarter of 2025, $368.49 in the second quarter of 2026) sits far above the bottom of the range, $90.30, so the
buyback with no stated price weighs against with no exception **[L2016-002]**, **[L1999-023]**.

- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case; the price is above the top of the range
  **[M2003-149]**, **[R1996-018]**, **[L2000-024]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: Q1 to Q6 passed or weighed (Q1 IN, Q2 IN, Q3 for, Q4 IN with the adjusted-figure habit against, Q5 integrity
IN, Q6 against on both parts); valued at **$90.30 to $199.82 a share against $371.50**, the price above the top of the range and
no case earning the floor of about ten percent. Fair price $45.91 (all-equity), $90.83 (equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box unchanged; operator rule 2.)* **[M1997-127]**
- **Q8:** the US 30-year Treasury at 5.56% (10/13/2026) against an owner-cash yield on the business's price of 1.87% (cycle) to
  2.60% (2025).
- **Q9, the target's debt:** debt $16,915M at 2026-06-30 (10-Q), up from $8,506M at 2016-12-31; weighted average rate 4.5% and
  maturity about 5.4 years at 2025-12-31; fixed-rate maturities $1,198M (2026), $1,392M (2027), $1,441M (2028), $1,283M
  (2029), $1,488M (2030), $6,924M thereafter, and floating $1,177M (2027) and $1,181M thereafter (10-K Item 7A). Revolver raised
  to $5.00B and extended to 2031-09-23 (8-K 2026-09-24, 0001193125-26-401051); it backs the commercial paper, which "generally
  have short-term maturities of 45 days or less" and is classed long-term on the intent to refinance (10-K Item 7). A single
  covenant, Adjusted Total Debt to EBITDA no more than 4.5 to 1.0. Coverage: operating income $4,141M against interest $809M in
  2025, about 5.1 times; in 2020, operating income $84M against interest $445M (10-K FY2022). Guarantees: maximum potential
  future fundings $225M (10-K Note 7). Stockholders' deficit $(4,525)M at 2026-06-30. The acquisition criterion "little or no
  debt" is stated for whole businesses.
- **Q9, sudden demands for cash:** the current ratio is 0.4 to 1.0; the loyalty liability is $8,444M at 2026-06-30
  ($3,680M current), settled in stays at hotels the company does not own.
- **Q10:** nothing beyond the box.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit a6e52fbe); written question by question; committed after each
      (write-early), with pathspec commits of the run file and the research folder only.
- [x] Dispatched: the brief allowed the per-question commits; the lock is held by the dispatching session (a lock file is
      present in `Screens/_daily/`, seen in a listing filtered for "lock", not opened); the fold is the dispatcher's.
- [x] The blind rule. Not opened, listed or searched: `PORTFOLIO.md`, holding reviews, `Screens/RESUME STATE*`, the queue, the
      reading list, other run files. **Contamination, declared and not used:** (1) at the start I ran a listing of `Test Runs/`
      filtered for "MAR " and "marriott" to check that my file did not already exist; it returned no names, but it was a search of
      that folder for this company, a breach of the blind rule's letter, declared here; (2) the session's opening context showed
      the last commit subjects (a TKAMY run and its fold, another company) and the working tree's untracked files, which name
      research folders of AYI and ARCB; (3) the memory index loaded with the session mentions counts of gate-clearers and owed
      holding reviews in general terms, naming no company. None of it bears on this name and none was used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (`check_cites.py`);
      no E-ids; every filing fact carries its document and accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance; Q8 to Q12 NOT REACHED.
- [x] Owner cash after every real cost (stock pay, all capital spending, contract acquisition costs inside operating cash),
      never a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP; no integrity facts
      needed the flag, since Q5 was reached and answered.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; two of its printed lines were checked against the filing and
      rejected (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Spec (a) when only one peak is visible.** The cycle is defined peak to peak or trough to trough, and growth between the
averages of successive cycles. For a business whose last trough (2020) is followed by no second peak yet, and whose earlier
cycle predates a merger (Starwood, 2016), neither can be applied as written; I took 2019 to 2025 as the cycle and the halves
either side of the trough for growth, each confessed as a CONVENTION of this run. A sentence saying what to do when the latest
year must close the cycle would make the next run of a recovered cyclical name reproducible. (2) **EBITDA talk: Q4's list
against Q4's convention.** Q4's "What it rules OUT" list still carries its item on EBITDA and the managements that talk it, citing the row
M2002-026, which reads as an exclusion, while the convention of 2026-10-06 sends a featured adjusted figure to a weighing
judged at Q5. Marriott features Adjusted EBITDA and pays on it; I applied the later, specific convention, but the list item
should say it is weighed. (3) **The loyalty float.** Spec (d) counts working capital, so a growing customer-prepaid liability
adds to owner cash; in the no-growth case that float would stop growing, yet the base carries its historic inflow. I showed the
range without it beside; the text could say which is central. (4) **Spec (e) and payments to customers for growth.** Contract
acquisition costs (key money) sit inside operating cash flow, so they cannot be separated into maintenance and growth by the
spec's own construction; the bottom case is conservative by their full amount. (5) **The equity-only figure** rises above the
all-equity figure when the debt grew late in the window; the text says it never decides alone, and here it would mislead if
it did.
