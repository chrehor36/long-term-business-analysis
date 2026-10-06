# Company Run: Newell Brands Inc. (NASDAQ: NWL), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch. Working folder: `Test Runs/_research 2026-10-06 NWL/` (every script and fetched document of this run is there).

**POSITION NOTE, declared before any verdict:** not checked. The brief's blind rule forbids opening `PORTFOLIO.md`, so
whether the operator holds NWL is unknown to this analyst.

**CONTAMINATION, declared.** (1) The session's opening git snapshot showed recent commit subjects for other v5 runs of
2026-10-05/06 (WKC, TPC and PATK closed OUT at Q2; REYN OUT at Q7; an OSIS/BCC addendum about quoting the framework's
phrase beside M2000-019) and the file names, not the contents, of three untracked 2026-10-06 runs (COLL, MD, MHO). None
was opened. The subjects show that Q2 OUT is a common close among recent small and mid caps; that is a pull toward the
same close, written down here so it can be discounted. (2) `tools/run.py` prints v4 material; only its arithmetic lines
were used (Part VII). No other `Test Runs/` file about Newell, no holding review, no RESUME STATE, no queue or reading
list, and no gap case were opened.

**Session note.** The first session stopped at its limit while fetching the Q4 earnings releases; this session resumed
from the files on disk under the same brief and blind rule. Nothing was re-decided; the run file was still the blank
template at the resume.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.48 (close 2026-10-05; `tools/run.py` aggregator quote, flagged per operator rule 5: live quote only).
- **Shares** from the latest filing's cover: 425,900,000 common, $1 par, one class (10-Q for the period ended 2026-06-30,
  filed 2026-07-31, accession `0000814453-26-000029`, cover as of 2026-07-27; `python Screens/cover_shares.py NWL`).
  Balance sheet issued count 457.3M includes treasury and is not used.
- **Market cap:** $2,334M (5.48 x 425.9M).
- **Sovereign for the earnings currency (USD):** 5.66%, 30-year par yield, US Treasury daily par yield curve, 2026-10-05
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-13, `0000814453-26-000008` (Items 1, 1A, 7, the
  statements, Footnote extracts); 10-Q Q2 2026, `0000814453-26-000029`; proxy DEF 14A filed 2026-03-26,
  `0001193125-26-126289`; 8-Ks `0001193125-25-303185` (productivity plan), `0001193125-26-051284` (2026 pay terms),
  `0001193125-26-221779` (annual meeting), `0001193125-26-328583` (new secured ABL facility),
  `0001193125-26-335521` and `0001193125-26-356986` (6.25% notes due 2031), `0001193125-26-412401` (receivables
  facility renewal); 10-Ks FY2016 `0000814453-17-000027`, FY2018 `0001193125-19-061714`, FY2022
  `0000814453-23-000026`, FY2023 `0000814453-24-000017`; the Q4 earnings releases (Ex. 99.1) for FY2016
  `0000814453-17-000004`, FY2017 `0001193125-18-047773`, FY2018 `0001193125-19-041662`, FY2019
  `0000814453-20-000047`, FY2020 `0000814453-21-000018`, FY2021 `0000814453-22-000008`, FY2022
  `0000814453-23-000016`, FY2023 `0000814453-24-000013`, FY2024 `0000814453-25-000003`, FY2025
  `0000814453-26-000004`; SEC press release 2023-210 (2023-09-29) on the settled order.
- **One figure cross-checked against the filed statement:** operating cash flow $264M / $496M / $930M and capital
  expenditures $247M / $259M / $284M for 2025 / 2024 / 2023 in the FY2025 10-K cash flow statement equal the
  `tools/run.py` lines. Year-end 2025 equity $2,391M, goodwill $3,101M, other intangibles $1,634M and long-term debt
  $4,543M on the filed balance sheet equal the run.py table.
