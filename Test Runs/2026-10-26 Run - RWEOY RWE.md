# Company Run: RWE AG (Frankfurt: RWE; US Level 1 ADR: RWEOY, one ADR per share), 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form as in
the template. Every judgment cites a v5 ledger id in bold; this name files nothing with the SEC, so every filing fact
carries its document and date in place of an accession (the brief's no-SEC paragraph). Dispatched blind run. The file was
copied from the template before any fetch (commit 9510d3e8).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no RWE or RWEOY row).*

**Contamination, declared and not used.** (1) The session context listed recent commit subjects about a PEG run and the
git status named a file in another run's research folder (`_research 2026-09-27 ARCB`); not opened, not used. (2) At the
start I ran a directory listing of `Test Runs/` filtered for "rwe" to see whether my dated file name was free; it returned
nothing. Under the blind rule that listing counts as a search of `Test Runs/`; it is declared here; it showed no file. (3)
A memory index line in the session context speaks of queue state and gate-clearers in general; it names no company I
used. Nothing of any other run, holding review, `PORTFOLIO.md` or the register was read.

**Lines of evidence chosen (the brief's one departure, stated):** from the Annual Report 2025 (published 12 March 2026),
the equivalent of Item 1 is section 2.1 "Business model and strategy" (pp. 21 to 27) and the segment reporting note (29)
(pp. 251 to 252); of Item 1A, section 2.9 "Development of risks and opportunities" (pp. 60 to 68); of Item 7, sections
2.5 "Business performance" and 2.6 "Financial position and net worth" (pp. 39 to 55), with the cash flow statement (p. 170)
and note (30). Read with them: the five-year overviews of the Annual Reports 2020 and 2025, the annual reports 2016 to
2024 (2021's file was not served by the site; its figures are taken from the 2022 and 2025 reports' comparatives), the
Interim Report H1 2026 (published August 2026), the Remuneration Report 2024 and the Executive Board remuneration system
put to the 2025 AGM (the Remuneration Report 2025 was not on the remuneration page).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 55.62, Frankfurt (Xetra) close 2026-10-23 (Yahoo Finance chart API via `tools/sources.py`; an aggregator
  quote, flagged per operator rule 5). Intraday 2026-10-26: EUR 56.56; the ADR RWEOY USD 62.39 close 2026-10-23 at
  EUR/USD 1.122 (same aggregator, 2026-10-22) is EUR 55.6, consistent. All figures below are in euros, the earnings currency.
- **Shares:** 743,841,217 no-par bearer shares at 31 Dec 2025 (Annual Report 2025, note 20, and the capital-stock
  disclosure, p. 69 region), of which 30,276,506 treasury; on 22 June 2026 RWE issued 36,143,952 new shares and sold all
  38,240,169 treasury shares at EUR 54.00 (Interim Report H1 2026, "RWE finances Amprion transaction via capital increase"
  and the equity note: "As of 30 June 2026, following the sale no treasury shares were held"). Count: 743,841,217 +
  36,143,952 = **779,985,169** shares outstanding, no treasury. `Screens/cover_shares.py` reads SEC data and was not run
  (the brief). No later capital measure found in the interim's events after the balance-sheet date.
- **Market cap:** 779.985M x EUR 55.62 = **EUR 43,383M**.
- **Sovereign for the earnings currency:** **3.62%**, ECB euro area AAA yield curve, 30-year spot
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), dated 2026-10-23, the issuing authority (`tools/sources.py`).
- **Filings read** (operator rule 4): Annual Report 2025 (RWE AG, 12 March 2026; no accession, IR site PDF); Interim Report
  H1 2026 (August 2026); Annual Reports 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024; Remuneration Report 2024;
  Executive Board remuneration system (AGM 2025). **One figure cross-checked against the filed statement:** cash flows
  from operating activities 2025, EUR 4,954M, in the five-year overview (p. 343) and in the cash flow statement (p. 170)
  and in note (30): they agree.
- `tools/run.py` reads SEC data and was not run (the brief). The arithmetic below is mine, in
  `Test Runs/_research 2026-10-26 RWEOY/q7_calc.py`, from the filed figures:

