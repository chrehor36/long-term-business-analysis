# Company Run — Innovex International, Inc. (NYSE: INVX) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
`c0fb0184`, "INVX run: template copied before any fetch").

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
INVX, Innovex or Dril-Quip).*

**Dispatched run.** Done by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` with its slots filled (operator
rule 10). The brief departs from the canonical brief in one stated place: the lines of evidence were derived by the analyst
from the 10-K's Items 1, 1A and 7; they are listed in Step 0.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check that this run's file and
folder did not already exist showed the names of seven other run files and research folders dated 2026-10-16 (HMH, NESR,
NGS, NOV, OIS, SEI, USAC); none was opened. NOV is a rival named in the INVX 10-K and is used below only through NOV's own
SEC filings, never through that run file. (2) The session's opening context showed recent commit subjects about the NESR
fold (a box, a range and a fair price for NESR); not about this company, not used. (3) A memory index line in the session
context speaks of a count of gate-clearers and of wave numbers; not about this company, not used. Nothing about INVX,
Innovex, Dril-Quip or DRQ in any run file, register, reading list, portfolio or holding review was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $27.39 (close 2026-10-15; printed by `python tools/run.py INVX`, an aggregator quote, flagged per operator
  rule 5, used for the live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **69,935,827** shares as of the
  10-Q cover (10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0001193125-26-332959`;
  `python Screens/cover_shares.py INVX`). Checked: the balance sheet in the same 10-Q shows 68,875,856 shares issued and
  outstanding at 2026-06-30 (no treasury shares; repurchased shares are retired). The difference, 1,059,971 shares, is
  close to the TCO Group consideration: the 8-K of 2026-06-15 (accession `0001193125-26-270295`) agreed "approximately
  1,063,829" new shares, and the 10-Q records that "The acquisition closed on July 1, 2026". The 8-K filed after the 10-Q
  (2026-08-10, accession `0001193125-26-342567`, a sale of 5,000,000 shares by Amberjack affiliates) issued no shares: "The
  Company did not sell any shares of Common Stock in the Offering". No later count is filed; the cover count is used.
