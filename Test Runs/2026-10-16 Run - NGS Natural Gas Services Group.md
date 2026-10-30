# Company Run — Natural Gas Services Group, Inc. (NYSE: NGS) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run. The template was copied to this file and committed (commit `af5b4e7e`) before any filing was fetched.
Working folder: `Test Runs/_research 2026-10-16 NGS/` (notes, scripts, the `tools/run.py` output, the extracted ledger rows;
raw filings under its `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
NGS or Natural Gas Services).*

**CONTAMINATION, declared and not used.** (1) To check whether today's run file already existed I listed `Test Runs/`
filtered to the date 2026-10-16; the listing showed four other runs of today and their research folders: HMH (HMH Holding),
NOV (NOV Inc.), OIS (Oil States International) and USAC (USA Compression Partners). The listing was itself a breach of the
letter of the blind rule (listing other companies' run files); none of the four was opened. USA Compression Partners is one
of the three rivals used at Q2; its figures here come from its own SEC filings only, never from that run file. (2) The
session context carried the latest commit subjects, which describe the OIS fold (OUT at Q2 on "a standing castle that
protects only ordinary returns", with NOV, Baker Hughes and Tenaris named). Oil States International also appears in NGS's own
2026 proxy compensation peer group; I did not use OIS for anything. (3) The memory index loaded into the session carries
general queue lines (counts of gate-clearers, a wave paused, "nothing buyable"); none names NGS. Nothing of any of these
was used; the Q2 judgment below rests on NGS's and the three rivals' own filings.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $30.96 (close 2026-10-15; aggregator quote via `tools/run.py`, **flagged per operator rule 5**: a live quote
  only).
- **Shares by class** from the latest filing's cover: **12,898,285** common shares, par $0.01, one class (10-Q for the
  period ended 2026-06-30, filed 2026-08-10, accession `0001084991-26-000079`; cover date 2026-08-07;
  `python Screens/cover_shares.py NGS`). **Check:** the 10-Q balance sheet shows 14,207 thousand shares issued less 1,310
  thousand treasury shares = 12,897 thousand, agreeing with the cover. The 241,803 shares issued for Flatrock on 2026-06-12
  (8-K `0001084991-26-000054`) are inside both counts. The only 8-K after the 10-Q (2026-08-12, `0001084991-26-000086`,
  items 2.02, 7.01, 9.01, the second-quarter call script) issues no shares. No preferred shares are outstanding.
- **Market cap:** $30.96 × 12.898M = **$399.3M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield on the US Treasury daily par yield
  curve, 2026-10-15 (issuing authority; read through `tools/run.py`, which calls `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-03-16, `0001084991-26-000015`), Items 1, 1A, 7, the
  statements and notes; 10-Ks for FY2024 (`0001084991-25-000024`), FY2023 (`0001084991-24-000017`), FY2022
  (`0001084991-23-000032`) and FY2021 (`0001084991-22-000009`), MD&A and controls sections; 10-Q for Q2 2026
  (`0001084991-26-000079`), the balance sheet, Note 3 (Flatrock), Note 10 (debt), Note 11 (taxes); 10-Q for Q1 2026
  (`0001084991-26-000043`, fetched, not relied on); proxy (DEF 14A filed 2026-04-28, `0001084991-26-000032`), the
  chairman's letter and the compensation discussion; 8-Ks: Flatrock (`0001084991-26-000054`, and the 8-K/A
  `0001084991-26-000081` with Flatrock's audited FY2025 statements, exhibit 99.1, and the pro forma, exhibit 99.3), the
  auditor change (`0001084991-26-000064`), the redomestication to Texas (`0001084991-26-000070`), the Q2 2026 earnings
  8-Ks (`0001084991-26-000080`, `0001084991-26-000086`). The 2022 10-K/A (`0001084991-22-000036`) and the 2022 and 2023
  4.01 and DEFA14A filings were seen in the filing index and not read.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2025,
  $62,927 thousand in the 10-K's cash-flow table (Item 7, `0001084991-26-000015`) against 62.9 in `tools/run.py`; total
  assets at 2025-12-31, $586,786 thousand on the face of the 10-Q's comparative balance sheet against 586,786 in the
  `tools/run.py` table. Both agree.
