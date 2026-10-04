# Company Run — e.l.f. Beauty, Inc. (ELF) — 2026-09-11
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**WRITE-EARLY NOTE.** This file was created as the first action of a resumed session
(22:25 ET, 2026-09-11) after the prior session was killed at the limit before anything was
on disk. Each section is appended as it closes and committed by name.

**POSITION NOTE, declared before any verdict:** no ELF position is held (checked against
`PORTFOLIO.md`). Fresh entry run: Q1→Q5 in hard sequence, stop at the first non-IN.

**BIAS DECLARATION [operator protocol rule 9; E4-27, E4-26, E3-41].** The brief's priors are
framed to be refuted and are listed here so they can be scored at the end: (1) growth is
units, not price; (2) the tariff-year price increase is the pass-through instrument and my
prior on Q2 is open; (3) the perimeter flag understates the acquisitions; (4) the adjusted
EBITDA culture fires [E4-29] in the releases even if the 10-K reads clean. The pull toward
a Q2 OUT by habit (most consumer names in this queue closed there) is named as a bias, and
so is the pull toward finding a franchise in a name that has compounded revenue at this rate.

---
## THE SCREEN ROW THAT PROMPTED THIS RUN — a prompt to read, never a score (operator rule 8)

```
cap_m 6179 | oe_bottom_m 18 | oe_top_m 56 | spread 2.037 ($18M to $56M)
yield_bottom 0.30% | vs_sovereign -5.07 pts | growth_required 9.70%
level_shift 3.17 "STEP UP - normalize down [E4-41]"     level_shift_oe n/a "EARLY HALF STRADDLES ZERO (-$8.6M)"
flags_disagree: FIRES        window_disagree: FIRES (12 years filed; full series refuses)
best_year_dep 0.226 "ONE YEAR CARRIES THE WINDOW"    best_year_dep_oe 0.291
acq_note: acquisitions are $857M, 14% of cap, inside the window
newest_filing 2026-03-31 (fiscal year ends March)    newest_periodic 2026-07-30
```

Every number above is re-derived below from the filed statements. Where the re-derivation
disagrees with the row, the filing governs (operator rule 4).
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.37 %** · date **2026-09-10** · source **US Treasury daily par yield curve, 30-year
  (the issuing authority; struck fresh this session via `tools/sources.py`, not inherited from
  the brief and not the FRED fallback)**
- FX: **none for the quote.** e.l.f. is a Delaware corporation reporting in USD; **79% of
  FY2026 net sales were in the United States** ($1,292.4M of $1,636.5M), the rest primarily the
  UK, Canada and Germany. The cost side is Chinese renminbi — the 10-K says a 10% adverse RMB
  move would cost *"approximately $51.0 million"* of cost of sales — and the company *"do[es]
  not have an active hedging program."* Recorded at Q4 as an exposure, not handled by swapping
  the sovereign.

**THE COVER COUNT, BY HAND.** `python Screens/cover_shares.py ELF`:
```
ELF  e.l.f. Beauty, Inc.
   10-Q filed 2026-08-06, period 2026-06-30, accession 0001600033-26-000040
   Common Stock, par value $0.01 per share              59,007,996
```
- **One class.** The tool's refusal to sum classes does not bite. Cross-check inside the same
  filing: the balance sheet reads *"58,936,996, 59,089,708 and 56,734,903 shares issued and
  outstanding as of June 30, 2026, March 31, 2026 and June 30, 2025"* — cover (59,007,996 at
  2026-07-30) against balance sheet (58,936,996 at 2026-06-30) differ by 71,000 shares in a
  month, ordinary RSU vesting. **Both agree.** The proxy's 58,937,041 at 2026-06-26 agrees too.
- **The count went UP 3.36M shares in FY2026 while $50M was spent buying back** — 2,582,371
  shares issued for rhode plus 1,403,349 from vesting and exercises, less 626,049 repurchased.
  Held at Q3 [E5-08, E5-15].

- **price $96.91 · 2026-09-11 close · aggregator, FLAGGED, live quote only** (operator rule 5)
- **shares 59,007,996** (10-Q cover, 2026-07-30)
- **MARKET CAP = $96.91 × 59,007,996 = $5,718M.** *(The screen row's $6,179M implies a quote
  near $104.7; the price has moved 7% since the row was struck. This run uses $5,718M.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2026 10-K, FYE 2026-03-31, filed 2026-05-21, accession
  `0001600033-26-000020`** (`elf-20260331.htm`). Read: Item 1, Item 1A (tariff, China,
  acquisition, customer risk factors), Item 7 in full, the four statements, Notes 2, 3, 4, 7,
  8, 9, 17 and 18.
- Also read: **Q1 FY2027 10-Q** (period 2026-06-30, filed 2026-08-06, `0001600033-26-000040`);
  10-Qs for 2025-12-31 (`0001600033-26-000007`), 2025-09-30 (`0001600033-25-000058`),
  2025-06-30 (`0001600033-25-000040`), 2024-12-31 (`0001600033-25-000006`), 2024-09-30
  (`0001600033-24-000050`), 2024-06-30 (`0001600033-24-000043`); FY2025 10-K
  `0001600033-25-000016`; FY2024 10-K `0001600033-24-000020`; FY2023 10-K
  `0001600033-23-000016`; FY2022 10-K `0001600033-22-000027`; **DEF 14A** filed 2026-07-08
  `0001600033-26-000030`; **8-K/A of 2025-10-17 `0001600033-25-000048`** (rhode's audited
  FY2024 and reviewed H1-2025 financials, Exhibits 99.1 and 99.2, and the Article 11 pro forma,
  Exhibit 99.3); the rhode announcement 8-K of 2025-05-28 `0001600033-25-000013`; the Naturium
  announcement 8-K of 2023-08-29 `0001193125-23-222959`; and **every quarterly earnings
  release (8-K Exhibit 99.1) from 2022-05-25 through 2026-08-05**, thirteen releases, for the
  guidance record and [E4-29].
- **Figure cross-checked against the filed statement.** XBRL returns FY2026 operating cash
  flow of $212.5M; the filed Consolidated statements of cash flows shows **"Net cash provided
  by operating activities 212,511"** — agrees. Second, because the (c) judgment turns on it:
  XBRL D&A $79.4M against the filed line **"Depreciation and amortization 79,361"** — agrees;
  filed capex **"Purchase of property and equipment (22,449)"** — agrees; filed
  **"Stock-based compensation expense 86,919"** — agrees (the equity statement carries 86,907;
  the $12k gap is rounding between two statements and is recorded, not smoothed).

---
## THE SCREEN ROW — REPRODUCED, AND WHERE IT IS BLIND

`python tools/run.py ELF`, today's facts: 3-year (FY2024–26) OE **20 to 56**; 5-year **16 to
47**; yield 0.34% to 0.98%; growth-the-price-assumes 55.2%. The published row (18 to 56,
spread 2.037) reproduces to within the price move. **Both ends are real ends this time** —
the tool's `OE lo` is (OCF − SBC − D&A) and `OE hi` is (OCF − SBC − capex) — so the row is a
capex band on the 3-year window and the 5-year is the second window. What the row cannot
see, rebuilt below: **(a)** the D&A series it subtracts has a presentation break (the FY2025
vintage moved *"Non-cash lease expense"* out of the D&A line: FY2024 D&A is 35,913 in the
FY2024 10-K and 30,167 in the FY2025 10-K, the 5,746 difference being exactly the new lease
line — the CERT class of defect, same tag, changed content); **(b)** `acq_note` reads the
investing line only, and the true perimeter is 44% larger (next section); **(c)** the
operating-cash numerator already carries $57.6M of acquisition consideration paid as
"seller expenses" across two years, and a $57.6M non-cash earnout charge added back; **(d)**
$35.0M a year of amortisation of **retail product displays** and a further slice of cloud
software sit inside the D&A line while the cash for both is spent through *operating*
working capital, so the D&A end of the band double-counts them (Q4).

---
## THE PERIMETER — REBUILT FROM THE BUSINESS-COMBINATION NOTES (Note 3, FY2026 10-K)

**The brief's prior — that the investing-cash flag understates the perimeter — is CONFIRMED,
for the sixth consecutive time, and this filer adds a third place for consideration to hide.**

| | **Naturium** (closed 2023-10-04, FY2024) | **rhode** (closed 2025-08-05, FY2026) |
|---|---|---|
| Announced | *"$355 million in a combination of cash and stock"* incl. *"approximately $70 million, or approximately 600,000 shares"* | *"$1 Billion Deal"*: $800M at close ($600M cash + $200M stock, *"approximately 2.6 million shares"*) + *"potential earnout consideration of $200 million"* |
| **Cash consideration** (Note 3) | **$275,266k** | **$590,149k** |
| **Stock consideration** (Note 3) | **$57,772k** = 577,659 sh at $100.01 opening price | **$300,278k** = 2,582,371 sh at $116.28 opening price |
| **Contingent consideration, initial FV** | none | **$7,100k** (three annual earnout targets to Sep-2028, **max $200.0M cash**) |
| **Total consideration** (Note 3) | **$333,038k** | **$897,527k** |
| **Seller expenses assumed and PAID BY E.L.F. THROUGH OPERATING CASH FLOW** | **$10,549k** (*"Acquisition-related seller expenses (10,549)"*, FY2024 cash-flow statement) | **$47,100k** (same line, FY2026) |
| **Cash in the INVESTING section** (what the flag reads) | $274,973k | $581,682k |
| Goodwill / identified intangibles | $168,962k / $162,100k (trademarks $124.5M, 15 yrs; retailer relationships $20.0M, 10 yrs; e-commerce relationships $17.6M, **3 yrs**) | $512,893k / $380,900k (trademarks $276.3M, 15 yrs; retailer relationships $104.6M, 12 yrs) |
| Target's own last-year numbers | ~$90M net sales, ~$17M adjusted EBITDA (company's forecast, 12 months to 2024-03-31) → **3.7x sales, ~21x adjusted EBITDA** by the company's own arithmetic | CY2024 audited (Ex. 99.1): **net sales $169.0M, gross profit $101.0M (59.8%), operating income $29.7M, net income $29.9M** (an LLC, no tax); H1-2025 reviewed: sales $102.8M, operating income $35.3M; LTM to 2025-03-31 $212.2M → **3.8x LTM sales at close**, 4.2x incl. the earnout at initial FV, **5.2x if the earnout pays in full** |