- **Market cap:** $27.39 x 69.936M = **$1,915.5M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (printed by `tools/run.py` from `tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-24, accession `0001193125-26-067228`), Items 1, 1A,
  5, 7 and 8 with both auditors' reports; 10-K for FY2024 (filed 2025-03-03, accession `0000950170-25-031003`); 10-Q for
  the quarter ended 2026-06-30 (filed 2026-08-04, accession `0001193125-26-332959`); proxy (DEF 14A filed 2026-03-27,
  accession `0001193125-26-129169`, fetched, read only for facts recorded after the stop); 8-Ks of 2026-02-27
  (`0001193125-26-082802`), 2026-06-15 (`0001193125-26-270295`), 2026-08-03 (`0001193125-26-330695`) and 2026-08-10
  (`0001193125-26-342567`); the merger prospectus (424B3 filed 2024-08-06, accession `0001193125-24-194905`) for Legacy
  Innovex's audited statements for 2021 to 2023 and its business history; Dril-Quip's 8-K of 2024-07-08 (item 4.02,
  accession `0000950170-24-082091`); Dril-Quip's own 10-K figures 2012 to 2023 through the XBRL company facts, first-filed
  vintage, with accessions (research folder, `facts.py`). **One figure cross-checked against the filed statement:** total
  revenues FY2025, $978,251 thousand on the face of the Consolidated Statements of Operations (10-K FY2025, page F-6),
  against $978.3M in the XBRL facts; they agree. Net cash provided by operating activities FY2025, $190,912 thousand in the
  MD&A table, agrees with the XBRL $190.9M.
- **Which history the statements carry before 2024-09-06.** The 10-K: "Following the Merger, Legacy Innovex became a wholly
  owned subsidiary of Dril-Quip" and the registrant's name changed; but the 2023 column of the statements is audited by
  Grant Thornton as the statements of "Innovex International, Inc. (formerly known as Innovex Downhole Solutions, Inc.)"
  (10-K FY2025, page F-4): revenue $555,539K, 30,928,647 weighted shares (Legacy's 15,368,503 shares times the 2.0125 exchange
  ratio). The merger produced a "Bargain purchase loss (gain)" of $(85,812)K in 2024, "related to the Merger". So Legacy
  Innovex is the accounting acquirer; the filed history before 2024-09-06 is Legacy Innovex alone, and Dril-Quip's own
  history to 2023 sits in Dril-Quip's own 10-Ks under the same CIK. **Treatment:** for the castle (Q2) both histories are
  read, since the business owned today is both; for the value range (Q7 (c), COMPUTATION) the merger, a deal paid in
  shares, is put on the combined companies' own averages, Legacy Innovex plus Dril-Quip for each pre-merger year.
- `python tools/run.py INVX` arithmetic lines: it prints a three-year owner-earnings window of 2021 to 2023 that **mixes the
  two registrants** (2021 OCF $38.4M is Dril-Quip's; 2022 $-5.8M and 2023 $75.9M are Legacy Innovex's, from the later
  filings; capex and D&A for 2022 and 2023 are Dril-Quip's first-filed figures), and it states that D&A and capex are not
  tagged for 2024 and 2025 under the elements it reads. Its window and its yield lines are therefore **not used**; owner
  cash is built from the filed statements under Q7 (COMPUTATION). Its ten-year balance-sheet table is used, read against
  the filings: 2016 to 2023 are Dril-Quip's first-filed balance sheets, 2024 and 2025 the combined company's.
- **The lines of evidence chosen** (the brief's departure; derived from Items 1, 1A and 7 of the FY2025 10-K): (1) one
  reportable segment, with revenue by product family and by geography; (2) margins over the cycle: Dril-Quip 2012 to 2023,
  Legacy Innovex 2021 to 2023, the combined company 2024 to 2026 H1, against Weatherford, NOV and Halliburton over 2016 to
  2025; (3) customers (top ten 26% of revenue, Saudi Aramco the largest end-user, consolidation pressing for "pricing
  concessions") and suppliers (concentration in frac plugs and intervention tools); (4) pricing: "Some jobs are awarded on a
  bid basis", and gross margin through the 2022 to 2023 inflation; (5) acquisitions and goodwill: Rubicon and AOT 2021, Pride
  2022, DWS 2023 and 2024, the Dril-Quip merger 2024, SCF and Citadel 2025, DIS and TCO Group 2026; (6) debt and leases;
  (7) buybacks and their prices; (8) stock pay; (9) litigation and investigations: the Impulse patent verdict against DWS,
  Dril-Quip's 2024 non-reliance 8-K, the former Saudi agent's receivables; (10) the 2024 dividend of $75.0M and the Amberjack
  sales of 2026.

**The balance sheets, eight to ten years, read here because the file closes before Q4** (`tools/run.py` table, checked
against the face of the 10-K FY2025 and the 424B3 for Legacy Innovex; USD millions):

| year-end | registrant | total assets | equity | cash | receivables | inventory | goodwill | intangibles | debt and finance leases | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | Dril-Quip | 1,461 | 1,356 | 423 | 214 | 355 | 34 | 30 | none | 1,501 |
| 2018 | Dril-Quip | 1,193 | 1,096 | 418 | 202 | 191 | 8 | 35 | none | 1,206 |
| 2020 | Dril-Quip | 1,151 | 1,042 | 346 | 116 | 213 | none | 29 | none | 1,125 |
| 2021 | Dril-Quip | 1,010 | 897 | 355 | 101 | 146 | none | 26 | none | 973 |
| 2023 | Dril-Quip | 1,028 | 881 | 187 | 136 | 195 | 17 | 42 | not tagged | 951 |
| 2022 | Legacy Innovex | 436.3 | 251.3 | 8.4 | 123.8 | 136.7 | 23.9 | 49.8 | 89.1 | 72.0 |
| 2023 | Legacy Innovex | 475.3 | 328.9 | 7.4 | 118.4 | 141.2 | 23.9 | 41.8 | 50.4 | 145.9 |
| 2024 | Innovex, combined | 1,197.5 | 958.2 | 73.3 | 239.5 | 271.2 | 60.2 | 108.4 | 35.4 | 211.3 |
| 2025 | Innovex, combined | 1,268.3 | 1,057.7 | 203.4 | 237.8 | 248.4 | 99.7 | 116.2 | 25.6 | 285.3 |
| 2026-06-30 | Innovex, combined | 1,327.7 | 1,058.5 | 222.1 | not read | not read | not read | not read | 25.1 | 279.5 |

What they say. **Dril-Quip** carried no debt and a large cash balance throughout, and its equity fell from $1,356M (2016)
to $881M (2023) while retained earnings fell from $1,501M to $951M: about $550M of retained earnings gone in seven years to
losses and buybacks, the balance sheet of a business that stopped earning. **Legacy Innovex** was small and borrowed before
the merger (debt and finance leases $89.1M against equity $251.3M at 2022; $50.4M against $328.9M at 2023), with
receivables and inventory together about 47% of 2023 revenue. **The combined company** is debt-light (debt and finance
leases $25.6M at 2025 and $25.1M at 2026-06-30, against cash of $203.4M and $222.1M); receivables of $237.8M are 24% of
2025 revenue and inventory of $248.4M a further 25%, so working capital, not plant, is where the capital sits:
"Historically, capital expenditures have been relatively modest, with working capital being the predominant use of cash"
(10-K FY2025, Item 7). The receivables of 2024 were stated after an allowance of $63,875K, cut to $19,752K at 2025 (face of
the balance sheet), and the 10-K credits a $10.4M fall in bad-debt expense to "recoveries of outstanding receivables from our
prior agent in Saudi Arabia". A net deferred tax asset of $102.4M rests largely on a net operating loss carryforward of
$457.3M (Item 1A). Retained earnings of $285.3M are Legacy Innovex's; the bargain-purchase accounting carried Dril-Quip in
below the fair value of its net assets. After 2025-12-31 a "Legal settlement accrual" of $51,607K appears (10-Q, the Impulse
verdict).

## THE FOUNDATIONS (not a gate)
Three foundations bear here. **A share is a business:** "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**; the question is put to the business at Q1 and Q2, not to the quotation, which has risen from the
$14.89 average the company paid for its own shares in the first half of 2025 to $27.39. **Who is paid to tell you:** the
10-K's framing (a TAM of "approximately $8.0 billion", "Big Impact, Small Ticket", a "through-cycle playbook" to
"outperform in all market environments") and its Rystad Energy forecasts are the seller's words: "you do not get impartial
advice from Wall Street" **[M2020-037]**; projections are not used: "we’ve never looked at a projection in connection with
either a security we’ve bought or a business we’ve bought" **[M1995-050]**. The merger prospectus's projections ("Innovex’s
Projections", 424B3) were not read, for that reason. **No macro forecast enters:** "macro conclusions are — just never enter
into the discussion" **[M2000-094]**; the oil price and the rig count are not forecast here; they enter only as the cycle
the filings already show. **Contrary evidence, written down as found** **[M1997-127]**: (1) Dril-Quip, now about a third of
revenue (Subsea Solutions 24% and Surface Wellheads 8% of 2025 revenue), earned operating margins near 30% in 2014 and 2015
and then lost money in four of the next eight years and earned about 1% in three more; (2) the 10-K: "Some jobs are
awarded on a bid basis" and "Pricing is one of the primary factors in determining which qualified contractor is awarded a
job"; (3) "The market is also fragmented and includes numerous small companies capable of competing effectively in our
markets on a local basis"; (4) "some of our largest customers have consolidated and are using their size and purchasing
power to seek economies of scale and pricing concessions"; (5) a jury found DWS's infringement of Impulse's patents willful
and awarded $47.6M; (6) Dril-Quip's 2021 statements were declared not to be relied upon in July 2024; (7) Legacy Innovex
earned 4.8% on revenue in 2021, its only filed year near a trough.

## THE STANDING RULE
The buyer's conduct, not the target's. A part-interest bought for cash, without borrowed money, sized so that no fall in the
quotation forces a sale, puts the buyer at no risk of ruin from this name: "borrowed money has no place in the investor's tool
kit" **[L2014-005]**; "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**.
Nothing in INVX's own structure (debt and finance leases $25.1M against cash $222.1M) reaches the buyer; the target's own
exposures are Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]** ("asses" is the transcript's spelling); the product may stay opaque if "I understand the economic
  dynamics of the industry" **[M2011-014]**.
- **What the business is, from the filings.** A maker, renter and installer of engineered, mostly consumable, downhole and
  wellhead products (centralizers, float equipment, liner hangers, toe sleeves, frac plugs, fishing tools, ESP penetrators,
  surface and subsea wellheads), sold mainly to the E&P operator; revenue 2025 $978.3M, about 70% products, 17% rentals, 13%
  services; NAM 52%, International and Offshore 48% (10-K FY2025, Item 1). "We believe that demand for our products is
  primarily activity-driven", measured by "the number of wells drilled and oil and natural gas production volumes"
  (Item 1). One reportable segment.
- **The key variables and whether they are foreseeable.** Three: the number of wells drilled and completed (the activity
  that consumes the products), the company's share of the spend per well, and the price per item against the cost to make
  it. The first is set by the oil and gas price, which the rows do not forecast: "We don’t think we can predict commodity
  prices" **[M2016-025]**; under the framework's commodity-business paragraph a dependence on a commodity price is never by
  itself a STOP at Q1, and the business is read "off the figures" **[M2008-069]**. The figures exist: Dril-Quip's own 10-Ks
  from 2012, Legacy Innovex's audited statements from 2021, the combined company's from 2024. The second and third
  variables are the castle question, Q2's: whether share and price hold against Baker Hughes, Halliburton, SLB,
  Weatherford, NOV and "numerous small companies".
- **Technology.** The products are mature mechanical consumables; the 10-K names 769 patents and a product pipeline and says
  "To compete in our industry, we must continue to develop new technologies and products". No change in the products fast
  enough to put the ten-year economics out of sight is shown in the filings; what technology could do to the castle is
  weighed at Q2 (test 11), not here **[M1998-008]**.
- **Routing.** Not a fast-changing industry closing here; not a bank; not a holding company (one segment; the product
  families are reported by revenue only, with no profit by part).
- **Doubt, stated.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
  The doubt here is not whether the economics can be pictured but what they show: a supplier of consumables whose volume
  follows a commodity cycle and whose price is contested, with a filed record that includes a full cycle for one of its two
  halves. That is an answerable question, and it is the castle question.
- **VERDICT: IN.** The economic dynamics can be read from the figures **[M2011-014]**, **[M2008-069]**; the commodity
  dependence is not a Q1 STOP by the framework's commodity paragraph; where the earning power and competitive position will
  stand **[M2012-065]** is answered at Q2, and the edge can be judged: "if we can’t understand it, obviously, [...] we can’t
  make a decision as to whether it has a sustainable edge" **[M1997-148]** does not apply.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat is what "protects
excellent returns on invested capital" **[L2007-004]**.

**The castle tests, each with its filing fact.**
- **The attacker with money (test 3).** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
  could I do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The filer answers it itself:
  "The market is also fragmented and includes numerous small companies capable of competing effectively in our markets on a
  local basis, as well as several large companies that possess substantially greater financial and other resources than we
  do. [...] our larger competitors may offer products at below-market prices or bundle ancillary products and services at no
  additional cost to our customers" (10-K FY2025, Item 1A). A field in which small local makers compete effectively is one of
  the industries "that are just never going to have barriers to entry" **[M2012-106]**; the company's own history shows the
  door: Legacy Innovex "was formed in 2016 through the combination of three consumable products companies" and has bought
  Buckhorn, QCI, Rubicon, AOT, Pride, DWS, SCF, Citadel, DIS and TCO since (424B3, 10-K FY2025, 10-Q), each a maker that
  entered the field and found a market. **Fails.**
- **Would the customer still choose it over the low bid (test 8).** The rows ask whether it would be "a question of people
  buying candy for the low bid" **[M2017-009]**; the failing answer is "most insureds don't care from whom they buy"
  **[L2004-003]**. The filer: "Some jobs are awarded on a bid basis, which further increases competition based on price.
  Pricing is one of the primary factors in determining which qualified contractor is awarded a job." (Item 1A). It also
  claims the opposite, "we believe our customers select our products and services based on the technical attributes of our
  products" (Item 1), and "Big Impact, Small Ticket"; the claim is the seller's, the bid basis is the filing's own risk
  statement. The Precision Castparts kind of supplier, "where people don’t simply just take the low bid in order to get this
  gadget" **[M2016-006]**, is not what the filing describes. **Fails on the filer's own words.**
- **Pricing power and the agony before a rise (test 4).** "you can almost measure the strength of a business over time by
  the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. The filer: "The pace
  of inflationary changes can also occur more quickly than our ability to respond with corresponding price increases" and
  "A significant price increase in or the unavailability of raw materials may result in a loss of customers" (Item 1A); and
  "some of our largest customers [...] are using their size and purchasing power to seek economies of scale and pricing
  concessions" (Item 1A). For the other side, written down as found: Legacy Innovex's gross margin (revenue less cost of
  sales before depreciation) rose through the 2022 to 2023 inflation, 29.6% (2021), 33.6% (2022), 35.1% (2023) (424B3, F-5),
  and the combined company's was 35.2% (2024), 31.0% (2025) and 34.7% (2026 H1) (10-K FY2025 F-6; 10-Q); but those were
  rising-activity years, and "over time the businesses with strong competitive positions manage to pass through increases"
  **[M2005-017]** is a test over time, which a single upswing does not pass. **Weighs against; not shown either way across a
  downturn for the Legacy half.**
- **The low-cost position (test 6), and the commodity exception.** In a field where price decides bids, the way through is
  to be the low-cost producer, "commodity businesses have risk unless you’re the low-cost producer, because the low-cost
  producer can put you out of business" **[M1997-010]**, measured against rivals, "you could spot differences in them. [...]
  The figures are available." **[M2009-059]**. The filings give no unit cost against rivals; the margins below are the only
  comparison they allow, and on them INVX is not the low-cost producer of its field over the cycle: its combined margin
  sits below Weatherford’s in each of 2023 to 2025 and below Halliburton’s in 2023 and 2024 (table below). The SCF purchase was made "to grow Innovex’s
  low-cost country supply chain" (Item 1), an effort toward cost, not a shown position. **Not shown.**
- **Unit volume and share of mind; the brand (tests 5 and 7).** The products are bought by the E&P operator's engineers,
  per well; the filer estimates its share at about 15% of a NAM TAM and 10% elsewhere, figures of its own construction
  ("an illustrative price per applicable product" times wells, Item 1). No customer asks for it by name in any filing read;
  "When we sell to service companies, it is typically to fill a gap in their product portfolio or because they have been
  directed by the E&P operator to utilize our products" (Item 1) is the nearest. **Not shown.**
- **Would it stand without the lord (test 2).** The 10-K credits a "No Barriers" culture and says "We rely on a few key
  employees whose absence or loss could adversely affect our business" (Item 1A). Not decisive here.
- **Ask the competitors (test 9).** Not done; no scuttlebutt is on the public record beyond the rivals' filings, read below
  **[M1998-144]**.
- **Widening or narrowing (test 10), and what could destroy it (test 11).** "whether it’s likely to widen further or shrink
  on you" **[M1999-108]**; "what can happen — say five, 10, 15 years from now — that will destroy, or modify, or reduce the
  economic strengths" **[M2000-014]**. The half of the business that has a full filed cycle is Dril-Quip's, and its record
  answers the question: operating margin 22.1% (2012), 25.6%, 29.9%, 29.5% (2015), 21.0% (2016), then -15.2% (2017),
  -31.9%, 0.7%, -17.4%, -38.6% (2021), 0.7%, 1.3% (2023) (Dril-Quip 10-Ks, first-filed XBRL; 2021's restatement moved $67M of
  inventory write-downs from restructuring into cost of sales and left operating income unchanged). A castle that earned
  about 30% on sales and then earned nothing for eight years is the "Roman Candle" of **[L2007-004]**, a castle crossed.
  Dril-Quip's lines are Subsea Solutions (24% of 2025 revenue) and Surface Wellheads (8%) (Item 7); the subsea tree line
  was sold in 2025. The filer's customers are consolidating (Item 1A), and the 10-K's own risk factors name "Conservation
  measures, commercial development and technological advances" and the transition from fossil fuels as threats to demand;
  "slow change can be much harder to perceive" **[M2014-038]**. **Narrowed, on the evidence, for the Dril-Quip half.**

**The competitor row**, same metric from the competitors' own filings: operating income over revenue, as filed (10-K XBRL,
latest-filed vintage; accessions in `facts.py` output, e.g. Weatherford `0001603923-26-000014`, NOV `0001193125-26-048350`,
Halliburton `0000045012-26-000015`). **Which three and why:** the 10-K names "Baker Hughes, Halliburton, Schlumberger,
TechnipFMC, Weatherford International, Aker Solutions, and NOV". Taken: **Weatherford** (its well construction, completions
and intervention lines make float equipment, centralizers, liner hangers and fishing tools, the closest overlap with the
Legacy Innovex product families), **NOV** (a maker of downhole tools and wellbore consumables sold to the same operators,
an equipment maker rather than a service company) and **Halliburton** (completion tools and a large completions business;
the largest product-and-service rival on the Legacy side). Not taken: TechnipFMC (closest to the Dril-Quip subsea half, a
third of revenue; its record would be a fourth line), SLB and Baker Hughes (broad conglomerates in which these products are
a small share). **Flagged: Aker Solutions does not file with the SEC** (listed in Oslo); not read.

| operating margin | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | span total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Weatherford | -39.1% | -38.1% | -36.3% | not tagged | -40.3% | 3.2% | 9.5% | 16.0% | 17.0% | 15.4% | -11.1% (9 yrs) |
| NOV | -33.3% | -3.8% | 2.5% | -74.1% | -39.8% | -2.4% | 3.6% | 7.6% | 9.9% | 5.6% | -11.8% |
| Halliburton | -42.6% | 6.7% | 10.3% | -2.0% | -16.9% | 11.8% | 13.3% | 17.7% | 16.7% | 10.2% | 4.4% |
| Dril-Quip (to 2023) | 21.0% | -15.2% | -31.9% | 0.7% | -17.4% | -38.6% | 0.7% | 1.3% | merged | merged | -7.9% (8 yrs) |
| Legacy Innovex (filed from 2021) | not filed | not filed | not filed | not filed | not filed | 4.8% | 16.4% | 17.5% | merged | merged | 14.3% (3 yrs) |
| Innovex combined (reported) | | | | | | -17.9% (sum of both) | 9.5% (sum) | 10.5% (sum) | 7.4% | 13.6% (9.5% without $39.8M of asset-sale gains) | |

(Span totals are total operating income over total revenue for the years shown. The combined 2021 to 2023 figures add the
two registrants' filed revenue and operating income: 2021 $617.7M and $-110.7M; 2022 $829.3M and $79.1M; 2023 $979.6M and
$102.7M. 2024 is as reported, Dril-Quip consolidated from 2024-09-06 only. 2026 H1: operating income $12.0M on $483.9M,
after the $51.6M Impulse provision and $11.9M of asset-sale gains; about 10.7% without both, 10-Q.)

**The parts table.** Not applicable as the framework writes it: the filer reports one segment and gives revenue, not profit,
by product family (Item 7, "We operate in one reportable segment"). The two halves are read through their own filed
histories above; neither can be shown to carry more than half of five-year operating profit, since Dril-Quip's five-year
operating profit before the merger was negative.

**The field's returns over the last full cycle**, from the filer's and the rivals' filings, judged in words, no figure (the
convention of section C). The cycle runs from the 2014 peak through the 2016 and 2020 troughs to the 2023 to 2025 recovery.
Over it, Weatherford and NOV lost money in total and went through a restructuring (Weatherford's 2019 is untagged across
its fresh start); Halliburton, the strongest of the three, earned about 4% on revenue over ten years and less than 2% over
2016 to 2023. Dril-Quip, the filer's own predecessor registrant, went from about 30% to losses and stayed there. Legacy
Innovex has no filed trough year except 2021, when it earned 4.8%. The durable players of this field earn ordinary returns
over a full cycle, or worse; the excellent returns of the recovery (the rivals' 15% to 18% in 2023 and 2024) are the
recovery, not the castle. "you can have only two competitors and they’re still terrible businesses, they beat each other’s
brains out" **[M2013-052]**.

**A change for the better?** The case for INVX is that Legacy Innovex is a different business from the field: consumables,
capital-light, 16% to 17% margins in 2022 and 2023, rising share. The framework credits such a change "only on the evidence
of a full cycle in which the price behaviour held" (section C), and that evidence is not filed for Legacy Innovex: its only
filed weak year earned 4.8%, and since the merger the combined margin has run near 10% without one-off gains in an
activity level the 10-K itself calls declining in NAM ("a continued reduction in drilling activity in North America"). Were
this the whole case, the file would close TOO HARD (NATURE) with a dated re-look. It is not the whole case: the filer's own
words put price first in the bids it wins, admit effective local competition and customers who press for concessions, and a
third of the business today is the castle whose fall the filer's own registrant history shows. The question is answered on
the evidence, not left open.

**VERDICT: OUT.** A standing castle that protects only ordinary returns, on the evidence of the filer's and the rivals' own
filings, closes OUT (the framework's list under Q2, section C): the field's durable players earned ordinary returns or
losses over the last full cycle **[L2007-004]**, **[M2013-052]**; the filer's own risk statements say its work is won on
price against rivals large and small **[L2004-003]**, **[M2012-106]**, and that its largest customers press it for
concessions **[M2005-020]**; and the part of the business with a full filed cycle is a castle shown crossed, "you do not
want to have something whose competitive position is going to erode over time" **[M2007-117]**. "If the answer had been
yes, we wouldn’t have done it." **[M2011-015]**. Price does not reopen it: "What you can’t do is turn any investment into a
good deal by paying little" **[M2019-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4. Facts found are
under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are under AFTER THE STOP, flagged in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found, including the buyback prices against the bottom of the computed range, are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The two reporting figures the owner asks for are computed under AFTER THE STOP, headed
COMPUTATION, NOT A CLEARANCE (operator rule 3).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator for this run).

---
## THE BOX
**OUT at Q2**: a standing castle that protects only ordinary returns, the field's durable players (Weatherford, NOV,
Halliburton) earning losses or about 4% on revenue over 2016 to 2025, the filer's own work won on bids where "Pricing is one
of the primary factors", and the Dril-Quip half of the business a castle shown crossed (about 30% operating margin in 2014
and 2015, losses or about 1% in seven of the eight years 2016 to 2023). **Integrity facts recorded, not judged** (the
willful-infringement verdict against the DWS subsidiary; Dril-Quip's 2024 non-reliance on its 2021 statements; the
featured Adjusted EBITDA that adds back stock pay). COMPUTATION, NOT A CLEARANCE, beneath the stop: value about $10.43 a share
(the no-growth case alone, on the organic pair) against $27.39; fair price about $6.75 all-equity ($4.55 equity-only); no
case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2). Each with its source* **[M1997-127]**.

**Bearing on Q3 (capital in, earnings out).**
- The company's own non-GAAP return on capital employed: 10% for 2025, 12% for 2024 (after-tax operating income before
  acquisition costs over average debt plus equity), on an equity base in which Dril-Quip was carried at a bargain-purchase
  value (10-K FY2025, Item 7, "ROCE").
- Capital expenditures were 4% of revenue in 2025 and 2% in 2024 ($35.1M and $13.6M), against depreciation and amortization
  of $60.7M and $31.2M (10-K FY2025). The filer: "Historically, capital expenditures have been relatively modest, with working
  capital being the predominant use of cash for the Company during periods of growth" and "if work activity increases, we
  expect further working capital investment will be required" (Item 7). Receivables plus inventory were $486.2M at 2025,
  about 50% of revenue.
- Acquisitions paid in cash over 2021 to 2025, net of cash acquired: $22.2M (2021), $28.9M (2022), $18.4M plus Dril-Quip's
  $82.3M (2023), $65.5M (2024), $83.7M (2025): $300.9M in all, against owner cash before purchases of $97.8M over the same
  five years on the combined basis (COMPUTATION below). Goodwill rose from $60.2M to $99.7M in 2025. Acquisitions are
  "a core competency" (Item 1).

**Bearing on Q4 (the accounts).**
- The featured figure is "Adjusted EBITDA" ($188.3M for 2025), which adds back stock-based compensation ($13.8M), acquisition
  and integration costs ($17.5M, called "one-time in nature" in each year they occurred: $2.3M 2023, $33.3M 2024, $17.5M
  2025, $3.2M 2026 H1), impairments and the bargain-purchase items (10-K FY2025, Item 7, Non-GAAP). The row on this:
  "it has become common for managers to tell their owners to ignore certain expense items that are all too real.
  "Stock-based compensation" is the most egregious example." **[L2015-003]**; recorded, not weighed.
- Dril-Quip's 8-K of 2024-07-08 (item 4.02): the 2021 consolidated statements "should no longer be relied upon"; about $67M of
  inventory write-downs had been classified as "Restructuring and other charges" rather than "Cost of sales"; a material
  weakness was disclosed; operating income and net income were unchanged. The rows on the class: the restructuring charge
  "too often is a device for manipulating earnings" **[L1998-031]**; recorded, not weighed. The FY2025 10-K: "we identified
  material weaknesses in the past that have been remedied"; PwC's 2025 opinion on internal control is clean.
- The receivables allowance was $63,875K at 2024-12-31 and $19,752K at 2025-12-31; bad-debt expense fell $10.4M in 2025 on
  "recoveries of outstanding receivables from our prior agent in Saudi Arabia", and the 10-Q credits a $13.6M recovery from
  "our former agent in Saudi Arabia" in Q2 2025. The filings read do not say why the agent was replaced or how the balance
  arose; not read further.
- A net deferred tax asset of $102.4M at 2025, a valuation allowance of $60.6M, and an NOL carryforward of $457.3M, of which
  "$149.5 million of NOLs acquired from Dril-Quip are not limited" and Rubicon's are "subject to a significant limitation"
  (Item 1A, Item 7).

**Bearing on Q5 (the people). Integrity facts, recorded, not judged.**
- **Impulse litigation:** a jury found that DWS (80% bought by Innovex on 2024-11-29, while the 2023 suit was pending; the
  first 20% held by Legacy Innovex since May 2023) infringed Impulse's patents on friction-reduction tools, "that such
  infringement was willful", and awarded $47.6M; Innovex accrued $51.6M and will appeal: "We strongly disagree with the
  verdict" (10-Q, Note 16).
- **Dril-Quip's non-reliance 8-K** of 2024-07-08, above; Dril-Quip's management of that time is not today's (the chief
  executive since the merger, Adam Anderson, ran Legacy Innovex from November 2016; proxy 2026).
- **The featured adjusted figure and the bonus:** the 2025 annual bonus of the named officers was paid on "achievement of
  certain EBITDA goals", a target "Adjusted EBITDA goal" of $195 million (proxy 2026, CD&A); the chief executive's 2025 total
  compensation in the Summary Compensation Table was $3,283,511.
- **Control and the sellers:** Amberjack Capital Partners held 22,757,322 shares, 33.2%, in the proxy's ownership table, and
  sold 6,612,500 shares in February 2026 at $25.75 to the public (the company bought 575,000 of them, $14.1M, approved by "a
  committee [...] consisting solely of independent and disinterested directors") and 5,000,000 more at $28.71 to the
  underwriter in August 2026 (8-Ks of 2026-02-27 and 2026-08-10). The 10-K: "Amberjack is not limited in its ability to compete
  with us."
- **The pre-closing dividend:** "Legacy Innovex paid a cash dividend of $75.0 million, or $2.39 per share, to the holders of
  Legacy Innovex Common Stock on September 6, 2024", the closing day, a term Legacy Innovex proposed in the negotiation along
  with a balance sheet of "not more than $125mm of net debt", "in part intended to facilitate" it (10-K FY2024; 424B3,
  Background of the Mergers). Amberjack was Legacy Innovex's largest holder.
- Legacy Innovex filed an S-1 in September 2023 and withdrew it in April 2024 "in light of the mergers" (424B3).
- Any later run that reaches Q5 must answer these facts first **[M2013-088]**.

**Bearing on Q6 (the money and the owners).**
- Buybacks: 624,531 shares at an average $14.89 in the first half of 2025 ($9.3M) and 575,000 at $24.59 in February 2026
  ($14.1M); $76.6M of authorization remains; the program names no price ("does not require us to repurchase a specific number
  of shares or have an expiration date"; 10-Q, Note 14). Against the bottom of the computed range below (COMPUTATION, about
  $10.43 a share), both sets of purchases were made above it; the framework's reading of a buyback with no stated price
  against the bottom of the range **[L2016-002]** is Q6's and is not applied here.
- Issuance: shares issued for Rubicon ($79.9M of stock, 2021), Pride ($10.0M, 2022), the Dril-Quip merger (32,183,966 shares
  to Legacy Innovex holders, 2024), DWS (1,918,558 shares, 2024) and TCO (about 1,063,829 shares, 2026). Whether the merger,
  legally Dril-Quip issuing its shares and in accounting Legacy Innovex acquiring Dril-Quip at a bargain, was an all-stock
  deal in undervalued stock **[L2009-019]** is Q6's narrower STOP and is not judged here.
- Dividends: none since the merger; "We do not anticipate declaring or paying any cash dividends" (Item 1A).

**Bearing on Q9 (debt and exposures).** Debt and finance leases $25.1M, cash $222.1M, revolver availability $156.5M, no
borrowings, maturity 2030, at 2026-06-30 (10-Q); the TCO cash price of $65M was paid on 2026-07-01; the Impulse accrual of
$51.6M is outstanding. Top ten customers 26% of revenue; Saudi Aramco the largest end-user (Item 1). Product liability and
well-site hazards are carried with "customer indemnifications and third-party insurance", and "Oilfield anti-indemnity
provisions enacted by many U.S. states may restrict or prohibit a party’s indemnification of us" (Item 1A).

### Q7: COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; Part VII; not a verdict, no entry language)
Built by Q7's range convention in full, applied to the filed statements (script `q7_compute.py` in the research folder;
USD millions).

**Owner cash** = net cash from operations, with the deferred-tax add-back reversed so that tax is charged at the book rate
(the company's own tax), less stock pay, less all capital expenditures, less finance-lease principal; plus interest paid
after a 21% tax for the all-equity basis. Proceeds from sales of property are left out (a CONVENTION of this run: capital
released, not earned, and the 2025 proceeds include the $90.0M Eldridge facility sale, whose cash already sits in today's
balance sheet). Working capital is counted (d). The filing gives no maintenance figure, and capital spending ran below
depreciation and amortization in each combined year, so the maintenance-only case (e) and the all-spending case are the same
here; said so.

**The merger on the combined averages (c).** The Dril-Quip merger was paid in shares, so each pre-merger year adds Legacy
Innovex (424B3, F-7) and Dril-Quip (Dril-Quip 10-K FY2023, page 59). For 2024 the reported year (Legacy Innovex in full,
Dril-Quip from 2024-09-06; 10-K FY2025 F-8) has Dril-Quip's first half added (10-Q, accession `0000950170-24-092740`) and its
1 July to 5 September 2024 prorated from that half (a CONVENTION of this run: no filing covers those 67 days; rationale: the
period is otherwise left out of a merger the rule says to combine). Rubicon (March 2021, paid mostly in stock, so a merger by
the speakers' usage) has no filed figures for its first ten weeks of 2021; not added, said so.

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| Legacy Innovex | -7.9 | -9.5 | 66.5 | combined | combined | |
| Dril-Quip | 22.1 | -72.4 | -32.9 | -36.1 (to 5 Sept.) | | |
| **combined, all-equity** | **14.3** | **-81.9** | **33.6** | **31.0** | **101.0** | **19.6** |
| combined, equity-only | 13.0 | -84.4 | 29.0 | 29.4 | 100.2 | 17.4 |
| cash paid for businesses, net | 22.2 | 28.9 | 100.6 | 65.5 | 83.7 | 60.2 |

- **(a) Cycle base:** the filer does not describe 2021 or 2025 as aberrational, and no full cycle of the combined owner cash
  is filed (Legacy Innovex begins in 2021); the literal window is the base.
- **(c) Acquisitions and the serial acquirer:** net purchases of $300.9M exceed half of owner cash before purchases ($97.8M),
  so the central figure is the **organic pair** (purchases left out, organic growth as the filer reports it), with the
  default pair beside. The filer reports **no organic growth figure** (its revenue growth is "primarily driven by an
  increase in market share and incremental business operations due to the Merger and acquisitions"), so none is credited.
  The default pair (purchases deducted, total growth credited) averages $-40.6M a year after purchases: no positive value.
- **(b) Decline and sign change:** the series changes sign; the halves are $-33.8M (2021 to 2022) and $66.0M (2024 to 2025),
  a rate from a negative base is meaningless, so **the range is the no-growth case alone**, said so.
- **(f) The cap:** not reached; no growth is carried.
- **TCO Group** (closed 2026-07-01, after the window and before the price date): valued on its own filed record, the 8-K of
  2026-06-15 ("Free Cash Flow of $11 million" for 2025), at no growth, its $65M cash price added to net debt; its shares are in
  the 69,935,827 count. **DIS** (April 2026, $17.6M including a $4M earnout): no earnings filed, credited at nothing; its cash
  is already out of the 2026-06-30 balance; the earnout is deducted.
- **Net debt, all-equity basis:** debt and finance leases $25.1M less cash $222.1M at 2026-06-30, plus the TCO cash paid
  2026-07-01 ($65.0M), a subsequent event the 10-Q itself states: net cash $132.0M (operating leases left out). Deducted beside
  it, as owed: the Impulse accrual $51.6M and the DIS earnout $4.0M (a CONVENTION of this run: an accrued, probable litigation
  payment is a claim ahead of the owner like debt; rationale: the cash is owed and is not in the window's owner cash).
- **Whose tax (the shelter):** owner cash is charged the book rate; the tax shelter of the carryforwards, which at the
  current earnings would be used inside ten years, is added at its present value at the long rate: the net deferred tax asset
  of $102.4M taken as used evenly over four years, $89.9M (a CONVENTION of this run in its four-year span; rationale: the
  filing gives the asset, not the schedule of its use).

**The two figures** (shares 69.936M; price $27.39):
- **(a) VALUE RANGE (the no-growth case alone):** owner cash $19.6M plus TCO $11.0M = $30.6M a year, level forever at the
  long government rate of 5.43%, plus net cash $132.0M, less claims $55.6M, plus the shelter $89.9M: **about $10.43 a share**
  against $27.39. The literal window without TCO and at the 2026-06-30 balance, beside: about $8.46. Beside, not the
  convention's central figure and never deciding: 2025 alone plus TCO ($112.0M a year) at no growth gives about $31.86 a share.
- **(b) FAIR PRICE** (each end case valued at ten percent, the two averaged; here one case): **about $6.75 a share on the
  all-equity basis** (the central figure); **about $4.55 equity-only** (owner cash after interest, $28.4M a year with TCO, at
  ten percent, plus the shelter, less the claims, with no net cash credited). Beside: the 2025-plus-TCO case gives about
  $18.39 all-equity.
- **The floor, tested first:** at $27.39 the central case yields about 1.8% on the market value plus net debt (1.5%
  equity-only), and even the 2025-plus-TCO case beside yields about 6.4%; no case in the range earns the floor of about ten
  percent at the price, so Q7 would close OUT whatever the width **[M2003-149]**. Not a verdict: the file closed at Q2.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `c0fb0184`); written question by question; committed after Step 0
      and Q1, after Q2, and at the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      only once folded into the register by the dispatcher (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed by search or searched; one directory listing of
      `Test Runs/` showed other file names, declared under contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the check script in the research folder (`check_cites.py`),
      and every quoted fragment beside an id checked to be in that row; every filing fact carries its document and accession.
- [x] The order was kept; Q2's STOP closed the run; everything after it is NOT REACHED or under AFTER THE STOP, and the
      valuation is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statements (stock pay, all capital spending, finance-lease
      principal, book tax), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and of those only the balance-sheet table and the price, share
      and sovereign lines; its owner-earnings window was rejected because it mixes two registrants (Step 0).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- **What is weak in this run, stated.** (1) Legacy Innovex has no filed trough year but 2021; the castle verdict rests on the
  field, on the Dril-Quip half and on the filer's own risk statements, not on a Legacy Innovex full cycle. (2) The rivals'
  margins are company-wide, not product-line; Weatherford's 2019 is untagged. (3) No unit-cost comparison with rivals exists
  in the filings. (4) The 67-day Dril-Quip gap in 2024, the four-year shelter and the legal claim in net debt are this run's
  conventions; together they move the central value by well under a dollar a share against a price of $27.39. (5) The
  proxy was read only for the facts above; the board, the pay design and the related-party policy were not read in full.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. **(1) A reverse merger and "which history".** The framework says a merger inside the window is valued on the
combined companies' own averages, but it does not say what to do when the accounting acquirer is the private company and
the registrant's own filed history before the merger is the target's; the run combined both registrants' filed statements
and prorated a 67-day gap no filing covers, and confessed both. A sentence saying that the business owned today is read on
both predecessors' filings, and how a gap is filled, would settle it. **(2) The serial-acquirer rule with no organic figure.**
Q7 (c) makes the organic pair central for a serial acquirer and credits "organic growth as the filer reports it"; when the
filer reports none, the organic pair collapses to no growth, which the run applied; the text does not say so in terms, and a
run could instead measure organic growth itself. **(3) "Ordinary returns" over "a full cycle" when one predecessor has a full
filed cycle and the other has none.** Section C's OUT rule and its change-for-the-better rule (TOO HARD (NATURE) until a
downturn) both reach this name; the run chose OUT because the filer's own risk statements and the Dril-Quip half answered
the question on the evidence, and recorded the TOO HARD reading it rejected. The framework does not say which governs when a
business is half a proven-ordinary castle and half an untested one, and the parts paragraph does not help when the filer
reports one segment. **(4) Litigation accruals and net debt.** "On what the floor is earned" defines net debt as borrowings and
finance leases less cash; an accrued, probable cash payment such as the $51.6M Impulse accrual is not named, and the run
deducted it beside net debt as a confessed convention.