| EUR M | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Cash flows from operating activities | 7,274 | 2,406 | 4,223 | 6,620 | 4,954 |
| Capital expenditure (PP&E, intangibles, financial assets, acquisitions) | 3,769 | 4,484 | 9,979 | 11,240 | 10,810 |
| Proceeds from divestments (FCF less CFO plus capex) | 1,057 | 110 | 1,162 | 514 | 360 |
| Free cash flow as the filer defines it | 4,562 | -1,968 | -4,594 | -4,106 | -5,496 |
| Dividends to non-controlling interests | 155 | 304 | 274 | 262 | 223 |
| **Owner cash after all spending (equity-only)** | 4,407 | -2,272 | -4,868 | -4,368 | -5,719 |
| Operating D&A (adjusted EBITDA less adjusted EBIT) | 1,465 | 1,742 | 1,947 | 2,119 | 2,219 |
| Owner cash after the maintenance guess (CFO less D&A less minorities) | 5,654 | 360 | 2,002 | 4,239 | 2,512 |

  Five-year averages: owner cash after all spending **EUR -2,564M**; after the maintenance guess **EUR 2,953M**; net
  growth spending above it **EUR 5,517M** a year. Interest paid and received and income tax paid sit inside operating cash
  (note 30), so these are equity-only figures. Borrowing costs capitalised into growth projects (EUR 798M in 2025, 217M in
  2024, adjusted financial result commentary p. 47 region) sit inside capital expenditure, not inside operating cash. Stock
  pay: the executive LTI is paid in cash after four years (remuneration system 2025), so it runs through operating cash;
  no share-settled plan of size found. Dividends to minorities are deducted because the KKR, Apollo, Masdar and other
  partners own parts of RWE's assets.

**Q4's balance sheets, read here because the file closes before Q4** **[M2025-032]**. Ten years from the two five-year
overviews (Annual Reports 2020 and 2025), EUR M:

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Balance sheet total | 76,402 | 69,059 | 80,108 | 64,009 | 61,668 | 142,309 | 138,573 | 106,512 | 98,442 | 101,717 |
| Equity | 7,990 | 11,991 | 14,257 | 17,467 | 17,971 | 16,996 | 29,304 | 33,604 | 33,623 | 41,564 |
| Net debt (-: net cash) | 22,709 | 20,227 | 19,339 | 7,159 | 4,432 | -360 | -1,630 | 6,587 | 11,177 | 10,921 |
| Adjusted EBIT | 3,082 | 1,170 | 619 | 1,267 | 1,771 | 2,185 | 4,568 | 5,802 | 3,561 | 2,868 |
| Income before tax | -5,807 | 2,056 | 49 | -752 | 1,196 | 1,522 | 715 | 3,999 | 6,343 | 3,539 |
| Shares (average, M) | 614.7 | 614.7 | 614.7 | 614.7 | 637.3 | 676.2 | 691.2 | 743.8 | 743.6 | 727.6 |

What moved and why, in the filer's own figures. (1) The company of 2016 to 2018 is not the company of 2025: innogy
(networks, retail) was consolidated until 2018 and swapped with E.ON in 2019 to 2020 for E.ON's renewables and an E.ON
stake; the 2019 net income of EUR 8,498M is that swap's gain, not earnings. (2) Equity rose from EUR 8.0bn to EUR 41.6bn,
but much of it was bought with new capital or partners' money, not retained: the 2020 capital increase (gross EUR 2bn at
EUR 32.55, Annual Report 2020), the Qatar Investment Authority mandatory convertible of 2023 (shares 676.2M to 743.8M),
EUR 5,283M of capital paid in by non-controlling interests in 2025 (cash flow statement 2025, chiefly the KKR partnership
of December 2025), and after the window the June 2026 placement (EUR ~4bn). (3) The balance sheet total doubled to
EUR 142bn in 2021 and 2022 and fell back: derivative assets and liabilities from the energy crisis, not business assets.
(4) Intangibles fell from EUR 12.7bn (2016, innogy) to EUR 2.2bn (2018), then rose to EUR 9.8bn in 2023 with the purchase
of Con Edison's clean energy businesses, and stood at EUR 8.7bn in 2025. (5) Property, plant and equipment went from
EUR 17.9bn (2020) to EUR 42.3bn (2025): the growth programme. (6) Net debt was paid down to a net cash position by 2021 and
2022 and has risen again with the investment; at 30 June 2026 RWE's own measure was EUR 14,984M, and the interim states
the leverage factor "is likely to be much higher" ahead. What the figures do not say: the mining provisions (EUR 5,511M
at 30 June 2026) are outside the filer's net debt, set against the E.ON stake (fair value EUR 7,136M) the filer assigns to
them; and adjusted EBIT leaves out impairments, which recur (EUR 1,359M in 2024 and EUR 729M in 2025, note 5).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own RWE "if the market closed for five years"
**[M1997-109]**, which turns on the cash the generation fleet will produce, not on the quotation. No macro enters: the
filer's own case for itself is a forecast of power demand (the IEA's 3.6% a year, AI and data centres; section 2.1), and a
forecast is answered with "So what?" **[M2000-095]**; what counts is the business's own profitability and competitive
position over time **[M2015-016]**. Who is paid to tell you: the company's 2031 earnings-per-share target is a seller's
projection of what it sells, read as such **[M2011-083]**. **Contrary evidence, written down as found** **[M1997-127]**:
(a) the castle evidence below runs against a durable advantage, and I wrote it down before reading the pay and the people;
(b) against my reading, RWE does hold contracts for difference and long-term PPAs on much of its renewable output, which
fixes prices for fifteen to twenty years on those assets (section 2.1), and the 2025 UK auction gave it CfDs on 6.9 GW;
that is a real stabiliser of the renewables parts and is weighed at Q2; (c) the deciding part's earnings in 2025
(EUR 973M) are still more than twice its 2021 level (EUR 418M), which a reader could take as a lasting step up; Q2 asks
whether a full cycle shows it.