- **The lines of evidence, chosen from the FY2025 10-K's Item 1, Item 1A and Item 7, and why.** (1) The key operating
  variables the filer itself reports: rented horsepower, utilization, rental revenue and the rental margin (Item 1, Rental;
  Item 7, Operating Highlights), because Q1 asks whether those can be foreseen. (2) Customer concentration: Occidental and
  Devon were 59 percent of 2025 revenue (Item 1, Customers; Item 1A), because a castle is judged by why the customer comes.
  (3) Competition: "highly competitive", rivals "some of which have greater financial resources", "Compressor industry
  participants can achieve significant advantages through increased size", and customers "may purchase and operate their
  own compression fleets" (Item 1, Competition; Item 1A), because these are the filer's own answers to the attacker and
  low-cost tests. (4) Cyclicality and contract terms: "highly cyclical", "lower rate rental contracts", about half the
  rented units month-to-month (Item 1A; Item 7), because Q2's price-behaviour and full-cycle tests turn on them. (5)
  Capital: growth against maintenance capital spending and the debt that funded the fleet's growth (Item 7, Cash Flows and
  Capitalization), because Q3, Q7 and Q9 turn on them. (6) The non-GAAP framing: Adjusted EBITDA and management's
  statement that depreciation "does not accurately reflect the costs required to maintain and replenish" the assets (Item 7,
  Non-GAAP), because Q4 and Q5 read how management describes its own earnings.
