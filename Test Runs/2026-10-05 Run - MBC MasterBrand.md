# Company Run — MasterBrand, Inc. (NYSE: MBC) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`. Every judgment cites a v5 ledger id in bold; every filing fact carries its
accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Working folder: `Test Runs/_research 2026-10-05 MBC/` (filings as text, `run_py_output.txt`, `valuation.py`,
`citecheck.py`).

**POSITION NOTE, declared before any verdict:** not checked. The brief's blind rule forbids opening `PORTFOLIO.md`;
whether the operator holds MBC is unknown to this analyst.

**CONTAMINATION DECLARED.** Seen before any verdict, none of it about MasterBrand: the session's git status listed three
untracked 2026-10-05 run files by name (ADNT, EFOR, WEN; not opened); the recent commit subjects named AHCO (OUT at Q2),
ABG (OUT at Q7), WSC (TOO HARD (WORK) at Q2) and CAG (OUT at Q2); a directory listing of `Test Runs/` showed the file
names of older MCFT and EMBC runs (not opened). No MBC file other than this one exists in `Test Runs/` (listing
checked). The commit subjects show that sister runs of today closed at Q2 on competitive evidence; that is a pull toward
the same verdict, and it is named here so the reader can weigh it **[M1997-127]**.

*Session note.* The first session copied the template, fetched the filings and ran the tools, and was stopped by the
session limit before writing; this file was written by the resumed session from the working folder on disk. Nothing was
committed (the brief forbids it), so the write-early commits of the self-audit did not happen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $6.99 (2026-10-05, as printed by `tools/run.py`; aggregator, live quote only, flagged under operator rule 5).
  Filed reference prices: $11.33 close on 2025-08-05, the day before the merger was announced (S-4/A, 0001193125-25-213439,
  "Implied Value of Merger Consideration"); $9.10 at the open on 2026-05-28, the closing date (10-Q, 0001941365-26-000072,
  note 3).
- **Shares by class:** one class, common, **203,490,490** outstanding (10-Q cover for the period ended 2026-06-28, filed
  2026-08-05, accession 0001941365-26-000072; `python Screens/cover_shares.py MBC`). Balance sheet: 209.4M issued, 203.4M
  outstanding. Before the merger: 127.2M (2025-12-28). 75,034,657 shares were issued for American Woodmark (note 3).
- **Market cap:** $1,422M (6.99 × 203.49M). Net debt $1,148.7M (debt $1,390.3M less cash $241.6M, 2026-06-28). EV about
  $2,571M (COMPUTATION).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02 (as
  printed by `tools/run.py` from the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-13, 0001941365-26-000006); 10-K FY2024
  (0001941365-25-000016); 10-K FY2023 (0001941365-24-000021); 10-Q Q2 2026 (0001941365-26-000072); 8-K merger close
  2026-05-28 (0001193125-26-243139); 8-K/A with American Woodmark financials and the pro forma (0001941365-26-000065,
  exhibit `proformafinancialsamerican.htm`); Q2 2026 earnings release (8-K 0001941365-26-000070, ex. 99.1); 8-K
  2026-09-24, resignation of the Chief Digital and Technology Officer (0001941365-26-000079); S-4/A (0001193125-25-213439);
  DEF 14A 2026 (0001193125-26-170568, fetched, not read: the file closed at Q2). Fortune Brands Home & Security: Form 10
  information statement 2011 (ex. 99.1 of 0001193125-11-234225) and 10-Ks FY2011 (0001193125-12-072886), FY2014
  (0001193125-15-062500), FY2017 (0001193125-18-063999), FY2020 (0001564590-21-008129), FY2021 (0000950170-22-002294).
  Competitors as listed at Q2.
- **One figure cross-checked against the filed statement:** FY2025 operating cash flow $195.7M, stock pay $16.1M and capex
  $78.2M printed by `tools/run.py` match the filed cash-flow statement (10-K FY2025, 0001941365-26-000006) line for line.
- `python tools/run.py MBC`, arithmetic lines only (Part VII): owner cash, capex basis, 2023 $330.5M, 2024 $189.2M, 2025
  $101.4M (OCF 405.6 / 292.0 / 195.7; SBC 17.8 / 21.9 / 16.1; capex 57.3 / 80.9 / 78.2; D&A 64.3 / 77.3 / 93.5). Five-year
  window (2021 to 2025) mean $175.4M capex basis, $167.9M D&A basis. The tool's yield and "growth the price assumes" lines
  are on the pre-merger cash and the post-merger share count, so they mix two companies and are not used.