- **`tools/run.py` arithmetic lines** (`_research.../run_py_output.txt`), extended by `calc.py` from the filed cash
  flow statements (OCF less stock pay less capital expenditures; USD millions):

  | year | OCF | SBC | capex | D&A | owner cash (capex) | owner cash (D&A) |
  |---|---|---|---|---|---|---|
  | 2019 | 1,044 | 42 | 265 | 446 | 737 | 556 |
  | 2020 | 1,432 | 41 | 259 | 357 | 1,132 | 1,034 |
  | 2021 | 884 | 52 | 289 | 325 | 543 | 507 |
  | 2022 | -272 | 12 | 312 | 296 | -596 | -580 |
  | 2023 | 930 | 50 | 284 | 334 | 596 | 546 |
  | 2024 | 496 | 74 | 259 | 323 | 163 | 99 |
  | 2025 | 264 | 68 | 247 | 311 | -51 | -115 |
  | 5-yr mean 2021-25 | | | | | **131.0** | **91.4** |
  | 7-yr mean 2019-25 | | | | | 360.6 | 292.4 |

  OCF is after cash interest (avg $297M 2021-25) and cash tax (avg $150M 2021-25). 2022 (an inventory build, OCF
  negative) and 2023 (a $673M inventory release) are abnormal working-capital years that roughly offset; 2021 was the
  pandemic sales peak. OCF also carries proceeds from factored receivables (about $395M of receivables sold and
  derecognised at 2025 year end: $270M under the customer agreement, $125M under the SPE facility; 10-K FY2025, MD&A).
- **The balance sheets, ten year-ends, read before the income account** **[M2025-032]** (run.py table, checked against
  the filed 2024-2025 balance sheet):
  - *Purchased goodwill and intangibles:* $24.3B at 2016 (goodwill $10.2B, intangibles $14.1B after Jarden) to $4.7B at
    2025. Divestitures took part (proceeds $2.1B in 2017, $1.0B in 2019, XBRL); impairments took most: $8.3B of
    goodwill and intangibles charged in 2018 alone (OI -$7,554M), $1.2B in 2019, $1.5B in 2020, then $474M, $339M,
    $345M and $340M in 2022-2025. The 2025 charge hit three tradenames; the Commercial reporting unit's fair value was
    "within 10%" of its $747M goodwill (10-K FY2025, Critical Accounting Estimates).
  - *Equity:* $11.3B (2016), $14.1B (2017, the tax-reform year), $2.4B (2025). Retained earnings +$4.6B (2017) to
    -$3.2B (2025): a decade's earnings, and more, written off.
  - *Debt:* long-term debt $11.3B (2016) to $4.5B (2025); total debt on the face $11.9B to $4.7B. Paid down by
    divestiture proceeds and the 2019-2020 cash, not by the earnings of the businesses kept. Debt is still twice the
    market value of the equity, now carries 6.25% to 8.5% coupons after the 2024-2025 downgrades (Moody's senior
    unsecured B2, 10-K FY2025), and since 2026-07-30 the revolver is an $800M asset-based facility secured by a
    first-priority lien on receivables, inventory, equipment and intellectual property (8-K `0001193125-26-328583`).
  - *Working capital:* receivables $2.7B to $1.0B and inventory $2.1B to $1.3B, both shrinking with sales; the
    receivables line is also lowered by the ~$395M factored, which is financing the balance sheet does not show as debt.
  - *Cash:* $203M at 2025, $133M of it abroad. Thin for a $7.2B seller with $333M of interest due within a year
    (contractual table, 10-K FY2025).
  - What the figures say: the 2016 price was mostly intangible, and the intangible has been written off a piece at a time
    for eight years. What they do not say: whether the remaining $4.7B of intangibles is worth its carrying value; the
    filer itself says some fair values sit close to carrying value and "future non-cash impairment charges may occur".

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content owning this "if the market closed for five years"
**[M1997-109]**, and the price says nothing of value by itself: "It just tells us prices." **[M2006-077]**. A share at $5.48,
down from $44.33 at the Jarden close (10-K FY2016), invites the reading that the fall is the bargain; the foundation says
the fall is information about price only. The analyst's habits govern this run most: "I’m looking for what’s wrong in
things" **[M2025-013]**, and the worst anchor "is always your previous conclusion" **[M2016-054]**.
**Contrary evidence, written down as found** **[M1997-127]**:
- Against the business: core sales down in seven of the eight full years 2018-2025 (table at Q2); filer's own words on
  retailer power and private label; impairments of tradenames or goodwill every year 2019-2025 ($340M to $345M in each of 2023-2025); net distribution losses in 2025.