- `python tools/run.py NGS` arithmetic lines only (saved as `run_py_output.txt` in the research folder). Owner cash after
  every real cost, as filed (OCF less stock pay less all capital spending): FY2023 -$138.0M, FY2024 -$7.5M, FY2025
  -$61.1M; on the depreciation basis $-10.6M, $33.0M, $23.7M. Five-year window (FY2021 to FY2025): all-spending mean
  -$49.0M, depreciation-basis mean $9.9M. Capital spending is almost all rental fleet (the filer splits FY2025's $121.5M
  into $109.8M growth and $11.7M maintenance, FY2024's $71.9M into $60.5M and $11.4M; 10-K Item 7, Cash Flows). Stock pay
  is small ($1.7M to $2.6M a year) and is deducted. The tool found finance-lease principal of $0.1M (2023) and $0.6M
  (2024), immaterial, and no other stock-pay, securities or paid-in-kind lines. Its other lines (yield, "growth the price
  assumes") are not used.

**The balance sheets, ten year-ends, read before the income account** **[M2025-032]** (the file closes before Q4, so they
are read here, as the template asks). From the `tools/run.py` table (first-filed XBRL, USD thousands), checked against the
filed balance sheets for 2024, 2025 and 2026-06-30:

| year-end | total assets | equity | cash | receivables | inventory | goodwill | retained earnings | credit facility |
|---|---|---|---|---|---|---|---|---|
| 2016 | 293,524 | 232,954 | 64,094 | 7,378 | 25,833 | 10,039 | 132,014 | 0 |
| 2017 | 298,310 | 257,319 | 69,208 | 8,534 | 26,224 | 10,039 | 151,865 | 417 |
| 2018 | 305,401 | 260,181 | 52,628 | 7,219 | 30,974 | 10,039 | 152,291 | 417 |
| 2019 | 286,577 | 247,693 | 11,592 | 9,106 | 21,080 | 0 | 137,478 | 0 |
| 2020 | 306,801 | 251,544 | 28,925 | 11,884 | 19,926 | 0 | 139,286 | 0 |
| 2021 | 298,506 | 235,910 | 22,942 | 10,389 | 19,329 | 0 | 130,103 | 0 |
| 2022 | 328,246 | 230,076 | 3,372 | 14,668 | 23,414 | 0 | 129,534 | 25,000 |
| 2023 | 478,729 | 235,894 | 2,746 | 39,186 | 21,639 | 0 | 134,281 | 164,000 |
| 2024 | 492,528 | 255,057 | 2,142 | 15,626 | 18,051 | 0 | 151,508 | 170,000 |
| 2025 | 586,786 | 274,716 | 0 | 18,497 | 20,647 | 0 | 168,771 | 230,000 |
| 2026-06-30 | 718,343 | 294,486 | 84 | 22,025 | 29,110 | 824 | 176,059 | 328,000 |

What the figures say. **Equity stood still for a decade:** $233M at the end of 2016, $275M at the end of 2025; retained
earnings rose $37M in nine years ($132.0M to $168.8M), and the 2017 figure includes an $18.4M credit from the cut in the
federal tax rate (XBRL `IncomeTaxReconciliationChangeInEnactedTaxRate`, FY2017), so the earnings retained from operations
over the nine years were nearer $18M on roughly $250M of equity. Retained earnings fell from 2017 to 2022 ($151.9M to
$129.5M), a five-year stretch of losses, and $10.0M of goodwill was written off in 2019. **The growth since 2022 was
borrowed:** total assets rose from $328M (2022) to $587M (2025) and $718M (June 2026) while equity rose $64M; the credit
facility went from nothing to $230M at year-end 2025 and $328M at June 2026 after the Flatrock purchase; the $64M to $69M of
cash held in 2016 and 2017 is gone. **Receivables jumped once:** $39.2M at the end of 2023 on revenue of $121.2M, against
$15.6M a year later; the FY2025 10-K ascribes the 2024 fall to "the substantial progress made in the 2024 period for
improving our processes for billings and collections from certain customers" (Item 7, Cash Flows). Inventory has moved
with no trend against sales. What the figures do not say: whether a fleet carried at 15 to 25 year lives (10-K, Critical
Accounting Estimates) is worth its book value through a downturn; the filer retired 263 units in 2021, 124 in 2022 and 95
in 2023 (10-Ks FY2021 to FY2023, MD&A), which is the fleet's book value meeting its market. What the management would like
them to say is in the next lines of this file: the featured figure is Adjusted EBITDA.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which for a compressor rental company means owning a fleet whose rent is set each cycle by the producers'
spending and the rivals' fleets, not by the quotation. No macro forecast enters **[M2000-094]**: nothing below rests on a
view of oil or gas prices; the business is read off its figures across the cycle it has already lived through. The analyst's
habit applied here is to look for "what’s wrong in things because that’s part of investing – looking at what you’re
missing" **[M2025-013]**: the filer's record year (2025) and its acquisition are where the run looked hardest for the case
against. **Contrary evidence, written down as found** **[M1997-127]**: (a) equity flat for ten years and retained earnings up
about $37M in nine years, with an $18.4M tax-rate credit inside that (Step 0); (b) two customers, 59 percent of revenue;
(c) the filer's own statement that size gives advantages in this industry, while it is the smallest of the field read; (d)
the filer's own statement that it has "been required to enter into lower rate rental contracts in response to market
conditions"; (e) management's statement that depreciation does not reflect the cost of keeping the fleet; (f) a material
weakness in internal control at the end of 2022, unremedied at the end of 2023, and interim chief executive and chief
financial officers at the end of 2022 (10-Ks FY2022 and FY2023, Item 9A); (g) the Flatrock purchase, $119.0M for a business
that earned $5.9M of operating income in 2025 (8-K/A `0001084991-26-000081`, exhibit 99.1); (h) the auditor's resignation in
2026 on a sale of its practice (8-K `0001084991-26-000064`), and 8-Ks under item 4.01 (change in the certifying accountant)
filed on 2022-06-03 and 2022-07-22 (filing index). Points (f) to (h) bear
on Q4 to Q6 and are carried under AFTER THE STOP.

## THE STANDING RULE
Owning a part-interest in NGS, bought with the buyer's own money and sized so that a fall of half or more could be borne,
puts the buyer at no risk of ruin; the rule governs the buyer's conduct, and borrowed money "has no place in the investor's
tool kit" **[L2014-005]**; "Never risk permanent loss of capital." **[L2023-005]**. Nothing in the target changes that; the
target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, not knowledge of the product; "What is important is that I
  understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
  **[M2011-014]**.
- **The business, from the filing.** NGS rents compressors, mostly large units of 400 horsepower and up, to oil producers
  for gas lift on unconventional wells; 78 percent of 2025 rental revenue came from the Permian and about 90 percent
  "supports oil production primarily in the form of gas lift operations"; rental was 95.4 percent of 2025 revenue; it buys
  the engines and compressor frames from OEM suppliers and has "Substantially all of our compressor assembly" done by third
  parties (10-K FY2025 Items 1 and 7, `0001084991-26-000015`). One reporting segment.
- **The key variables and whether they are foreseeable** **[M1998-044]**: rented horsepower, the rate per horsepower,
  utilization, the cost to keep a unit running, and the capital cost of a new unit. The technology is slow (a compressor
  driven by a gas engine or an electric motor; the filer's innovations are emissions capture and telemetry, Item 1,
  Competitive Strengths), so the business is not one where "future technology could hurt the business as it presently
  exists" **[M1998-008]** in the sense the rows mean. Demand rides on oil production in a few basins and so on a commodity
  price, which the rows do not forecast, "We don’t think we can predict commodity prices." **[M2016-025]**; the framework
  places that dependence at Q2 and Q7, never as a STOP here (Q2, A commodity business). Can the business be read "off the
  figures" **[M2008-069]**? Yes: the filer reports the variables above every year, and the economics in ten years are a
  rental fleet earning whatever rent the field allows over the cycle; that is a question about the castle, which is Q2's.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The doubt
  here is not about what the business is or how it makes money; it is about whether its rent holds, and the rows give that
  question to Q2. Test 5 settles the cause: the industry's insiders do write down multi-year contracts (464,137 of the
  562,676 rented horsepower at 2025 year-end was under contracts expiring 2026 to 2030, Item 7), so the forecast is not one
  they "would not want to put down on paper" **[M2000-105]**.
- **VERDICT: IN.** The economics can be understood from the filings and the industry does not change fast; what remains is
  whether anything protects the return, which is Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**; the moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The rivals.** The FY2025 10-K names no competitor (Item 1, Competition; Item 1A); the FY2021 to FY2024 10-Ks name none
either (a text search of each for the three rival names below). The proxy's compensation peer group is a list of
oilfield-service companies, none a compression renter (DEF 14A `0001084991-26-000032`, Peer Group), so it is not a list of
competitors. **A CONVENTION of this run:** the rivals read are the three US contract-compression companies that file with
the SEC and describe themselves as the large outsourced compression providers: Archrock (AROC), USA Compression Partners
(USAC) and Kodiak Gas Services (KGS). Rationale: the brief's rule (the rivals the 10-K names) yields none; the filer's own
words point to "competitors in the compression industry, some of which have greater financial resources", and these three
are the ones whose own 10-Ks describe that position. No named rival is left unread or unflagged, because none is named.

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**. NGS owns no unit a rival cannot buy: it purchases "engines, compressors,
  coolers, frames and other components" from OEM suppliers and has "Substantially all of our compressor assembly" done by
  third parties (10-K FY2025 Items 1 and 7). The largest rival writes of the same business: "The natural gas compression
  services business is highly competitive with low barriers to entry." (Archrock 10-K FY2025, Competition,
  `0001389050-26-000009`); USA Compression adds "On a regional basis, we experience competition from numerous smaller
  companies" (USAC 10-K FY2025, `0001522727-26-000015`). This is the case of the airline exchange, "you can create another
  airline. WARREN BUFFETT: Very easily, and you have people that like to do it." **[M2013-054]**, and of "there are some
  industries that are just never going to have barriers to entry." **[M2012-106]**. NGS's own account of its recent gains
  confirms it: the strength it names is "Availability of new units", a "dearth of available rental compression units" caused
  by rivals' "Capital constraints", which "allowed us to strategically gain market share" (Item 1, Competitive Strengths). An
  advantage that lasts while rivals lack capital is the attacker test failed in advance; Archrock grew its operating
  horsepower from 3,607 thousand (2023) to 4,571 thousand (2025) (Archrock 10-K FY2025, operating statistics).