### The balance sheets first (read here because the file closes before Q4) **[M2025-032]**
Year-ends, $M (2022 to 2025 from the 10-Ks; 2026-06 from the 10-Q; 2020 and 2021 are carve-out equity only):

| | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06 |
|---|---|---|---|---|---|---|
| Equity | 2,454 | 1,009 | 1,194 | 1,295 | 1,345 | 1,969 |
| Goodwill | 926 | 924 | 925 | 1,126 | 1,128 | 1,318.5 |
| Other intangibles | n/a | 350 | 336 | 571 | 548 | 888.6 |
| Debt | 0 third-party | 979 | 708 | 1,008 | 974.5 | 1,390.3 |
| Cash | 141 | 101 | 149 | 121 | 183 | 241.6 |
| Receivables | n/a | 290 | 203 | 191 | 150 | 247.2 |
| Inventory | n/a | 373 | 250 | 276 | 269 | 435.6 |
| Retained earnings | n/a | 1,022 | 1,204 | 1,330 | 1,357 | 1,284.1 |

What the figures say: (1) the spin put $985M of debt on the business to pay a $940M dividend to Fortune Brands (10-K
FY2023, cash-flow statement and liquidity section), so equity fell from $2,454M to $1,009M with no change in the
business; (2) every later rise in goodwill and intangibles is a purchase: Supreme in 2024 ($514.5M cash, funded on the
revolver and new notes) and American Woodmark in 2026 ($1,059.8M of consideration, $192.8M of it goodwill, $356.0M
intangibles; 10-Q note 3); (3) tangible equity is negative at every year-end shown from 2022 (2025: 1,345 − 1,128 − 548 =
−331; 2026-06: 1,969 − 1,318.5 − 888.6 = −238), so the equity is the price paid for acquisitions, not plant; (4) debt has
gone from zero third-party to $1,390M in under four years, and the term loan of $375M was drawn only to retire American
Woodmark's debt; (5) receivables fell from $290M to $150M on flat sales, which the FY2023 10-K credits to collections,
but the FY2025 cash-flow statement shows a bad-debt provision of $17.8M against $0.4M and $1.9M in the two years before:
a customer went bad or credit loosened, and the 10-K text read does not say which; (6) retained earnings fell $73M in the
first half of 2026 on the loss. What they do not say: whether the goodwill is worth its carrying amount. The 10-Q says the
market value was "at times, was below the carrying value of its net assets" and no interim impairment test was run
(note 7).

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is what cabinets will earn over a housing cycle, not where a stock that fell from
$11.33 to $6.99 in fourteen months will trade. The habit that bears hardest is looking for "what’s wrong in things"
**[M2025-013]** and writing contrary evidence down as it is found **[M1997-127]**. Primary documents came first and the
competitors' filings last, as the scuttlebutt row orders it **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the filer's own risk factor, "The cabinet industry is
highly competitive with relatively low barriers to entry and market share losses could occur" (10-K FY2025, Item 1A);
(b) Lowe's 20% and Home Depot 13% of FY2025 sales, ten largest customers about 50%; (c) legacy unit volume down in 2025
($156.5M) and again in the first half of 2026 ($90.0M); (d) legacy gross margin 32.8% to 27.4% in Q2 2026 (earnings
release); (e) an all-stock merger closed at $9.10 a share, below the $11.33 at announcement; (f) negative tangible equity
and $1.39B of debt; (g) the record of Masco's and American Woodmark's cabinet businesses through 2008 to 2015. On the
other side, and written down with the same weight: through the bust Fortune Brands' cabinet segment lost less than either
rival (Q2), which is some evidence of a relative cost position.

## THE STANDING RULE
Owning this exposes the buyer to ruin only through the buyer's own borrowing or sizing; the target's leverage is Q9's
(not reached). Any position would be bought with no borrowed money and sized so that a total loss is survivable, "Never
risk permanent loss of capital." **[L2023-005]**; **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? STOP.
- Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or
  10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- The business: a maker of wood kitchen and bath cabinets in three tiers (stock, semi-custom, premium), sold through over
  7,900 dealers, the home centers and builders, from 26 plants in the US, Mexico and Canada (10-K FY2025, Items 1 and 2).
  The product changes with fashion, not technology. The key variables **[M1998-044]** are housing activity (new
  single-family starts and repair-and-remodel spending), unit share, price against wood, labor and freight costs, tariffs,
  and the terms the two home centers set. Housing activity cannot be timed, but its range over a cycle can be read from
  the record: the Fortune Brands information statement records US home prices down about 30% and remodeling down about
  15% from 2006 to 2009, and its own sales down 36%.