## THE STANDING RULE
A part-interest bought for cash, unlevered, puts the buyer at no risk of ruin through its own conduct; nothing here
requires borrowing to own it, which the rows rule out **[L2014-005]**, **[M2012-081]**. The target's own debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, identifying "the key variables in that particular business, and evaluating
  how predictable they were first" **[M1998-044]**.
- **The key variables, from the filings.** RWE sells one product, electricity, plus trading. Its earnings come from five
  parts (section 2.1): Offshore Wind and Onshore Wind/Solar, where most new output is sold under government contracts for
  difference or long-term fixed-price PPAs; Flexible Generation (gas, hydro, biomass, batteries), sold on wholesale markets
  hedged forward, plus capacity payments set at auction; Supply & Trading; and Phaseout Technologies (lignite to March
  2030, nuclear dismantling). The variables are capacity built, the contracted price per MWh won at auction, the wholesale
  spread for the gas fleet, capacity-market prices, and the cost of capital on a EUR 35bn six-year programme with a stated
  "minimum required average return for new projects" of 8.5% (section 2.1, p. 22).
- **Are they foreseeable?** The economics of the renewables parts are foreseeable in kind: a capital-heavy business
  that earns roughly the return it bid into an auction. The deciding part (Q2, Flexible Generation) earns a spread set by
  the market, which moved EUR 418M, 2,005M, 2,695M, 1,464M, 973M in 2021 to 2025. That is a commodity dependence, and
  under Q2's commodity-business paragraph a dependence on a commodity price "is never by itself a STOP at Q1 or Q2": the
  speakers "don't think we can predict commodity prices" **[M2016-025]** and still decide "off the figures"
  **[M2008-069]**. The figures here are readable: the segments, the auction rules, the hurdle rate, the risk report's own
  classification of market and regulatory risk as "high" (p. 61).
- **Test 3, do the past statements tell me the future ones?** **[M2008-033]**: for the competitive position, yes, the past
  ten years show it plainly (Q2 below); for the level of earnings in a given year, no, and that is the commodity
  dependence Q2 must judge, not a reason to stop here.
- **Test 5, would the insiders write it down?** **[M2000-105]**: they do; RWE publishes a 2031 per-share target. That is a
  projection, not evidence; but it means the industry's insiders do not call the forecast too hard.
- **Doubt, written down.** "if you have doubts about something being into your circle of competence, it isn't"
  **[M2002-092]**. My doubt is about the level of the gas fleet's earnings in 2035 (a German capacity mechanism not yet
  legislated, a 2026 review of the lignite exit, hydrogen-ready plants), not about what kind of business it is. The rows
  define understanding as foreseeing earning power and competitive position, and the competitive position is the part I
  can foresee with most confidence; how far off I could be on the level **[M2011-084]** is the width Q7 would carry.
  Technology: no "technological component that's of significance" decides the deciding part **[M1998-008]**; gas turbines
  and wind turbines are bought from suppliers.
- **VERDICT: IN**, narrowly. The business can be understood from its figures **[M2008-069]**; the competitive position
  over ten years is the question, and it is Q2's. The doubt above is carried, not dismissed.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