- Against the management: the SEC's settled 2023 order on the 2016-2017 core sales figures; buybacks of $1.5B (2018,
  ~63M shares) and $325M (2022, at $25.86 and $22.01) before a dividend cut in 2023; a 2023 special award paid at 200%.
- For the business (hunted as hard): Learning and Development (Sharpie, Paper Mate, EXPO, Elmer's, Dymo, Graco, NUK)
  earned a 17.2% operating margin in 2025 and grew 5% in the first half of 2026; the filer says over half of its U.S.
  revenue is made in the U.S. or Mexico and is not subject to the 2025 tariffs; gross margin recovered from 28.9% (2023)
  to 33.8% (2025).
- Flattering items in the 2026 recovery: a ~$126M IEEPA tariff refund booked in Q2 2026 and $25M of "refinement of
  estimates related to customer programs" in first-half 2026 sales (10-Q `0000814453-26-000029`).

## THE STANDING RULE
Owning NWL equity cannot ruin a buyer who owns it unlevered and sized within his means; the rule binds the buyer's own
borrowing ("borrowed money has no place in the investor's tool kit" **[L2014-005]**) and is not breached by the target's
debt, which Q9 would weigh. The target's leverage does make permanent loss of the equity a live outcome, which the buyer
must size against "Never risk permanent loss of capital." **[L2023-005]**. Not a bar here.

---
## Q1 - CAN I UNDERSTAND IT? STOP.
- The test: "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**. The products are old and slow-moving: pens, markers, food containers, commercial cleaning
  carts, candles, slow cookers, car seats, coolers. The chemistry or design is not the question; "I understand the
  economic dynamics of the industry" is **[M2011-014]**: are there moats, is there ease of entry.
- Key variables **[M1998-044]**: unit volume (core sales) against the big retailers and private label; net price against
  resin, sourced goods and tariffs; the debt and its refinancing. Each is visible in ten years of filings and releases.
  The forecast is about "consumer behavior and threats to a business" **[M2023-030]**, not technology; the filer writes
  annual core sales guidance, so the insiders do put a forecast on paper (test 5, **[M2000-105]**).
- Doubts, written down: the doubt rule is "if you have doubts about something being into your circle of competence, it
  isn’t" **[M2002-092]**, and consumer goods sold through retailers is the field Buffett names for false understanding:
  "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**. Read as
  a holding company of parts (the Q1 CONVENTION): three segments, each a set of understandable consumer categories; no
  part that matters is opaque. The doubt is about the direction of the economics, which is Q2's question, not about
  whether they can be seen.
- **VERDICT: IN.** The economics can be pictured ten years out; what the picture shows is decided at Q2.

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**

**The volume record (test 5).** Core sales (the filer's non-GAAP organic measure; Q4 earnings releases, accessions in Step 0):

| year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| core sales | +3.7% (later the subject of the SEC order) | Q4 -1.9% (full year not located in the release read) | -5.2% | -1.9% | -1.1% | +12.5% | -3.4% | -12.1% | -3.4% | -4.6% |
| net sales $B (as later reported) | 9.2 | 11.2 | 10.2 | 9.7 | 9.4 | 10.6 | 9.5 | 8.1 | 7.6 | 7.2 |

Seven of the eight full years read from 2018 fell; the one rise was the 2021 stay-at-home year, given back by 2023. The
2026 outlook is core sales "(2%) to flat" (release `0000814453-26-000004`). Volume falling is not by itself a fail, since a declining category can still be "a very good
business" **[M2015-066]**; what decides is why it falls, below.

**Pricing power and the retailer (tests 4, 7, 8).** The filer's own words (10-K FY2025, Item 1): retailers foster "high
levels of competition among suppliers", require "suppliers to maintain or reduce product prices", and "import generic
products directly from foreign sources and [...] source and sell products under their own private label brands"; "This
environment may limit the Company’s ability to recover cost increases through pricing." Amazon is 17% and Walmart 13%
of 2025 sales. The speakers' test of a brand under retailer pressure is that "the brand has to stand for something in
the consumer’s mind" **[M2015-038]**, and where shoppers trust the retailer as much as the brand, "the value of having
the brand moves over to the retailer from the product itself" **[M2001-090]**; Buffett's own Kraft Heinz error was to
underestimate "what the retailer is" **[M2019-041]**. The positive mark, to "charge more for a product and maintain or
increase market share" **[M2000-031]**, is absent: in 2025 the filer priced against $114M of tariff cost and lost volume
in every segment and "net distribution losses" in H&CS and O&R (MD&A). That is the "prayer session before you raise
your prices a penny" **[M2005-020]**, and the opposite of the strong position that manages "to pass through increases
in raw material costs" **[M2005-017]**.

**Margins against the field, whole span (tests 6, 10).** Gross margin, from each filer's own XBRL (`peers_output.txt`;
NWL 2013-2015 is the pre-Jarden Newell Rubbermaid portfolio and 2016-2018 mixes restatement vintages, so the honest
comparison is the two ends):

| filer | early span | late span | sales trend over the span |
|---|---|---|---|
| NWL | 37.9-39.0% (2013-15) | 28.9-33.8% (2019-25) | $10.6B (2021) to $7.2B (2025) |
| CLX (Clorox) | 42.5-45.1% (2013-17) | 35.8% (2022) back to 45.2% (2025) | $5.6B to $7.1B (2013-25) |
| SPB (Spectrum) | 41.0% (2016) | 31.6-37.4% (2019-25); OM 11.0% to 4.4% | OCF negative 2022 and 2023 |
| HELE (Helen of Troy) | 40-41% | 46-48%, then OM -43.8% in FY2026 (impairments) | $2.2B (FY2022) to $1.8B (FY2026) |
| HBB (Hamilton Beach) | 24.8-26.0% (2015-16) | 20-26%; OM 4-7% throughout | $768M to $607M |
| TUP (Tupperware) | 66-68%, OM 14-16% | OM 1.8% (2022); Chapter 11 filed 2024-09-17 (8-K `0001008654-24-000068`) | $2.7B to $1.3B (2013-22) |

The one comparator that held its margin and grew through the decade is Clorox, a consumables maker of brands customers
ask for by name ("you’re probably going to get better gross of margins if they ask for you by name" **[M2023-073]**).
Newell's categories sit with the durable-housewares filers (Hamilton Beach, Spectrum, Tupperware, Helen of Troy's
recent write-down), whose record over the same years is shrinking sales, thin or collapsing operating margins, and one
bankruptcy. Newell lost five to ten points of gross margin over the span while Clorox did not.