- What I can see ten years out: a cyclical, labor-heavy manufacturer in a fragmented field, earning low-to-high single-digit
  operating margins over a cycle with losses at the trough (Q2 table). That is a forecast of earning power and competitive
  position, which is what the row asks; it is not a forecast of the timing. No doubt that it sits inside the circle
  **[M2002-092]**: the product is plain, the change is slow, the filings state the economics.
- **VERDICT: IN** **[M1995-051]**, **[M2012-065]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**

**The competitor row** (operating income ÷ net sales, from each company's own filings; Fortune's figure is the segment's,
before corporate expense; Masco's is the "Cabinets and Related Products" segment; American Woodmark's is the company's,
fiscal years ending 30 April, FY2006 to FY2009 pre-tax as printed in its five-year table):

| Year | Fortune / MasterBrand cabinets | Masco cabinets | American Woodmark |
|---|---|---|---|
| 2004 | n/a | 16.9% (519 / 3,065) | n/a |
| 2005 | n/a | 15.5% (515 / 3,324) | n/a |
| 2006 | n/a (consolidated only) | 3.7% after a $316M goodwill charge; 13.3% before | 6.4% pre-tax (sales 837.7) |
| 2007 | n/a | 11.9% (336 / 2,829) | 6.7% pre-tax (760.9) |
| 2008 | 7.4% (114.3 / 1,552.2) | 0.2% (4 / 2,276) | 0.9% pre-tax (602.4) |
| 2009 | −2.2% (−25.1 / 1,125.7) | −3.8% | −1.1% pre-tax (545.9) |
| 2010 | 2.4% | −17.1% | −9.2% (406.5) |
| 2011 | 0.5% | −16.7% | −6.9% |
| 2012 | 1.5% | −10.1% | −6.5% |
| 2013 | 5.9% | −1.0% | 2.7% |
| 2014 | 7.7% | −6.2% | 4.7% |
| 2015 | 8.9% | 5.0% | 6.6% |
| 2016 | 10.8% | n/a | 9.8% |
| 2017 | 10.8% | n/a | 10.5% |
| 2018 | 5.9% | n/a | 8.6% |
| 2019 | 7.5% | n/a | 8.6% |
| 2020 | 9.5% | n/a | 7.9% |
| 2021 | 9.8% (279.3 / 2,855.0) | n/a | 6.6% |
| 2022 | 6.2% (MBC standalone, after a $46.4M tradename impairment) | n/a | 1.9% |
| 2023 | 11.2% (306.3 / 2,726.2) | n/a | 6.6% |
| 2024 | 8.7% (235.7 / 2,700.4) | n/a | 8.7% |
| 2025 | 4.4% (119.0 / 2,734.7) | n/a | 8.2% (FY to April 2025); CY2025 pro forma 83.1 / 1,595.7 = 5.2% |
| 1H 2026 | −3.2% (−46.3 / 1,433.2) | n/a | merged |

Sources: Fortune Brands information statement 2011 (2008 to 2010); FBHS 10-Ks FY2011, FY2014, FY2017, FY2020, FY2021;
MBC 10-Ks FY2023 and FY2025, 10-Q Q2 2026; Masco 10-Ks FY2006 (0000950124-07-001157), FY2009 (0000950123-10-013437),
FY2012 (0001193125-13-062852), FY2015 (0001047469-16-010135); American Woodmark 2010 annual report (ex. 13 of
0001193125-10-151335) and XBRL facts from its 10-Ks FY2012 to FY2025 (accessions listed in
`_research 2026-10-05 MBC/amwd_facts.json`), 10-K FY2025 (0000794619-25-000061); pro forma (0001941365-26-000065). Masco's
segment after 2015 was not read. Fortune's cabinet segment for 2006 and 2007: no instance found in the information
statement, which gives segment data from 2008 and the consolidated 2006 figure only.

Over the whole span the three businesses earned single-digit margins at best outside 2004 to 2007, lost money or came
near it in 2009 to 2012, and the leader's margin has been at parity with American Woodmark's since 2016, not above it.