**The parts table** (Q2, a business of parts; "lumping them together [...] impedes analysis" **[L2008-005]**). Adjusted
EBIT by segment, EUR M, from the Annual Reports 2022 (2021), 2023 (2022, 2023 as first reported), 2024 (2023 restated, 2024)
and 2025 (2025). The 2023 segment re-cut renamed Hydro/Biomass/Gas as Flexible Generation; from 2024 Phaseout
Technologies is reported outside adjusted EBIT and managed on adjusted cash flow.

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share of the positive parts | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Offshore Wind | 636 | 836 | 1,010 | 895 | 736 | 4,113 | 21% | contracted price won at auction | no |
| Onshore Wind/Solar | -145 | 370 | 535 | 559 | 742 | 2,061 | 10% | contracted price won at auction | no |
| Flexible Generation (Hydro/Biomass/Gas) | 418 | 2,005 | 2,695 | 1,464 | 973 | 7,555 | **38%** | wholesale spread, capacity auctions | **yes, the largest** |
| Supply & Trading | 721 | 1,111 | 1,520 | 653 | 305 | 4,310 | 22% | trading | no |
| Phaseout Technologies (Coal/Nuclear) | 661 | 456 | 614 | not reported | not reported | 1,731 (three years) | 9% | closing by law, March 2030 | no |
| Other, consolidation | -106 | -210 | 42 | -10 | 112 | -172 | | | |

No part carries more than half of five-year operating profit, so the largest decides: **Flexible Generation**. It is also
the largest part in 2025 alone (EUR 973M against 742M and 736M), so the choice does not rest on the crisis years.

**The castle tests on the deciding part, each with its filing fact.**
1. **Who sets the price?** Flexible Generation's power is sold on wholesale markets, forward, at the market's price; the
   risk report says "the energy sector is characterised by the free formation of prices" and that falling wholesale prices
   "can impact the economic viability of generation assets" (Annual Report 2025, p. 61). The part takes the price the
   marginal plant sets: "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit"
   **[M2023-079]**. On the OUT list: the business whose price a competitor sets.
2. **The low bid.** The contracted half of this part's income, capacity payments, is set by auction at a single clearing
   price: the March 2025 British capacity auction "cleared at" GBP 60 "per kilowatt plus inflation adjustment" for all of
   RWE's 6,444 MW that qualified (Annual Report 2025, p. 38). Germany's coming tenders for 12 GW of new dispatchable plant
   are auctions too (p. 32). The renewables parts are won the same way: German offshore support is set by "a competitive
   tender process, in which participants with the lowest bids are selected", and the lowest successful bid in the 2018
   round was zero (Annual Report 2020, business environment). The buyer is the auctioneer, who takes the low bid
   **[M2017-009]**; "most insureds don't care from whom they buy" **[L2004-003]** has its counterpart in a grid that cannot
   tell one megawatt-hour from another.
3. **The money test.** Could a well-funded attacker build this? The filer's own conduct answers it: it sells stakes in its
   assets to financial investors as a matter of course (the KKR partnership agreed December 2025; capital paid in by
   non-controlling interests of EUR 5,283M in 2025), and it buys development rights for money (three UK offshore projects
   and the Magnum gas plant, both from Vattenfall). Capital and permits, both purchasable, are the inputs; the question
   "could I do it?" **[M2011-015]** is answered yes, and the field is one of those "that are just never going to have
   barriers to entry" **[M2012-106]**.
4. **Pricing power and the agony before a rise.** None to read: the part does not set a price **[M2005-020]**.
5. **The low-cost position.** No report read states the fleet's cost per MWh against its rivals'. The rows make the
   low-cost producer the road through a commodity field **[M1997-010]**, and the filer's own figures point the other way
   for at least part of the fleet: in 2024 it wrote down its Dutch gas, biomass and coal portfolio by EUR 654M on property,
   plant and equipment, "The reason for this was the deterioration in market conditions in the Netherlands" (Annual Report
   2025, note 4), leaving a recoverable amount of EUR 0.2bn. I do not rest the box on this test (see the commodity
   paragraph below).
6. **Widening or narrowing, and the full cycle.** The part earned EUR 342M (2019) and 283M (2020) as Hydro/Biomass/Gas
   (Annual Report 2020), then 418M, 2,005M, 2,695M, 1,464M, 973M. The filer names the cause of the middle years: "margins
   from electricity forward sales dropped, reflecting the normalisation of prices since the record highs witnessed during
   the 2022 energy crisis" (Annual Report 2025, p. 31). A change for the better is credited only on a full cycle in which
   the price behaviour held **[M2005-020]**; what the filings show so far is a spike falling back, with the 2024
   write-down inside it, a moat shrinking rather than widening **[M1999-108]**.
7. **What could destroy or reduce it.** The risk report classes market risks and regulatory and political risks as
   "high" (p. 61): the part's future income depends on capacity mechanisms the German government has not yet legislated,
   and on batteries, which RWE itself is building, taking the peak-price hours a gas plant lives on.