- **The customer and the low bid** **[M2017-009]**. NGS competes "on the basis of compression unit availability, customer
  service, flexibility in meeting customer needs, and quality and reliability of our compressors and related services as
  well as price", and "our customers may purchase and operate their own compression fleets in lieu of renting compressors"
  (Item 1, Competition; Item 1A). Two customers, Occidental and Devon, were 59 percent of revenue in 2025 and 2024 and 52
  percent in 2023 (Item 1, Customers): the buyer is large and can bring the work in-house.
- **Pricing power and the agony before a rise** **[M2005-020]**. The filer: "Our industry is highly cyclical, with periods of
  high demand and high pricing followed by periods of low demand and low pricing. [...] At times, we have been required to
  enter into lower rate rental contracts in response to market conditions and our revenues have decreased as a result of
  such conditions." (Item 1A). About half the rented units and a quarter of rented horsepower are month-to-month (Item 1A;
  Item 7: 491 of 1,245 units, 98,539 of 562,676 horsepower). Its strategy speaks of "targeted price increases, particularly
  in geographic areas that have experienced high rates of cost inflation" (Item 1, Business Strategy): price rises as a
  pass-through of cost, not as a show of power. "You can learn a lot about — you learn a lot about the durability of the
  economics of a business by observing the behavior of — the price behavior." **[M2005-020]**; the price behaviour did not
  hold through the last downturn.
- **The low-cost position** **[M1997-010]**. The filer: "Compressor industry participants can achieve significant advantages
  through increased size and geographic breadth." (Item 1, Competition); the largest rival: "Increased size and geographic
  density offer compression services providers operating and cost advantages." (Archrock 10-K FY2025). NGS is the smallest
  of the four by a factor of six or more (table below), and its rental margin before depreciation is the lowest. In a field
  sold on availability and price, "commodity businesses have risk unless you’re the low-cost producer, because the
  low-cost producer can put you out of business." **[M1997-010]**; NGS is not that producer.
- **Unit volume, and widening or narrowing** **[M1999-108]**. NGS has grown: rented horsepower 420,432 (2023), 491,756 (2024),
  562,676 (2025), and 87,233 more bought with Flatrock in June 2026 (10-K Item 7; 10-Q Note 3). The growth was bought with
  borrowed capital (Step 0) and earned, at its best, the returns below. Volume shows the place in the market holding while
  rivals were short of units; it does not show the moat widening.
- **Ask the competitors** **[M1999-130]** cannot be done from the filings: no rival's FY2025 10-K names NGS (a text search of
  the three for "Natural Gas Services"); USA Compression's "numerous smaller companies" is the nearest it comes.