**The tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**: the answer is yes, and the filer gives it. "The cabinet industry is highly
   competitive with relatively low barriers to entry" and "there are few barriers to entry in the U.S. and Canadian
   cabinet markets and new competitors may enter these markets at any time" (10-K FY2025, Item 1A). American Woodmark:
   "a highly fragmented industry that is composed of several thousand local, regional, and national manufacturers" (10-K
   FY2025, Item 1). Masco in 2016: "Additional local and regional competitors may enter this industry as conditions
   improve." (10-K FY2016). This is the industry the row names: "there are some industries that are just never going to
   have barriers to entry." **[M2012-106]**
2. **Pricing power and the agony before a rise** **[M2005-020]**: "we face significant price competition from our
   competitors, which tends to intensify during economic downturns [...] This price competition impacts our ability to
   implement price increases or, in some cases [...] maintain prices" (10-K FY2025, Item 1A). The price realized in 2025
   was tariff pass-through ("favorable ASP from tariff pricing flow-through", Q2 2026 release), and gross margin still fell
   from 33.1% (2023) to 30.3% (2025) to 25.3% (1H 2026, 362.1 / 1,433.2).
3. **Unit volume** **[M1999-108]**: legacy volume fell $156.5M in 2025 and $90.0M in the first half of 2026; sales to
   retailers fell 5.3% in 2025. Some of this is the market (the company guides its market "down mid-single digits" for
   2026), and the filings do not give share, so whether the castle lost share cannot be read; that it lost volume and
   margin together can.
4. **The low-cost position, the one exception for a commodity field** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**:
   the filer claims "an advantaged cost structure" from "volume leadership" (Item 1). The record: in the bust Fortune's
   segment lost far less than Masco's or American Woodmark's (2010 to 2012 above), which is real evidence of a relative
   position, written down as contrary to the verdict. But the advantage the rows ask for is "costs [...] on parity or
   less" against the major competitors, held over time **[M2001-013]**, and the margins since 2016 are at parity with the
   number two, not ahead; MasterBrand's 2025 margin (4.4%) is below American Woodmark's (8.2%, and 5.2% on the 2025
   calendar pro forma); and its own MD&A says "realized savings from various cost reduction actions were more than offset
   by higher manufacturing costs" (10-K FY2025 and 10-Q Q2 2026). The filer also names cheaper producers abroad:
   "competitors who operate in countries that have lower labor and compliance costs" (Item 1A). The leader is not the
   low-cost producer the exception requires; at best it is at parity.
5. **The brand in the customer's mind, and the retailer** **[M2001-090]**, **[M2015-038]**: the brands (Aristokraft,
   Diamond, KraftMaid is Masco's, etc.) are trade brands; the buyer in the home center chooses on price among similar
   boxes, and the filer says so: "price is a significant factor for consumers as well as our trade customers" (Item 1A).
   Lowe's and Home Depot took 33% of FY2025 sales, and the filer warns their size "may further limit our ability to
   maintain or raise prices in the future"; American Woodmark's share with the same two was 40.8% (FY2025). Combined, on
   the 2025 figures, the two retailers buy roughly 36% of the merged company's sales (COMPUTATION: 0.33 × 2,734.7 + 0.408
   × 1,595.7 ≈ 1,553 of 4,330).
6. **Would the customer still choose it over the low bid?** **[M2017-009]**: the filer's raw-material risk factor reads
   "Because our component products have few distinguishing properties from producer to producer, competition for these
   products is based primarily on price, which is determined by supply relative to demand" (10-K FY2025, Item 1A). The
   commodity marks are the rows': "most insureds don't care from whom they buy" **[L2004-003]**; the improvement one maker
   gets, "your competitor gets the next day" **[M2004-053]**.
7. **Labor content and imports** **[M2007-116]**: 81% of the 12,633 associates are hourly production and distribution
   (Item 1); American Woodmark calls its process "labor-intensive" and its Mexican plants "a low cost alternative to Asian
   manufacturers". The product can be shipped in: the 25% Section 232 tariff on cabinets and vanities from 2025-10-14
   exists because it is (10-Q Q2 2026). Part of what now keeps the castle standing is a tariff, which a government can
   raise or lower; the IEEPA tariffs were struck down in February 2026. That protection is not the business's.
8. **Ask the competitors** **[M1999-130]**: on the public record the competitors answered by their conduct: American
   Woodmark sold itself to MasterBrand for stock; Masco reported six straight years of cabinet losses, 2009 to 2014,
   after a profit of $4M on $2,276M in 2008, and in 2016 deliberately exited "certain lower margin business in the
   direct-to-builder channel" (10-K FY2017). No instance found in the filings read of a competitor that would buy
   MasterBrand's position rather than its own.