**The field's returns over the last full cycle** (section C). Same measure as near as the reports allow, from the
filer's and two rivals' own reports. The Annual Report 2025 names no company as a competitor ("several of our
competitors' offshore wind projects", p. 31, are unnamed). As counterparties in its own markets it names Vattenfall
(seller of the UK offshore projects and of Magnum), Uniper (a partner in German LNG and hydrogen, Annual Reports 2022 and
2023), and TotalEnergies and Equinor (partners). **Vattenfall and Uniper do not file with the SEC; both are flagged and
read from their own annual reports.** TotalEnergies and Equinor file 20-Fs but are oil and gas groups whose power units are
a small part of them; they were not read, and that is a gap.

| | 2021 | 2022 | 2023 | 2024 | 2025 | Source |
|---|---|---|---|---|---|---|
| **RWE**: adjusted EBIT / (equity + net debt), year-end | 13.1% | 16.5% | 14.4% | 7.9% | 5.5% | five-year overview, Annual Report 2025 (my division) |
| **RWE**: income before tax / (equity + net debt) | 9.1% | 2.6% | 10.0% | 14.2% | 6.7% | same |
| **Vattenfall** (Swedish state): ROCE, operating profit / average capital employed | 22.2% | 4.2% | 5.3% | 12.4% | 8.9% | Vattenfall Annual and Sustainability Report 2025, five-year overview, p. 209 |
| **Vattenfall**: underlying EBIT / average capital employed | 11.5% | 12.5% | 6.3% | 5.4% | 10.2% | same (2021 to 2023 my division of its figures) |
| **Uniper** (Germany): adjusted EBIT, EUR M | | | | 2,001 | 568 | Uniper Annual Report 2025 (published 2026), financial condition and income statement sections |

Over RWE's ten filed years (2016 to 2025) income before tax summed EUR 12,860M against an average of EUR 32.5bn of equity
plus net debt: about 4% a year before tax. On adjusted EBIT, which leaves out the recurring impairments, about 8% (EUR
26,893M over the ten years). Vattenfall sets its own target as an 8% ROCE "over a business cycle" (its 2025 report,
targets page), and its five years average about 10% only because 2021 and 2024 carried crisis-year gains. Uniper, the
German gas-fired generator and trader, had to be rescued: "Following the implementation of the stabilization measures in
2022, the Federal Republic of Germany holds a total of more than 99% of the shares in Uniper SE" (Uniper Annual Report
2025). RWE's own required return on new projects is "the sum of the WACC and project-specific risk premiums, which
usually range from 150 to 350 basis points" (Annual Report 2025, p. 27): the insiders build the business to earn its
cost of capital plus a margin, and the auctions it bids in are designed to compete that margin away. Judged in words, as
the convention asks: **ordinary returns, high only in the crisis years, with a rival in the same field taken over by the
state in the same cycle.** The moat the rows ask for "protects excellent returns on invested capital" **[L2007-004]**; "you
can have only two competitors and they're still terrible businesses" **[M2013-052]**, and here the improvement one bidder
gets "your competitor gets the next day" **[M2004-053]**. A regulated return would be the exception, carried to Q3 as a
second best **[M2009-104]**; but the deciding part is merchant, priced by a market, and Q7's text keeps "Merchant
generation and unregulated renewables, priced by a market" on the ordinary basis.

**The commodity paragraph, applied.** The dependence on the power price is not the ground of this box. Q2 asks whether it
is the low-cost producer, measured "more by cost of production" **[M2006-004]**, and "The figures are available."
**[M2009-059]** only where an operator publishes them; no report read states the fleet's cost against rivals', so on that
test alone the file would be TOO HARD (WORK). The box rests instead on three grounds the filings do state: the price is
set by others (test 1), the contracted income is won on the low bid (test 2), and the field's durable players earned
ordinary returns over the cycle on their own figures (the table). Each is on Q2's OUT list, and the third is the item the
framework added for this case: a field whose durable players earn ordinary returns over a full cycle is OUT, not TOO HARD.

**The contrary evidence, weighed.** The CfDs and fixed-price PPAs on the renewables parts are real; they make those parts'
income steady, but steady at the return bid into the auction, which is the ordinary return above. Flexible Generation's
level since the crisis is higher than before it; only a full cycle can credit that **[M2017-026]**, and the second year
after the peak already took it to about a third of 2023's. Neither moves the box.

- **VERDICT: OUT.** The deciding part's castle is shown open on the evidence: it takes its price from the market
  **[M2012-109]**, wins its contracted income on the low bid **[M2017-009]**, and its field earned ordinary returns over
  the cycle **[L2007-004]**, **[M2013-052]**. A castle shown open closes OUT **[M2011-015]**, and price does not reopen
  it. Q3 onward: NOT REACHED; Q7 below is a COMPUTATION, NOT A CLEARANCE.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion.