- **What could destroy, modify or reduce it** **[M2000-014]**: a fall in Permian oil activity, a customer bringing
  compression in-house or moving to a larger renter, and rivals' new fleets ending the shortage that gave NGS its share.

**The competitor row**, the same metrics from each company's own FY2025 10-K and XBRL facts (pre-tax operating earnings
over average tangible assets, that is total assets less goodwill and intangibles, averaged over each year's two year-ends;
for Archrock, whose filings carry no operating-income line, pre-tax income plus interest expense; script `returns.py`):

| company (accession of the FY2025 10-K) | fleet, end of 2025 | rental or contract-services margin before depreciation, 2025 | pre-tax return on tangible assets, 2025 | the same, summed over the span |
|---|---|---|---|---|
| NGS (`0001084991-26-000015`) | 662,542 hp, 562,676 rented | 60.6% | 6.9% | 2.4% over 2014-2025; 8.5% to 9.6% in 2012-2014 |
| Archrock (`0001389050-26-000009`) | 4,571 thousand operating hp | 73% (contract operations) | 15.2% | 6.8% over 2016-2025 (before 2016 the filer was Exterran Holdings, a different business, left out) |
| USA Compression (`0001522727-26-000015`) | 3,958 thousand hp | 67.1% | 12.4% | 3.5% over 2014-2025 |
| Kodiak (`0001767042-26-000012`) | about 4.5 million hp | 68.4% (contract services) | 8.9% | 7.9% over 2021-2025 (no full cycle on file) |

NGS by year (operating income over average tangible assets): 2014 8.5%, 2015 5.6%, 2016 3.0%, 2017 0.6%, 2018 0.2%, 2019
-5.2%, 2020 -1.2%, 2021 -4.1%, 2022 0.1%, 2023 2.6%, 2024 6.9%, 2025 6.9%. In 2016 to 2018 NGS held $53M to $69M of cash
inside those assets; with it taken out, 2017 and 2018 are still under one percent. The losses of 2019 and 2021 include a
$10.0M goodwill write-off (2019) and retirements of rental units ($1.5M in 2019, $3.1M in 2021); retirements recur in nine
of the eleven years 2015 to 2025 (XBRL `ImpairedAssetsToBeDisposedOfByMethodOtherThanSaleAmountOfImpairmentLoss`) and are
the fleet's real cost, not one-time items.

**The parts table:** not needed. NGS reports one segment, and rental was 95.4 percent of 2025 revenue (Item 7).

**The field's returns over the last full cycle, judged in words.** The cycle runs from the 2014 peak through the troughs of
2016 to 2021 to the record years of 2024 and 2025. Over it the field's durable players earned ordinary returns: NGS, with
almost no debt for most of the span, earned low single digits before tax on its tangible assets and lost money in three of
the twelve years; USA Compression earned about the same; Archrock earned under seven percent before tax over its ten years
as a compression company; only in 2024 and 2025 did the two largest reach the low to middle teens. That is the standing
castle that protects only ordinary returns, the case of "you can have only two competitors and they’re still terrible
businesses, they beat each other’s brains out." **[M2013-052]**. The improvement of 2023 to 2025 is a change for the better
that the framework credits only on a full cycle **[M2017-026]**, **[L1995-022]**; it does not decide this file, because
NGS's own return at the very top of the improvement, 6.9 percent before tax in each of 2024 and 2025, and 9.6 percent at its
previous peak in 2012, is itself ordinary. Crediting the change in full would not make NGS's castle one that protects
excellent returns.

- **Why OUT and not TOO HARD.** The castle's future is not unknowable; its past is on file and shows it open: low barriers in
  the largest rival's own words, the units bought from the same suppliers by everyone, a buyer that can own its own fleet,
  rent cut in downturns, and NGS neither the largest nor the lowest-cost. "If the answer had been yes, we wouldn’t have done
  it." **[M2011-015]**. The tenuous-moat row sends a castle to TOO HARD for the reason "We don’t know how to valuate that"
  **[M2000-019]**, which does not apply when the returns are on file. Price does not reopen it: "What you can’t do is turn
  any investment into a good deal by paying little" **[M2019-015]**.
- **VERDICT: OUT.** The castle is open on the evidence and the field's returns over the full cycle are ordinary; NGS is the
  smallest and the lowest-margin of the four read. The file closes here. Q3 to Q10 and Q12 are NOT REACHED.

## Q3 to Q10, Q12 — NOT REACHED
The Q2 STOP closed the file OUT (operator rule 2). Nothing below is a clearance.

---
## THE BOX
**OUT at Q2** (a castle open on the evidence: low barriers to entry in the largest rival's own words, units bought from the
same suppliers by every renter, customers who can own their own fleets, rent cut in downturns, and NGS the smallest and
lowest-margin of the four read; the field's returns over the 2014 to 2025 cycle ordinary, NGS's 2.4 percent before tax on
tangible assets and 6.9 percent at its 2025 peak), **integrity facts recorded, not judged**. COMPUTATION beneath the stop:
the central range is below zero a share ($-13.75 to $-5.29 all-equity) against $30.96; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).*