**The earnout, and it is the CERT round trip at four times the size.** Initial fair value
$7.1M. At 2026-03-31, *"remeasured to $64.7 million, driven by the outperformance of rhode's
revenue results … and a revised upward forecast"* — a **$57,649k charge** to operating income
(*"Change in fair value of contingent consideration"*), **added back inside operating cash
flow** as a non-cash item. At 2026-06-30, remeasured again to **$80.8M**, a further **$16.1M**
charge, again added back. **$73.7M of the eventual payment has already been expensed and
already been added back; not one dollar of it has yet left through operating cash flow, and
when it leaves it will leave through financing** — the 10-Q says payments fall *"within 45
days after each measurement period ending September 30, 2026, 2027, and 2028"*, with
$28.2M classified current. **The owner-earnings numerator this project builds on operating
cash flow therefore carries a $57.6M seller-expense DEBIT that is really purchase price, and
will never see up to $200M of earnout CREDIT it should.** The two run in opposite directions
and are treated separately at Q4.

**The perimeter in one line:** the screen's `acq_note` says **$857M**. Total consideration
per Note 3 is **$1,230.6M**; add the **$57.6M** of seller expenses paid through OCF and the
**$73.7M** of earnout accretion booked to date, and the amount e.l.f. has committed to the
two deals is **$1,361.9M, 23.8% of today's market cap** — rising to **$1,488M (26.0%)** if
the earnout pays at its $200M maximum, which two consecutive upward remeasurements make the
direction of travel. **The investing line understated the perimeter by 44% before the
earnout and by 74% at the maximum.**