NOT REACHED. The balance sheets were read in Step 0 as the template asks; the facts on the accounts are under AFTER THE STOP.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity-bearing facts found before the stop are recorded under AFTER THE STOP, not judged.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback prices are set against the bottom of the computed range under AFTER THE STOP, as a fact only.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question. What follows is the operator's reporting figure, computed after the stop.

### COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention and specifics, in `Test Runs/_research 2026-10-26 RWEOY/q7_calc.py`. No entry language.

- **Window and base.** 2021 to 2025. Specific (a): the first year is aberrational on the filer's own figures, operating
  cash swollen by variation margins received in the energy crisis (Annual Report 2022, note on the cash flow statement:
  "variation margins paid in the amount of 4,026 million (previous year: 2,154 million received)"), and 2022 and 2023 are
  the crisis itself; no full cycle of owner cash is filed, so the base is the five-year average and the growth is
  measured between the first and second halves of the window (specific (b), since the end-year rate, -18.4% a year, is
  distorted by the aberrational first year). The literal window is shown beside.
- **Maintenance guess** (specific (e)). The reports give no split of capital spending into maintenance and growth; the
  guess is operating depreciation, the rows' own proxy, "not inappropriate in most companies to use as a proxy for
  required capital expenditures" **[M1998-127]**, said to be a guess. It understates by the Phaseout capital spending
  (EUR 266M in 2025), which I did not add for 2021 to 2023 for want of a like figure; confessed.
- **Equity-only owner cash after maintenance** = operating cash less operating D&A less dividends to minorities less
  capitalised borrowing costs (EUR 217M in 2024 and 798M in 2025; earlier years not found and taken as nil, confessed):
  five-year average **EUR 2,750M**. Growth spending above it (capital spending including acquisitions, less divestment
  proceeds, less the maintenance guess, less the capitalised interest): **EUR 5,314M** a year on average.
- **All-equity owner cash** adds back the after-tax interest cost (cash net interest in operating cash plus capitalised
  interest, at RWE's own 20% planning tax rate): EUR 215M, giving **EUR 2,965M**.
- **Growth shown** between halves: 3.9% a year (owner cash after maintenance, EUR 3,007M to 3,376M). Carried ten years
  with the growth spending grown at the same rate (year one EUR 5,523M, year ten EUR 7,813M) and stopped after year ten
  (specific (e)); then zero nominal growth. Specific (f): 3.9% is below the discount rate and below any absurdity; no cut.
- **The inversion.** The growth spending of the window (about EUR 26.6bn net over five years) bought no rise in owner
  cash after maintenance (EUR 5,654M in 2021, 2,512M in 2025) and EUR 683M of adjusted EBIT (2,185M to 2,868M), much of the
  capital still under construction. Growth bought is worth less than its cost on the window's evidence, so the
  maintenance-only no-growth case is the top of the range and the growth case the bottom: "growth can destroy value"
  **[L2000-023]**.
- **Acquisitions** (specific (c)): deducted with the total growth credited (the default pair; Con Edison's clean energy
  businesses in 2023 is inside the window's capital spending). The serial-acquirer test: net purchases over the window
  (EUR 8.7bn of financial assets and acquisitions less EUR 3.2bn of divestments) do not exceed half of owner cash before
  purchases, which is itself negative after the property spending, so the test is not met in its terms; the default pair
  stands, said so. The Amprion step-up of June and July 2026 (indirect stake to 55.5%, EUR 3.6bn) closed after the window:
  credited at nothing beyond the Amprion dividends already inside operating cash (equity-method rule), its financing in
  the share count (the June placement) and in net debt (the July tranche of EUR 1.8bn). The KKR partnership (assets held
  for sale, EUR 3,366M at 31 Dec 2025) is left out of both cash and debt until closed, said so.
- **Net debt** (all-equity basis): financial debt EUR 23,473M with the 50% hybrid correction reversed (+504M) less
  financial assets EUR 14,996M at 30 June 2026 (Interim Report H1 2026, net debt table), plus the July 2026 Amprion tranche
  stated in that report's events after the balance-sheet date (EUR 1.8bn): **EUR 10,781M**. Left out and said so: the
  provisions for nuclear waste (EUR 4,369M), mining (5,511M), dismantling (1,515M) and pensions (net 455M), because their
  cash is paid through operating cash as it falls due; and the 15% E.ON stake (fair value EUR 7,136M), because its
  dividends are inside owner cash. Operating leases: inside "other financial debt" as the filer states it; not separated.
- **Basis.** The deciding part is merchant generation, priced by a market; Q7's text keeps "Merchant generation and
  unregulated renewables, priced by a market" on the all-equity basis. **All-equity is central; equity-only beside.**
- **Sovereign:** 3.62% (ECB, 2026-10-23). **Shares:** 779,985,169. **Price:** EUR 55.62. **Market cap:** EUR 43,383M.

| EUR per share | Bottom (growth case) | Top (maintenance-only, no growth) | Expected return at EUR 55.62 |
|---|---|---|---|
| **All-equity (central)**, at 3.62% | **63.74** | **91.19** | growth case 3.8%; no-growth case 5.5% |
| Equity-only (beside), at 3.62% | 66.93 | 97.41 | growth case 4.0%; no-growth case 6.3% |
| Literal window beside: owner cash after all spending, no growth, all-equity | -97.03 | | negative (-4.3% cash yield) |

- **The floor is tested first.** No case earns the floor of about ten percent at the price: the best case returns 5.5%
  on the all-equity basis and 6.3% on the equity-only basis, "a point at which we drop out of the game" **[M2003-149]**.
  Q7, had it been reached, would close **OUT** on the floor whatever the width (the width is 1.4 to 1). The price sits
  below the range at the government rate only because 3.62% is far below the floor; the computation does not reverse
  that.
- **Fair price** (Part VII, the owner's price; a reporting figure, never a verdict): each end case valued at ten percent,
  the two averaged, after the company's own tax. **All-equity (central): EUR 4.79 a share** (growth case EUR -14.61, top
  case EUR 24.19). **Equity-only (beside): EUR 15.44** (EUR -4.39 and EUR 35.26). No cheap price is reported.

## Q8 to Q10, Q12
NOT REACHED.

---
## THE BOX
**OUT, at Q2** (the deciding part, Flexible Generation, takes its price from the market, wins its contracted income on
the low bid, and its field earned ordinary returns over the cycle). Computation only, after the stop: value range
EUR 63.74 to 91.19 a share (all-equity, at 3.62%) against EUR 55.62; no case earns the floor at the price (best 5.5%);
fair price EUR 4.79 all-equity, EUR 15.44 equity-only. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).**
- RWE's stated hurdle for new projects is an 8.5% average return, built as WACC plus 150 to 350 basis points (Annual Report
  2025, pp. 22 and 27). Net investment planned EUR 35bn for 2026 to 2031 (p. 21).
