# Company Run - Exxon Mobil Corporation (NYSE: XOM) - 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its accession. Working folder: `Test Runs/_research 2026-10-06 XOM/` (`fetch.py` and
`list_10k.py` for EDGAR, `arithmetic.py` and its output for every computed number below, `ledger_grep.py` and
`ledger_show.py` for the ledger, the `tools/run.py` print and the routing wrapper `run_py_legacy_cik.py`; raw filings and
their text dumps under `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not opened,
so whether the operator holds XOM is unknown to the analyst.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, `tools/alerts.json`, and any earlier run or research folder
for XOM in `Test Runs/`, `Framework/v4/` or `Framework/v5/tests/` (no listing of `Test Runs/` was filtered for XOM or
Exxon). Opened for form only: `Test Runs/2026-10-05 Run - AMR Alpha Metallurgical.md` (Step 0 to Q3), a coal producer, not
this name. Seen without opening: a listing of ten 2026-10-05 run file names (ABG to BRK.B), none of them XOM. Training
memory, declared as a prior to be replaced by the filings: that Berkshire has owned large stakes in other oil producers in
recent years and that Exxon is a descendant of Standard Oil; and an expectation that the ticker resolved to Exxon Mobil
Corp, CIK 34088. The filings replaced that last one at once: the ticker now resolves to ExxonMobil Holdings Corporation
(Step 0).

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **The registrant changed on 2026-07-01.** Exxon Mobil Corporation (New Jersey, CIK 34088) completed a redomiciliation
  merger into ExxonMobil Holdings Corporation (Texas, CIK 2115436); each share was "automatically exchanged for one share"
  of the new parent, which "replaced ExxonMobil as the publicly held corporation traded on the New York Stock Exchange"
  under "XOM"; the directors and officers are the same (8-K12B, filed 2026-07-01, accession 0001193125-26-291990). Every
  annual report read below was filed by CIK 34088.
- **Price:** $164.00 (close 2026-10-05; `tools/run.py`, aggregator, live quote only, flagged per operator rule 5).
- **Shares:** one class, 4,111,911,960 outstanding at 2026-06-30 (10-Q cover, filed 2026-08-03, accession
  0000034088-26-000093; `python Screens/cover_shares.py XOM`). The 10-Q balance sheet agrees: 8,019M issued less 3,907M in
  treasury. The one-for-one exchange of 2026-07-01 leaves the count unchanged.
- **Market cap:** $164.00 x 4,111.912M = **$674,354M** (`arithmetic.py`).
- **Sovereign for the earnings currency (USD; the XBRL unit of the cash-flow series):** 5.66%, US Treasury daily par yield
  curve, 30-year, 2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-18, 0000034088-26-000045): Item 1, Item 1A in part, the
  oil and gas production price and cost tables, MD&A (business environment, Upstream results, Frequently Used Terms, cash
  flow), the cash-flow statement, Note 18 (Incentive Program). 10-K FY2022 (0000034088-23-000020), FY2019
  (0000034088-20-000016) and FY2016 (0000034088-17-000017): cash-flow statements, ROCE tables, production cost tables,
  identified items, Note on the Incentive Program. 10-Q Q2 2026 (0000034088-26-000093): cover, balance sheet, cash flow.
  8-K of 2026-07-31 (0002115436-26-000006), EX-99.1 earnings release, its headline page only. 8-K12B above. DEF 14A 2026
  (0001193125-26-147614) fetched and not read (the file closed before Q5).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, $51,970M on
  the filed cash-flow statement (10-K FY2025) equals the $51,970M `tools/run.py` transcribes from XBRL.
- **`tools/run.py XOM` failed** ("XOM: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.", saved as
  `run_py_output.txt`): SEC's ticker file maps XOM to the new holding company, CIK 2115436, which has no annual XBRL
  history. A routing wrapper (`run_py_legacy_cik.py`) pointed the tool's CIK lookup at 34088 and changed nothing else;
  its print is `run_py_output_legacy_cik.txt`, and only its arithmetic lines are used (Part VII). It found no stock pay in
  XBRL ("n/f") and could not read any linkbase (HTTP 429); stock pay is taken from the filed notes below.

**Owner cash by year** (filed cash-flow statements; OCF less stock pay as charged against income in Note 18 or its
predecessors, less additions to property, plant and equipment, less additional investments and advances into equity
companies, plus other investing activities including collection of advances; USD millions; `arithmetic.py`):

| year | OCF | stock pay | PP&E | invest. & adv. | collections | owner cash | source |
|---|---|---|---|---|---|---|---|
| 2014 | 45,116 | 831 | 32,952 | 1,631 | 3,346 | 13,048 | 10-K FY2016 |
| 2015 | 30,344 | 855 | 26,490 | 607 | 842 | 3,234 | 10-K FY2016 |
| 2016 | 22,082 | 880 | 16,163 | 1,417 | 902 | 4,524 | 10-K FY2016 |
| 2017 | 30,066 | 856 | 15,402 | 5,507 | 2,076 | 10,377 | 10-K FY2019 |
| 2018 | 36,014 | 774 | 19,574 | 1,981 | 986 | 14,671 | 10-K FY2019 |
| 2019 | 29,716 | 741 | 24,361 | 3,905 | 1,490 | 2,199 | 10-K FY2019 |
| 2020 | 14,668 | 672 | 17,282 | 4,857 | 2,681 | -5,462 | 10-K FY2022 |
| 2021 | 48,129 | 612 | 12,076 | 2,817 | 1,482 | 34,106 | 10-K FY2022 |
| 2022 | 76,797 | 648 | 18,407 | 3,090 | 1,508 | 56,160 | 10-K FY2022 |
| 2023 | 55,369 | 600 | 21,919 | 2,995 | 1,562 | 31,417 | 10-K FY2025 |
| 2024 | 55,022 | 800 | 24,306 | 3,299 | 1,926 | 28,543 | 10-K FY2025 |
| 2025 | 51,970 | 1,000 | 28,358 | 4,133 | 3,406 | 21,885 | 10-K FY2025 |
| H1 2026 | 32,260 | not in the 10-Q | 12,997 | 711 | 734 | 19,286 before stock pay | 10-Q Q2 2026 |

Five-year mean 2021-2025: **$34,422M** ($32,445M without crediting collections), a 5.10% yield on the market cap. Ten-year
mean 2016-2025: **$19,842M**, a 2.94% yield. The five-year window opens in the year after the 2020 trough and holds the
2022 peak; the ten-year window holds both troughs. The 2024 and 2025 figures include Pioneer Natural Resources, bought
2024-05-03 for 545 million new shares (Q6, not reached).

---
## THE FOUNDATIONS (not a gate)
A share is a business, and the market "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. No macro forecast
enters **[M2000-094]**, and the speakers apply that to this commodity by name: "We’re not going to comment, you know, on oil
or the prices of anything in terms of making any forecasts about it." **[M2001-103]**; "I really didn’t think we could guess
the price of oil" **[M2011-044]**; "if we were in an oil stock, it’s because we think it offers a lot of value at this price,
but it does not mean that we think the price of oil is going up." **[M2007-129]**. For a producer, then, the analyst must find
what the business earns without a view on the price it sells at; the speakers' own measure for a commodity producer is its
cost: "If we owned a copper mining company in its entirety, we would measure it, probably, more by cost of production than
we would by whether copper was selling for $2.00 a pound or a dollar a pound." **[M2006-004]**. Who is paid to tell you: the
earnings release headlines "Cumulative structural cost savings of $16.3 B, more than all other IOCs combined" (EX-99.1,
0002115436-26-000006); that is the seller's claim and is tested against the competitors' filings at Q2, not taken
**[M2011-083]**. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**.

**Contrary evidence, written down as found** **[M1997-127]**. Against the business: (1) a net loss of $22,440M in 2020,
$20,060M of it impairments, and a loss of $1,412M even after the company's own "Identified Items" are removed (10-K FY2022);
(2) owner cash of -$5,462M in 2020 and $2,199M to $4,524M in 2015, 2016 and 2019 (table above); (3) in 2020 operating cash
of $14,668M against $22,139M of capital spending and $14,865M of dividends, with total debt rising from $46,920M to $67,640M
(10-K FY2019, FY2022); (4) the 10-K's own words, "the commodity-based nature of many of our businesses" and prices "may be
significantly impacted by [...] the actions of OPEC or OPEC+ and other large government resource owners" (10-K FY2025);
(5) Chevron's consolidated production cost per oil-equivalent barrel was below Exxon's in every year 2020-2025 (Q2 row).
For the business: (6) 4.7 million oil-equivalent barrels a day in 2025, "our highest production in over 40 years", and a
2025 production cost of $3.75 to $5.15 a barrel in Asia and $5.60 in Australia/Oceania (10-K FY2025); (7) Exxon's
corporate ROCE beat Chevron's in eight of the nine years 2017-2025, 9.8% against 7.9% on the mean (Q2 row); (8) the
dividend was paid in full through 2020 (10-K FY2022, cash flow); (9) the speakers themselves name a big integrated oil
company as easy to understand **[M2004-081]**, and Standard Oil as "practically the only one, after it got monstrous,
continued to do monstrously well" **[M2013-009]**.

## THE STANDING RULE
A cash purchase of a listed share, unlevered and sized so that its total loss is survivable, gives no one a call on the
buyer: "One investment rule at Berkshire has not and will not change: Never risk permanent loss of capital." **[L2023-005]**;
"You never get in a position, obviously, where the other fellow can call your tune." **[M2006-079]**. The target's own debt
and exposures (the 2020 borrowing, the single-well loss of **[M2014-080]**) are Q9's, not the buyer's ruin. No breach.

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]**; the product can stay opaque if "I understand the economic dynamics of the industry. Is there —
  are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The economics, from the filings.** Four segments: Upstream (oil, gas, bitumen; 2025 earnings $21,354M), Energy Products
  (refining and fuels), Chemical Products and Specialty Products (10-K FY2025). Upstream sells at the market: 2025 realized
  crude $65.18 a barrel against $76.57 for consolidated crude in 2024, and the 2025 Upstream earnings driver reads "Price –
  Lower realizations decreased earnings by $6.1 billion" (10-K FY2025). Profit per barrel is the world price less a cost
  that moves slowly; the downstream segments earn a margin between two commodity prices ("Chemical margins remaining at
  bottom-of-cycle", 10-K FY2025). The speakers on this very kind of company: "a big integrated oil company, it’s fairly easy
  to get your mind around the economic characteristics that will exist in the business" **[M2004-081]**; and the decision
  is made "off the figures" **[M2008-069]**, from a report "anybody can get" **[M2005-015]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**. (1) Volume: production of 4.7 Moebd in 2025, with
  "about two thirds" from Permian, Guyana and LNG and the Permian planned to "approximately 2.5 Moebd by 2030" (10-K FY2025):
  foreseeable within a band, from reserves and projects on the record. (2) Cost per barrel: consolidated production cost
  $11.29 to $13.09 a barrel over 2020-2025 (Q2 row): foreseeable within a band. (3) The price of oil, gas and refined and
  chemical margins: crude realizations fell from $76.57 to $65.18 in one year (10-K FY2025), and net income ran from
  -$22,440M (2020) to $55,740M (2022) (10-K FY2022). Not foreseeable, and the speakers say so of oil itself **[M2001-103]**,
  **[M2011-044]**, **[M2011-047]**. (4) Ten-year demand for oil and gas: the 10-K names "net-zero scenarios" and government
  actions as risks to demand (Item 1A); the change is slow, and "slow change can be much harder to perceive, and can lull
  you to sleep easier" **[M2014-038]**.
- **Would the insiders write it down?** **[M2000-105]**. They do: the company plans to 2030 on its own "Global Outlook" and
  states production and cost-saving plans to 2030 (10-K FY2025, MD&A). That is a written forecast of volume and cost, not
  of price.
- **Routing.** Not a fast-changing industry closing at Q1 (the routing fixed under What understanding means). What cannot be
  foreseen is the price, and for a price-taker the price is the castle question (Q2: whose cost sets it) and the value
  question (Q7: how sure is the cash). The doubt rule **[M2002-092]** is applied to the economics, which can be read from
  the filings of Exxon and its competitors.
- **VERDICT: IN**, with the price carried forward as the open variable **[M2004-081]**, **[M2011-014]**, **[M2006-004]**.
  (The alternative reading, TOO HARD (NATURE) on the price, is recorded under What in the framework was wrong or unclear.)

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

- **Is it a commodity?** The rows define the commodity by the customer's indifference: "the product is available from many
  suppliers [...] most insureds don't care from whom they buy." **[L2004-003]**. Exxon's own words: "the commodity-based
  nature of many of our businesses"; "The energy and petrochemical industries are highly competitive"; competition comes
  "not only from other private firms, but also from state-owned companies"; and on price, "prices may be significantly
  impacted by political events, the actions of OPEC or OPEC+ and other large government resource owners" (10-K FY2025,
  Items 1, 1A and MD&A). A barrel is sold at the world price for its grade; nobody asks for an Exxon barrel by name. The
  price is set by others, as at the gas station: "whatever he charged for gas was my price" **[M2012-109]**; "he determined
  our profit, because we looked at his price every day" **[M2023-079]**. The speakers on this industry: "supply and demand on
  a huge commodity" **[M2007-056]**; and of a huge oil producer, "It is a — it is a investment that depends on the price of
  oil." **[M2020-035]**. The downstream segments are commodity too: "Chemical margins remaining at bottom-of-cycle" (10-K
  FY2025); "most chemical products are sort of commoditized" **[M2017-039]**. It is a commodity business in all four segments.
- **Pricing power and the agony before a rise** **[M2005-020]**. None to test: the company reports price as an outcome,
  "Price – Lower realizations decreased earnings by $6.1 billion" (2025 Upstream driver, 10-K FY2025).
- **The one exception: the low-cost producer.** "when a company is selling a product with commodity-like economic
  characteristics, being the low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless
  you’re the low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**; measured against
  "your other major competitors" **[M2001-013]**; "It’s like comparing a copper producer whose costs are $2.50 a pound with a
  copper producer whose costs are $1 a pound. Those are two different kinds of businesses. One is going to go broke at a
  buck-fifty a pound. And the other one’s going to still be doing fine." **[M2009-059]**.

**The competitor row** (each from the filer's own 10-K; `arithmetic.py`). ROCE is each company's corporate total as it
defines it (net income before after-tax financing costs over average capital employed; Exxon includes its share of equity
companies' debt, Chevron adds back noncontrolling interest). Production cost is "average production costs" per
oil-equivalent barrel of consolidated subsidiaries, gas at 6 mcf to the barrel in both, before depreciation and depletion.

| year | XOM ROCE | CVX ROCE | XOM production cost $/boe | CVX production cost $/boe |
|---|---|---|---|---|
| 2014 | 16.2 (32,984 / 203,110, filed lines) | not read | not read | not read |
| 2015 | 7.9 | not read | not read | not read |
| 2016 | 3.9 | not read | not read | not read |
| 2017 | 9.0 | 5.0 | not read | not read |
| 2018 | 9.2 | 8.2 | not read | not read |
| 2019 | 6.5 | 2.0 | not read | not read |
| 2020 | **-9.3** | -2.8 | 11.57 | 10.07 |
| 2021 | 10.9 | 9.4 | 12.15 | 9.90 |
| 2022 | 24.9 | 20.3 | 13.09 | 10.16 |
| 2023 | 15.0 | 11.9 | 12.05 | 10.23 |
| 2024 | 12.7 | 10.1 | 11.70 | 9.23 |
| 2025 | 9.3 | 6.6 | 11.29 | 9.71 |
| mean 2017-2025 | **9.8** | **7.9** | | |
| mean 2020-2025 | | | **11.97** | **9.88** |

Sources: Exxon 10-K FY2016 0000034088-17-000017, FY2019 0000034088-20-000016, FY2022 0000034088-23-000020, FY2025
0000034088-26-000045 (Frequently Used Terms, ROCE; Oil and Gas Production, production prices and costs). Chevron 10-K
FY2019 0000093410-20-000010, FY2022 0000093410-23-000009, FY2025 0000093410-26-000078 (Return on Average Capital Employed;
Table IV, average production costs per barrel, consolidated companies total). Chevron's 10-K FY2016 (0000093410-17-000013)
was fetched; its primary document carries no ROCE table and it was not read further. Exxon's equity companies (Qatar,
Kazakhstan) produce far cheaper, $4.49 a barrel in 2025, which brings its all-in figure to $10.20; Chevron's affiliates are
likewise cheap (TCO $3.80, others $3.47 in 2025), and Chevron prints no all-in figure, so the like-for-like line is the
consolidated one.

- **What the row shows, over the span, not one year.** On return, Exxon is the better of the two in eight of nine years and
  by about two points on the mean. On cost per barrel, Exxon is the dearer of the two in every year read, by 15% to 29%. On
  the trough test it is the worse: in 2020 Exxon's ROCE was -9.3% against Chevron's -2.8%, its net income -$22,440M with
  $20,060M of impairments, and -$1,412M even after the company's own Identified Items are removed (10-K FY2022). Neither
  company is the producer that is "still going to be doing fine" at the low price **[M2009-059]**: both lost money in 2020,
  and the price that year was set by the "large government resource owners" Exxon's filing names, not by either of them
  (10-K FY2025). The national companies' own costs were not read (no SEC filings); the evidence that they, not Exxon, set the
  price is Exxon's own sentence. Exxon is not the low-cost producer of its industry, and on the one direct cost measure the
  filings give it is not even the low-cost producer of the pair.
- **The trough, in cash.** 2020: operating cash $14,668M, capital spending $22,139M, dividends $14,865M; total debt rose from
  $46,920M to $67,640M (10-K FY2019, FY2022). Owner cash was negative that year and $2,199M to $4,524M in 2015, 2016 and 2019
  (Step 0). In an unregulated commodity business "a company must lower its costs to competitive levels or face extinction"
  **[L1994-035]**; Exxon did not face extinction, which the balance sheet bought (Q9, not reached), but the castle did not
  hold the return: ROCE 16.2% to 3.9% in two years (2014 to 2016) and 6.5% to -9.3% in one (2019 to 2020).
- **The returns the castle protects, if any.** The moat must protect "excellent returns on invested capital" **[L2007-004]**,
  for "a very long period of time" **[M2007-023]**. Exxon's twelve-year mean ROCE is 9.7% (2014-2025), swinging from -9.3% to
  24.9% with the price. The swing is the price, not the company: the speakers' own description of the oil business is that
  "if oil sells at X, you know, you do very well. And if it sells at half of X, you know, your costs are the same"
  **[M2023-082]**.
- **The attacker with money** **[M2011-015]**. Oil reserves are costly to find and slow to develop, so entry is not free. But
  money buys them: Exxon itself bought Pioneer's Permian position for 545 million shares worth $63B (10-K FY2025, cash-flow
  statement note). The barrier protects the barrels, not their price, and fewness does not cure a commodity: "you can have
  only two competitors and they’re still terrible businesses" **[M2013-052]**. The speakers on choosing among the majors:
  "You’re not going to have a big edge in trying to pick Chevron against Exxon against Continental and Occidental, and you
  name it." **[M2011-012]**.
- **Unit volume, widening or narrowing.** Production 4.7 Moebd in 2025, the highest "in over 40 years", Permian 1.6 Moebd and
  Guyana 715 kbd (10-K FY2025). The volume is real, but volume is the moat's evidence only where it measures a place in the
  customer's mind **[M1999-054]**, **[M1997-099]**; here it is barrels sold at the market. Structural cost savings of $15.1B
  since 2019 (10-K FY2025) are the "unrelenting foot-to-the-floor strategy" **[L2004-007]**, but of a company that does not
  hold the low-cost title on the filings above.
- **A moat that must be rebuilt every year.** A field depletes as it is produced; the speakers compare it to float: "every
  day, some goes out [...] and the question is, did you find more oil than you produced that day?" **[M2002-006]**. Exxon
  spent $15.4B to $33.0B a year on property, plant and equipment over 2014-2025 (Step 0) to stand still or grow. "A moat
  that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**. This is a weight on the castle; it
  is also Q3's question, and Q3 is not reached.
- **Ask the competitors** **[M1999-130]**, **[M2025-043]**. Not done (no access); the filed returns and costs above are the
  nearest public answer.
- **What could destroy it.** A long low price set by others (2015-2016 and 2020 show what that does); a single accident
  **[M2014-080]**; the Kazakh export route through Russia (10-K FY2025, "Transportation of Kazakhstan Production"); demand
  policy (Item 1A). Each is a reason the 2020 result can recur.
- **The other routes through a commodity field.** **[L2004-007]** begins "Another way", so the low-cost position is not the
  only route **[L2004-007]**. Searched for one here: integration of upstream, refining and chemicals is the company's own
  claim of advantage (10-K FY2025, "integrated business model"). Its segments did not offset one another in the trough:
  Energy Products lost $2,572M in 2020 and $347M in 2021 while Upstream lost $20,030M in 2020 (10-K FY2022); Chemical
  Products earned $800M in 2025 at "bottom-of-cycle" (10-K FY2025). No route found that earns a return independent of the
  commodity prices.
- **Contrary evidence, written as found** **[M1997-127]**. The speakers have bought oil producers: PetroChina "simply because
  it was very, very cheap" and "far cheaper than Exxon, or BP, or Shell" **[M2004-082]**, and a later oil purchase that was
  "something to act on" though "I dont know what the price of oil is going to be next year" **[M2024-054]**. Both rows are
  bought-cheap rows, about price; neither names a castle, and **[M2020-035]** says what such a purchase depends on. Standard
  Oil as the one giant that "continued to do monstrously well" **[M2013-009]** is a statement about size and history, not
  about the price-setting in the industry today, which Exxon's own filing assigns to OPEC+ and government owners.
- **VERDICT: OUT.** A commodity seller whose price is set by others (its own 10-K: OPEC, OPEC+ and "large government resource
  owners") **[M2012-109]**, **[L2004-003]**, that is not the low-cost producer of its industry and is not even the low-cost
  producer against Chevron on the filed cost per barrel **[L2000-017]**, **[M1997-010]**, **[M2009-059]**, whose returns follow
  the price of oil rather than any advantage of its own **[M2020-035]**, **[M2023-082]**, and whose reserves must be bought or
  found again each year **[L2007-005]**. The castle is shown open on the evidence, so the box is OUT, not TOO HARD
  **[M2006-013]**, **[M2011-015]**; price does not reopen it: "What you can’t do is turn any investment into a good deal by
  paying little" **[M2019-015]**; marginal businesses bought cheap "are the wrong foundation on which to build a large and
  enduring enterprise" **[L2014-009]**. The policy in one line: "We’re going to be investors in businesses, not commodities,
  by and large." **[M2007-131]**.

**The file closes here. Q3 to Q12 are NOT REACHED; nothing below is a clearance.**

---
## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
Facts only, for the record: additions to property, plant and equipment ran $15,402M (2017) to $32,952M (2014), and were
$28,358M in 2025 against depreciation and depletion of $25,993M including impairments (10-K FY2025; Step 0 table).

## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
Facts only, not a reading: the ten-year balance-sheet table is in `run_py_output_legacy_cik.txt` (XBRL transcription,
first-filed vintage). Total equity attributable to Exxon rose from $167,325M (2016) to $259,386M (2025), with the $63B of
stock issued for Pioneer in 2024 inside the rise; cash and equivalents $10,681M at end-2025 (10-K FY2025). The company
reports "Earnings (loss) excluding Identified Items" and the Q2 2026 release headlines "adjusted EPS" (EX-99.1,
0002115436-26-000006); whether that is a tell under Q4 was not judged.

## Q5 - WHO RUNS IT. NOT REACHED. (DEF 14A 2026, 0001193125-26-147614, fetched, not read.)

## Q6 - WHAT WILL THEY DO WITH THE MONEY. NOT REACHED.
Facts only: Pioneer was acquired on 2024-05-03 "in an all-stock transaction", 545 million shares with a fair value of $63
billion (10-K FY2025, cash-flow statement note); common stock acquired $17,748M, $19,629M and $20,273M in 2023-2025 (same
statement). The all-stock STOP of Q6 Part A and the buyback test need the bottom of a Q7 range, which was not built.

## COMPUTATION - NOT A CLEARANCE (the file closed OUT at Q2)
Owner cash yield on the market cap of $674,354M: 5.10% on the 2021-2025 mean of $34,422M, 2.94% on the 2016-2025 mean of
$19,842M, against the 30-year Treasury at 5.66% (`arithmetic.py`). `tools/run.py` (via the wrapper) prints a 5.40% capex-basis
yield on its own five-year owner-earnings mean, which deducts no stock pay and no investments in equity companies; its
lines 2 and 3 are not used. No value range was built; Q7 is NOT REACHED.

## Q7 to Q10, Q12 - NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q2**: a commodity seller whose price is set by others, not the low-cost producer of its industry nor of
the pair with Chevron on the filed cost per barrel, whose returns follow the price of oil **[M2012-109]**, **[L2000-017]**,
**[M2009-059]**, **[M2020-035]**. Q7 not reached; no range. Price $164.00 (aggregator, 2026-10-05), 4,111,911,960 shares
(10-Q cover, 0000034088-26-000093), market cap $674,354M, 30-year Treasury 5.66% (2026-10-05). The reversal condition, in
the rows' terms and not in price: filed evidence, over a span that includes a price trough, that Exxon produces at a cost
below the competitors that set the price, so that it is the one "still going to be doing fine" when the price falls
**[M2009-059]**, **[L2000-017]**; a lower price does not reopen the file **[M2019-015]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0
      to Q1 in 89cd57b, Q2 in e4588f2, this close in the next commit.
- [x] Every v5 id resolves (`cite_check.py`: no missing ids); every filing fact has its accession; no number without a row or
      a filing; computed numbers are in `arithmetic.py` and its output.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance (Q3, Q4 and Q6 carry facts only;
      the computation is headed as operator rule 3 requires).
- [x] Owner cash after every real cost, never a net-income proxy: OCF less stock pay from the filed notes, less all capital
      spending including investments in equity companies (operator rule 5); the sovereign from the US Treasury; the price
      flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations; Q2's contrary-evidence line).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its stock-pay gap and linkbase failure are recorded.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Whom the low-cost producer is measured against.** Q2 asks for the low-cost position and **[M2001-013]** measures it
against "your other major competitors", but in oil the price is set, on the filer's own word, by OPEC+ and government
resource owners who file nothing with the SEC, while the template asks for a competitor row "from the competitors' own
filings". The run used the one listed peer of like size and recorded the national producers as not read. The two measures
the filings give also pointed opposite ways: Exxon beat Chevron on ROCE in eight of nine years but had the higher cost per
barrel in all six years read. The framework names no measure that decides between return and unit cost; the run let the
unit cost and the 2020 trough decide, because **[M2009-059]** and **[M2006-004]** speak of cost of production and the
trough, and recorded the ROCE lead as contrary evidence. A second analyst could weigh it the other way and still close OUT
on the price-setter point; a rule naming the measure would make the row decisive. (2) **Q1 against Q2 for a price that
cannot be foreseen.** As in the AMR run of 2026-10-05, the unforeseeable variable is the commodity price; the run read Q1 as
the economics and sent the price to Q2 under the routing paragraph, but **[M2020-035]** ("It is a — it is a investment that
depends on the price of oil") could equally close Q1 TOO HARD (NATURE). The routing sentence speaks of industries that
"change fast", not of a stable industry whose one key variable is unforecastable; a sentence for the price-taker would
settle it. (3) **The speakers' own oil purchases.** The ledger holds rows of the speakers buying oil producers on price
(**[M2004-082]**, **[M2024-054]**), and Q2's STOP says price does not reopen a castle. Q2 carries one stated exception, the
newspapers bought at a low multiple; it carries none for a commodity producer bought cheap, and is silent on whether these
rows are such an exception or the "fair business at a wonderful price" the rows otherwise refuse. The run treated them as
contrary evidence, not as an exception. (4) **Tool defects, reported, not fixed.** `tools/run.py XOM` returned "no
overlapping OCF/D&A/capex annual facts. UNRESEARCHED." because SEC's ticker file now maps XOM to ExxonMobil Holdings Corp
(CIK 2115436, formed by the redomiciliation of 2026-07-01), which has no annual XBRL; the tool has no CIK override and
`tools/sources.py` has a name-change note but no successor-registrant check. Any redomiciled or newly holding-company filer
will fail the same way. Through a routing wrapper the tool also found no stock pay in Exxon's XBRL ("n/f" in all five
years, though Note 18 states $0.6B to $1.0B a year), and its linkbase reads failed on HTTP 429, so its owner-earnings line
overstates by the stock pay and omits investments in equity companies.

## WHAT I COULD NOT GET
Chevron's ROCE and production costs before 2017 and 2020 respectively (its FY2016 primary document holds no such table;
the FY2019 10-K's production-cost table was not read); the national oil companies' costs; any competitor interview. None of
these would move the price-setter finding, which rests on Exxon's own 10-K.
