# Company Run — Peabody Energy Corporation (NYSE: BTU) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*(Copied from the template before any fetch. Working folder: `Test Runs/_research 2026-10-06 BTU/`; every script used is
there: `fetch.py`, `h2t.py`, `tables.py`, `xbrl_annual.py`, `peer_returns.py`, `value.py`, `q.py`. Template headings are
kept as the template prints them; the prose of this run uses no em dashes.)*

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this run's blind rule, so
whether the operator holds BTU is unknown to the analyst. The run is written as a purchase run of record.

**CONTAMINATION DECLARED.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the
prepped reading list, any other `Test Runs/` file about BTU, any other 2026-10-05 or 2026-10-06 run or research file, the
unadopted small-cap gaps case. Seen without opening, in the session's own context: the subjects of the five most recent
commits (ADT OUT at Q2; GPOR OUT at Q2 as a "gas price-taker with no barrier to entry"; POOL OUT at Q7; KTB TOO HARD
(NATURE) at Q2; SBH OUT at Q2), the git-status file names of the HRMY, NSIT and PTEN runs of 2026-10-06, and a memory
note that the wave so far has "57 gate-clearers, nothing buyable". The GPOR subject is the closest to this name (another
price-taker); it was read before any BTU filing was opened and is named here so that the reader can weigh it.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $25.50 (close 2026-10-05; aggregator quote via `tools/run.py`, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock, **121.9 million** outstanding at
  2026-08-03 (10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001064728-26-000050`, cover page:
  "There were 121.9 million shares of the registrant’s common stock ... outstanding at August 3, 2026"). Read by hand:
  `python Screens/cover_shares.py BTU` printed 1,064,728,000,000 shares, which is the company's CIK (1064728) scaled by a
  million, a tool fault recorded in the last section. No preferred or series common outstanding (same balance sheet).
- **Market cap:** $3,108.5M (121.9M × $25.50).
- **Sovereign for the earnings currency:** USD, **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, `0001064728-26-000006`); 10-Q Q2 2026 (filed
  2026-08-06, `0001064728-26-000050`); proxy DEF 14A (filed 2026-03-26, `0001064728-26-000012`); 8-Ks of 2024-11-25
  (Anglo agreements, `0001193125-24-264712`), 2025-08-19 (termination, `0001064728-25-000122`), 2026-06-02 (convertible
  notes, `0001193125-26-252668`), 2026-06-15 (Australian surety facilities, end of the 2020 surety support agreement,
  `0001193125-26-270268`), 2026-07-01 (revolver amendment, `0001193125-26-291466`), 2026-07-29 (Q2 results and dividend,
  `0001064728-26-000038`); 8-K of 2017-03-20 (plan confirmation, `0001193125-17-088305`); predecessor and later 10-Ks
  FY2011 (`0001064728-12-000020`), FY2014 (`0001064728-15-000021`), FY2016 (`0001064728-17-000026`), FY2019
  (`0001064728-20-000007`), FY2021 (`0001064728-22-000008`), FY2022 (`0001064728-23-000013`), FY2024
  (`0001064728-25-000018`); XBRL company facts for 2009 to 2026.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$333.7M**
  in the filed consolidated statement of cash flows (10-K `0001064728-26-000006`, page F-6) against 334 in `tools/run.py`
  and 333.7 in the XBRL facts. Additions to property, plant, equipment and mine development FY2025 $411.4M (F-7) against
  411 in `tools/run.py`. Both agree.
- `python tools/run.py BTU`, arithmetic lines only (Part VII; its printed yields, "growth the price assumes" and floor
  lines were not used): OCF − SBC − capex 2023 to 2025: 680, 198, −92 ($M); five-year window 391 (capex basis) and 370
  (D&A basis). Its "mine development alternates" line did not print: Peabody files one combined line, "Additions to
  property, plant, equipment and mine development", so there is no separate mine-development figure to choose. The tool
  does not separate the collateral postings and releases inside OCF (2023 −199.6, 2024 +149.1, 2025 −7.3, H1 2026 +75.8;
  10-K and 10-Q cash-flow statements), nor the distributions to noncontrolling interests (2021 4.0, 2022 17.5, 2023 59.0,
  2024 34.8, 2025 22.9; FY2022 and FY2025 10-Ks), which are cash that does not reach Peabody's owners. Fresh-start
  accounting on 2017-04-01 breaks every series: 2017 is filed as a predecessor quarter and a successor nine months.

### The balance sheets, read before the income account (Q4's instruction, read here because the file closes before Q4)
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. USD millions;
`tools/run.py` table checked against the filed statements of the FY2019, FY2022 and FY2025 10-Ks and the Q2 2026 10-Q.

| year-end | total assets | equity (Peabody) | cash | debt (filed) | retained earnings | inventory | ARO | restricted cash and collateral |
|---|---|---|---|---|---|---|---|---|
| 2017-04-01 fresh start | 8,267 | 3,132 | n/a | 1,881 | 0 | n/a | n/a | n/a |
| 2017 | 8,181 | 3,656 | 1,070 | 1,461 | n/a | n/a | 691 | n/a |
| 2018 | 7,424 | 3,396 | 982 | 1,367 | 1,074 | 280 | 750 | n/a |
| 2019 | 6,543 | 2,614 | 732 | 1,311 | 597 | 332 | 752 | n/a |
| 2020 | 4,667 | 930 | 709 | 1,548 | −1,273 | 262 | 728 | n/a |
| 2021 | 4,950 | 1,762 | 954 | 1,138 | −913 | 227 | 720 | n/a |
| 2022 | 5,611 | 3,231 | 1,307 | 334 | 384 | 296 | 750 | n/a |
| 2023 | 5,962 | 3,547 | 969 | 334 | 1,113 | 352 | 703 | n/a |
| 2024 | 5,954 | 3,650 | 700 | 348 | 1,446 | 393 | 724 | 810 |
| 2025 | 5,807 | 3,536 | 575 | 336 | 1,356 | 383 | 755 | 844 |
| 2026-06-30 | 5,449 | 3,249 | 526 | 339 | 1,214 | 440 | n/a (692 non-current) | 460 |

What the figures say: the equity of a company emerged from bankruptcy in April 2017 at $3,132M fell to $930M by the end
of 2020 (retained earnings −$1,273M after a $1,418.1M impairment of North Antelope Rochelle, FY2021 10-K note 3); it came
back only through the 2021 and 2022 price spike and about $492M of new shares (below). Debt fell from $1,548M (2020) to
$334M (2022) and has stayed there. No goodwill of note after fresh start. Inventory rose from $227M (2021) to $440M
(June 2026) while revenue fell from $4,982M (2022) to $3,862M (2025): more coal on the ground, less sold for money. The
asset retirement obligation stays near $700M to $755M across nine years and is matched by a growing pile of restricted
cash and collateral ($844M at the end of 2025), cash the owners cannot use; $384M of it was released in H1 2026 when
Australian surety facilities replaced 100% cash-collateralised programmes (8-K `0001193125-26-270268`). What they do not
say: the cost of the next reclamation decades (bonding is $908.8M of surety for reclamation alone, 10-K MD&A, off-balance
sheet table), and the size of the Anglo damages claim ($755.0M, Q2 2026 10-Q note), which sits off the balance sheet.
Total assets have shrunk by a third since fresh start.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own Peabody "if the market closed for five years?" **[M1997-109]** only if
the business's cash in those years could be pictured, which is the question below. The market "just tells us prices."
**[M2006-077]**: the 2026 talk of data-centre demand and deferred plant retirements is a forecast about electricity, and
"macro conclusions are" **[M2000-094]** kept out of the analysis; it is recorded only as contrary evidence. Margin of
safety: if it needs pencil and paper it is too close; the price must show a "huge margin of safety" **[M1996-084]**. The
analyst's habits: the hunt below is aimed "to possibly reject your original hypothesis" **[M1998-144]**, and evidence for
the business is written down as it is met, "in the first 30 minutes" **[M1997-127]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the 10-K says US coal consumption "is expected to
increase in 2026 which has led to deferrals of planned coal plant retirements", US electricity demand rose over 2% in
2025, coal's generation share rose to about 16% and stockpiles fell 20 million tons (10-K FY2025, Item 1 and MD&A);
(2) the sales backlog rose to 238 million tons at 2026-01-01 from 153 million a year earlier, about two years of output;
(3) North Antelope Rochelle is the lowest-cost large mine in the Powder River Basin on the competitor row below;
(4) seaborne thermal has earned a positive margin every year read (2014 to 2025); (5) Centurion's longwall started in
February 2026 and should add metallurgical tons; (6) net cash about $187M at June 2026, debt only $339M, and the 2020
surety support agreement ended in June 2026 with all obligations satisfied; (7) the 2025 Anglo deal was walked away from
under a MAC clause after the mine fire rather than closed at a price set before it.

## THE STANDING RULE
A cash purchase of a listed share, unlevered and sized so that its loss would not touch what the buyer has and needs,
cannot ruin the buyer through Peabody's own debts or claims: "the only way smart people can get clobbered, really, is
through leverage" **[M2004-065]**; "Never risk permanent loss of capital." **[L2023-005]** is answered by the size and
the financing, not by the target. The target's history (equity cancelled once, near-cancelled again in 2020) bears on
sizing, and is weighed at Q2 and would be at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the product may stay opaque if "What is important is that I understand the
  economic dynamics of the industry." **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]** ("trying to identify the key variables in that
  particular business, and evaluating how predictable they were first"):
  1. *Realized price* in four markets (seaborne metallurgical, seaborne thermal, Powder River Basin, Illinois Basin).
     Not foreseeable, by Peabody or anyone: the 10-K says demand and prices are "influenced by factors beyond the
     Company’s control" (Item 1, Competition). The speakers say the same of every commodity: "we are not two fellows who
     think we can predict the price of soybeans or corn or oil or anything else" **[M2016-025]**; and of the ten-year
     horizon, "if you are going to try and figure out whether when to be long or short oil, or natural gas, or copper or
     cotton or whatever" **[M2011-047]**, no one has the edge. Seaborne metallurgical revenue per ton ran from $75.04
     (2015) to $243.78 (2022) to $120.88 (2025).
  2. *Cost per ton against rivals*: readable, segment by segment, from Peabody's and its competitors' filings over twelve
     years (Q2's competitor row). The rows measure a mine exactly this way: "we would measure it, probably, more by cost
     of production than we would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**;
     "Those are two different kinds of businesses." **[M2009-059]**.
  3. *Volume in US thermal*: the direction is foreseeable and the speakers have said it: "But the decline in coal, for
     sure, is secular." **[M2016-021]**; "coal is going to be phased out over time" **[M2021-041]**. US coal capacity is
     down about forty-six percent since 2010 (10-K FY2025, Item 1).
  4. *Legacy claims* (reclamation, retiree health, black lung, surety collateral): stated, bonded and readable in the
     filings, within a range.
- **Routing.** This is not an industry of fast technological change that puts the ten-year economics out of reach
  (Q1's routing to TOO HARD); its change is a slow secular decline plus a violent price cycle, and slow change is Q2's
  business: "slow change can be much harder to perceive" **[M2014-038]**. The level of a commodity price is "important"
  but it is not one of the "things that are important and knowable" **[M2006-076]**; what is knowable is the cost
  position and the direction of volume, which is what the rows say they would measure a mine by **[M2006-004]**.
- **The doubt rule** ("if you have doubts about something being into your circle of competence" **[M2002-092]**). The
  doubt is real for the price, and it is a doubt every reader shares, which is why the rows send a producer of a
  commodity through Q2's commodity test instead of out at Q1. I can say where Peabody stands in each of its four cost
  curves and where US thermal is heading; I cannot say what coal will fetch. On the reading that Q1 asks about the
  economic dynamics and the competitive position, and that Q2's commodity exception exists precisely to judge a price-
  taker by its costs, the file passes, narrowly. The alternative close (TOO HARD (NATURE) at Q1 on price) is recorded in
  the last section; it would not change the box's meaning, since neither is a pass.
- **VERDICT: IN (narrowly)**, on **[M2011-014]**, **[M2006-004]**, **[M2009-059]** and the filings above, with the price
  level named as unknowable and carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. The answer, test by test, from the filings.

- **Is it a commodity?** Yes, by the filer's own words: thermal customers are "focused on securing the lowest cost fuel
  supply in order to coordinate the most efficient utilization of generating resources in the economic dispatch of the
  power grid"; met coal competes "on the basis of coal quality and characteristics, delivered energy cost (including
  transportation costs), customer service and support and reliability of supply"; US contract terms "result from
  competitive bidding" (10-K FY2025, Item 1). The filing names eight US and eleven international thermal rivals and
  thirteen met rivals. That is the row's mark of a commodity: "most insureds don't care from whom they buy"
  **[L2004-003]**; and the rival sets the price: "whatever he charged for gas was my price" **[M2012-109]**, "he
  determined our profit, because we looked at his price every day" **[M2023-079]**. Fewness of rivals is no cure: "you can
  have only two competitors" **[M2013-052]** and still have a terrible business.
- **Pricing power, and the agony before a rise.** Powder River Basin revenue per ton was $13.49 (2014), $13.45 (2015),
  $13.02 (2016), $11.84 (2018), $11.37 (2019, 2020), $10.99 (2021), $12.89 (2022), $13.74 (2023), $13.81 (2024),
  $13.64 (2025) (FY2016, FY2019, FY2021, FY2022, FY2024, FY2025 10-Ks, MD&A segment tables): flat in dollars for twelve
  years, falling in real terms. Seaborne prices are index prices. No pricing power anywhere.
- **Unit volume and share of mind.** Powder River Basin tons: about 148 million in 2011 (North Antelope Rochelle 109.0,
  Caballo 24.2, Rawhide 15.0; FY2011 10-K, mine table), 142.6 (2014), 113.1 (2016), 120.3 (2018), 87.2 (2020), 82.6
  (2022), 79.6 (2024), 84.5 (2025). Total tons sold from mining segments 229.2 million (2011) to 121.9 million (2025), a
  decline of about 4.4% a year (computed, `value.py`). The test's failing form is the newspaper's: "Fixed costs are high
  in the newspaper business, and that's bad news when unit volume heads south." **[L2006-009]**.
- **Would the customer still choose it over the low bid?** No; the low bid is the whole basis of thermal dispatch (filing
  above), the reverse of See's: "it wouldn’t be a question of people buying candy for the low bid" was the passing
  answer **[M2017-009]**.
- **Could a well-funded attacker take it, and would it be started today?** The attacker is not another miner; it is gas,
  wind and solar, already inside the walls. The 10-K: "since 2010, U.S. coal power capacity has fallen by approximately
  forty-six percent". The 2020 impairment of $1,418.1M at North Antelope Rochelle was booked because of "the accelerated
  decline of coal-fired electricity generation in the U.S., driven by the reduced utilization of plants and plant
  retirements, sustained low natural gas pricing and the increased use of renewable energy sources" (FY2021 10-K, note 3).
  The test is whether the business would be started today against its substitutes: "if cable and satellite broadcasting,
  as well as the internet, had come along first, newspapers as we know them probably would never have existed"
  **[L2006-008]**; no new coal-fired plant appears in any filing read, and banks and insurers "have limited financing and
  insurance coverage for the development of new coal-fueled power plants and for coal producers" (10-K FY2025, Item 1A).
  The speakers' own verdict on the industry: "But the decline in coal, for sure, is secular." **[M2016-021]**.
- **Ask the competitors** **[M2014-057]** ("I would know more about the coal companies from an economic standpoint than any
  one of those managers probably would"). On the public record, the competitors answer with their capital: Arch's FY2020
  10-K speaks of "our stated objective of shrinking our thermal operational footprint" and of idling Coal Creek
  (`0001558370-21-000957`). Arch filed Chapter 11 on 2016-01-11 (Arch FY2017 10-K, `0001628280-18-002109`); Peabody
  followed on 2016-04-13 (8-K `0001193125-16-539191`). The two largest US producers both went through bankruptcy inside
  one year.
- **The low-cost position: the commodity exception.** "Another way to prosper in a commodity-type business is to be the
  low-cost operator." **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**; "the low-cost
  producer can put you out of business" **[M1997-010]**; the measure is relative, "if your costs are on parity or less"
  **[M2001-013]**. Segment by segment, from the competitor row below:
  - *Powder River Basin*: Peabody **is** the low-cost producer (cash cost $9.14 to $12.07 a ton, $0.6 to $2.3 below Arch
    and Core in every year compared). It does not save the segment: its margin has been $0.83 to $3.57 a ton for twelve
    years, segment Adjusted EBITDA $68M (2022) to $285M (2018) on $1.0bn to $1.9bn of revenue, and in Q2 2026 the margin
    was **negative** ($13.63 revenue against $14.06 cost a ton; 10-Q `0001064728-26-000050`, segment table). The rows
    put the exception's force in what is sold: "being a low-cost producer of something that" is "essential to people"
    **[M2004-091]** is "a very good business usually"; the speakers' own example adds "Being the low-cost producer, for
    example, is a terribly important moat." **[M2018-043]**, said of a product that is not shrinking. Here the cheapest
    supplier of a fuel in secular decline **[M2016-021]** keeps about two dollars a ton.
  - *Seaborne metallurgical*: Peabody is **not** low-cost. Its margin was negative in 2014, 2015, 2016 and 2020, $6.57 in
    2025 and negative again in H1 2026 ($143.57 revenue against $148.96 cost a ton, even with Centurion's longwall
    running). Warrior Met Coal, selling at the same kind of port price, earned $27.3 to $66.6 a metric ton more than Peabody in
    every year 2018 to 2025 (row below; Warrior's own margin ran $20.8 to $196.5). Of the high-cost producer the rows say: "In an unregulated commodity business, a
    company must lower its costs to competitive levels or face extinction." **[L1994-035]**.
  - *Other US thermal (Illinois Basin and the West)*: margin $5.33 to $13.19 a ton against Alliance Resource Partners'
    $14.18 to $22.34 over the years compared; not the low-cost operator.
  - *Seaborne thermal*: positive margins every year ($8.59 to $41.42 a ton); no SEC-filing peer was read (Whitehaven is
    not an SEC filer and was not read; flagged). This is the one segment where the record does not answer the cost
    question against a rival.
- **Is the moat widening or narrowing?** Narrowing on every measure the filings give: PRB volume, PRB margin (2026 Q2
  negative), met costs rising from $76.20 (2015) to $114.31 (2025) to $148.96 (H1 2026) a ton, the asset impairment of
  2020, the equity cancellation of 2017. "the old moats, some of them are getting filled in" **[M2001-070]**.
- **What could destroy, modify or reduce it** **[M2000-014]** ("destroy, or modify, or reduce the economic strengths"):
  substitution in US power (under way), steel made without coking coal ("electric arc furnaces", 10-K Item 1),
  financing and surety withdrawn by banks and insurers (10-K Item 1A), and the price cycle itself, which took the equity
  to zero in 2016 and to $930M in 2020.
- **The hunt the other way** (the strongest case for a castle, written down as found): 2025 to 2026 US coal burn rose and
  retirements were deferred; NARM is the cheapest big mine in the basin; seaborne thermal has never lost money in the
  years read; the speakers record that a long-bad industry can turn, "the railroads were a terrible business for decades
  and decades and decades and then they got good" **[M2017-026]**. None of these is a reason the customer must buy from
  Peabody rather than the next bidder, and the best recent US demand year (2025) still left the PRB at $2.08 a ton and
  the company at a net loss to common of $52.9M.

**The competitor row** (same metric, the competitors' own filings; Peabody's "Costs per Ton" and the rivals' cash cost
both exclude depreciation; Arch and Core sell met FOB mine in short tons, Warrior FOB Port of Mobile in metric tons,
Peabody's met FOB vessel in short tons, converted at 1.1023 to metric where set against Warrior):

| metric | 2014 | 2015 | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTU PRB cost / margin, $ per short ton | 9.92 / 3.57 | 9.97 / 3.48 | 9.66 / 3.36 | 9.47 / 2.37 | 9.32 / 2.05 | 9.14 / 2.23 | 9.46 / 1.53 | 12.06 / 0.83 | 11.98 / 1.76 | 12.07 / 1.74 | 11.56 / 2.08 |
| Arch (2025: Core) PRB cash cost / margin | 12.58 / 0.28 (incl. DD&A) | 10.54 / 2.61 | 10.95 / 2.06 (Jan to Oct) | n/a | 10.63 / 1.45 | 11.48 / 0.90 | n/a | n/a | n/a | n/a | Core 13.15 / 1.31 |
| BTU met margin, $ per metric ton | −9.69 | −1.28 | −1.34 | 44.19 | 19.09 | −25.47 | 35.58 | 129.92 | 69.97 | 24.47 | 7.24 |
| Warrior (HCC) met margin, $ per metric ton | n/a | n/a | n/a | 90.37 | 71.57 | 20.81 | 84.00 | 196.54 | 109.04 | 69.22 | 34.54 |
| Arch (2025: Core) met cash margin, $ per short ton FOB mine | −8.82 (incl. DD&A) | 8.26 | 1.75 (Jan to Oct) | n/a | 39.26 | 13.04 | n/a | 130.30 | 77.03 | n/a | Core 6.23 |
| BTU Midwestern / Other US thermal margin, $ per short ton | 12.29 | 12.69 | 11.90 | 7.69 | 8.18 | 9.22 | 9.71 | 13.19 | 12.79 | 10.34 | 5.33 |
| Alliance (ARLP) coal sales less cost per ton | 20.77 | 19.40 | 19.67 | 15.73 | 14.18 | n/a | n/a | 22.34 | n/a | n/a | n/a (cost 41.29) |

Sources: Peabody 10-Ks FY2014 to FY2025 as listed in Step 0; Arch 10-Ks FY2014 (`0001047469-15-001419`), FY2017
(`0001628280-18-002109`), FY2020 (`0001558370-21-000957`), FY2023 (`0001558370-24-001229`); Core 10-K FY2025
(`0001710366-26-000007`); Warrior 10-Ks FY2019 (`0001691303-20-000014`), FY2022 (`0001691303-23-000010`), FY2025
(`0001193125-26-048914`); Alliance 10-Ks FY2016 (`0001558370-17-000983`), FY2019 (`0001558370-20-001103`), FY2022
(`0001558370-23-002034`), FY2025 (`0001104659-26-020468`). Alliance's per-ton figures cover its Illinois Basin and
Appalachian mines together; Arch 2014 "cost per ton sold" includes depreciation, unlike the later cash-cost rows. 2017 is
not shown because both Peabody and Arch report it in split fresh-start periods.

**Returns over the whole span** (net income to common over average equity, XBRL facts, `peer_returns.py`): Peabody lost
money in 2012, 2013, 2014, 2015, 2016, Q1 2017, 2019, 2020 and 2025; cumulative net loss to common 2012 to 2016 $4,633M,
and the equity was cancelled with "No recovery" for holders (8-K `0001193125-17-088305`, plan summary: "The Company’s
current equity securities will be cancelled and extinguished upon the Effective Date"); the plan cut debt "by over $6.6
billion" (FY2016 10-K). Arch's equity was negative at the end of 2015. Alliance earned a positive return in every year
2011 to 2025 except 2020; Warrior in every year 2017 to 2025 except 2020. The low-cost operators in this industry earn
through the cycle; Peabody does not.

**VERDICT: OUT.** The castle is shown open on the evidence, not merely unjudgeable: a commodity sold on the low bid
**[L2004-003]**, with the price set by others **[M2012-109]**, in an industry whose decline the speakers call secular
**[M2016-021]**; low-cost only in the segment that earns about two dollars a ton and is shrinking, and high-cost where
the money is made in good years (met coal, against Warrior every year), which is the case the rows close: "a company must
lower its costs to competitive levels or face extinction" **[L1994-035]**; there are "some industries that are just
never going to have barriers to entry" **[M2012-106]**. A cheap price does not reopen it: "If you really think a business
is declining, most of the time you should avoid it." **[M2012-062]**; "You can turn any investment into a bad deal by
paying too much." **[M2019-015]**, and the converse row rules out "marginal businesses purchased at cheap prices"
as "the wrong foundation on which to build a large and enduring enterprise" **[L2014-009]**. A castle shown open is OUT,
not "too hard" **[M2006-013]** ("in, out, and too hard").

---
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed OUT at Q2).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Operator rule 3. Everything below was produced after the file closed OUT at Q2, at the owner's request (reporting, not
a rule change). It carries no entry language and clears nothing. Arithmetic in `value.py`.*

**Facts gathered for the questions not reached (recorded, not judged):**
- *Capital against depreciation.* Capex 2011 to 2016 $2,609M against D&A $3,579M; 2018 to 2025 $2,343M against D&A
  $3,301M (XBRL facts). Capex exceeded D&A in 2011 and 2012 (the expansion years before the bankruptcy) and again from 2023 (Centurion); 2026 target about $340M (10-K MD&A). Owner
  cash, OCF less SBC less capex less distributions to noncontrolling interests: 2021 $222.9M, 2022 $926.2M, 2023
  $621.3M, 2024 $163.1M, 2025 −$114.4M; H1 2026 about −$131.5M (OCF 28.6, capex 143.8, SBC 8.6, NCI 7.7; 10-Q).
- *Buybacks and issuance.* 2017 to 2019: 41.5 million shares repurchased for $1,340.3M, about **$32.30** a share (FY2022
  10-K, equity note). 2021 and 2022: about 34.9 million new shares sold at the market for $491.8M, about **$14.09** a share,
  the 2022 tranche "to meet its near-term liquidity requirements, particularly with respect to cash margin" (FY2022 10-K,
  liquidity). 2023: 16.1 million for $347.7M (about $21.60); 2024: 7.7 million for $180.5M (about $23.44); none in 2025;
  $469.6M of the 2023 authorisation unused (FY2025 10-K, Item 5). The programme names no price. The owner-facing record
  is buying at about $32 and selling at about $14; the rows on that pattern: "they sell low and then they buy high"
  **[M1998-027]**, said of option issuers; "what is smart at one price is dumb at another" **[L2011-003]**.
- *Deals.* 2011: Macarthur Coal bought with "$4.1 billion of new debt" (FY2011 10-K), at the met-coal peak, five years
  before the bankruptcy. 2024 to 2025: the Anglo American met-coal purchase ($2.05bn upfront, $725M deferred, up to
  $1.0bn contingent; 8-K `0001193125-24-264712`) was terminated 2025-08-19 under a MAC notice after the Moranbah North
  ignition (8-K `0001064728-25-000122`); $78.9M of costs in 2025; Anglo's arbitration claim quantified on 2026-06-05 at
  about $755.0M (Q2 2026 10-Q, contingencies), about $6.19 a share.
- *Debt and claims at 2026-06-30.* Debt $339.0M (new 0.50% convertible notes due 2031, $250M, conversion price about
  $38.32, capped call to about $50.61; the rest of the 3.25% 2028 notes after $241.2M principal was bought back for
  about $388.8M; 8-K `0001193125-26-252668`). Cash $526.3M. Asset retirement obligations $754.9M (end 2025);
  postretirement obligation $121.1M; legacy cash outflows for retirees, injuries, pensions and reclamation estimated at
  about $110M in 2026 and $1,318M after 2030 (FY2025 10-K, Other Requirements); take-or-pay rail and port about $113M in
  2026 and $540M after 2030; surety bonds $997.2M, letters of credit $112.6M.
- *Stock pay.* SBC $13.8M in 2025 (cash-flow statement). Chief executive's 2025 total $9,025,131, with a STIP paid at
  128.4% of target and a $718,750 bonus in a year of a net loss to common of $52.9M; incentives keyed to Adjusted EBITDA
  (DEF 14A `0001064728-26-000012`, summary compensation table and CD&A). Adjusted EBITDA is the chief operating decision
  maker's "primary financial metric" (10-K MD&A); the rows' view of the figure: "The one figure we regard as utter nonsense
  is the so-called EBITDA" **[M1998-086]**.

**(a) VALUE RANGE, the Q7 CONVENTION as written.** Five-year average owner cash 2021 to 2025, after every real cost and
the minority's cash: **$363.8M** (capex basis; $341.9M on the D&A basis). Shown growth on aggregate owner cash cannot be
computed: the series runs from $222.9M to −$114.4M and changes sign. CONVENTION of this run: the shown-growth end uses
the fourteen-year volume trend, −4.41% a year (mining tons 229.2 million in 2011 to 121.9 million in 2025), because the
cash series gives no rate and the volume series is the business's own record; rationale: it is the only rate the filings
show for the whole span, and it is not above the shown record. Ten years, then zero nominal growth, at 5.66%, plus net
cash of $187.3M (cash $526.3M less debt $339.0M): **$38.83 to $54.27 a share** (width 1.41 to 1). By the convention's
letter the price of $25.50 sits 34% below the bottom of a narrow range. **This is a false screamer, and it is reported
so.** The five-year window holds 2022 and 2023, when seaborne met earned $117.86 and $63.48 a ton; "a base year in which
earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**, and a window that holds the
peak produces a breathtaking level for the same reason.

**(a') WHOLE-CYCLE VARIANT** (asked for by the owner because the window holds the spike). CONVENTION of this run: each
segment's margin per ton averaged over every year the filings give on a like basis (2014, 2015, 2016, 2018 to 2025;
eleven years, covering two busts and one boom), times 2025 volumes: seaborne thermal $20.12 × 15.4 Mt, seaborne met
$24.14 × 8.6 Mt, PRB $2.27 × 84.5 Mt, other US thermal $10.30 × 13.4 Mt = segment EBITDA $848M; less corporate $80M (2024
and 2025 average), capex $375M (between the 2026 target and the 2024 to 2025 average), legacy cash $70M (retiree and
reclamation payments in the cash-flow statement), SBC $14M, minority distributions $28M = **$281M pre-tax**; less
Australian tax at 30% on Australian segment EBITDA after its depreciation, $81M = **$200M after tax**. Rationale: the
averages cover a full cycle; 2017 is left out only because the fresh-start split breaks its per-ton series. Same
construction (ten years, then flat; ends at no growth and at −4.41%): **$22.01 to $30.48 a share**, width 1.41 to 1. The
price of **$25.50 sits inside it.** Two facts the construction does not carry: reserves are 2.0 billion tons, about 16.6
years at the 2025 output (10-K MD&A), so a perpetuity after year ten overstates; a seventeen-year life with nothing after
gives about $19.16 a share. And the Anglo claim ($6.19 a share if lost in full) is not deducted.

**(b) FAIR PRICE.** The floor is the Q7 CONVENTION, about ten percent pre-tax ("a very high probability of at least 10%
pre-tax returns" **[L2002-020]**; "our real expectancy is below 10 percent" **[M2003-149]** is where they quit). Applied to
**equity**, with net cash added back; tax treatment: the $281M whole-cycle owner cash is **before** Australian income
tax, so it is set against the ten percent pre-tax floor directly. Central case: growth at the midpoint of the two ends,
−2.20% a year, so the expected pre-tax return is the yield plus that growth; the floor is met when the pre-tax yield on
equity is 12.2%: $281M / 12.2% = $2,302M, plus net cash $187M, **about $20.42 a share**. If volume were flat for ever
the same test gives about $24.58. At $25.50 the whole-cycle pre-tax yield on the enterprise is 9.62% before any decline,
about 7.4% after the central decline: below the floor.

**(c) CHEAP PRICE.** CONVENTION of this run: half the bottom of the whole-cycle range, **about $11.00 a share**.
Rationale: the margin widens with volatility, "the more volatile the business is [...] the larger the margin of safety"
**[M1997-080]**, and this is the most volatile business read in the run (owner cash from +$1,154M to −$215M within two
years); in the bust years (2015, 2016, 2020) owner cash was negative, so no positive price passes a bust-year test, and
half the bottom is the least invented line that still leaves room for one more bust. It is not a buy signal: the file is
closed at Q2, and "we don’t really try to compensate for that sort of thing by having some extra large margin of safety"
**[M2007-022]**.

---
## THE BOX
**OUT, at Q2.** A price-taking commodity producer whose customers buy on the low bid, low-cost only in the Powder River
Basin where twelve years of margins average about $2.27 a ton and volume has fallen about 43% since 2011, and high-cost in
seaborne metallurgical coal against Warrior in every year compared; equity cancelled in 2017 and near-cancelled in 2020.
Not reached: Q3 to Q12. Computation only, after the close: convention range $38.83 to $54.27 (a false screamer from the
2022 to 2023 spike); whole-cycle range **$22.01 to $30.48** against **$25.50**; fair about $20.42 (equity, ten percent
pre-tax, central decline); cheap about $11.00.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Committed after each: **not done**, by the
      task's instruction not to commit; the file was written in one pass after the reading, which is a departure from
      write-early, declared.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked to be the row's own words); every filing fact has its accession; no number without a filing or a
      CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, and the hunt the other way at Q2).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 material was ignored.
- [x] `python tools/check_framework.py` run 2026-10-06 after the file was written: **PASS** (no commit made, per the task).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a price-taker.** Q1 asks for "a reasonable fix on about what the earning power and competitive
position will look like" **[M2012-065]**; for a commodity producer the competitive position can be fixed and the earning
power cannot, because the price cannot. The framework does not say whether that passes Q1. I passed it narrowly, on the
rows that measure a mine by its cost of production **[M2006-004]**, because otherwise Q2's commodity exception could never
be reached; a second analyst could close TOO HARD (NATURE) at Q1 on the price. The two closes are not passes, but they
mean different things for the alert file. A sentence is needed. (2) **The low-cost exception in a company of several
segments.** Peabody is the low-cost producer in one market and high-cost in another; the rows give the exception for a
business, not for a segment, and do not say whether it holds for the cheapest producer of a product in secular decline
(**[M2004-091]** and **[M2018-043]** both speak of an essential product). I judged it segment by segment and by where the
cash comes from. (3) **The Q7 range convention in a cyclical business.** Its five-year window put the 2022 to 2023 spike
in the base and produced a range whose bottom ($38.83) is 34% above the price: a screamer by the letter, false by the
cycle. The convention has no rule for a window that holds a peak, no rule for a cash series that changes sign (no shown
growth can be computed), and its zero-growth perpetuity after year ten ignores a finite reserve life (about 16.6 years
here) and the terminal reclamation. A whole-cycle base (margins per unit averaged over at least one full price cycle,
times current volume) is what the owner asked for and is what I would propose as a sentence for commodity producers.
(4) **Em dashes.** Operator rule 3 prescribes the heading "COMPUTATION — NOT A CLEARANCE" and the template's headings carry
em dashes, while the standing instruction is no em dashes; the mandated label and the template's headings were kept
verbatim, and the run's own prose has none. (5) **Tools.** `Screens/cover_shares.py BTU` returned the CIK scaled by a
million (1,064,728,000,000 shares) from a cover whose renderer said "shares in Millions"; the cover was read by hand.
`tools/run.py` did not print the promised mine-development alternate (Peabody files one combined capex line) and does
not separate collateral postings inside OCF or distributions to noncontrolling interests, both of which move owner cash
here by tens to hundreds of millions a year.