**Which years describe the business that exists now [E4-41].** With a March year-end the
window straddles both closes: FY2024 carries **six months** of Naturium; FY2025 is the first
full Naturium year and the last clean e.l.f.-plus-Naturium year; **FY2026 carries eight
months of rhode** (Aug 5 to Mar 31: *"$293.5 million of net sales and $112.8 million of net
income"*; by quarter $52.4M, $128.2M, $112.9M); Q1 FY2027 is the first quarter of the
combined company on both sides. **No fiscal year in the filed history describes the company
that exists today**, and the 10-K's own pro forma (rhode from 2024-04-01) is the nearest
thing: **FY2025 $1,525.7M / net income $114.8M; FY2026 $1,734.4M / net income $30.1M.** The
Q4 owner-earnings grid carries both the filed series and a combined-perimeter reading.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

e.l.f. designs a lipstick, a primer or a serum, has a contract factory in China make it, ships
it to a third-party warehouse in California, and sells it to Target, Walmart, Amazon or
Sephora, who put it on the shelf at about **$7** — against about $10 for the other mass
brands and $30 for prestige (the 10-K, citing Nielsen). It owns no plant, no store and no
warehouse: **849 employees** for $1.64bn of sales. The factory invoice, freight, customs and
duties are the cost of sales, and they come to **29 cents of every net-sales dollar** (gross
margin 70.7%), which is a prestige-brand gross margin on a drug-store price point, because
the thing being sold is a formula plus a name plus a shelf position, not a manufactured
good. The other 71 cents is then spent: **37 cents on marketing, merchandising and
distribution** ($604.9M, the filed segment line), **14 cents on people** ($231.1M), and 15
cents on everything else including amortisation of the acquired brands and, this year, the
earnout charge. What reaches the operating line was **15 cents in FY2024, 12 in FY2025 and 4.5
in FY2026** (8.0 before the earnout remeasurement).

Two acquired brands sit beside the namesake now: **Naturium** (skin care, ~$18 price point,
bought 2023) and **rhode** (Hailey Bieber's skin care, ~$30 price point, direct-to-consumer
plus Sephora, bought 2025). rhode is a different animal from e.l.f. Cosmetics — its own
audited FY2024 shows a 60% gross margin *before* e.l.f. reclassifies fulfilment out of cost of
sales (81% after), sold at prestige prices online — and it is now about a quarter of the
company by revenue.

**How the money is actually made — the filed price/volume split, every vintage [E2-63,
E4-55].** The brief asked whether growth is units or price, and said a consumer company
either files the answer or it does not. **e.l.f. files it, every year and every quarter, in
dollars-of-effect**, and the series turns over inside the window:

| period | net sales growth | **from unit volume** | from price and mix | source |
|---|---|---|---|---|
| FY2021 | +$35.3M (+12%) | *"volume remained flat"* | *"substantially drove"* it | FY2022 10-K |
| FY2022 | +$74.0M (+23%) | **+$59.4M** | +$14.6M | FY2022 10-K |
| FY2023 | +$186.6M (+48%) | **+$97.7M** | +$88.9M | FY2023 10-K |
| FY2024 | +$445.1M (+77%) | **+$320.4M** | +$124.7M | FY2024 10-K |
| FY2025 | +$289.6M (+28%) | **+$246.1M** | +$43.5M | FY2025 10-K |
| **FY2026** | +$323.0M (+25%) | **−$10.5M** | **+$333.5M** | FY2026 10-K |
| Q1 FY2026 (Apr–Jun 2025) | +$29.3M (+9%) | **+$29.3M** (*"a higher volume of units sold drove $29.3 million of the increase"*) | nil | 10-Q 2025-06-30 |
| Q2 FY2026 (Jul–Sep 2025) | +$42.9M (+14%) | **−$19.4M** | +$62.2M | 10-Q 2025-09-30 |
| Q3 FY2026 (Oct–Dec 2025) | +$134.2M (+38%) | **−$1.8M** | +$136.0M | 10-Q 2025-12-31 |
| Q4 FY2026 (Jan–Mar 2026) | +$116.6M (+35%) | **−$18.0M** *(derived: FY less nine months; the filer's own quarterly and cumulative splits do not sum exactly, so this one is approximate)* | +$134.6M | 10-K |
| **Q1 FY2027 (Apr–Jun 2026)** | +$125.6M (+36%) | **−$11.7M** | +$137.4M | 10-Q 2026-06-30 |

Two things are in that table. First, **through FY2025 this was a unit-volume story**: 85% of
FY2025's growth and 72% of FY2024's was more items sold. Second, **from the quarter in which
the global price increase took effect (August 1, 2025) and rhode closed (August 5, 2025), the
filed volume line has been negative for four consecutive quarters** — −$19.4M, −$1.8M,
−$18.0M, −$11.7M — and all growth is *"higher average item price and mix"*. A caveat the
filing does not resolve: the company does not say whether rhode's units are counted inside
"volume" or inside "mix"; since the volume line is negative in a quarter when rhode added
$128.2M of sales, rhode is evidently carried in mix, and the volume line reads as
approximately the legacy brands' units at prior-year prices. **Either way, the units of the
business that existed before August 2025 have been falling for a year.** That is
Precision Steel's series [E4-55] and it is carried to Q2, where it decides the gate.

**The legacy business, separated from rhode, by quarter.** The 10-Qs and 10-K give rhode's
contribution since close ($52.4M, $128.2M, $112.9M; $293.5M for the year):

| quarter | FY2025 | FY2026 total | rhode | **legacy (e.l.f., Naturium, Well People, Keys)** | legacy YoY |
|---|---|---|---|---|---|
| Q1 (Apr–Jun) | 324.5 | 353.7 | — | **353.7** | **+9.0%** |
| Q2 (Jul–Sep) | 301.1 | 343.9 | 52.4 | **291.5** | **−3.2%** |
| Q3 (Oct–Dec) | 355.3 | 489.5 | 128.2 | **361.3** | **+1.7%** *(the 10-Q's own words: "the remaining $6.0 million contributed from our existing business")* |
| Q4 (Jan–Mar) | 332.6 | 449.3 | 112.9 | **336.4** | **+1.1%** |
| **FY** | **1,313.5** | **1,636.5** | **293.5** | **1,343.0** | **+2.2%** *(the 10-K: "the remaining $29.5 million contributed from our existing business")* |

**The company that grew 28% in FY2025 grew 2.2% in FY2026 on its own, and 0.03% over the
three quarters after it raised every price it charges.** Q1 FY2027 (+36% headline) does not
split rhode out; e-commerce (where rhode lives) rose 129% and retail 16%, and the volume line
was −$11.7M, so the legacy brands were somewhere between flat and down mid-single digits.

**Who it sells to, and how that has moved (Note 2, five vintages):**

| % of net sales | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|
| Walmart | **31** | 26 | 26 | 20 | 17 | 16 | **13** |
| Target | 22 | 22 | 23 | 25 | 25 | 23 | **18** |
| Ulta Beauty | * | * | 12 | 15 | 16 | 12 | **<10** |
| Amazon | * | * | * | * | * | 12 | 11 |
| Sephora | * | * | * | * | * | * | **10** |
| **Walmart + Target** | **53** | 48 | 49 | 45 | 42 | 39 | **31** |

Retailers 76% / e-commerce 24% of FY2026 sales; US 79% / international 21% ($344.1M, +38%).
Target is 30% of receivables and Walmart 17%. *"As is customary in the industry, none of our
customers are under any obligation to continue purchasing products from us in the future."*
Ulta went from 16% of sales to below the 10% reporting line in two years; part of that is
denominator (rhode, Sephora, Amazon), and the filing does not give the dollar figure.

**The scarce input this business controls.** Not manufacturing — *"substantially all of our
finished goods"* come from third parties, *"ample manufacturing capacity as well as redundant
capabilities"*, *"not overly dependent on any single raw material."* Not the shelf — the
retailer owns it and can reset it; the filing says shelf resets and *"the timing of product
restocking or rearrangement by our major retail customers"* drive the quarters. What e.l.f.
controls is **the brand's standing with a young consumer and the speed at which it copies
prestige at a third of the price** (*"holy grails … the e.l.f. Glow Reviver Lip Oil at $9
versus a prestige item at $42"*), plus, since 2025, a second brand whose scarce input is a
named person, Hailey Bieber, *"Founder … Chief Creative Officer and Head of Innovation"*.
The 10-K's own ranking of its five advantages — team, value proposition, innovation,
*"disruptive marketing engine"*, productivity model — names no cost advantage and no
proprietary formulation; it names execution.

**Will the fundamentals look broadly the same in ten years?** Mass colour cosmetics will be
sold through Target and Walmart, and the contract-manufacturing model in Asia will exist.
Whether **this brand** holds its shelf, and whether a celebrity skin-care line bought at 3.8x
sales is a ten-year asset, are Q2 questions. The revenue mechanism itself is simple enough to
state in three sentences, which is [E4-46]'s five-minute test passed; the complications in
this file are the perimeter (two acquisitions, one earnout) and the reading of a
price-for-volume swap, and both are documented in the company's own filings rather than
hidden.

- **VERDICT: [x] IN**
  *Recorded and carried to Q2: the filed volume line turned negative in the quarter of the
  price increase and has stayed negative for four quarters; the legacy brands grew 2.2% in
  FY2026 and 0.03% post-increase; the two mass anchors fell from 53% to 31% of sales in six
  years; no cost advantage and no proprietary input is claimed in Item 1.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief said its prior here was genuinely open and that the tariff year was the
instrument. The instrument was run first, before any class was written, and the two halves of
it point in opposite directions: the price held and the margin came back; the units left.**

### THE PASS-THROUGH TEST — the tariff year, quarter by quarter

The facts, all filed. The majority of product is made in China and has carried a 25% Section
301 tariff since May 2019. *"Throughout 2025 we were subject to a range of tariff rates on
imports from China ranging from 25% to as high as 170%."* *"During the fiscal year 2026, the
Company paid approximately $58.5 million of IEEPA Tariffs"* — **4.4% of the legacy brands'
$1,343M of sales**. The response: *"on August 1, 2025, we raised prices globally for all
products sold"* (10-K risk factor, and the same sentence in three 10-Qs), which the company
itself files as a risk — *"which could result in the loss of consumers."* Then the Supreme
Court invalidated the IEEPA tariffs on 2026-02-20, a 10% Section 122 surcharge replaced them
from 2026-02-24, and **$51.1M of refunds arrived in the June 2026 quarter, $50.1M of it
booked as a reduction of cost of sales**.

| quarter | net sales | gross margin | YoY | the filing's own attribution | rhode share of sales |
|---|---|---|---|---|---|
| Q1 FY25 (Jun-24) | 324.5 | 71.3% | | | — |
| Q2 FY25 | 301.1 | 71.1% | | | — |
| Q3 FY25 | 355.3 | 71.3% | | | — |
| Q4 FY25 (Mar-25) | 332.6 | 71.3% | | | — |
| **Q1 FY26 (Jun-25)** — tariffs in, no price increase yet | 353.7 | **69.1%** | **−215bp** | *"primarily driven by tariffs, partially offset by favorable foreign exchange impacts and mix"* | 0% |
| **Q2 FY26 (Sep-25)** — price increase from Aug 1; rhode from Aug 5 | 343.9 | **69.4%** | −165bp | *"higher tariff costs, partially offset by benefits from pricing and mix"* | 15% |
| Q3 FY26 (Dec-25) | 489.5 | 71.0% | −30bp | same wording | 26% |
| **Q4 FY26 (Mar-26)** | 449.3 | **72.7%** | **+140bp** | *"benefits from pricing, partially offset by higher tariffs"* | 25% |
| **Q1 FY27 (Jun-26)** | 479.4 | 83.2% reported / **72.7% ex the $50.1M refund** | +1,400bp / **+360bp** | *"1,050 basis points benefit from IEEPA tariff refunds, with the remaining increase primarily driven by pricing and lower year-over-year tariff rates"* | not filed |

**Margin: recovered.** A 215bp give in the first tariff quarter, back above the pre-tariff
level within three quarters of the increase, and 140bp above it by the fourth. Two caveats
the filing does not let me remove. rhode's own pro forma gross margin on e.l.f.'s
presentation is **80.8%** (8-K/A Exhibit 99.3: $212.2M sales, $40.8M cost of sales), so a
quarter of the company arriving at 81% lifts the consolidated line by something between
one and three points on its own, which means **the legacy brands' gross margin in the second
half of FY2026 sat somewhere between roughly 68% and 71%** and the filing does not say
where. And Q1 FY2027's recovery is explicitly part *"lower year-over-year tariff rates"* —
the tax went away — not all pricing. **What is filed without ambiguity is the direction: the
price increase was taken, was not rolled back, and the reported gross margin is now higher
than before the tariff.** On PLPC's yardstick (87% of a 7.7-point shock passed through inside
a year with no volume loss) e.l.f. passed the cost through at least as completely.

**Volume: lost, and still being lost.** The other half of [E2-44]'s first characteristic —
*"raise prices even when product demand is flat"* — is answered by the volume line at Q1:
**−$19.4M, −$1.8M, −$18.0M, −$11.7M in the four quarters since August 1, 2025**, against
prior-year quarterly sales of $301M, $355M, $333M and $354M: **−6.4%, −0.5%, −5.4%, −3.3%**.
Before the increase, volume had grown every year and every quarter on record, and had
carried 85% of FY2025's growth. **PLPC passed its cost through and kept its units. e.l.f.
passed its cost through and lost them.** Dollar revenue in the legacy brands was held flat
(+0.03% over the three post-increase quarters) by price; that is Precision Steel's
sentence — *"a serious reverse, not likely to disappear in some 'bounce back' effect"* —
and it is the honest series [E4-55].

**[E4-37], the agony metric.** The company took one uniform increase, across every product,
globally, once, and only when a 55–170% tariff forced it; its 10-K files the increase as a
risk to consumers in the same breath. Before that, the last realised price effect of size
was FY2023 ($88.9M, the 2022 inflation year). Two increases in six years, each under
external cost pressure, each disclosed as a hazard: **that is nearer the prayer-session end
of the scale than the yawn end**, and the volume line says the prayer was warranted.

### DOES E.L.F. FILE A COST ADVANTAGE? — NO NUMBER; A DESCRIPTION

The brief asked whether the claimed speed-to-market and price-point advantages are filed
numbers. Item 1: *"a scalable, asset-light supply chain centered on the combination of speed
to market, high-quality and low costs"*; *"Our broad supply base gives us the ability to
fulfill our product requirements and remain cost competitive."* **No unit-cost figure, no
cost-per-item comparison, no speed-to-market metric appears in any of the five 10-K vintages
read.** The only quantified cost fact is the outcome: cost of sales is 29% of net sales at a
$7 shelf price. The competitor row below shows that this gross margin is *the same* as the
prestige houses earn at $30 price points — which says e.l.f.'s unit cost is very low, but
not that it is lower than what Coty's or L'Oréal's Chinese contract manufacturers would
charge for the same tube. The 10-K's own five *"unique areas of advantage"* are *team, value
proposition, innovation, marketing engine, productivity model*. **Not one is a cost claim.
[E2-58]'s "wide and sustainable" cost-advantage exception is not filed, and I do not claim it
for them.** What the filing describes instead is the PLPC shape: a real advantage (here,
brand momentum with a young consumer) that costs a rising share of every sales dollar to
keep — **advertising 9.2% of sales in FY2020, 22.1% in FY2026** (tagged
`AdvertisingExpense`: $26.0M → $361.3M), and *"marketing and digital"* $399.8M, 24%.

### [E3-03] — THE THREE CRITERIA, AGAINST THE COMPANY'S OWN WORDS

**(1) Needed or desired — desired, yes.** e.l.f. Cosmetics is, by its own Nielsen citation
(rhode announcement 8-K, 2025-05-28), *"the No. 1 brand in units across U.S. cosmetics and
No. 2 in dollar share"*, and *"the most purchased cosmetics brand among Gen Z, Gen Alpha and
Millennials"* (2026 proxy). Twenty-nine consecutive quarters of net-sales growth. The desire
is real and it is measured.

**(2) "Thought by its customers to have no close substitute" — FAILS, and the company's own
positioning is the reason.** e.l.f.'s pitch is that it *is* the close substitute: *"the e.l.f.
Glow Reviver Lip Oil at $9 versus a prestige item at $42, e.l.f. Cosmetics Power Grip Primer
at $11 versus a prestige item at $38"*. A business whose value proposition is *we are the
substitute for the thing you wanted* has, by construction, told you that its customer thinks
in substitutes. The risk factor says the rest: *"Competition in the beauty industry is based
on the introduction of new products, pricing of products, quality of products and
packaging…"*; competitors *"may attempt to gain market share by offering products at prices
at or below the prices at which our products are typically offered, including through the
use of large percentage discounts and 'buy one and get one free' offers"*; *"Increasing shelf
space allocated to our products may be especially challenging in instances when a retailer
has its own brand"*; and *"numerous online, 'indie,' celebrity and influencer-backed beauty
companies"* keep arriving. **Price is named; private label is named; the celebrity brand
is named — and e.l.f. then bought one.** The four-quarter volume decline after a $1 move is
what "close substitute" looks like in a filed number.

**(3) Not subject to price regulation — yes.** No regulator sets cosmetics prices; the
tariff is a cost, not a price cap.

### [E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? YES, BY THE FILING'S OWN DESCRIPTION

*Does a lapse in spending destroy the structure, or merely narrow it — and does the spending
defend the same advantage, or buy its replacement?* The 10-K: *"We leverage insights from
our site and Beauty Squad loyalty program to proactively change out a portion of our retail
assortment each year"*; the flagship held *"four of the top 10 new products in all of mass
cosmetics in 2025 … six of the top 10 new products in 2024."* The advantage is a **pipeline
of new products marketed on social media to a young consumer**, and each season's products
replace last season's. That is Coca-Cola's trademark only if the *name* carries the
purchase; the volume series says that when the price moved, the name did not hold the
units. **And the spending buys replacements, literally: $1.23bn of consideration for two
brands in three years, both of them younger than e.l.f.'s own loyalty programme, one of them
a person.** Advertising at 22% of sales and rising is [E4-04]'s continuous rebuild, not
[E5-23]'s defence of a fixed structure.

**[E4-36], which of the four causes?** Wave-riding, principally: the 2022–2025 run coincided
with an inflation-driven trade-down, a TikTok "dupe" culture that e.l.f. names as its
mechanism, and a Gen Z cohort it names as its consumer. Plus one variable at an extreme (the
$7 price point). *"If he gets off the wave, he becomes mired in shallows"* [E3-51] — the
quarter the price rose, the legacy units fell.

**[E4-23] — key person, recorded HERE as a moat defect.** rhode, a quarter of revenue and
$898M of consideration, is filed as dependent on named individuals: *"The success of our
acquisition of rhode will depend, in part, on our ability to successfully integrate and
retain key employees of, and other certain personnel affiliated with, rhode"*; the
announcement names Hailey Bieber as *"Founder … Chief Creative Officer and Head of
Innovation"* with shares under a one-year lock-up. *"The partnership's moat will go when
the surgeon goes."* This is a defect in the business, not a compliment to the person.

### [E3-46] — THE SECOND QUESTION IS A NUMBER, AND HERE IT CUTS BOTH WAYS

| FY | net income | ROE on beginning equity | beginning tangible equity | ROTE |
|---|---|---|---|---|
| 2020 | 17.9 | 8.3% | −39.2 | n/m |
| 2021 | 6.2 | 2.6% | −31.5 | n/m |
| 2022 | 21.8 | 8.1% | 3.7 | n/m |
| 2023 | 61.5 | 19.7% | 54.6 | 113% |
| 2024 | 127.7 | 31.1% | 161.4 | 79% |
| 2025 | 112.1 | 17.4% | 76.9 | 146% |
| 2026 | 26.3 | 3.5% | 212.6 | 12.4% |

**The legacy operating business earns extraordinary returns on tangible capital**, because
it has almost none: 849 people, $41.5M of property, third-party plants, third-party
warehouses. That is the strongest structural fact for the business and it is stated here at
full strength. **But the [E2-43] goodwill wedge is where the retained capital went** — equity
$1,130.5M of which $1,406.6M is goodwill and purchased intangibles; **tangible equity is
negative $276M** after rhode — and the return on *that* capital is what Q3's [E2-56] test
judges. On the whole-equity series the FY2026 ROE is 3.5%.

### [E2-53] dominance / [E3-33] untapped pricing power / [E4-32] direction

- **[E2-53] — NO.** *"Once dominant, the newspaper itself, not the marketplace, determines
  just how good or how bad the paper will be."* e.l.f. is No. 1 in units in US mass
  cosmetics and the marketplace still set the answer to a $1 increase inside one quarter.
- **[E3-33] / [E5-28] — NO.** Untapped pricing power means a near-monopoly that has not
  priced. The company just priced, once, under duress, and lost units; the 10-K names
  Walmart's and Target's own brands as the constraint on shelf. There is nothing ungathered
  here; there is a price that was tested and answered.
- **[E4-32] direction — NARROWING, on every filed series.** Legacy growth **28% → 2.2%**;
  operating margin **14.6% (FY2024) → 12.0% → 4.5%** (8.0% before the earnout charge); unit
  volume **+$246M → −$10.5M**; advertising **20.4% → 22.1%** of sales to hold it; Walmart
  and Target **42% → 31%** of sales in two years; Ulta 16% → below the reporting line. The
  moat *widened every year* is the corpus's primary criterion, and the last two years read
  the other way.

### THE COMPETITOR ROW — required **[E3-28]**. *Full working, with accessions, in
`Test Runs/_research 2026-09-11 ELF/COMPETITOR_ROW.md`.*

**Peers taken: 5 of the industry's 8-plus real competitors, plus the channel.** The 10-K
names L'Oréal, Estée Lauder, Coty, Unilever, LVMH, Shiseido, Beiersdorf and Procter & Gamble
as the multinationals, plus indie and celebrity brands and retailers' own labels. Taken:
Estée Lauder and Coty (SEC filers, XBRL, latest 10-Ks `0001001250-26-000041` and
`0001024305-26-000048`); Revlon (**rung BLOCKED**: Chapter 11 2022-06-15, Form 15 filed
2023-05-02, private; last 10-K FY2022 `0000887921-23-000006`, three years stale); L'Oréal
(**no SEC filing; one rung down**, IFRS in euros from the issuer's own 2025 results release
of 2026-02-12 — recorded for position only); Ulta, reused from `Test Runs/2026-09-02 Run -
ULTA Ulta Beauty.md` as **the channel, not a brand peer**. Not taken: Unilever, LVMH,
Shiseido, Beiersdorf, P&G (none discloses a mass colour-cosmetics line that can be compared;
the obstacle is segmentation, not access). **Private label: no filer in the set discloses
it as a number; EL and Coty both name it as a competitor class in words.** The EDGAR
full-text sweep of who names e.l.f. Beauty returned **HTTP 403 from efts.sec.gov on every
transport**; what the filings read say is that **neither Estée Lauder nor Coty names e.l.f.
anywhere** — EL names nine competitors and e.l.f. is not among them. **Moat class carries
PROVISIONAL for the L'Oréal rung and the blocked sweep; the verdict below does not rest on
either.**

| latest filed FY, same metric | **ELF FY2026 (Mar)** | Estée Lauder FY2026 (Jun) | Coty FY2026 (Jun) | **Coty Consumer Beauty (mass) FY2026** | Revlon FY2022 (stale) | L'Oréal CY2025 (IFRS) | **L'Oréal Consumer Products CY2025** | Ulta FY2025 (retailer) |
|---|---|---|---|---|---|---|---|---|
| Gross margin | **70.7%** | 75.5% | 62.9% | n/d | 57.8% | NOT OBTAINED | n/d | 39.1% |
| GAAP operating margin | **4.5%** (8.0% before the earnout charge) | 5.2% | (1.4)% | **(22.1)%** | 4.0% | 20.2% | **21.4%** | 12.4% |
| Best operating margin in the five-year window | 14.6% (FY2024) | 17.9% (FY2022) | 9.8% (FY2023) | 4.0% (FY2024) | 5.0% (FY2021) | 20.2% | 21.4% | 15.0% (FY2023) |
| Advertising / promotion, % of sales | **24%** (marketing and digital) | 24.8% (incl. product development) | 27.7% | n/d | 16.7% | n/d | n/d | n/a |
| ROE on beginning equity, latest | 3.5% | 4.7% | (17.1)% | | negative equity | | | |
| Goodwill / intangible impairments, last two FY | **none** (single reporting unit) | $1.29bn FY2025 | $212.8M FY2025 + **$362.8M FY2026, every mass trademark: CoverGirl, Sally Hansen, Max Factor, Bourjois** | | $144M FY2020 | | | |
| Owned plants | **none** | yes | yes (Ashford, Hunt Valley, Senador Canedo) | | | yes | | |

**What the row says, and it decides the [E2-58] question the brief asked.**

1. **e.l.f.'s gross margin is high for mass and low for prestige — and it is a price
   outcome, not a filed cost advantage.** 70.7% at a $7 price point against Coty's 62.9%
   with owned plants and Estée Lauder's 75.5% at $30. The low-cost Chinese sourcing model
   is real and shows up exactly where a cost advantage should: above every mass peer with
   plants. **Then all of it is spent.** SG&A 62.7% of sales; marketing 24%, the same ratio
   as Estée Lauder's prestige machine and within four points of Coty's.
2. **The [E2-58] test — a competitor with a worse cost position earning a comparable
   operating margin — is not merely met, it is exceeded threefold.** L'Oréal's Consumer
   Products Division — NYX and L'Oréal Paris on the same Target shelf, with the group's
   own manufacturing and research base (stated in its URD, not verified in this file) —
   reports **21.4% profitability on €16.1bn**; e.l.f.'s best year was 14.6%
   and its latest 4.5%. Estée Lauder, carrying $813M of restructuring, printed 5.2% GAAP
   against 4.5%. **The two competitors e.l.f. does out-earn — Coty Consumer Beauty at
   (22.1)% and Revlon into Chapter 11 — are the ones whose own filings record share loss
   in US mass colour cosmetics, trademark write-downs on every mass brand they own, and a
   strategic review to exit.** Coty's FY2026 10-K: *"In Consumer Beauty, color cosmetics
   net revenues declined by a mid-single digit percentage despite mid-single digit market
   growth."* That is the share e.l.f. took, from the weakest incumbents, in a market that
   was itself growing. Keyence-against-Cognex: the peer with the heavier cost base out-earns
   the subject at the operating line, so **the moat claim cannot be a cost moat**.
3. **The channel out-earns the brand (the ULTA run's finding, reused):** Ulta's 12.4%
   operating margin against e.l.f.'s 4.5%; *"the retailer is currently a better business
   than most of its suppliers."* And the ULTA run closed that name at Q2 OUT, NARROWING,
   with cosmetics its shrinking category (41% → 37% of sales) and the Ulta-at-Target
   shop-in-shop concluding August 2026.
4. **The row's limit, stated [E3-61].** It shows position at one date. It cannot show
   whether NYX will price against e.l.f., whether Coty's mass brands go to an owner who
   fights or harvests, whether Target fills freed feet with its own label (no filer
   discloses private label), or whether e.l.f.'s 24% marketing ratio is the price of
   holding position or of buying it. Two gaps stay open in the row: the blocked EFTS
   sweep and L'Oréal's gross margin. Neither changes the shape of the finding.

### THE Q2 VERDICT

- Needed or desired **[x]** · no close substitute **[ ] FAILS** · not price-regulated **[x]**
- Must the moat be continuously rebuilt? **Yes** — a seasonal product pipeline marketed
  at 22–24% of sales, rising, and two brands bought to replace organic growth [E4-04].
  Does success depend on a great manager? **The 10-K says so in its own list of
  advantages, and a quarter of the company depends on a named founder [E4-23].**
- Primary moat metric, filing-sourced, and its trend: **the filed unit-volume line —
  +$246M (FY2025) to −$10.5M (FY2026) and negative in each of the four quarters since the
  August 2025 price increase; legacy net sales +2.2% for the year, +0.03% post-increase.**
- Untapped pricing power [E3-33]: **no — pricing was tested once and answered.**
- Peers named: 5 of 8+, plus the channel; L'Oréal one rung down; sweep blocked.
- **Class: NARROW · Direction: NARROWING · PROVISIONAL only as to the L'Oréal rung.**
- **VERDICT: [x] OUT — on [E3-03] criterion (2), evidenced by the company's own
  dupe-of-prestige positioning, its naming of price, private label and celebrity brands as
  the competition, and the filed four-quarter unit decline after a $1 price move; on [E2-44]
  half one, the same series; on [E4-04], a moat rebuilt each season at 24% of sales; and on
  [E2-58], answered by the competitor row.**

**THE CASE FOR IN, STATED AS WELL AS I CAN STATE IT [E4-51, E4-26], because the
framework's own bias is to close consumer names here and I have been told so.**

> e.l.f. Cosmetics is **the No. 1 brand by units in US mass cosmetics and No. 2 by
> dollars**, the most purchased brand among Gen Z and Millennials, with **twenty-nine
> consecutive quarters of net-sales growth** and seven straight years of share gains
> through a pandemic, an inflation shock and a 170% tariff. It earns a **prestige gross
> margin (70.7%) at a $7 price**, needs **no plant, no store and $41M of property**, and
> earned **79–146% on tangible equity** in the three years before rhode. It passed a
> 4.4%-of-sales tariff through in three quarters and its gross margin is now higher than
> before the tariff. Its two acquisitions are the two fastest-growing skin-care brands of
> their cohorts, and rhode's earnout is being beaten so hard that the liability has gone
> from $7M to $81M in eleven months. Coty is writing off every mass brand it owns and
> reviewing an exit; Revlon went bankrupt; the share they lost went to e.l.f. The
> categories it named as whitespace — skin, international, Sephora — are all growing
> double digits. The quarter just reported grew 36%. If the cost pass-through and the
> unit share are not a franchise, the word has no meaning in mass consumer goods.

**Why it still does not carry the gate.**

1. **Criterion (2) asks what the customer thinks, and the filed volume line answers for
   the customer.** A brand with no close substitute in its buyers' minds does not lose
   units in four consecutive quarters on a $1 move at a $7 price point. The company's own
   pitch — *"$9 versus a prestige item at $42"* — is a statement that the customer
   substitutes, and the risk factor names price, BOGO, private label and celebrity brands
   as the substitutes. The unit share is a share of a category e.l.f. calls *"highly
   competitive"*, not a position that the marketplace cannot revisit.
2. **[E2-44] half one fails on the company's own number, in the only test the window
   contains.** Price up, volume down, four quarters running, dollar sales flat — which is
   the Precision Steel shape [E4-55] and the opposite of PLPC's.
3. **[E4-04]: the moat is a marketing engine and a novelty pipeline, and its cost is rising
   as a share of sales (9% → 22–24% in six years) while its output (units) has turned
   down.** A lapse in that spending would not narrow the structure; it would remove it.
   And $1.36bn was spent buying replacements — one of which is a person [E4-23].
4. **[E2-58]: the competitor row shows a peer with a worse cost position earning three
   times the operating margin.** The gross-margin advantage is real and is spent entirely
   below the gross line; what e.l.f. has out-earned are the two incumbents already
   failing. There is no filed cost advantage and none is claimed.
5. **[E4-32]: direction outranks existence, and every filed series narrowed in the last
   two years** — organic growth 28% → 2%, operating margin 14.6% → 4.5%, volume positive
   → negative, mass anchors 42% → 31% of sales.

**What would flip this verdict, named in advance so it is falsifiable.** Any one of:
**(a)** the filed volume line positive for four consecutive quarters at the post-August-2025
price, which would show the units came back and the price stuck — [E2-44] half one passed;
**(b)** GAAP operating margin at or above 12% for two consecutive fiscal years with
advertising at or below 20% of sales, which would show the moat is holding without being
rebought; **(c)** a filed cost-per-unit or speed-to-market metric against a named peer;
**(d)** Walmart and Target holding their combined share of e.l.f.'s sales for two years at
a stable dollar amount. **Each is a document I can name, so the verdict is reviewable; it
is OUT and not UNRESEARCHED because every document that exists has been read and they
answer the question as it stands.**

**Q2 CLOSES THE FILE. Everything below is recorded because the brief commissioned it and
because a closed file still owes the register its findings. None of it is a verdict, and
per operator rule 2 none of it can promote the name.**

---
# TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

Q2 returned OUT. Per operator rule 2 the file is closed and **nothing below promotes the
name.** It is written because the brief commissioned specific work ([E4-29] from the
releases, pay metrics, SBC/OCF to the dollar, [E5-11] with the rhode debt, [E5-08] against
the count including acquisition stock, the width over six-plus windows) and because a
closed file still owes the register its findings. **No verdict is written for Q3, Q4 or Q5.**

## Q3 ITEMS — recorded **[E2-01, E4-22, E4-29, E5-08, E2-30]**

**The weight case, declared because a run that does not declare it has not done Q3.**
Daily execution **[E3-38]** — **yes**: the 10-K's five advantages are all execution
(innovation cadence, marketing engine, assortment change-outs), the product is a
fashion-cycle good, and *"a business, unlike a franchise, can be killed by poor
management"* [E3-43] is exactly the Q2 finding. Control **[E1-16]** — no. Leverage
**[E3-29]** — **partly**: $841.7M of covenanted bank debt against negative tangible equity.
**One ticked, arguably two → Q3 would be a BINARY GATE and no price would compensate.**

**Honesty — the dated record [E5-16].** Securities class actions filed **2025-03-06** and
2025-04-08 (N.D. Cal.), consolidated; on **2026-02-04 the court dismissed nearly all
challenged statements but found a claim adequately stated as to statements made on
November 21, 2024**; answer filed 2026-04-03; *"early stages of discovery."* Four derivative
suits (2025-03-28, 2025-04-09, 2025-04-22, 2025-05-19, 2026-04-14), stayed or early. The
surviving statement date sits between the Nov-2024 guidance raise and the Feb-2025 guidance
cut *("softer than expected trends in January")*. **This is litigation, which the framework
says is a source to read, not the checklist; nothing in it is a filed-figure integrity
finding, and the standard is [E5-22]: what matters is what they did when they learned.**
Recorded, dated, not scored as a disqualifier.

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15]. The brief's prior — clean in the 10-K, firing
in the releases — is CONFIRMED, and it is the CGNX pattern exactly.**
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES at full strength.** The word
  *"Adjusted EBITDA"* does not headline the 10-K (Item 7 discusses GAAP lines). In every one
  of the thirteen earnings releases read it is the third bullet and the guided metric: FY2027
  outlook *"Adjusted EBITDA $401-407 million"* against a FY2026 GAAP operating income of
  $73.6M. **The definition excludes stock-based compensation ($86.9M), the earnout charge
  ($57.6M), and *"amortization of internal-use software costs related to cloud
  applications"*** — a cash cost that was spent and is being amortised, [E5-41]'s reverse
  float deleted by name. Adjusted net income additionally removes *"amortization of acquired
  intangible assets"* ($35.5M). FY2026: GAAP net income **$26.3M**; Adjusted EBITDA
  **$335.2M**; the ratio is 12.7x.
- [x] **Trumpeted projections / growth targets [E4-22 third flag; E3-48 action taken].**
  Guidance is issued and revised every quarter. The record, initial outlook vs outturn:

| fiscal year | initial net-sales outlook (date) | raises / cuts in the year | **outturn** |
|---|---|---|---|
| FY2023 | $432–440M, +10–12% (2022-05-25) | raised through the year | **$578.8M, +48%** |
| FY2024 | $705–720M, +22–24% (2023-05-24) | raised Aug (+37–39%), Nov (+55–57%), Feb ($980–990M) | **$1,023.9M, +77%** |
| FY2025 | $1,230–1,250M, +20–22% (2024-05-22) | raised Aug ($1,280–1,300M), Nov ($1,315–1,335M); **CUT Feb-2025 to $1,300–1,310M** *("softer than expected trends in January")* | **$1,313.5M, +28%** |
| FY2026 | **none** (2025-05-28: *"Due to the wide range of potential outcomes related to tariffs, the Company is not providing a Fiscal 2026 financial outlook"*); issued Nov-2025 at $1,550–1,570M | raised Feb-2026 to $1,600–1,612M | **$1,636.5M, +25%** |
| FY2027 | $1,835–1,865M, +12–14% (2026-05-20) | raised Aug-2026 to $1,938–1,968M, +18–20% | open |

  Nine raises, one cut, one withdrawal in four years; the initial number has been beaten by
  between 5% (FY2025) and 42% (FY2024). This is a **guide-low-and-raise culture**, and
  [E5-30] says it is a ratchet: *"do it once and you probably never stop."* The one cut
  is the one the class action attaches to. On the projections flag's own action [E3-48] —
  demand the record of the people making them — the record is that the projections were
  systematically too low, which is the benign direction, and that the company stopped
  guiding the moment the tariff made the number unknowable, which is the candid direction
  [E2-49]. Fires as a prompt; reads as promotion rather than fabrication.
- [x] **Serial share issuance [E5-15] — partial.** No equity raised for cash. But 2,582,371
  shares issued for rhode at $116.28 (a price the stock has not seen since) and 577,659 for
  Naturium, plus 1.0–1.4M a year from vesting; the count rose 55.7M → 59.1M in FY2026 while
  $50M was spent buying back. **Every employee receives an annual equity grant** (the 10-K's
  *"one-team"* approach), which is why SBC runs 41–57% of operating cash flow (below).
- [ ] Weak accounting — none found. Deloitte since 2014, unqualified; two CAMs (customer
  incentive reserves; rhode valuation and earnout), both the estimates one would expect.
- [ ] Unintelligible footnotes — no. Note 3 is model disclosure: every element of
  consideration, the seller expenses, the earnout mechanics and each remeasurement.
- [x] **Metric-switching [E2-49] — one instance, candid direction.** The "consecutive
  quarters of net sales *and market share* growth" line ran for 25 quarters; from the
  Q1-FY2026 release the market-share half is dropped for the company and retained only for
  *"our namesake e.l.f. brand"* (140bp, 130bp). Announced with the number, not silently.
- **Filed-figure tells [E4-30]:** growth is not smooth (12/23/48/77/28/25%); cash taxes as a
  share of pretax ran 30% / 21% / 9% / 17% / 53% — the 9% (FY2024) is stock-option deduction
  timing and the 53% (FY2026) is a collapsed pretax base, neither the Salomon shape.

**Pay metrics [E4-52] — the flags converge on one number.** From the 2026 proxy: *"Since we
became publicly traded in 2016, our annual cash incentive plan has been based on Adjusted
EBITDA performance against pre-established targets."* FY2026: **$335M Adjusted EBITDA
funded the bonus at 200% of target** in a year GAAP net income fell 77% to $26.3M and
GAAP operating income fell 53%. In October 2025 the Committee *"increased the plan's
Adjusted EBITDA threshold, target and maximum performance goals"* after rhode closed — the
right direction — and it still paid at maximum. PSUs vest on a three-year **net sales
CAGR** with stretch on market share; no return-on-capital, margin or per-share metric
anywhere in the plan. CEO total compensation $8.83M (FY2026), 84% equity; Amin owns 2.6%
(1,546,270 shares); Baillie Gifford 12.5%, BlackRock 8.6%, Vanguard 5.1%. **The metric that
pays management is the one that deletes SBC, the earnout and cloud amortisation; the
metric that vests the PSUs is the one the acquisitions bought.** That is the lollapalooza
shape: a non-GAAP headline, a guidance ratchet, an all-employee grant programme, and a
top-line PSU, reinforcing one another toward growth-at-any-margin.

**SBC/OCF, cross-checked to the dollar (calibrated row: CRWD 68.0% · PINS 68.6% · QLYS
24.9% · CRM 23.4% · SHOP 22.1%).** Filed cash-flow lines: FY2024 40,625 / 71,154 =
**57.1%**; FY2025 71,786 / 133,840 = **53.6%**; FY2026 86,919 / 212,511 = **40.9%** (on OCF
before the $47.1M of seller expenses paid through it, 33.5%); Q1 FY2027 19,677 / 111,665 =
17.6% on a quarter carrying a $52.1M tariff refund. **e.l.f. sits between the software
names and the mature ones — for a cosmetics company.** SBC grew 5.6x in six years (15.5 →
86.9) while operating cash flow grew 4.8x. Grants are RSUs and PSUs (no options granted
since FY2024), so grant-date value and market value coincide and the reported charge is the
right subtraction rather than a floor [E3-70].

**STEP 3 — THE PRIMARY TEST [E2-01].** Return on beginning equity: 8.3 / 2.6 / 8.1 / 19.7 /
31.1 / 17.4 / **3.5%** (FY2020–26); on beginning tangible equity, extraordinary where
positive (79–146%) and undefined where negative — the [E2-43] denominator says the
operating business needs almost no capital and the acquisitions consumed all of it. The
[E2-56] incremental test: **equity rose $888M over FY2020–26 ($242M → $1,130M), of which
$358M is shares issued for acquisitions; net income went from $17.9M to $26.3M.** On
retained-plus-issued capital the incremental return is under 1%. Segment-by-segment is
impossible: one segment, one reporting unit, *"due, in part, to the integrated nature of
the Company's various distribution channels"* — which also means **the goodwill from
Naturium and rhode can never be impaired separately from the namesake brand's cash flows.**

**The half-owner test [E2-26].** Note 3 tells me everything about the deals; the price/volume
split tells me units fell; the release tells me Adjusted EBITDA rose 13%. Both are true and
only one is the headline. Passes on the footnotes, fails on the front page.

**The institutional imperative [E2-30]:** (2) **projects materialise to soak up funds —
ticked**: $1.23bn on two brands inside three years, the second financed with $650M of new
debt; (4) **peer behaviour imitated — ticked**: the celebrity/influencer brand acquisition
is what every large house has done (EL, Coty, L'Oréal), and e.l.f.'s own risk factor names
the genre as competition. (1) and (3): not evidenced.

**Capital allocation — buybacks [E5-08, E4-31, E5-44].** (1) Ample funds? Cash $344M against
$834M of debt and up to $200M of earnout; the buyback is covenant-gated (*"require the
Company to be in compliance with certain leverage ratios to make repurchases"*). (2)
Material discount? Repurchases: FY2025 108,753 shares at **$157.04** and 701,346 at
**$71.29**; FY2026 626,049 at **$79.85**; Q1 FY2027 900,063 at **$55.53**. Against those,
**2,582,371 shares were issued for rhode at $116.28** and 577,659 for Naturium at $100.01 —
[E5-44]'s test in shares: the company sold its own paper at $116 in August 2025 and has
been buying it back at $55–80 since, which is the right sequence only if the stock was
overvalued at $116, in which case rhode was cheaper than it looked, and the earnout is
making it dearer. The share count still rose. **Capital-allocation flag: recorded, with the
humility clause [E4-13] — management knows the brand better than I do, and the buyback
at $55 may prove the cheapest purchase in this file.**

**THE GUARDRAIL.** Nothing here promotes the name. The Q2 finding that this business
*requires* an execution engine to hold its shelf is recorded at Q2 as a moat defect, not
here as a strength.

## Q4 ITEMS — recorded **[E2-23, E4-20, E5-11, E2-27, E3-24]**

### Owner earnings — the eight-window rebuild the brief demanded
### **COMPUTATION — NOT A CLEARANCE**

Method, per the standing convention: **OE = operating cash flow − share-based compensation −
(c)**, with (c) shown at both ends and then judged. All figures from the filed cash-flow
statements (FY2026 10-K `0001600033-26-000020`, FY2025 `0001600033-25-000016`, FY2024
`0001600033-24-000020`, FY2023 `0001600033-23-000016`, FY2022 `0001600033-22-000027`). Two
adjustment columns: **"+seller"** adds back the acquisition seller expenses paid through OCF
($10.5M FY2024, $47.1M FY2026), which are purchase price and not operating cost; **"−earnout"**
additionally removes the non-cash earnout addback ($57.6M FY2026), treating the accrued
earnout as a cost of the year in which it was earned. The D&A series carries the FY2025-vintage
presentation from FY2023 forward (lease expense outside D&A) and the older presentation
before it, which is stated rather than smoothed.

| FY (Mar) | OCF | SBC | D&A | capex | **OE @capex** | OE @D&A | +seller @capex | +seller @D&A | −earnout @capex |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 44.3 | 15.5 | 22.8 | 9.4 | **19.4** | 6.0 | 19.4 | 6.0 | 19.4 |
| 2021 | 29.5 | 19.7 | 25.2 | 6.5 | **3.3** | −15.4 | 3.3 | −15.4 | 3.3 |
| 2022 | 19.5 | 19.6 | 27.1 | 4.8 | **−4.9** | −27.2 | −4.9 | −27.2 | −4.9 |
| 2023 | 101.9 | 29.1 | 17.6 | 1.7 | **71.1** | 55.2 | 71.1 | 55.2 | 71.1 |
| 2024 | 71.2 | 40.6 | 30.2 | 8.7 | **21.9** | 0.4 | 32.4 | 10.9 | 32.4 |
| 2025 | 133.8 | 71.8 | 44.1 | 18.5 | **43.5** | 17.9 | 43.5 | 17.9 | 43.5 |
| 2026 | 212.5 | 86.9 | 79.4 | 22.4 | **103.2** | 46.2 | 150.3 | 93.3 | 92.7 |

| window | OE @capex | OE @D&A | +seller @capex | +seller @D&A | −earnout @capex | yield @capex, filed / +seller (cap $5,718M) |
|---|---|---|---|---|---|---|
| 2yr FY25–26 | 73.3 | 32.0 | 96.9 | 55.6 | 68.1 | 1.28% / 1.69% |
| 3yr FY24–26 *(the screen's window)* | 56.2 | 21.5 | 75.4 | 40.7 | 56.2 | 0.98% / 1.32% |
| 4yr FY23–26 | 59.9 | 29.9 | 74.3 | 44.3 | 59.9 | 1.05% / 1.30% |
| **5yr FY22–26** *(corpus default [E2-42])* | **47.0** | **18.5** | **58.5** | **30.0** | **47.0** | **0.82% / 1.02%** |
| 6yr FY21–26 | 39.7 | 12.9 | 49.3 | 22.5 | 39.7 | 0.69% / 0.86% |
| 7yr FY20–26 | 36.8 | 11.9 | 45.0 | 20.1 | 36.8 | 0.64% / 0.79% |
| 5yr FY21–25 *(alt terminal)* | 27.0 | 6.2 | 29.1 | 8.3 | 29.1 | 0.47% / 0.51% |
| 5yr FY20–24 *(alt terminal)* | 22.2 | 3.8 | 24.3 | 5.9 | 24.3 | 0.39% / 0.42% |

**The width, in dollars and a word.** Single years run from **−$27M to +$150M**; every
multi-year mean that can be built lands between **$4M and $97M**. The screen row said $18M
to $56M. **The bottom of this range sits at zero** — the D&A end of any window that includes
FY2021–22 is single-digit or negative — and a percentage width against it is manufactured,
not measured; it is refused here for the same reason `level_shift_oe` refused its ratio
(*"EARLY HALF STRADDLES ZERO"* — the flag was right). The word is: **the owner earnings of
this company have a level only from FY2025 onward, and that level is two years old and
contains an acquisition each year.**

**[E5-11] on the width: the distorted years are named.** FY2021–22 (COVID retail, the
first e-commerce push, SBC equal to operating cash flow); FY2024 (a $93.9M inventory build
*"to support net sales growth … and $7.8 million related to a change in certain vendor
arrangements where we now take ownership of inventory at shipment from China"*, plus
Naturium); FY2026 (rhode, $47.1M seller expenses, $57.6M earnout addback, and the working
capital line *"prepaid expenses and other assets (67,401)"*). **And normalise down [E4-41]:**
Q1 FY2027's $111.7M of operating cash carries a **$52.1M IEEPA refund** — a one-time
recovery of a tax the company had already passed through in price. It is named and removed
before any run-rate is trusted.

### THE (c) JUDGMENT — DISCLOSED, NOT COMPUTED [E2-23, E3-44, E2-41, E5-20]

*"(c) must be a guess."* **This filer is the mirror image of the [E5-20] exception, twice
over, and the D&A end of the band is INVALID in the direction that flatters the bear case.**
FY2026 D&A of $79.4M decomposes, from the notes, into:

| component | FY2026 $M | where the cash went |
|---|---|---|
| Amortisation of **acquired intangibles** (Note 4) | **35.5** | purchase price; renews nothing that marketing above the line does not already renew (the QCOM/AVGO/CERT ruling) |
| Amortisation of **retail product displays** (Note 2: *"included in other assets … generally amortized over a period of three years"*) | **35.0** | **bought through OPERATING cash flow** — the working-capital line *"prepaid expenses and other assets"*; net displays rose $69.3M → $75.6M, so roughly **$41M** was spent in the year and is already deducted in OCF |
| Amortisation of **cloud-application software** (Note 2: in prepaid expenses, three years) | **13.3** | same: roughly **$25M** spent through OCF working capital in FY2026 |
| Depreciation of property and equipment (Note 5) | **8.7** | against capex of $22.4M in investing |

**So the D&A end subtracts $48.3M of amortisation whose cash is already inside the OCF
numerator, and $35.5M that is purchase accounting.** The [E3-44] default (D&A as the proxy
for (c)) presumes the cash for what is amortised went through investing; here two-thirds of
it did not. **JUDGMENT: (c) = purchases of property and equipment ($22.4M), because the
fixturing, display and software renewal that a shelf-based consumer brand actually requires
is already charged through operating working capital at roughly $66M a year, and adding it
again would triple-count.** The capex end is therefore the honest end, and OCF is already a
conservative numerator for this filer. Windage: **none** spent here — this is a
classification, not a haircut. The one adjustment that spends conservatism *against* the
company is "−earnout", which treats $57.6M of accrued rhode earnout as a FY2026 cost; it is
shown, not adopted, because the earnout is acquisition consideration and belongs in the
perimeter, not in owner earnings — **and it will be paid in cash, up to $200M, out of
financing, where this series never sees it.**

**Judged owner earnings for the business as it stands: roughly $100M to $150M** — FY2026 at
the capex end, filed ($103M) and with the seller expenses restored ($150M) — against a
five-year mean of $47M to $59M that describes a smaller company. **The combined-perimeter
reading (rhode for the four months it was not owned) adds roughly $10M:** rhode earned
$35.5M of net income in the six months to June 2025 on its own books, and the $650M of debt
that bought it costs about $45M a year at 5.4%, so a full year of rhode in FY2026 would have
added ~$25M of operating cash and ~$13M of extra interest. The 10-K's own pro forma agrees:
net income $30.1M pro forma against $26.3M actual.

**Stock compensation subtracted in full [E5-06]:** $86.9M, 41% of OCF. RSUs and PSUs only.

### Great, good, or gruesome? [E4-20]

**Two businesses, two answers.** The legacy asset-light brand is the *great* account on its
own capital: $41.5M of property, negative tangible equity, and returns on tangible capital
in three digits when positive. **The corporate whole is being run as the gruesome account
on the incremental dollar:** $1.36bn committed to two brands at 3.7–3.8x sales whose
combined pre-deal operating income was about $90M (Naturium ~$17M adjusted EBITDA; rhode
$71M LTM) — a **6.6% pre-tax yield on the purchase price before amortisation, integration
or the earnout**, financed at 5.4% — while the legacy business's own volume fell. [E4-43]
says the *good* class passes; a 6.6% pre-tax return on $1.36bn of new capital, at a
company whose organic growth just went to 2%, is below the good class's own number
(*"~12% on retained utility capital is quite satisfactory"* [E5-40]). **Not a verdict; the
gate is closed. Recorded: good-to-gruesome on incremental capital, great on the base.**

### Staying power — all three [E5-11], with the rhode debt

- **(1) A large and reliable stream of earnings — large, not reliable.** Operating cash flow
  $212.5M and rising; but operating margin has run 10.6 / 3.0 / 7.6 / 11.8 / 14.6 / 12.0 /
  4.5% over seven years, the legacy volume line is negative, and 79% of sales go through
  retailers who owe nothing. *"Reliable"* is not the word for a 3-to-15-point margin range.
- **(2) Massive liquid assets — no.** Cash $344.2M (2026-06-30) against **$834.2M of bank
  debt** (term loan $585M amortising $30–37.5M a year; revolver $256.7M; **$744M due in a
  single year, FY2030**), floating at SOFR + 1.50–2.25% (**~5.4%, unhedged**: *"A hypothetical
  1% increase … approximately $8.4 million"*), plus **$80.8M of earnout at fair value and up
  to $200M at maximum, in cash, over the next 27 months**. Net debt plus earnout **$570M at
  fair value, $690M at the earnout maximum, against $100–150M of judged owner earnings —
  4x to 7x.** Goodwill and intangibles $1,407M exceed total equity $1,131M; **tangible
  equity is negative $276M**. Covenants: a maximum consolidated net leverage ratio (level
  not disclosed, *"increased"* in the Fifth Amendment to permit the deal) and **interest
  coverage of at least 3.50x** on EBITDA to cash interest; buybacks are gated on the leverage
  test. [E2-54]'s coverage test — interest *"comfortably met out of current cash flow net of
  ample capital expenditures"* — passes today: (OCF − capex) / cash interest = **5.1x**
  (6.3x with the seller expenses restored), and $45M of annual interest against $190M of
  cash flow after capex. Comfortable, and every dollar of it depends on strangers renewing
  $744M in 2030 [E5-39].
- **(3) No significant near-term cash requirements — FAILS.** In order: the first earnout
  tranche within 45 days of 2026-09-30 ($28.2M at fair value, more if rhode keeps beating
  its targets); $30M of term-loan amortisation a year; ~$45M of interest; the Section 122
  10% tariff and whatever succeeds it, with refunds of $51.1M already received and
  the CBP refund process and the administration's appeal both open; RMB unhedged at
  $51M per 10%; and a $500M buyback authorisation with $350M unused that the covenants,
  not the board, will decide.
- **Leverage, named and quantified [E4-16, E3-29]:** debt/OE 5.6–8.1x on the judged range;
  debt/FY2026 GAAP operating income 11.4x; debt/Adjusted EBITDA (the covenant metric)
  2.5x. No ratio ceiling in this framework; the number is stated so the reader can judge.

### Name the specific way THIS business dies [E2-27, E3-24, E4-51, E4-40]

**Mechanism 1 — the shelf reset (the retailer's private label, or the next indie, takes the
linear feet).** The filing names it: *"Increasing shelf space allocated to our products may
be especially challenging in instances when a retailer has its own brand."* Target and
Walmart are 31% of sales and 47% of receivables. **Quantified:** if the two lose a quarter
of their e.l.f. space, revenue falls ~$127M; at a 71% gross margin that is **$90M of gross
profit**, against FY2026 operating income of $131M before the earnout charge and marketing
of $400M that cannot be cut without accelerating the loss. Operating income goes to ~$40M;
interest is $45M. **Likelihood: a real possibility** — Ulta went from 16% of sales to under
10% in two years, and the volume line has been negative for four quarters, which is the
same event in slow motion at the checkout rather than the reset.

**Mechanism 2 — the wave ends [E3-51].** Legacy units fall 5% a year at a fixed price;
the dupe-and-TikTok cohort ages out or moves on; advertising has to rise from 22% of sales
to hold share. **Quantified from filed figures:** a 5% annual legacy volume decline on
$1,343M is −$67M of sales and −$48M of gross profit a year; two years of it consumes the
whole of FY2026's pre-earnout operating income. **Likelihood: a real possibility — it is
the filed trend of the last four quarters.** [E4-40]: model the exposure, not the benign
history; the 29-quarter growth streak is the experience, the volume line is the exposure.

**Mechanism 3 — rhode without its founder, or without Sephora.** A quarter of the company
and $898M of consideration rest on a brand three years old whose founder holds shares under
a one-year lock-up (expired August 2026) and an earnout that ends in September 2028. If
rhode's growth stops at, say, $450M, the goodwill ($513M) and trademark ($276M) tests will be
run against a single reporting unit and pass anyway — but $650M of debt raised for it stays.
**Likelihood: a low-level possibility over the earnout period (the earnout is being beaten),
rising after 2028.**

**The bear case as its holders would state it [E4-51]:** *e.l.f. is a marketing company that
rents shelf from three retailers and a factory from China, whose own volume stopped growing
the day it raised prices, that has spent $1.36bn of shareholder money and debt buying the
growth it no longer generates, that pays its people on a number that deletes $87M of stock
and $58M of earnout, and whose stock is 43% of the way from its acquisition currency at
$116 to its buyback price at $55.* And the bull case, stated at Q2, is that the namesake
brand is No. 1 in units in US mass cosmetics, earns a prestige gross margin at a $7 price,
needs no tangible capital, and just bought the fastest-growing skin-care brand in the
country.

**No verdict is written. The gate above is closed.**

## Q5 — **COMPUTATION — NOT A CLEARANCE** *(Q2 is OUT; no entry language anywhere below)*

The floor first [E4-28]: honest pre-tax expectancy at this price is nowhere near 10%, and
the arithmetic is recorded so the register can see the gap.

- **The yield:** judged owner earnings **$100–150M** (FY2026 at the capex end, filed and
  with the seller expenses restored) ÷ market cap **$5,718M** = **1.7% to 2.6%**; on the
  five-year mean ($47–59M) **0.8% to 1.0%**. Sovereign **5.37%**. Every construction sits
  below the long bond.
- **What the price already assumes:** on the perpetual-growth form (g = 10% − OE/price) the
  quote needs **7.4–8.3% perpetual growth** from today's owner earnings to reach the floor;
  on a ten-year engine (then 3% terminal, discounted at the floor) it needs **15.8%** a year
  for ten years from $150M, or **21.4%** from $100M. [E4-35]: fewer than one in twenty of
  the best businesses sustain 15% for twenty years; the legacy brands just grew 2.2%.
- **What you are paid:** **−2.8 to −3.7 points** against the sovereign.
- **Value as a round-number range [E4-01, E4-44, E2-63]**, at the 10% floor: **zero
  growth ~$15–25/share; 10% for ten years ~$40–65; 15% for ten years (the fewer-than-one-
  in-twenty case) ~$60–90.** At the bare sovereign instead of the floor the same engine
  gives ~$30–50 (no growth) to ~$200–300 (15%), which is the arithmetic of a 5.37% rate
  and not a valuation. **Price $96.91: above the whole of the floor-based range unless
  15%-plus for a decade is assumed.** Windage count: zero — no margin applied, because
  no bar is chosen for a name that failed at Q2.
- **The ceiling [E2-63]:** the upside is bounded by how much shelf and how many units a
  $7 brand can add before its retailers' own labels answer; the last four quarters put a
  number on that.

## Q6 — the watch specification, in words *(no alerts armed and no PORTFOLIO row: the
file closed on the business at Q2, and a price band on a business finding is a category
error, the QLYS ruling)*

- **Thesis-breaking for the OUT** (what would reopen the file): the four flip conditions
  named at Q2 — volume positive four quarters at the post-increase price; GAAP operating
  margin ≥12% two years with advertising ≤20% of sales; a filed unit-cost or
  speed-to-market metric; Walmart+Target share stable two years.
- **Thesis-confirming:** another year of negative filed volume; a Target or Walmart shelf
  reset disclosed in the customer table; advertising above 25% of sales; a goodwill
  impairment test that cannot be run separately because there is one reporting unit.
- **Next catalyst dates:** the first rhode earnout tranche (measurement period ends
  2026-09-30, payable within 45 days); the Q2 FY2027 10-Q (~2026-11-05), which will show
  the volume line for the fifth post-increase quarter and rhode's second Sephora holiday;
  the CBP IEEPA refund process and the administration's appeal; FY2030 debt maturity.
- **The moat-downgrade question [E3-30, E4-17]:** *is this erosion an aberrational cycle
  or has the business slipped in a way that permanently reduces intrinsic value?* The
  filed answer so far is four quarters, which is too short to be permanent and too
  consistent to be noise; it is why the flip conditions are written in quarters.
- **Position size:** none; nothing held.

---
## SELF-AUDIT
- [x] Questions answered in order; the run stopped at Q2; Q3–Q5 recorded below the closed
      gate as tests, not verdicts, and headed as such
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN is on
      filed figures; Q2's PROVISIONAL applies to the L'Oréal rung and the moat class, and
      the verdict is OUT, which the framework permits to carry a provisional class)
- [x] Every UNRESEARCHED item names the artifact: none carried at a gate; two named gaps in
      the competitor row (EFTS sweep, 403; L'Oréal gross margin, the URD)
- [x] Every UNKNOWABLE item states what cannot be known: private-label share (no filer
      discloses it); the legacy brands' own gross margin post-rhode (single segment)
- [x] Step 0: filing read, accession recorded, three figures cross-checked
- [x] Owner earnings on multi-year means; eight windows and both (c) ends; (c) disclosed as
      a judgment with the filed decomposition behind it; width given in dollars and a word
- [x] Competitor row filled; class PROVISIONAL as to one rung and said so
- [x] Sovereign for the earnings currency, from the issuing authority, dated 2026-09-10
- [x] Value stated as a round-number range, and headed COMPUTATION — NOT A CLEARANCE
- [x] No bar chosen, windage zero, because no clearance
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git after Step 0, Q1, Q2 and the closed-gate sections
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the
      fold)

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **Q1 IN · Q2 OUT · Q3–Q6 not opened. FAIL at Q2, on the business, not on
  price.** A $7 brand with a prestige gross margin and no tangible capital whose filed unit
  volume turned negative the quarter it raised prices and has stayed negative for four; a
  moat rebuilt each season at 24% of sales; $1.36bn committed to two acquired brands, one
  of them a person, with an earnout that has gone from $7M to $81M and will be paid out of
  financing; and a competitor row in which the heavier-cost peer earns three times the
  operating margin. Price $96.91 against a floor-based value of roughly $15–25 with no
  growth and $60–90 only if 15% compounds for a decade.
- **Strongest single fact against this conclusion, recorded [E4-26]:** e.l.f. Cosmetics is
  the No. 1 brand by units in US mass cosmetics with 29 consecutive quarters of growth, it
  passed a 4.4%-of-sales tariff through in three quarters and its gross margin is now above
  the pre-tariff level, and the incumbents it took share from are writing off their brands
  and leaving. A business that does that to Coty and Revlon has something; the finding is
  that what it has is not the thing [E3-03] names.