**The attacker with money (test 3), and the low-bid test (test 8).** "if I had a hundred million dollars and I wanted to
go in and take on See’s Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
For most of Newell's sales the attacker is already inside: the retailer's private label and "generic products directly
from foreign sources" (Item 1) and "A proliferation of digitally native brands" (Item 1A). The customer for a slow cooker,
a food container, a cooler or a candle takes the low bid often enough that the filer names price as the battleground. That is the commodity mark the rows give, where "most insureds don't care
from whom they buy" **[L2004-003]**, against the See's question of whether people would choose it "in preference to other candies" **[M2017-009]**. And "we do not want
to buy into a business that has a very high labor content and that has a product that can be shipped in from abroad very
easily" **[M2007-116]**: Newell itself ships much of its line in from abroad, which is why 2025 carried $174M of cash tariff.

**Widening or narrowing (test 10), and what could destroy it (test 11).** "the number one question [...] is whether
[...] the competitive advantage have been made stronger and more durable" **[M2000-075]**. The filer's own fair-value
tests answer it for the brands: tradenames or goodwill written down in every year from 2019 to 2025, the 2025 charge
"primarily from a downward revision of the forecasted cash flows" (10-K FY2025). The newspapers "lost a notch"
**[L1995-023]**; Newell's brands have lost a notch a year. Leadership is no shield: "for every Inevitable, there are
dozens of Impostors" **[L1996-031]**.