9. **Widening or narrowing** **[M2000-075]**, **[L2005-010]**: narrowing on the evidence of 2025 and 2026: volume down,
   gross margin down 540 basis points in the legacy business in Q2 2026, an operating loss in the half, a $17.8M bad-debt
   charge, $30M of announced cost cuts plus a "transformative" merger whose stated aim is cost. A moat kept by cutting
   cost each year to stay level is the one the rows describe as rebuilt, not widened **[L2007-005]**.
10. **What could destroy or reduce it** **[M2000-014]**: a housing bust (2009 to 2012, above), a home center moving volume
    to another vendor ("one or more retailers may stop carrying certain of our products", Item 1A), a change in tariff
    policy reopening imports, and the debt (Q9, not reached).

**Reading.** The castle questions ask what keeps the high return in, and the filer's answer is that nothing does: low
barriers, price competition, price-driven buyers, two customers with a third of sales, and a cost position at parity at
best. "In an unregulated commodity business, a company must lower its costs to competitive levels or face extinction."
**[L1994-035]**; "whatever he charged for gas was my price." **[M2012-109]**. The one argument for a castle, a relative
advantage in the bust, is recorded above and does not survive the decade after it, in which the margin settled at the
level of the number two and has fallen below it in 2025. This is a castle shown open on the evidence, so the box is OUT,
not TOO HARD **[M2011-015]**, **[M2006-013]**; a lower price does not reopen it: "What you can’t do is turn any investment
into a good deal by paying little" **[M2019-015]**; **[L2014-009]**.

- **VERDICT: OUT** at Q2 **[M2011-015]**, **[M2012-106]**, **[L2004-003]**, **[M1997-010]**.

---
## Q3 — NOT REACHED. (For the record only, not a clearance: on tangible capital the business earns well at mid-cycle,
since the tangible capital is small; on the capital owners have actually paid, about $2.2B of goodwill and intangibles
plus $1.39B of debt, the 2025 operating income of $119M is about 3% to 4%.)
## Q4 — NOT REACHED as a verdict. The balance-sheet reading is in Step 0. Noted, not weighed: the Q2 2026 release leads
with "Adjusted EBITDA" and states leverage as "net debt to adjusted EBITDA" of 3.9x, which is the figure the rows call
"utter nonsense" **[M1998-086]**; the covenant definition adds back stock pay (release text), against **[L2015-003]**.
## Q5 — NOT REACHED.
## Q6 — NOT REACHED. Noted for the record: the American Woodmark merger was paid wholly in MasterBrand stock issued at
$9.10, against a COMPUTATION below that puts MasterBrand's own value at about $9.69 (whole-cycle) to $22.48 (five-year
convention) a share before the merger; if either figure is right, it is the deal the rows call "impossible" to make
sensibly **[L2009-019]**, softened only if American Woodmark's shares were as undervalued as MasterBrand's (its holders
received 37% of the shares for about 37% of the combined 2025 sales).
## Q7 — NOT REACHED. Reporting at the owner's request follows, all of it COMPUTATION.
## Q8, Q9, Q10, Q12 — NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE (reporting at the owner's request; the file closed OUT at Q2)
Arithmetic in `_research 2026-10-05 MBC/valuation.py`; rate 5.63% (the 30-year Treasury) **[L2000-021]**, **[M1996-025]**.

**Inputs.** The company now is MasterBrand plus American Woodmark on 203.49M shares, so owner cash is taken for both:
OCF − stock pay − all capex, five years, MasterBrand calendar 2021 to 2025 and American Woodmark fiscal years to April 2021
to April 2025 (CONVENTION of this run: the nearest filed years, paired by year; American Woodmark's calendar 2025, weaker,
is not in a filed cash-flow statement). Because MasterBrand had no outside debt before December 2022 and both companies'
debt was replaced at the merger, each year is put on a debt-free basis by adding back net interest after a 24% tax
(CONVENTION of this run: the 2023 effective rate was 23.8%), and the equity value is the enterprise value less net debt of
$1,148.7M at 2026-06-28. Combined debt-free owner cash, $M: 2021 212.9; 2022 144.0; 2023 541.0 (MasterBrand released about
$162M of working capital that year); 2024 380.8; 2025 226.2. Mean $301.0M; growth between the end years 1.5% a year, on the
aggregate.