- Owner cash after all spending was negative in four of five years (EUR -2,272M to -5,719M, 2022 to 2025); the growth
  spending of the window raised adjusted EBIT by EUR 683M (Step 0 and Q7 computation).
- Capital paid in by others: the 2020 capital increase (EUR 2bn), the QIA mandatory convertible (shares 676.2M to 743.8M by
  2023), EUR 5,283M from non-controlling interests in 2025, the June 2026 placement (EUR ~4bn at EUR 54.00).

**Bearing on Q4 (the accounts).**
- Impairments outside adjusted EBIT, recurring: EUR 1,359M (2024) and EUR 729M (2025) (note 5); by segment in 2025,
  Onshore Wind/Solar EUR 542M and Offshore EUR 177M; in 2024 Flexible Generation EUR 668M.
- The filer's headline measures are adjusted EBITDA, adjusted EBIT and adjusted net income, which remove "capital gains
  and losses, temporary effects from the fair valuation of derivatives, goodwill impairments and other relevant special
  items as well as total earnings from our phaseout technologies coal and nuclear" (Annual Report 2025, p. 26), with a
  budgeted 20% tax rate in place of the actual.
- Capitalised borrowing costs rose to EUR 798M in 2025 from 217M, "reducing adjusted interest expenses" (p. 47 region).
- Mining provisions (EUR 5,511M) sit outside the filer's net debt against the E.ON stake.

**Bearing on Q5 (integrity: recorded, not judged).**
- Guidance: RWE publishes annual ranges for adjusted EBITDA, adjusted EBIT and adjusted net income and reports against
  them ("At 2,868 million, adjusted EBIT was at the upper end of the guided range of 2,350 million to 2,950 million",
  Annual Report 2025, p. 44 region); the H1 2026 interim raised the full-year forecast; a per-share target is published to
  2031 (now EUR 4.55 after the Amprion deal).
- The adjusted figures above are the ones featured in the CEO's letter ("RWE's adjusted EBITDA totalled 5.1 billion,
  placing us at the top of our forecast range") and the ones pay is set on (below).
- No instance found, in the sections read, of a restatement, an auditor qualification or a regulator's penalty; the
  sweep was the risk report and the major events of the 2025 annual report and the H1 2026 interim, not a full search.