**What stands, hunted hardest.** Learning and Development is the part with a castle on the evidence: 17.2% operating
margin in 2025, 36% in Q2 2026 (inflated by the tariff refund), growth in Writing and Baby in 2026, brands asked for by
name (Sharpie, EXPO, Paper Mate). Against it, from the same filings: Writing led the segment's 2025 decline ("soft demand
primarily in the Writing business"), the 2017 Q4 release records "a double-digit decline in Writing related to retailer
inventory destocking", and the Baby unit has "a single source of supply for products that comprise a majority of its
sales and that owns the intellectual property for many of those products" (Item 1). L&D is about 37% of sales; it
cannot be bought apart from Home and Commercial Solutions (52% of sales, operating loss $138M in 2025) and Outdoor and
Recreation (operating loss in 2024 and 2025), nor from the $4.7B of debt. The U.S. manufacturing footprint is a cost
advantage against tariffed rivals for as long as the tariffs stand, which is a policy, not a castle. Rubbermaid
Commercial Products is the other candidate, and its reporting unit is the one whose fair value sits within 10% of
carrying value.

**Routing.** The rows' boxes are "in, out, and too hard" **[M2006-013]**, and their reason for the third is ignorance: "We
don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. Here the evidence is not missing; it
runs one way, so the box is OUT, not TOO HARD (the routing of the framework's Q2): a decade of volume loss, margin loss against the one peer that
held, the filer's own description of retailer and private-label pricing pressure, and its own impairments. Price does not
reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "If you really
think a business is declining, most of the time you should avoid it." **[M2012-062]**; marginal businesses bought cheap
"are the wrong foundation" **[L2014-009]**.

- **The competitor row** (metric: gross margin and sales over the span; accession of the filer's facts in the working
  folder `peers/`): above.
- **VERDICT: OUT.** The castle is shown open on the evidence for the larger part of the business, and the part that
  stands cannot be bought apart from it.

---
## Q3 to Q10 and Q12: NOT REACHED
The file closed OUT at Q2. Nothing below is a clearance; it is recorded because the brief asks for it and because the
facts were found before the close.

### Facts found beyond the closing STOP (no verdict)
- **Q4 (accounts).** SEC press release 2023-210 (2023-09-29): the settled order finds that in 2016 and 2017 Newell and
  its then CEO "took actions that increased the company’s publicly disclosed core sales growth in ways that were out of
  step with Newell’s actual but undisclosed sales trends", "pulled sales forward into earlier quarters without adequate
  disclosure and engaged in accounting practices that were inconsistent with GAAP, while overriding its internal
  accounting controls", and that the CEO instructed staff to "scrub" accruals after learning of a projected miss;
  penalties $12.5M (company) and $110,000 (CEO), neither admitting nor denying. That is the make-the-numbers habit
  **[L2002-041]** with a second tell (reserves moved to meet a figure), which under the two-tell CONVENTION is suspicion;
  it concerns a management two CEOs ago. The current releases still feature normalized EPS and the 2026 PRSUs pay on
  "Annual Adjusted Earnings Per Share" (8-K `0001193125-26-051284`). Featuring adjusted figures is the habit of which
  the rows say it "makes us nervous" **[L2016-006]**. Restructuring charges in every year 2012-2025 ($15M to $110M; XBRL) are recurring costs, not one-time.
- **Q5/Q6 (people, money, owners).** Jarden was bought in 2016 for $18.7B including debt, $9.9B of it in Newell stock at
  $44.33 (10-K FY2016), and the purchased intangible has since been largely written off. Buybacks of about $1.5B in 2018
  and $325M in 2022 at $22-26 a share, against $5.48 today, were followed by a cut of the quarterly dividend to $0.07 in
  2023 (10-K FY2023). CEO pay: $25.5M (2023), $12.4M (2024), $12.5M (2025) in years of net losses (proxy
  `0001193125-26-126289`); a 2023 special award adopted because of "significant decline in the Company’s stock price,
  high executive retention concerns" paid out at 200% in February 2026 on "free cash flow productivity" (free cash flow
  divided by adjusted net income) and adjusted gross margin. The rows' word for pay that holds when owners lose is
  "heads I win, tails you lose" **[L1994-020]**. Directors and officers as a group own 1.64%.
