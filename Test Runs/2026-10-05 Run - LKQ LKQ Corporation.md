# Company Run: LKQ Corporation (NASDAQ: LKQ), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch. Working folder: `Test Runs/_research 2026-10-05 LKQ/` (filings as text, `calc.py`, `organic_sentences.txt`, the
`tools/run.py` and `Screens/cover_shares.py` outputs, the ledger rows read).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this run's blind rule, so the
analyst does not know whether the operator holds LKQ. (The template's instruction to check `PORTFOLIO.md` and the run's
blind rule conflict; recorded at the end.)

**CONTAMINATION, declared.** Seen before or during the run, none opened: (1) the session's git snapshot named recent commit
subjects for the v5 runs of AMR (OUT at Q2), MBC (OUT at Q2) and ADNT (OUT at Q2) with their prices, a commit "Session
state: S&P 600 screen top ten", and an untracked `2026-10-05 Run - KSS Kohls.md`; (2) a directory listing of `Test Runs/`
showed the names of other 2026-10-05 run, research-pass and holding-review files (BN, BRK.B, CCB, HRB, MITSY, NCLTY, SONY,
TBTC, V holding reviews), which implies those names are held and LKQ is not among them; (3) the same listing showed two
older files whose titles name LKQ, `2026-07-16 Run - Industrials & Misc 9-pack (LKQ ...)` and `2026-07-17 Pre-Entry
Verification - HRB SBH LKQ ESNT CPB`, which implies LKQ passed some v4-era screen in July; (4) the memory index loaded
with the session says the v4 queue had "57 gate-clearers, nothing buyable". None of these files was opened. The three OUT
verdicts at Q2 on other names are a possible anchor toward OUT here; the counter-case for the business is therefore
written out in full at Q2, so as "to be able to state their case better than they can" **[M2016-055]**.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $22.41 (2026-10-05, live quote via `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 253,002,086 common, single class (10-Q for the period ended
  2026-06-30, filed 2026-07-30, cover as of 2026-07-23, accession `0001065696-26-000044`; `python Screens/cover_shares.py
  LKQ`). Balance sheet of the same 10-Q: 324.3M issued, 70.9M treasury, 253.4M outstanding at 2026-06-30.
- **Market cap:** $5,670M (253.0M x $22.41).
- **Sovereign for the earnings currency:** USD 30-year par yield **5.63%**, US Treasury daily par yield curve, 2026-10-02
  (`python tools/sources.py`). The reporting and XBRL currency is USD; about 46% of revenue and 39% of segment EBITDA are
  earned in euros, sterling and other European currencies (EUR 30-year 3.72%, ECB, same date). USD is used, as
  `tools/run.py` selects it; the question is recorded at the end.
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-19, `0001065696-26-000012`): Item 1, Item 1A, Item 7,
  the cash-flow statement, notes 4 (discontinued operations), 9 (goodwill), 17 (supply chain financing), 18 (debt), 26
  (segments). 10-Q for Q2 2026 (filed 2026-07-30, `0001065696-26-000044`): statements, notes 2, 3, 5, segment MD&A. Proxy
  (DEF 14A filed 2026-03-24, `0001065696-26-000026`), read and not reported here (Q5 and Q6 not reached; operator rule 2).
  8-Ks: Q2 2026 results `0001065696-26-000041`; strategic review including a possible sale of the company, 2026-01-26,
  `0001065696-26-000002`; Specialty sale process, 2025-12-04, `0001065696-25-000068`; Self Service sale agreed 2025-08-26
  `0001065696-25-000051` and completed 2025-10-01 `0001065696-25-000055`; new chairman 2025-08-21 `0001065696-25-000049`;
  credit agreement amendment 2025-12-18 `0001065696-25-000071`. Ten-K history FY2010 to FY2024 for the fifteen-year
  organic-growth and segment-margin series (accessions in the Q2 tables).
- **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities $1,063M, capital
  spending $216M and stock-based compensation $34M, each read on the filed cash-flow statement of `0001065696-26-000012`
  and equal to the XBRL figures `tools/run.py` printed.
- **`tools/run.py LKQ`, arithmetic lines only** (Part VII; nothing it printed as a rule, id or verdict was used; it printed
  none this time). Owner cash after every real cost, USD millions, recomputed in `calc.py` from the filed lines:

| FY | OCF | SBC | capex | finance-lease principal | owner cash (capex basis) | owner cash (D&A basis) | owner cash / revenue |
|---|---|---|---|---|---|---|---|
| 2016 | 635 | 22 | 207 | n/a | 406 | 414 | 4.7% |
| 2017 | 519 | 23 | 179 | n/a | 317 | 266 | 3.3% |
| 2018 | 711 | 23 | 250 | 9 | 429 | 385 | 3.6% |
| 2019 | 1,064 | 28 | 266 | 12 | 759 | 710 | 6.1% |
| 2020 | 1,444 | 29 | 173 | 12 | 1,230 | 1,104 | 10.6% |
| 2021 | 1,367 | 34 | 294 | 13 | 1,026 | 1,036 | 7.8% |
| 2022 | 1,250 | 38 | 222 | 14 | 976 | 934 | 7.6% |
| 2023 | 1,356 | 40 | 358 | 19 | 939 | 978 | 6.8% |
| 2024 | 1,121 | 30 | 311 | 28 | 752 | 657 | 5.2% |
| 2025 | 1,063 | 34 | 216 | 30 | 783 | 581 | 5.7% |
| TTM to 2026-06-30 | 825 | 35 | 200 | 30 | **560** | | |

  Five-year mean (2021 to 2025), capex basis **$895M**; D&A basis $837M. The as-filed cash flows include the Self Service
  segment, sold 2025-09-30 for an enterprise value of $410M, the proceeds used to repay about $390M of revolver debt (10-Q
  note 3). The 10-K states Self Service "contributed approximately $50 million and $40 million" of free cash flow in 2025
  and 2024; for 2021 to 2023 this run estimates it (CONVENTION of this run: segment EBITDA of $175M, $83M, $36M less segment
  capex of $16M, $14M, $36M, less 25% tax, from the FY2022 and FY2023 10-K segment notes; rationale: the filings give no
  segment cash flow for those years and the business is gone). Continuing-operations owner cash: 2021 $907M, 2022 $924M,
  2023 $939M, 2024 $712M, 2025 $733M; mean **$843M**. Shown growth 2021 to 2025: **-5.2% a year** continuing (-6.5% as
  filed). H1 2026 operating cash was $55M against $293M a year earlier (10-Q), driven by payables down $288M and receivables
  up $270M; the trailing figure of $560M carries that swing.
- **Capex and maintenance.** Capex ran below depreciation and amortization in 2024 and 2025 ($311M and $216M against $406M
  and $418M; D&A includes amortization of acquired intangibles). The filings do not separate maintenance from growth
  capex; the capex basis is the run's figure, the D&A basis is shown beside it, and no maintenance judgment is possible
  from the filing.

### The balance sheets, ten year-ends, read first
The rule: "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
(`tools/run.py` table, first-filed XBRL vintages; the FY2025 and Q2 2026 lines checked on the filed statements.)

| year-end | assets | equity | goodwill | intangibles | goodwill + intangibles | cash | receivables | inventory | payables | debt |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 9,367 | 4,198 | 3,537 | 744 | 4,281 | 280 | 1,027 | 2,381 | n/a | 3,428 |
| 2018 | 11,393 | 4,782 | 4,381 | 929 | 5,310 | 332 | 1,154 | 2,836 | 942 | 4,348 |
| 2019 | 12,780 | 5,009 | 4,407 | 850 | 5,257 | 528 | 1,131 | 2,773 | 943 | 4,072 |
| 2020 | 12,361 | 5,656 | 4,592 | 814 | 5,406 | 312 | 1,073 | 2,415 | 932 | 2,897 |
| 2021 | 12,606 | 5,772 | 4,540 | 746 | 5,286 | 274 | 1,073 | 2,611 | 1,176 | 2,824 |
| 2022 | 12,038 | 5,453 | 4,319 | 653 | 4,972 | 278 | 998 | 2,752 | 1,339 | 2,662 |
| 2023 | 15,079 | 6,167 | 5,600 | 1,313 | 6,913 | 299 | 1,165 | 3,121 | 1,648 | 4,281 |
| 2024 | 14,955 | 6,017 | 5,448 | 1,150 | 6,598 | 234 | 1,122 | 3,220 | 1,801 | 4,198 |
| 2025 | 15,137 | 6,537 | 5,414 | 1,072 | 6,486 | 319 | 1,204 | 3,426 | 2,108 | 3,695 |
| 2026-06 | 15,029 | 6,447 | 5,369 | 1,040 | 6,409 | 301 | 1,399 | 3,284 | 1,791 | ~4,000 |

What the figures say, in the order the row asks: "what the figures are saying and what they don’t say and what they can’t
say" **[M2025-032]**.
- **Equity against goodwill and intangibles.** Purchased goodwill and intangibles have equalled the whole of shareholders'
  equity in every year shown: tangible equity was about -$83M in 2017, +$51M at 2025 and +$38M at June 2026. Retained
  earnings rose from $3,124M to $8,019M; $3.0B went to buying 71M shares back from late 2018 to June 2026 (8-K
  `0001065696-26-000041`) and $1.4B to dividends since 2021. The book equity is the price paid for acquisitions, not
  capital left in the business.
- **Cash** has sat between $234M and $528M throughout; $292M of the $319M at 2025 year-end was held abroad (10-K Item 7).
- **Receivables and inventory against sales.** Revenue rose about 40% from 2017 ($9,737M) to 2025 ($13,651M); receivables
  rose 17% and inventory 44%. Inventory runs at about a quarter of revenue in every year: the business carries roughly
  $3.4B of stock to sell $13.7B. No build-up out of line with sales until H1 2026, when receivables rose $270M.
- **Payables.** Payables rose from $942M (2018) to $2,108M (2025), from a third of inventory to 62% of it. Of the 2025
  figure, $481M sat in supply chain finance programmes in which "The financial institutions participate in the supply chain
  financing initiative on an uncommitted basis and can cease purchasing receivables from our suppliers at any time" (10-K
  note 17). Over 2021 to 2025 the payables increase (+$954M on the cash-flow statement) roughly paid for the inventory
  increase (-$808M), so the five-year owner-cash mean is not inflated by net working capital (net about +$100M over five
  years); but the funding of a quarter of a year's sales of stock now leans on suppliers' banks, and H1 2026 showed it
  running back ($288M out).
- **Debt.** $3.4B (2017) to $4.3B (2018, Stahlgruber) to $2.8B (2021) to $4.3B (2023, Uni-Select, $2,225M cash) to $3.7B
  (2025) and about $4.0B at June 2026, plus $1.4B of operating lease liabilities. A $500M term loan matures January 2027
  (current at June 2026, $545M current portion); $1.1B falls due in 2028. Covenant leverage 2.4x at 2025 year-end (10-K),
  2.8x at June 2026 (8-K `0001065696-26-000041`), against a 4.0x maximum.
- **What they can't say.** The figures cannot say whether the 2024 to 2026 fall in earnings is the claims cycle and a
  German system failure, or the castle; that is Q2's question.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own LKQ "if the market closed for five years"
**[M1997-109]**; the price of $22.41 is information about prices only, "It just tells us prices." **[M2006-077]**, and the
strategic review and a possible sale of the company (8-K `0001065696-26-000002`) are a next-buyer story the run does not
count. No macro view enters, "we just don’t get into the macro factors" **[M2000-094]**: the repair cycle, insurance premiums and tariffs are read only as properties of this business. The analyst's habits govern the method: look for "what’s wrong in things" **[M2025-013]**, ask "What do I
not know that I need to know?" **[M1999-129]**, use competitors and the record "to possibly reject your original
hypothesis" **[M1998-144]**, and "destroy our previous ideas" **[M2016-054]** (the July 2026 v4-era file on LKQ, seen by
name only, is such an idea). **Contrary evidence, written down as found**, "write it down in the first 30 minutes" **[M1997-127]**:
1. (against the business) Europe organic parts and services revenue fell 4.3% in 2025 "driven by decreased volumes due to
   heightened competition in certain markets" (10-K Item 7), and 12.6% in Q2 2026 (10-Q).
2. (against) The filer on Europe: "We face significant competition across many of our markets, where even smaller
   participants can compete effectively on price and service" (10-K Item 1).
3. (against) North America 2025: "higher other input costs not fully offset by price increases due to market
   competition" (10-K Item 7).
4. (against) Consolidated operating margin 12.1% (2010) to 7.3% (2025), while O'Reilly's rose 13.2% to 19.5% (Q2 table).
5. (for the business, found and written down the same way) Q2 2026: "record alternative-parts utilization of over 40%"
   and North America "returned to positive organic growth for the first time in nine quarters" (8-K
   `0001065696-26-000041`).
6. (for) North America segment EBITDA margin held 12.7% to 13.7% from 2012 to 2019 and 14.1% in H1 2026: across the span it
   has not collapsed.
7. (against the cash figure) H1 2026 operating cash $55M; trailing owner cash $560M against a five-year mean of $843M.

## THE STANDING RULE
Bought for cash with no borrowed money and sized so that no outcome at LKQ touches what the buyer has and needs, the
purchase puts the buyer at no risk of ruin: "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Passes; the
company's own debt is Q9's matter (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]** (the transcript's spelling). The work is "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **The business, from the 10-K (Item 1, `0001065696-26-000012`).** A distributor of non-OEM replacement parts: in North
  America, aftermarket collision parts (largely made in Taiwan), salvage parts dismantled from total-loss vehicles bought at
  auctions, remanufactured engines and transmissions, and paint and body supplies, sold to collision and mechanical repair
  shops; in Europe, aftermarket hard parts (brakes, clutches, filters, electrical, steering) through Euro Car Parts (UK),
  Rhiag (Italy), Stahlgruber (Germany) and Benelux businesses, sold mainly to independent garages; Specialty (RV, marine,
  truck accessories), now in a sale process. Self Service was sold in 2025.
- **The key variables and whether they are foreseeable.** (1) The number of repairable collision claims and the share
  insurers steer to alternative parts; (2) the age and powertrain mix of the vehicle parc (Europe sells parts "used in the
  repair of vehicles between 3 and 15 years old"); (3) OEM restrictions (design patents, telematics, certified-shop
  programmes, price matching), which the filer says are "increasing over time"; (4) the competitive structure of European
  independent parts distribution; (5) tariffs on Taiwanese parts. All five are written in the filer's own risk factors and
  all move slowly: the parc a decade out is largely the cars already registered, and EVs remove engine and transmission
  parts only as the fleet turns over. This is slow change, which "can be much harder to perceive, and can lull you to
  sleep easier" **[M2014-038]**, but it is not the fast-moving technology the routing sends to TOO HARD here. The test is whether "the financial statements will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**; they do in kind: fifteen years of segment revenue, organic growth and margin
  are filed (Q2 tables). The doubt test, "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**, was put: the doubt that remains is about the castle, which Q2
  owns, not about what the economics are made of.
- **VERDICT: IN.** The economics can be described and their drivers are "important and knowable" **[M2006-076]**; an
  insider in parts distribution would write a ten-year parc and claims forecast down, unlike the forecast the speakers
  call "That’s too hard." **[M2000-105]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? [...] What are the key factors? And how permanent are they?"
**[M1995-038]**, knowing that "there are going to be marauders. And they’ll never go away." **[M2017-012]**.

**The fifteen-year record, from the filer's own 10-Ks.** Organic growth in parts and services revenue, and Segment EBITDA
margin, by segment (North America includes Self Service until the 2022 10-K split it out; the figures are as each 10-K
first printed them).

| year | NA organic | Europe organic | Specialty organic | total organic P&S | NA EBITDA margin | Europe EBITDA margin | Specialty EBITDA margin | source 10-K |
|---|---|---|---|---|---|---|---|---|
| 2010 | | | | 6.6% | | | | `0001193125-11-047657` |
| 2011 | | | | 7.9% | | | | `0001193125-12-081978` |
| 2012 | | | | 6.0% | 12.9% | 10.6% | | `0001065696-15-000007` |
| 2013 | 6.0% | 31.8% (UK branch openings) | | 11.0% | 12.8% | 11.3% | | `0001065696-15-000007` |
| 2014 | 6.1% | 16.1% | | | 13.3% | 9.1% | 9.8% | `0001065696-15-000007` |
| 2015 | 5.6% | 9.2% | 7.8% | | 13.2% | 10.1% | 10.1% | `0001065696-16-000076` |
| 2016 | 2.9% | 7.2% | 6.9% | | 13.3% | 9.7% | 10.4% | `0001065696-17-000005` |
| 2017 | 3.0% | 5.3% | 4.7% | | 13.7% | 8.8% | 10.9% | `0001065696-18-000004` |
| 2018 | 5.7% | 2.9% | 4.6% | | 12.7% | 8.1% | 11.4% | `0001065696-19-000010` |
| 2019 | 0.9% | 0.1% | -0.7% | | 13.7% | 7.8% | 11.0% | `0001065696-20-000008` |
| 2020 | -13.3% per day | -6.9% per day | 3.0% | -7.6% | 16.8% | 7.8% | 10.8% | `0001065696-21-000010` |
| 2021 | 5.8% | 6.2% | 20.2% | 7.9% | 18.3% (wholesale NA 17.6%) | 10.2% | 12.0% | `0001065696-22-000006`, `0001065696-23-000008` |
| 2022 | 11.4% | 5.1% | -9.9% | 5.0% | wholesale NA 18.7% | 10.2% | 11.1% | `0001065696-23-000008` |
| 2023 | 8.2% | 6.9% | -10.1% | 4.7% | 18.5% | 9.7% | 8.0% | `0001065696-24-000009` |
| 2024 | -5.6% | 1.2% | -4.5% | -2.2% | 16.6% (restated 16.3%) | 9.9% | 6.8% | `0001065696-25-000015` |
| 2025 | -2.3% | -4.3% | 2.3% | -2.7% | 14.4% | 9.3% | 6.5% | `0001065696-26-000012` |
| H1 2026 | Q2 +0.5% | Q2 -12.6% | | H1 -3.4% | 14.1% | 7.6% | 5.7% | `0001065696-26-000044` |

The 2021 to 2023 growth was mostly price: the filer says "primarily driven by pricing initiatives which focused on
offsetting inflation on input costs" (NA 2022, 2023) and "pricing initiatives across all geographies" (Europe 2023).

**The castle tests, each with its filing fact.**
1. **Key factors and their permanence**, "how permanent are they?" **[M1995-038]**. North America: the filer believes it "operates the largest
   distribution network of alternative vehicle parts and accessories serving the vehicle collision and mechanical repair
   markets in North America", with salvage yards on one inventory system (LKQX) and insurer programmes. Europe: "the
   broadest and largest footprint in the European aftermarket industry". The reason the North American customer comes is
   price: insurers prefer alternative parts because of "lower repair costs, reduced repair times and lower associated
   rental-car expenses". Permanence: insurer arrangements "may be terminated by them at any time" (10-K Item 1A).
2. **The money test**, "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]**. In Europe the attack is already being made with less than money: "even smaller
   participants can compete effectively on price and service", and "local companies have formed cooperative efforts to
   compete in our industry" (10-K). Genuine Parts runs the same model in Europe (AAG, 2,617 locations) at the same margin
   (competitor row). In North America the salvage-plus-aftermarket network would be hard to rebuild, but the majority
   holder of the market is not an attacker to be kept out; it is the OEM, which supplies "a majority of collision parts
   by dollar amount" and is "able to exert pricing pressure in the marketplace" (10-K Item 1A).
3. **Pricing power**, "the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. North America 2025: gross margin fell on "higher other
   input costs not fully offset by price increases due to market competition", and on "the dilutive effect of increasing
   prices to recoup tariff costs". Against the OEM: "We compete with the OEMs primarily on price". The OEM's price matching
   on the very parts LKQ sells is named in the risk factors. This is the failing answer: the price is set by the field,
   as "whatever he charged for gas was my price" **[M2012-109]** and "he determined our profit, because we looked at his
   price every day" **[M2023-079]**.
4. **The low bid**, "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. LKQ is the low bid; that is its proposition to
   insurers. Among alternative-parts suppliers the European customer buys on "price and service". The rows' failing answer
   fits the European garage: "most insureds don't care from whom they buy" **[L2004-003]**.
5. **The low-cost position, the commodity exception.** "Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**; "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**. The low-cost claim would show as a margin above peers that
   widens with scale. Europe went from $1.26B of parts revenue at 11.3% Segment EBITDA margin (2013) to $6.3B at 9.3%
   (2025) and 7.6% (H1 2026) after buying Sator, Rhiag, Andrew Page and Stahlgruber: scale lowered the margin. GPC's
   International Automotive segment earned 9.3% in 2025 against LKQ Europe's 9.3%. No low-cost position is shown.
   "commodity businesses have risk unless you’re the low-cost producer, because the low-cost producer can put you out of
   business" **[M1997-010]**.
6. **Unit volume and share of mind.** Volumes fell: North America organic -5.6% (2024) and -2.3% (2025), Europe -4.3%
   (2025), with pricing carrying 2021 to 2023. For the business: alternative-parts utilization "over 40%", a record, in
   Q2 2026; the claims fall in 2024 and 2025 is tied by the filer to "lower repairable claims".
7. **Ask the competitors.** GPC names LKQ among its "Key competitors in North America" (GPC 10-K FY2025,
   `0000040987-26-000003`); no competitor states which rival it fears; not available from the public record.
8. **Widening or narrowing**: "whether it’s likely to widen further or shrink on you" **[M1999-108]**; "the competitive position of each of our businesses grows either weaker or stronger" **[L2005-010]**; "could the competitive advantage have been made stronger and more durable" **[M2000-075]**. Every segment is narrower now than in 2021
   to 2023: North America 18.7% to 14.1%, Europe 10.2% to 7.6%, Specialty 12.0% to 5.7% (Specialty goodwill impaired $52M
   in 2025). Over the whole span Europe has "lost still another notch" **[L1995-023]** twice (11.3% in 2013, 7.8% in 2019,
   9.3% in 2025); consolidated operating margin went 12.1% (2010), 10.6% (2012), 8.9% (2016), 7.2% (2019), 12.4% (2022),
   7.3% (2025), mostly by mix as lower-margin Europe was bought, and the mix is the business on offer.
9. **What could** "destroy, or modify, or reduce the economic strengths that we perceive currently exist in a business" **[M2000-014]**. Named by the filer: OEM design patents and trademarks,
   telematics data withheld, software that "prevents them from being recycled", certified-shop programmes "that, in some
   cases, require the repair shops to use only OEM parts"; accident-avoidance systems reducing "the number and severity of
   accidents"; EVs, since "Engines and transmissions represent some of our largest revenue generating SKUs in North
   America, and parts for engines and transmissions represent a significant amount of the revenue of our European
   operations"; a salvage supply controlled by "a small number of companies" that could raise fees. "one competitor is
   frequently enough to ruin a business" **[M2012-108]**, and here the competitor with the majority share and the
   pricing pressure is the OEM.

**The competitor row** (same metric, competitors' own filings; operating income over revenue unless stated).

| company | metric | start of span | end of span | accession |
|---|---|---|---|---|
| LKQ | operating margin | 12.1% (FY2010: $298M on $2,470M) | 7.3% (FY2025: $993M on $13,651M) | `0001193125-11-047657`; `0001065696-26-000012` |
| O'Reilly (ORLY), NA mechanical parts | operating margin | 13.2% (FY2010) | 19.5% (FY2025: $3,461M on $17,782M) | `0001193125-11-049998`; `0000898173-26-000009` |
| Copart (CPRT), salvage auctions, LKQ's supplier of total-loss vehicles | operating margin | 30.9% (FY Jul-2010) | 35.4% (FY Jul-2026: $1,653M on $4,666M) | `0001145443-11-001073`; `0001193125-26-405731` |
| Genuine Parts (GPC), NAPA and Europe's AAG | segment EBITDA margin, 2024 to 2025 only (segments re-cut at 2025) | NA Automotive 7.8%, International Automotive 10.2% (2024) | NA Automotive 7.1%, International Automotive 9.3% (2025) | `0000040987-26-000003` |
| LKQ, same years | Segment EBITDA margin | NA 16.3%, Europe 9.9% (2024) | NA 14.4%, Europe 9.3% (2025) | `0001065696-26-000012` |
| Boyd Group | not SEC-registered; a collision-repair operator (a customer, not a competitor); not fetched | | | flagged |
| OEM dealer parts businesses | not separately reported in any filing found; not obtained | | | flagged |

Read across the span: O'Reilly widened its margin by six points while LKQ's fell by five; Copart, which sells LKQ its
salvage input, kept a margin between 24% and 39% in every year of the span; GPC's European business earns what LKQ's earns. LKQ's North American
margin is above GPC's North American automotive margin (different mix: collision and salvage against mechanical), which is
the best evidence of a North American advantage.

**The case for the castle, stated as its holder would**, "to be able to state their case better than they can" **[M2016-055]**. North America is the largest alternative-parts
network on the continent; it held a 12.7% to 13.7% margin through 2012 to 2019 and is at 14.1% in a claims trough; insurers'
incentive to use cheaper parts is permanent, and utilization hit a record over 40% in Q2 2026; the 2024 and 2025 volume
fall is the claims cycle after premium increases, which the filer says is easing, with insurance premiums "negative in May and June" 2026 and "continued sequential improvement in repairable claims"; Europe's H1 2026 fall is
a German ERP failure, which is a self-inflicted wound, not a competitor's win; the Specialty segment, the weakest, is being
sold. On this reading the castle is narrow but standing, and the right box is TOO HARD (WORK) on North America.

**Why the case does not carry.** (a) The business offered is the whole company, and 46% of its revenue (Europe) shows the
open castle on the evidence: the filer's own words that smaller rivals compete effectively on price, a margin that fell as
scale rose, organic declines attributed to "heightened competition" before the ERP problem began, and no margin advantage
over the one listed peer doing the same thing. (b) The North American part fails the pricing test in the filer's 2025
words, and its dominant rival, which supplies the majority of collision parts, sets price pressure and is increasing its
efforts "over time". (c) The record, read for its turn: "you do not want to have something whose competitive position is
going to erode over time" **[M2007-117]**; "If we can think of very much that can go wrong with them, we just forget it."
**[M2000-016]**; and the improvements of one participant pass to the next, "the improvement you get one day, your
competitor gets the next day" **[M2004-053]**, which is what the European margin record shows. (d) The cheap price does
not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "If you
really think a business is declining, most of the time you should avoid it." **[M2012-062]**.

OUT or TOO HARD: a castle shown on the evidence to be filling in closes OUT, "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; a castle whose future cannot
be judged closes TOO HARD, "We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. Europe is
not a castle whose future cannot be judged; fifteen years of its own filings judge it. North America alone would be the
second kind. The file is closed on the whole as offered.

- **VERDICT: OUT** at Q2, of the three boxes "in, out, and too hard" **[M2006-013]**: the European half of the business is
  a scale distributor in a field where, in the filer's words, smaller participants compete effectively on price, with no
  low-cost advantage shown over its fifteen-year record or against its peer; the North American half has a narrower,
  older castle whose pricing answer failed in 2025 against a majority competitor, the OEM. Not an error of omission inside the circle, which the row
  defines as "when it’s something we understand, and we stand there and stare at it, and we don’t do anything" **[M2001-006]**:
  the business is understood, and what is understood is the open castle.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (closed at Q2).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion; otherwise WEIGHING.
NOT REACHED. The balance-sheet reading the template requires is in Step 0.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED (operator rule 2; the proxy was read and nothing from it is reported).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## COMPUTATION - NOT A CLEARANCE
*(Operator rule 3: valuation arithmetic after a closing STOP, at the owner's request; no entry language; Q7 to Q10 are not
reached and nothing below is a verdict. The heading uses a hyphen where the protocol's text has a dash, under the
no-em-dash rule.)*

**(a) VALUE RANGE, by the Q7 CONVENTION** (Part VI: five-year mean of owner cash after every real cost, carried at the
growth shown and never above it, ten years then no growth, nominal, discounted at the sovereign; the ends are the
no-growth and shown-growth cases; aggregate cash, not per share). The rows behind the convention: owner cash "after
interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**; a range, since "working with a
range of possibilities is the better approach" **[L2000-024]**; the base years read "to be suspicious as to why the beginning and terminal years have been selected" **[L2005-003]**. All at
5.63%, 253.0M shares, `calc.py`:

| case | owner cash X | growth for ten years | value | per share |
|---|---|---|---|---|
| continuing operations, no growth (top) | $843M | 0% | $14,975M | **$59.19** |
| continuing operations, shown growth (bottom) | $843M | -5.2% | $9,958M | **$39.36** |
| as filed (with Self Service), no growth | $895M | 0% | $15,902M | $62.85 |
| as filed, shown growth | $895M | -6.5% | $9,527M | $37.66 |

**Range $39.36 to $59.19 a share against $22.41**; width 1.5 to 1. Owner cash already pays the interest on the $3.7B to
$4.0B of debt, so the equity value is read directly; it assumes the debt is refinanced as it falls due, the assumption the
rows call "usually valid" and then warn on, "Even a short absence of credit can bring a company to its knees."
**[L2010-020]**.

**Whole-cycle variant.** The five-year window holds abnormal years at both ends: 2021 and 2022 carry post-pandemic pricing
and high scrap and precious-metal prices (Self Service earned a 22.3% margin in 2021), and 2025 to 2026 carries the claims
trough and the German ERP failure. Variant: the ten-year mean ratio of owner cash to revenue, 2016 to 2025, is 6.15%;
times 2025 revenue of $13,651M gives $839M, which gives **$39.17 to $58.90**, the same range. Stress variant on the
trailing twelve months to June 2026 ($560M): **$26.14 to $39.31**.

**(b) FAIR PRICE.** The price at or below which the central case clears the ~10% pre-tax floor (the CONVENTION at Q7, from
"a very high probability of at least 10% pre-tax returns" **[L2002-020]** and "there’s just a point at which we drop out
of the game" **[M2003-149]**). Tax treatment: owner cash is after corporate tax, so the floor is converted at LKQ's 2025
effective rate on continuing operations, $204M of tax on $800M of pre-tax income (25.5%), to about 7.45% after tax.
Central case (CONVENTION of this run): growth halfway between the two ends, -2.6% a year for ten years, then flat.
**Fair price $36.96** on the five-year continuing base; **$24.55** on the trailing base. At $22.41 the central case returns
about 12.7% after tax (17.0% pre-tax equivalent) on the five-year base and 8.2% after tax (11.0% pre-tax) on the trailing
base.

**(c) CHEAP PRICE.** Rule (CONVENTION of this run): half the bottom of the range, so that the price is plainly below even
the declining case without arithmetic, the condition the rows put as "It should scream at you." **[M2009-005]** and "it’s
too close to think about" **[M1996-084]** when a pencil is needed, set against "the bottom boundary of our estimate"
**[L2013-012]**. **Cheap price $19.68** ($39.36 / 2). The price, $22.41, sits between cheap ($19.68) and fair ($36.96); on
the trailing base it sits just below fair ($24.55), a case that needs a pencil.

What the computation cannot say: it assumes the owner cash of the last five years declines no faster than it did. With
the castle open in Europe that is the assumption Q2 removed; "we don’t really try to compensate for that sort of thing by
having some extra large margin of safety" **[M2007-022]**.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED (closed at Q2). The figures above are computation only.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED. (Facts for a later reader, not weighed: $545M current debt at June 2026, $1.1B due 2028, $481M of payables in
uncommitted supply chain finance, covenant leverage 2.8x against 4.0x.)

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked.

---
## THE BOX
**OUT**, decided at **Q2**: the European half is shown on fifteen years of the filer's own record and words to be a scale
distributor without a castle, and the North American castle failed its 2025 pricing test against a majority competitor,
the OEM. No research pass is opened (an OUT, not a TOO HARD). For the owner, labelled computation only: value range
$39.36 to $59.19 (whole-cycle $39.17 to $58.90; trailing stress $26.14 to $39.31), fair price $36.96 (trailing $24.55),
cheap price $19.68, against $22.41.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed after each question: the
      dispatch for this run forbade commits (write-early kept in the file only).
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (Python check run, result at the end); every filing fact has its
      accession; numbers carry a filing or are labelled CONVENTION (the Self Service estimate, the central case, the
      cheap-price rule).
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; Q5 output not reported.
- [x] Owner cash after every real cost (OCF less SBC, capex and finance-lease principal), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury, dated; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, "write it down in the first 30 minutes" **[M1997-127]** (foundations list, items 1 to 7, both directions).
- [x] No row dated after the anchor is cited (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS (no commit made; the dispatch forbade it).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no rule for a business whose segments answer the castle question differently.** Q1 carries a CONVENTION for
the holding company read by its parts, with doubt about a part that matters keeping the whole out; Q2 has none. Here
Europe (46% of revenue) is shown open and North America is narrower but standing. The run applied the castle tests to the
whole as offered and closed OUT; an analyst who carried Q1's by-parts reading into Q2 could close TOO HARD (WORK) on North
America instead. A sentence in Q2 is needed. (2) **The template's position note and the run's blind rule conflict:** the
template says check `PORTFOLIO.md`; the dispatch forbids opening it. Position recorded as unknown. (3) **The Q7 convention
does not say what to do with a business sold out of the five-year window**: the Self Service cash had to be estimated for
2021 to 2023 (confessed). (4) **The earnings currency for a company that reports in dollars and earns about two-fifths in
euros and sterling** is not settled: the protocol asks for the sovereign "for the earnings currency"; USD 5.63% was used, a
blend with EUR 3.72% would raise every value above. (5) **When the growth shown is negative**, the convention's "shown
growth" end becomes the bottom of the range and is carried for ten years; whether a decline should be carried ten years or
read as a sign for Q2 is not said. (6) **Fair and cheap prices** are the owner's request, not the framework's; both rules
used here (central case at the floor after tax; half the bottom of the range) are this run's and are confessed. (7) The row that reads "Unless, however, we see a very high probability of at least 10% pre-tax returns"
**[L2002-020]** carries a damaged character in its after-tax figure; the run used only its pre-tax words.

**Checks run after writing.** `python tools/check_framework.py`: PASS. Python check
(`Test Runs/_research 2026-10-05 LKQ/check_ids.py`): no E-ids; 55 distinct M, L and R ids cited, none missing from
`principle_ledger_v5.csv`; 62 quoted fragments beside ids, each found in its row; every id in the file stands directly
after a verbatim fragment of its own row.