**Bearing on Q6 (the money and the owners).**
- Buyback: EUR 1.5bn programme, no stated price ceiling found, completed 3 June 2026 at an average EUR 38.52 for
  38,240,169 shares (Interim Report H1 2026); those shares were resold three weeks later at EUR 54.00 with 36,143,952 new
  shares to fund the Amprion purchase, a deal paid in cash raised by the placement, not in shares. Against the computed
  range (bottom EUR 63.74 all-equity) the buyback prices sat below its bottom; against the fair price at ten percent
  (EUR 4.79) far above. Recorded only.
- Share count: 614.7M (2016 average) to 780.0M (October 2026), about +27% in ten years.
- Pay (remuneration system from 2025): STI on adjusted EBIT, with no capital charge named; LTI in performance shares on
  adjusted EPS, relative TSR against the STOXX Europe 600 Utilities, and carbon intensity; caps on total pay raised from
  EUR 9.3M to EUR 11.0M for the CEO, explained as "doing justice to the general developments in the market and
  remuneration"; share ownership guideline 200% of base pay for the CEO, held two years after leaving. CEO total
  remuneration EUR 5,646k in 2024, 6,396k in 2023 (Remuneration Report 2024).

**Bearing on Q9 (debt and exposures).**
- Net debt (filer's measure) EUR 14,984M at 30 June 2026; target leverage "at the lower end of the range of 3.0 to 3.5"
  times adjusted EBITDA, from 2.1 at end-2025 (p. 27); EUR 10bn of syndicated credit lines kept for liquidity; hybrid bonds
  outstanding; variation margins on exchange-traded hedges of EUR 4,026M paid in 2022 (sudden cash calls of the kind the
  standing rule names); trading VaR cap EUR 60M a day (p. 62).

**Bearing on Q12.** Lignite mining and generation in the Rhenish region to March 2030, with the German state; no named
business of Q12's list.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9510d3e8); written question by question; committed after Q1
      (d2d0453a), after Q2 (5bddc564) and after this section.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present (held by
      the dispatcher, not touched by me); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One filtered listing of `Test Runs/` for "rwe" was
      run before I recalled that a listing counts; it returned nothing and is declared under contamination.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (`check_ids.py`, every quoted fragment beside an id checked
      against its row); no E-ids. Every filing fact carries its document and date (no SEC accessions exist for this name).
- [x] The order was kept; Q2's STOP closed the run; Q7 is a computation under its heading, with no entry language.
- [x] Owner cash from operating cash less capital spending, never a net-income proxy; the sovereign from the ECB;
      the price and the FX rate flagged as aggregator quotes.
- [x] Contrary evidence written as found (foundations, Q1 doubt, Q2's weighing of the CfDs); facts for later questions
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run; rows to 2025 cited.
- [x] `tools/run.py` and `Screens/cover_shares.py` not run (SEC-only, per the brief); arithmetic is mine and in the
      research folder.
- [x] `python tools/check_framework.py` PASS before the final commit (recorded in the commit message).

**Honest slips and limits.** (1) The Annual Report 2021 PDF was not served; 2021 figures are the 2022 and 2025 reports'
comparatives. (2) Page references marked "region" are located from the text extraction, not from the printed page.
(3) The maintenance guess is depreciation, and capitalised interest for 2021 to 2023 was not found and taken as nil;
both flatter the top of the computed range. (4) TotalEnergies and Equinor, which file with the SEC, were not read; the
competitor comparison rests on Vattenfall and Uniper, which do not. (5) RWE's own return measure (adjusted EBIT over
equity plus net debt) is my construction from the five-year overview; RWE publishes no ROCE in the reports read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. First, Q2's commodity paragraph says that where the low-cost position cannot be read because no filing
states it, the file is TOO HARD (WORK or NATURE); the "ordinary returns" OUT item and the price-setter and low-bid OUT
items can close the same file OUT on other evidence. The text does not say which governs when both apply; I read the
commodity paragraph as governing only a file whose sole question is the cost position, and closed OUT on the three
grounds the filings state, saying so. A one-line rule would settle it. Second, the parts convention measures parts on
five-year operating profit, but here the five years straddle an energy crisis that tripled one part's earnings for two
years; I checked that the same part is also the largest in the latest year, and the convention could say to do so.
Third, Q7's specific (e) assumes the filing "allows the maintenance guess"; RWE gives no split, and the text does not say
whether depreciation (the rows' proxy, **[M1998-127]**) may stand in, or whether the all-spending case must then be
central. I used depreciation and showed the literal all-spending case beside; on this name the choice moves the range
from deeply negative to positive but does not change the floor's answer.