- **Q9 (debt).** Debt $4.7B at 2025 year end against a $2.3B equity value; 2025 loss before tax -$301M against net
  interest $321M (pre-tax earnings before impairments, $45M, barely covers interest); cash interest paid $354M in 2025;
  rated B2; secured ABL since July 2026; $1.25B of 8.5% notes due 2028 and $750M due 2030. "you can’t talk about debt
  levels without relating it to the ability to pay debt" **[M1995-104]**; "maturities must actually be met by payment"
  **[L2010-020]**. A whole business with this debt would fail the "little or no debt" criterion.

### Q7 reporting at the owner's request: COMPUTATION - NOT A CLEARANCE
(Protocol heading written with a hyphen under the no-em-dash rule; see the last section.) All figures from `calc.py`
and `calc_output.txt`; owner cash is after every real cost (OCF less stock pay less all capex), never net income.
- **(a) VALUE RANGE** (Q7 CONVENTION: five-year mean owner cash, ten years at the growth shown, then no growth,
  discounted at the 5.66% sovereign):
  - Five-year window 2021-2025, owner cash $131.0M: no-growth end **$5.43** a share ($2,314M); shown-growth end
    **$2.66** ($1,135M), growth taken as the 2021-2025 net sales rate of -9.18% a year (CONVENTION of this run: the
    framework measures growth on aggregate owner cash, but the window's owner cash runs from +$543M to -$51M through a
    negative year, so no rate can be computed on it; sales are the nearest filed series). Top to bottom 2.0 to 1, inside
    the three-to-one width. Depreciation variant (owner cash $91.4M): $3.79 no-growth.
  - Whole-cycle variant 2019-2025 (the five-year window holds two abnormal working-capital years and the 2021 peak),
    owner cash $360.6M: **$7.33 to $14.96**. Its weakness: 2019-2020 cash includes businesses since sold and the
    working-capital release of a shrinking company.
  - Price $5.48 sits at the top of the five-year range and inside the bottom of the whole-cycle range. Under the
    convention the first would close OUT (no margin) and the second would be a pencil case, not a screamer **[M2009-005]**.