**Q3 (capital).** Total assets rose from $328M (2022) to $718M (June 2026), funded by $328M of borrowing; operating income
rose from $0.4M (2022) to $37.3M (2025). Capital spending less depreciation, summed 2015 to 2025, was about $313M, and owner
cash on the depreciation basis rose from $9.8M (2014) to $35.8M (2025) (script `q7_computation.py`, series by year). The
filer reports growth and maintenance capital separately for 2024 and 2025 only ($60.5M and $11.4M; $109.8M and $11.7M; 10-K
FY2025 Item 7), and guides 2026 growth capital to $60M to $80M and maintenance to $15M to $19M (Q2 2026 call script, 8-K
`0001084991-26-000086`). Rental equipment carries 15 to 25 year lives (10-K, Critical Accounting Estimates).

**Q4 (the accounts).** (a) The featured figure is Adjusted EBITDA: in the chairman's letter ("Adjusted EBITDA increased to
$81 million, also an all-time high", DEF 14A `0001084991-26-000032`), in the guidance ("increasing full-year 2026 adjusted
EBITDA guidance to $103 million to $108 million", Q2 2026 call), and in pay (below). Its definition adds back impairments,
retirements of rental equipment, inventory allowances and stock pay as well as depreciation (10-K Item 7). (b) Management
states that "Depreciation and amortization expense does not accurately reflect the costs required to maintain and replenish
the operational usage of our assets" (10-K Item 7, Adjusted Gross Margin), while retiring rental units in nine of the
eleven years 2015 to 2025. (c) The Q2 2026 call calls "adjusted net income" one "providing a much better view of the
underlying earnings performance of the business". (d) A material weakness over the inventory process at 2022 year-end
(10-K FY2022 Item 9A), unremedied at 2023 year-end (10-K FY2023 Item 9A), reported remediated at 2024 year-end (10-K FY2024
Item 9A); the FY2022 controls certification was signed by an interim chief executive and an interim chief financial
officer. (e) Receivables of $39.2M at 2023 year-end against revenue of $121.2M, $15.6M a year later, explained by the filer
as improved billing and collection processes (Step 0). (f) Auditors: Moss Adams resigned effective 2022-06-08 with no
disagreements reported (8-K `0001084991-22-000062`); Ham, Langston & Brezina was appointed 2022-07-21, having prepared the
company's income tax provision and tax compliance for 2020 and 2021 (8-K `0001084991-22-000092`); it resigned 2026-07-09 when
CohnReznick acquired certain of its assets, again with no disagreements reported, and CohnReznick was appointed
(8-K `0001084991-26-000064`). (g) Federal NOL carryforwards of $124.2M, indefinite, usable up to 80 percent of taxable income
(10-K FY2025, Note 11); the company paid almost no cash income tax from 2018 to 2025 (XBRL `IncomeTaxesPaid`) and collected
$13.8M of carryback refunds and interest in 2026 (10-Q Note 11).

**Q5 (the people).** The chief executive, Justin C. Jacobs, came to the board on 2023-04-28 under a cooperation agreement
with Mill Road Capital, of which he is "a Management Committee Director" (8-K `0001084991-23-000047`); the company filed
additional proxy materials in 2023 (DEFA14A `0001084991-23-000077`, not read in full). Directors and officers as a group
own 3.12 percent (DEF 14A, beneficial ownership). The habits carried from Q4 for a later run that reaches Q5: the
Adjusted EBITDA featured and guided, and an "adjusted net income" offered as the better view (Q4 (a) and (c) above), which a
later run must read with the integrity record **[M2013-088]**.