**(a) VALUE RANGE, the Q7 convention** (five-year mean, ten years at the growth shown then zero, at 5.63%): **$20.63
(no growth) to $24.03 (shown growth) a share.** The five-year window holds abnormal years: 2021 and 2022 are the pandemic
housing boom and pre-spin carve-out cash with no interest, 2023 is a working-capital release, and none of it includes a
housing bust **[L2005-003]**. So the whole-cycle variant governs the reporting:
**Whole-cycle variant:** Fortune's cabinet segment margin averaged 6.2% over 2008 to 2021 (bust and boom); less 1.6% of
sales of standalone corporate cost (2021: segment 279.3 against carve-out 234.3), after 24% tax, plus amortization of
about 0.7% of sales, on the 2025 pro forma combined sales of $4,330.4M: debt-free owner cash about $180.5M. **Range $10.11
(no growth) to $12.15 (shown growth) a share.** CONVENTION of this run: the whole-cycle margin and the sales base are mine,
chosen because they are the only span in the filings that includes a bust; the pro forma sales base is itself a weak year.
Run-rate today is below both: pro forma 2025 operating income $153.9M (3.6%), first-half 2026 an operating loss, and
guidance for the second half of adjusted EBITDA $129M to $149M.

**(b) FAIR PRICE** (the price at which the central case clears the ~10% pre-tax floor **[M2003-149]**, **[L2002-020]**):
central case is the whole-cycle owner cash, no growth, less after-tax interest on the pro forma $91.1M of interest: $111.2M
to equity after tax, grossed up at 24% to $146.3M pre-tax. Tax treatment: owner cash is after corporate tax; the floor is
stated pre-tax, so the equity cash is divided by 0.76. **Fair price about $7.19.** On the five-year convention cash instead,
about $14.98.

**(c) CHEAP PRICE:** rule of this run (CONVENTION): half the fair price, a 20% expected pre-tax return, because the margin
must widen with the volatility of the business **[M1997-080]** and leverage doubles that volatility for the equity; the
picture is buying "at 35 billion" what is worth near 100 **[M2008-068]**. **Cheap price about $3.60.**

**Against the price of $6.99:** below the whole-cycle range ($10.11 to $12.15) by about a third, just under the fair price
of $7.19, well above the cheap price. It would need a pencil: "if you have to actually do it on — with pencil and paper,
it’s too close to think about." **[M1996-084]**; **[M2009-005]**. None of this reopens Q2 **[M2019-015]**.

---
## THE BOX
**OUT**, decided at **Q2**: the filer itself says the cabinet industry has "relatively low barriers to entry" and that its
products compete "primarily on price"; two retailers buy a third of sales; the leader's margin over 2016 to 2025 is at
parity with, and in 2025 below, the number two; Masco and American Woodmark lost money for years in the last bust; legacy
volume and gross margin are falling. Q1 IN. Not reached: Q3 to Q12. Value (COMPUTATION): whole-cycle $10.11 to $12.15,
five-year convention $20.63 to $24.03, fair about $7.19, cheap about $3.60, against $6.99.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: **yes**. Written question by question and committed after each: **no**.
      The first session was stopped before writing; this file was written at once by the resumed session; the brief
      forbids commits.
- [x] Every v5 id resolves (checked by `_research 2026-10-05 MBC/citecheck.py`); every filing fact has its accession; no
      number without a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; everything after it is NOT REACHED or headed COMPUTATION.
- [x] Owner cash after every real cost (OCF − stock pay − all capex), never a net-income proxy; sovereign from the
      Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations; Q2 test 4).
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield line was rejected (pre-merger cash on post-merger
      shares).
- [x] `python tools/check_framework.py` PASS (run after writing; result recorded in the reply to the coordinator).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The Q7 convention's five-year average has no rule for a company that has just merged: the cash history
belongs to two companies with different fiscal years, one of which had no outside debt for two of the five years. I
combined them, unlevered both and subtracted today's net debt, and confessed each step; another analyst could
reasonably value the old MasterBrand alone, and the two answers differ. (2) The convention says the range is built on the
five-year average "so that no single year sets the base", but in a cyclical business a five-year window that misses a
bust sets the whole base; the framework gives no rule for when a whole-cycle variant replaces the convention (the brief
asked for one; the framework does not), and here the two differ by a factor of two. (3) Q2's commodity exception asks
whether the business is "the low-cost producer", but the evidence is often relative and time-varying (best of three in
the 2009 to 2012 bust, at parity after 2016, below in 2025); the rows give no rule for which span decides. I let the
latest decade decide, as the ten-year horizon of understanding suggests, and recorded the bust evidence as contrary.