- **(b) FAIR PRICE** (central case the five-year window at no growth; the floor CONVENTION, about 10% pre-tax; pre-tax
  means owner cash plus cash taxes paid, mean $150M 2021-2025):
  - **On equity plus net debt (governing here, since the business must be valued as if it had no debt, "on an
    all-equity basis" **[L2017-004]**):** pre-tax, pre-interest owner cash $578M (adding back mean cash interest $297M)
    yields 8.5% on the $6,804M enterprise value at $5.48 (net debt $4,470M at 2025 year end). The price at which it
    yields 10%: **$3.08 a share**. Whole-cycle: $8.31.
  - On equity alone: pre-tax owner cash $281M yields 12.0% at $5.48; 10% at **$6.60**. Whole-cycle: $11.86. The gap
    between the two bases is the leverage: the equity yield is high only because the debt is large.
- **(c) CHEAP PRICE** (CONVENTION of this run: the price at which the central case yields twice the floor, 20% pre-tax,
  taken as "so obvious that you don’t have to carry it out to tenths of a percent" **[M2009-005]**): on equity plus net
  debt, **none**: at 20% the enterprise is worth $2,890M, less than the net debt, so no positive share price qualifies
  (whole-cycle also none). On equity alone, $3.30 (whole-cycle $5.93). No price makes this a screamer on the all-equity
  basis, and the file closed at Q2 before price could matter.

## Q12 (optional): NOT REACHED.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: core sales down in seven of the eight full years 2018-2025, gross
margin down from 38-39% to 29-34% while Clorox held 43-45%, the filer's own words that big retailers and private label
limit its pricing, net distribution losses in 2025, and impairments of tradenames or goodwill in every year 2019 to 2025. Price was not reached;
for the record the computation puts the value range at $2.66 to $5.43 (five-year) or $7.33 to $14.96 (whole cycle)
against $5.48, fair price $3.08 on the all-equity basis ($6.60 on equity alone), and no cheap price on the all-equity basis.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the brief forbids
      commits, so the write-early commit after each question was not made (declared).
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_ids.py` in the working folder); every filing
      fact has its accession; no number without a filing or a labelled CONVENTION.
- [x] The order was kept; Q2 closed the run; everything after it is marked NOT REACHED or COMPUTATION.
- [x] Owner cash after every real cost (stock pay and all capex deducted; D&A variant shown), never a net-income proxy;
      the sovereign from the Treasury curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, both ways, in THE FOUNDATIONS.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before finishing (result recorded in the reply; no commit made).
- Not obtained: the full-year 2017 core sales figure (only Q4 2017 located); the SEC order's full text (the press
  release was read, not the order); Tupperware's results after 2022 (no 10-K after the FY2022 one filed 2023-10-13);
  Newell's sales split by price and volume (not disclosed by the filer in the documents read); competitors' own words
  on Newell (the scuttlebutt of **[M1998-144]** is beyond public filings).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7's growth input fails when the owner-cash window crosses zero.** The convention measures shown growth on
aggregate owner cash, but 2021-2025 runs +543, -596, +596, +163, -51; no compound rate exists. I used the net sales rate
and confessed it as a CONVENTION of this run; the framework should say what to use. (2) **The five-year window and the
abnormal year.** The convention averages five years "so that no single year sets the base", but here two opposite
working-capital years (2022, 2023) and a peak year (2021) sit in the window, and the five-year and seven-year means
differ by a factor of 2.75 ($131M against $361M). The brief's whole-cycle variant was needed; the framework has none.
(3) **The floor's base under leverage.** The floor CONVENTION sets the return on the price paid without saying whether
the price is the equity or the equity plus the debt. For a company whose debt is twice its equity the
two give fair prices of $6.60 and $3.08; I governed by the all-equity basis from Q9 test 2 and **[L2017-004]**, which is
my reading, not the framework's text. (4) **The protocol's heading and the no-em-dash rule collide.** Operator rule 3
spells the heading with an em dash; the brief forbids em dashes; I wrote "COMPUTATION - NOT A CLEARANCE" with a hyphen.
(5) **Holding company by parts against Q2.** The Q1 CONVENTION reads a conglomerate by its parts, but Q2 has no
matching rule for a business with one castle-bearing part inside a larger open one, carried with shared debt. I closed
on the whole, since the part cannot be bought apart; the framework does not say so.