**Q6 (the money and the owners).** (a) **Flatrock:** bought 2026-06-12 for $108.9M in cash (including $45.7M to repay
Flatrock's line of credit), 241,803 shares valued at $10.0M and a royalty right, $119.0M in all (10-Q Note 3); Flatrock
earned $5.9M of operating income and $2.5M of net income on $38.8M of revenue in 2025, with operating cash of $10.1M and
capital spending of $16.8M, and its two largest customers were 33 percent of revenue (8-K/A `0001084991-26-000081`, exhibit
99.1). Paid mostly in cash, it is an acquisition, not a merger, by Q7's definition. (b) **Dividends** began in the third
quarter of 2025 ($0.10, then $0.11, and $0.15 a share by the second quarter of 2026, declared again on 2026-08-10; 10-K Note 14;
10-Q dividends and subsequent events) while borrowings rose from
$170M to $328M. (c) **Buybacks:** a $6M programme approved 2025-08-08, expiring 2027-08-06, with no stated price; no shares
were bought in 2025 (10-K Item 5); the Q2 2026 10-Q shows none. (d) **Pay:** 85 percent of the 2025 annual bonus rested on
Adjusted EBITDA, which paid at 131 percent of target ($80.97M against a $76.58M target), with 5 percent each on safety,
vehicle incidents and a reporting project; half the long-term award is in relative-TSR performance units; the chief
executive's 2025 total was $2,968,713 (DEF 14A, STIP and Summary Compensation Table). (e) **Texas:** redomesticated from
Colorado 2026-07-20 (8-K `0001084991-26-000070`); the board says it did not opt into the Texas provisions that set an
ownership threshold for derivative suits or proposals, and the new bylaws make the Texas Business Court the exclusive forum
for derivative and fiduciary claims (DEF 14A, Texas Redomestication). The classified board and the 80 percent votes to
remove a director or change board size stood in the FY2025 10-K (Item 1A).

**Q7 (COMPUTATION, NOT A CLEARANCE).** Built by Q7's range convention, all-equity basis central, from `q7_computation.py`
(output in `q7_output.txt`). No entry language attaches to any figure (operator rule 3).
- *Owner cash.* OCF less stock pay less maintenance, with interest paid added back after tax at 21 percent for the
  all-equity basis. **The maintenance guess (e):** the filer gives "capital maintenance projects" of $11.4M (2024) and $11.7M
  (2025) against depreciation of $31.3M and $36.7M. The central case takes depreciation as the maintenance need, because
  depreciation is "almost always true costs" **[L2015-004]**, is "not inappropriate in most companies to use as a proxy for
  required capital expenditures" **[M1998-127]**, and "there’s very few businesses where I think I can spend a whole lot
  less than depreciation year after year and maintain the economic strength of the business" **[M2003-108]**; the filer's
  maintenance figure covers work on units in service, while the fleet also loses units to retirement every year (Q2). The
  filer's figure is shown beside as a variant. The all-spending case is negative in four of the five window years (mean
  -$42.4M all-equity) and is the growth spending charged with no growth credited, which (e) forbids as the central case.
- *Base (a).* The window's first year, 2021, is a trough on the filer's own description (an operating loss of $12.4M with
  263 units retired, 10-K FY2021 MD&A), and its last, 2025, a record ("Rental revenue reached a record $164 million",
  proxy letter). The base is therefore the last full cycle, 2014 peak to 2025 peak: **$9.65M** a year (maintenance at
  depreciation, all-equity), against **$17.10M** a year over 2009 to 2014. The literal window 2021 to 2025 is $16.41M, shown
  beside.
- *Growth (b), (f).* Between the cycles owner cash fell, about -6.9 percent a year, which is carried as the bottom; the
  no-growth case is then the top. In the literal window the series changes sign and the half-window rate (from $1.7M to
  $41.8M a year) is the "breathtaking, but meaningless, growth rate" of a poor base year **[L2005-003]**; the window is
  therefore shown at no growth alone.
- *Flatrock (c).* Closed after the window, before the price date: credited on its own filed record at its 2025 operating
  income after NGS's 2025 effective tax rate, $4.45M a year (more generous than its operating cash on the same basis, about
  $1.6M); its financing is inside the June 2026 debt.
- *Net debt:* $328.0M of borrowings less $0.08M of cash at 2026-06-30 (10-Q), **$327.9M**; no finance leases; operating
  leases left out. Assets held for sale of $11.0M (real estate) are not added; they would add about $0.85 a share.
- *Tax:* owner cash is after the company's own tax as paid, near nil because of the NOLs, which do not expire; the
  carryforward convention (a shelter running out inside ten years) does not apply. At a statutory rate the cash would be
  lower, so every figure below is generous on tax.

| case | owner cash a year | value at 5.43%, per share after net debt | value at 10%, per share |
|---|---|---|---|
| central top: cycle base, no growth | $14.10M | **$-5.29** | $-14.49 |
| central bottom: cycle base, decline between cycles | $14.10M falling 6.9% a year for ten years | **$-13.75** | $-18.48 |
| beside: literal window 2021-2025, no growth | $20.85M | $4.35 | $-9.26 |
| beside: the filer's maintenance figure, 2024-2025 only, no growth | $68.73M | $72.70 | $27.86 |

- **Value range (central): $-13.75 to $-5.29 a share against $30.96.** The floor is tested first: at the price the business
  costs $727.2M (market value $399.3M plus net debt), and the floor of about ten percent needs about $72.7M a year of
  all-equity owner cash with no growth. The central cases yield 1.9 percent on that price, the literal window 2.9 percent.
  The nearest case is the filer's-maintenance variant at 9.5 percent, which rests on the two record years that (a) forbids
  as a base and on maintenance at a third of depreciation, which the rows above reject as a cost; with depreciation as the maintenance on the
  same two years it is 6.4 percent, and on the cycle base 1.9 percent. No case the analyst could defend earns the floor at the price **[M2003-149]**, so the
  computation would close OUT whatever the width; the width test does not arise.
- **Fair price (reporting figure, Part VII):** each end of the central range valued at ten percent and averaged, all-equity
  less net debt: **$-16.48 a share**, that is, no positive fair price; at ten percent the whole business is worth less than its
  net debt on the central cases. **Equity-only beside:** owner cash after interest as actually paid over the cycle ($6.98M)
  plus Flatrock after the cost of the cash paid for it ($-1.13M), $5.84M a year, against the market value: **$3.71 a share**.
  The equity-only figure flatters, because the cycle's interest was paid on little or no debt; on the June 2026 debt
  ($328.0M at 6.48 percent, $16.8M a year after tax) the central all-equity owner cash less that interest is $-2.69M a year.
- Q6's buyback line: not run, Q7 not reached; for a later run, the programme names no price and no shares have been bought.

**Q9 (debt and exposures).** Borrowings of $328.0M under a revolving credit facility secured by "a first priority lien on
most of our assets", maturing 2028-02-28, at a weighted 6.48 percent; covenants of leverage at or below 3.50 to 1.00 and
fixed-charge coverage at or above 1.25 to 1.00; an event of default on "certain defaults with respect to any other Company
indebtedness in excess of $ 1.0 million" (10-Q Note 10). The proxy letter puts leverage at 2.7 times Adjusted EBITDA at
2025 year-end. Two customers were 62 percent of receivables at 2025 year-end (10-K Item 1). The "little or no debt"
criterion **[R1997-001]** would be read against a debt that equals 82 percent of the market value at the price.

**Q12.** Compression rental to oil and gas producers is none of the businesses the rows name; no fact found bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `af5b4e7e`); written question by question; committed after Step 0
      to Q1, after Q2, and at the close (write-early).
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits; the lock is the dispatching session's
      (not checked by this analyst); the fold is the dispatcher's.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened or searched; **one listing breach:** `Test Runs/` was
      listed filtered to today's date, which showed four other runs' file names (declared under CONTAMINATION; none opened,
      nothing used). Marked unchecked because the letter of the rule forbids the listing.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (checked by
      `check_citations.py` in the research folder); every filing fact has its accession or its filing named; no number
      without a filing, the script or a CONVENTION label.
- [x] The order was kept; Q2's STOP closed the run; everything after it is a fact recorded or a COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); depreciation taken as the maintenance
      need in the central case, the filer's figure beside; the sovereign from the US Treasury; the price quote flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations' list, then Q2); facts for later questions
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor date applies.
- [x] Only the arithmetic lines of `tools/run.py` were used (prices, share counts, filed figures and sums); its yield and
      "growth the price assumes" lines were not.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **No named rival.** The brief and Q2 ask for the rivals the 10-K names; this 10-K names none, in five years
of filings, and the proxy's peer group is a list of oilfield-service companies chosen for pay. The framework has no rule for
that case; I confessed a CONVENTION of this run (the three SEC-filing contract-compression companies that describe themselves
as the field's large providers). A rule is wanted: where the filer names none, the rivals its largest competitors' own
filings describe, or the companies the filer's own statements point to, chosen and stated before any of their figures are
read. (2) **The change for the better against the ordinary castle.** Q2's section C sends an unproven improvement to TOO
HARD (NATURE) with a re-look condition, and its "standing castle that protects only ordinary returns" to OUT. Here both
were present: the field improved in 2023 to 2025. I closed OUT because the filer's own return at the top of the improvement
was itself ordinary, so crediting the change would not alter the box; the text does not say which paragraph governs when
the improvement, credited in full, still leaves ordinary returns, and a sentence saying so would stop two analysts closing
the same file in different boxes. (3) **The maintenance guess (e).** Q7 makes the maintenance-only case central "where the
filing allows the guess", but does not say what to do when the filer's own maintenance figure is a third of depreciation
and the rows on depreciation point the other way; the choice moved the computed value from below zero to $72.70 a share.
I took depreciation, citing the depreciation rows, and showed the filer's figure beside; the text should say which
governs, or that the lower of the two maintenance guesses is never central without evidence that the fleet keeps its
place on it. (4) **The equity-only figure's interest.** Part VII's equity-only figure is owner cash after interest; where
debt has risen sharply after the window (here from nil to $328M), interest as paid over the window or cycle understates
what the equity now bears, and the figure comes out positive while the all-equity figure is negative. The text should say
whether the interest is as paid or on the latest filed debt; I showed both.
