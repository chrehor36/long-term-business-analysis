# Company Run — The Procter & Gamble Company (NYSE: PG) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, holding
reviews, the session-state files, the register, the prepped reading list and `tools/alerts.json` were not opened, and no
attempt was made to learn whether anyone holds or wants this name.

**CONTAMINATION, declared.** (1) The governing framework itself names "the PG reproducibility pair" and "Four specifics
the PG re-test asked for (2026-10-05, both analysts)" in Q7's CONVENTION, so I know that this name was run twice under
the v5 drafts and that those runs raised the four specifics now in the rule; I do not know their boxes, ranges or
reasoning, and I opened nothing in `Framework/v5/tests/` and no earlier PG run or research folder. (2) Commit subjects
visible at session start name other 2026-10-05 runs (none about PG). (3) The ledger itself carries rows in which the
speakers name P&G, Gillette and Duracell (for example **[M2016-080]**, **[M2009-060]**, **[M2002-051]**); they are
evidence of the v5 scope and are cited where they bear, and this is not a point-in-time run, so later rows are admitted.
(4) Training memory: I know P&G in general terms (the brands, the 2005 Gillette purchase, the Duracell exchange with
Berkshire). That memory is a prior; every fact below is from the filings cited.

Working folder: `Test Runs/_research 2026-10-06 PG/` (`fetch.py`, `h2t.py`, `series.py`, `ids.py`, `peers.py`,
`value.py` and their outputs; raw filings and text dumps under its gitignored `cache/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $145.94 (close 2026-10-05; aggregator quote via `tools/run.py`, live quote only, flagged per operator
  rule 5).
- **Shares by class** from the latest filing's cover: common stock, one undimensioned class, **2,324,433,060** as of
  2026-07-31 (Form 10-K for FY ended 2026-06-30, filed 2026-08-04, accession `0000080424-26-000103`;
  `python Screens/cover_shares.py PG`). **The charter note:** the balance sheet also carries Series A and Series B ESOP
  Convertible Class A Preferred Stock, each share "convertible at the option of the holder into one share of the
  Company's common stock", paid the common dividend, 18 million Series A and 48.642 million Series B outstanding at
  2026-06-30 (Note 8, same accession). They are in the diluted count (68.3M weighted). The value per share below is
  therefore taken on **2,391.1M common-equivalent shares** (2,324.4M + 66.6M), and owner cash is not reduced by the
  preferred dividend ($292M) since those shares are counted as converted.
- **Market cap:** 2,324.4M x $145.94 = **$339,228M** on the common; **$348,953M** with the preferred as converted.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (`python tools/sources.py`, issuing authority). Over half of sales are outside the US (10-K Item 1A), but the
  statements, the dividend and the quote are in dollars, and the XBRL unit of the cash-flow series is USD.
- **Filings read** (operator rule 4): **10-K FY2026** (filed 2026-08-04, `0000080424-26-000103`): Item 1, Item 1A,
  Item 5 (issuer purchases, dividend record), Item 7 in full (segments, market shares, restructuring, cash flow,
  liquidity, contractual commitments, critical estimates), the statements, Notes 1, 4, 7, 8 (EPS, ESOP), 10 (debt) and
  the supplier-finance note; **10-Q for the quarter to 2026-03-31** (filed 2026-04-24, `0000080424-26-000060`, the latest
  10-Q; the 10-Q for the quarter to 2026-09-30 is not yet due); **proxy DEF 14A** filed 2026-08-28
  (`0001193125-26-372211`); **8-K of 2026-07-29, Item 2.02, Exhibit 99.1** (`0000080424-26-000093`, the FY2026 results
  release, read before judging the non-GAAP habits); **8-K of 2026-07-29, Item 5.02** (`0000080424-26-000094`, the
  chairman appointment). The ten-year statement series are XBRL transcription (`series_output.txt`) of the 10-Ks filed
  2017 to 2026 (accessions in that file and in `run_py_output.txt`).
- **One figure cross-checked against the filed statement:** operating cash flow FY2026 **$19,556M**, capital
  expenditures **$4,409M**, share-based compensation **$524M** and depreciation and amortization **$3,160M** in the filed
  Consolidated Statements of Cash Flows (10-K FY2026, `0000080424-26-000103`) against `tools/run.py`'s 19,556, 4,409, 524
  and 3,160: they agree.
- **`python tools/run.py PG`, arithmetic lines only** (saved as `run_py_output.txt`). Nothing it prints as a rule, id,
  floor or verdict is used (Part VII). Its share count agrees with the cover; stock pay is not zero; "OE capex" is the
  lower of its two variants in every year shown, because capital spending has run above D&A since FY2024.

**Owner cash after every real cost** = operating cash flow less stock pay less all capital expenditures (USD millions;
stock pay is added back inside operating cash flow, so it is deducted again here as the real cost it is; interest,
taxes, pension contributions and restructuring cash are already paid inside operating cash flow):

| FY (June) | OCF | stock pay | capex | owner cash | D&A variant (OCF less stock pay less D&A) | source |
|---|---|---|---|---|---|---|
| 2022 | 16,723 | 528 | 3,156 | **13,039** | 13,388 | 10-K FY2024 `0000080424-24-000083` |
| 2023 | 16,848 | 545 | 3,062 | **13,241** | 13,589 | 10-K FY2025 `0000080424-25-000076` |
| 2024 | 19,846 | 562 | 3,322 | **15,962** | 16,388 | 10-K FY2026 `0000080424-26-000103` |
| 2025 | 17,817 | 476 | 3,773 | **13,568** | 14,494 | same |
| 2026 | 19,556 | 524 | 4,409 | **14,623** | 15,872 | same |
| **5-yr mean** | | | | **14,087** | 14,746 | |

The longer record on the same definition (XBRL transcription, `series_output.txt`; FY2017 to FY2019 include businesses
since sold): 9,018 (2017), 10,755 (2018), 11,380 (2019), 13,772 (2020), 15,044 (2021). Owner cash yield at the price:
14,087 / 348,953 = **4.0%** after corporate tax, on the as-converted count.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be content to own P&G "if the market closed for five years"
**[M1997-109]**, so the run asks what will happen to the business and not when the quotation moves. No macro forecast
enters **[M2000-094]**: the filings lead with tariffs, currencies, the Middle East and Russia (10-K Item 1A and MD&A,
`0000080424-26-000103`), and these are read only as properties of the business (its freedom to pass costs through), never
as a forecast. The margin of safety bears hardest at Q7: if the decision needs pencil and paper "it’s too close to think
about" **[M1996-084]**. Who is paid to tell you: the 10-K and the release carry a management "long-term growth
algorithm" (organic growth above market, Core EPS "mid-to-high single digits", free-cash productivity of 90% or more);
it is a projection, and projections are not consulted **[M1995-050]**; the non-GAAP Core EPS is weighed at Q4. The
analyst's habits: look for "what’s wrong" and "what you’re missing" **[M2025-013]**, and state the other side's case
**[M2016-055]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the speakers themselves, in 2016: "The packaged good
business, the Procter & Gambles and so forth of the world — General Mills — they’re all weaker than they used to be at
their peak" **[M2016-080]**; (2) FY2026 organic volume was flat for the whole company, with volume down in Grooming
(1%), Health Care (2%) and Baby, Feminine & Family Care (1%), and North American volume losses "due to competitive
activity" named in hair care, oral care, home care, baby care and family care (MD&A, `0000080424-26-000103`); (3) global
share fell in hair care (0.5 points), skin care (0.6), fabric care (0.4), grooming (0.4) and North American family care
(0.7) in FY2026 (same); (4) the company has restructured in some form in most years (an "ongoing" programme of $250 to
$500 million a year, plus Argentina and Nigeria in FY2024, plus a $1.5 to $2.0 billion two-year plan from June 2025),
and impaired the Gillette intangible by $1.3 billion in FY2024 (same).

## THE STANDING RULE
The buyer's conduct: a purchase made with the buyer's own money and no borrowing, sized so that no fall in the
quotation forces a sale, cannot put the buyer at risk of ruin; "you don’t want to put yourself in a position where you
have to sell" **[M2020-007]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. No position
is taken here; the rule is met if any purchase is unlevered, and it binds above every answer below **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
  The filing describes a maker of "daily-use products" in eleven categories (fabric care, home care, baby care, feminine care,
  family care, hair care, personal care, skin care, grooming, oral care and personal health care), sold through retailers
  in about 180 countries, five reportable segments from Fabric & Home Care (35% of sales) to Grooming (8%) (10-K FY2026
  Item 1 and MD&A, `0000080424-26-000103`).
- **The key variables and how predictable they are** **[M1998-044]**: (a) unit volume in daily-use categories, which in
  FY2022 to FY2026 moved +2%, -3%, 0%, 0%, 0% for the whole company (the "Net Sales Change Drivers" tables of the 10-Ks
  for FY2022 `0000080424-22-000064`, FY2023 `0000080424-23-000073`, FY2024 `0000080424-24-000083`, FY2025
  `0000080424-25-000076` and FY2026); (b) price, which moved +4%, +9%, +4%, +1%, +1% in the same years; (c) share against
  branded rivals and private label; (d) the cost of resins, pulp and energy, passed through or not; (e) shares
  outstanding. These are the Coca-Cola kind of variables, "unit case sales and shares outstanding" **[M1998-040]**: the
  demand for detergent, diapers, toilet paper, toothpaste and razor blades ten years out is a question about consumer
  behaviour, not about a technology **[M2017-019]**, **[M2023-030]**.
- **Do the past statements tell me the future ones?** **[M2008-033]** Largely yes: owner cash has run between $9.0B and
  $16.0B a year for ten years on the same categories (Step 0), operating margin between 22.1% and 24.3% in FY2021 to FY2026
  (`peers_output.txt`, from the filed statements), with acquisitions of only $21M, $11M and $85M in FY2024 to FY2026
  (cash flow statements, `0000080424-26-000103`); the $3.8B Thorne purchase agreed on 2026-08-04 is pending (MD&A).
- **Would the insiders write it down?** **[M2000-105]** The company does: it publishes a "long-term growth
  algorithm" and annual guidance (10-K MD&A; Exhibit 99.1 `0000080424-26-000093`). That is not a reason to rely on it
  **[M1995-050]**, but it is evidence that the industry's insiders do not regard the ten-year shape as unknowable. The
  speakers name this very company as the easier kind of judgment: "it’s much easier to come to a conclusion on something
  like Coca-Cola or Procter & Gamble" **[M2009-060]**.
- **Contrary evidence for Q1, written down** **[M1997-127]**: the 10-K says "consumer expectations and purchasing habits are
  evolving at an accelerating pace" and names digital commerce, fragmented media, AI-based search, "ease of competitive
  entry into certain categories" and "growth in hard discounter channels" (Item 1A and the MD&A's Strategic Focus); and the company calls innovation its
  "lifeblood" (MD&A), which asks whether this is a business that lives on continued invention **[M1999-075]**. I read both
  as threats to the castle, which Q2 owns (rapid change sent there by the routing of Q1), not as a forecast out of reach:
  the change named is in how the product is sold and advertised, not in whether people will wash clothes, change diapers
  or shave; and research and development is $2.1B a year against $10.2B of advertising (Note 1), so the business is not a
  pharmaceutical pipeline.
- **How far off could I be?** **[M2011-084]** The range of error is in the growth rate and the margin, not in the
  existence of the earnings: the worst years of the five-year window (FY2022 and FY2023, the cost spike) still left
  owner cash above $13.0B.
- **VERDICT: IN.** The economics ten years out are a judgment about consumer demand for daily-use goods and P&G's place in
  eleven categories, and the past statements tell the future ones well enough to judge; no doubt about the perimeter
  **[M2002-092]** arises on the filings read.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**. The castle tests, each with its filing fact:

- **The key factors and how permanent they are** **[M1995-038]**. The filing names them: brands that lead their
  categories, product performance in "daily-use product categories where performance plays a significant role in the
  consumer's choice of brands", $10.2B of advertising a year (11.7% of sales), and the scale of supply chains across about
  65 countries (10-K FY2026, Item 1, MD&A and Note 1, `0000080424-26-000103`). The shares the filing states, FY2026 against
  FY2022 (`0000080424-22-000064`; the bases are the company's own and are not always the same market definition, so they
  are read as direction only): blades and razors "more than 60%" both years; fabric care "over 35%" both years; baby care
  "more than 20%" to "more than 30%"; feminine care "over 20%" to "nearly 30%"; oral care "nearly 20%" to "nearly 30%";
  home care "nearly 25%" to "more than 30%"; hair care "more than 20%" to "about 20%"; Olay "approximately 6%" to "about
  5%"; Bounty "over 40%" to "nearly 40%"; Charmin "over 25%" both years. The reasons people buy these products (clean
  clothes, a dry baby, a close shave) are unchanged and unlikely to change in twenty years; whether they buy them from P&G
  is the question below.
- **Would it stand without the lord?** The filings tie the business to brands, categories and a "develop-from-within"
  management (Item 1), not to one person; the chief executive changed on 2026-01-01 and the chairman on 2026-08-01 (proxy
  `0001193125-26-372211`; 8-K `0000080424-26-000094`) without a change in the strategy the 10-K describes.
- **The attacker with money** **[M2011-015]**: the speakers asked it of this very franchise: "it isn’t like the world —
  the capitalist world — is unaware of the money that could be made if they could knock off Gillette. But they can’t"
  **[M2002-051]**; "why are there no new entrants into the field?" **[M2000-077]**. The filing names the attackers that
  exist: "a wide variety, and increasing number, of global and local competitors", "ease of competitive entry into certain
  categories", private label and hard discounters (Item 1A). The competitor row below shows that the funded attackers in
  the same categories (Unilever, Colgate, Kimberly-Clark, Clorox, Church & Dwight) earn less on each dollar of sales than
  P&G, which is not what an open castle looks like.
- **Pricing power and the agony before a rise** **[M2005-020]**, **[M2005-019]**: in FY2022 to FY2024 P&G raised prices
  4%, 9% and 4% (company total; Fabric & Home Care 11% and Baby, Feminine & Family Care 8% in FY2023) while unit volume
  moved +2%, -3% and 0% (sales-driver tables of the 10-Ks for FY2022, FY2023 `0000080424-23-000073` and FY2024
  `0000080424-24-000083`). Sales did not "fall off a cliff". Gross margin went 51.2% (FY2021) to 47.4% (FY2022) and back to
  51.4% (FY2024) (MD&A tables, same filings): the cost increase was passed through within two years, which is what "the
  businesses with strong competitive positions manage to pass through increases in raw material costs" describes
  **[M2005-017]**. *Contrary:* FY2025 and FY2026 pricing was +1% and +1% with flat volume, and Family Care cut price
  ("lower pricing (due to merchandising investments)", FY2026 MD&A); the FY2027 release names $1B after tax of higher
  materials, energy and transport costs (Exhibit 99.1, `0000080424-26-000093`). The next pass-through is untested.
- **Unit volume and share of mind** **[M1999-054]**, **[M1997-099]**: company volume was flat over five years (+2, -3, 0,
  0, 0), with price carrying the sales line. Volume is "the evidence that the place in the mind holds"; flat volume across
  a cost cycle in which prices rose about 18% (compounded FY2022 to FY2024) is evidence that it held, not that it widened.
- **The low-cost position** **[M2018-043]**, **[L2000-017]**: the filing claims "180 basis points of manufacturing
  productivity savings" in FY2026 and 160 basis points of SG&A productivity (MD&A). The competitor row is the better
  evidence: P&G's operating margin is the highest in the group and its owner cash per dollar of sales the highest.
- **The brand in the customer's mind; would the customer still choose it over the low bid** **[M2015-038]**,
  **[M2023-073]**, **[M2017-009]**: P&G sells through retailers, and Walmart alone is about 16% of sales, the top ten
  customers 43% (Item 1). That is the Kraft Heinz exposure the speakers misjudged: "we did underestimate [...] what the
  retailer is. [...] the brand is our protection against the intermediaries making all the money" **[M2019-041]**; "to the
  extent that people trust Costco or Walmart more than [...] they trust the brand, then the value of having the brand moves
  over to the retailer" **[M2001-090]**. The evidence that the brand still protects: prices up about 18% over three
  years without volume loss, and margins held at the top of the group. The evidence against: the 10-K's own risk factor on
  "increased offerings of other branded manufacturers, private label brands and generic non-branded products" and
  North American volume losses "due to competitive activity" in five categories in FY2026.
- **Does it travel?** **[M1997-068]**: sold in about 180 countries; more than half of sales outside the US; Greater China,
  UK, Canada, Japan and Germany together 21% (MD&A). It travels.
- **Ask the competitors** **[M1999-130]**: not done from the competitors' mouths (no interview; the competitors' own 10-Ks
  were read only for the metric row). Recorded as a gap, not a finding.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: by the share statements, widening in oral, home, baby and
  feminine care and narrowing slightly in hair, skin and paper towels; FY2026 alone shows global share down in hair (0.5),
  skin (0.6), fabric (0.4), grooming (0.4) and North American family care (0.7), and up in personal care (0.2), personal
  health care (0.5), home care (0.3) and baby care (0.3) (FY2026 MD&A). The speakers' own read, from 2016: "The packaged
  good business, the Procter & Gambles and so forth of the world [...] they’re all weaker than they used to be at their
  peak" **[M2016-080]**. A notch, in their word; not a breach.
- **What could destroy, modify or reduce it** **[M2000-014]**: (a) the retailer taking the brand's margin (above);
  (b) "evolving and more fragmented digital marketing and selling platform requirements", AI-based search and social
  commerce changing how a brand reaches the customer (Item 1A, MD&A), which could erode the advantage of the largest
  advertiser; (c) the slow kind of change that "can lull you to sleep easier" **[M2014-038]**. Would the business be
  started today against its substitutes? Yes: people still need the products and nothing substitutes for them; the
  question is the price they will pay for the brand, not whether the category exists.

**The competitor row**, from the competitors' own filings (XBRL company facts of each filer's 10-K or 20-F; transcription,
`peers_output.txt`; the latest annual accession for each: PG `0000080424-26-000103`, Colgate-Palmolive
`0000021665-26-000006`, Kimberly-Clark `0001628280-26-007567`, Clorox `0000021076-25-000039`, Church & Dwight
`0001193125-26-048139`, Unilever 20-F `0000217410-26-000007`). Five-year means; owner cash = operating cash flow less
stock pay less capital spending:

| company (fiscal years) | operating margin | owner cash / sales |
|---|---|---|
| **P&G** (FY2022 to FY2026, June) | **22.7%** | **16.9%** |
| Colgate-Palmolive (2021 to 2025) | 18.6% | 14.8% |
| Unilever (2021 to 2025, EUR, IFRS) | 17.3% | 13.2% |
| Church & Dwight (2021 to 2025) | 16.1% | 14.7% |
| Kimberly-Clark (2021 to 2025) | 13.6% | 11.1% |
| Clorox (FY2021 to FY2025, June; pre-tax margin, no operating line tagged) | 9.0% | 9.2% |

P&G is the largest and the most profitable, and the least variable: its operating margin ranged 22.1% to 24.3%, against
Colgate 16.1% to 21.2%, Church & Dwight 11.1% to 20.8% and Clorox (pre-tax) 3.2% to 15.2% over the same years.

- **A castle shown open on the evidence closes OUT; a castle whose future cannot be judged closes TOO HARD.** Neither is
  shown. The castle is not shown open: no attacker has taken a category, prices were passed through, and margins lead the
  group. Its future can be judged: the threats named are real but slow, and they act on the price of the brand, not on
  the demand for the product. The speakers' own 2016 verdict, "weaker than they used to be at their peak" **[M2016-080]**,
  is weighed, and it is the same speaker's next clause that governs a business still strong: "we can’t change [...] every
  time something is a little less advantaged than it used to be" (same row).
- **VERDICT: IN**, narrowly as to widening: a castle standing on brands, scale and the low-cost position in a commodity-like
  field **[L2004-007]**, with the retailer and the media shift as the named threats, carried to Q7 as the reason the growth
  input is not raised above what the business has shown.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]**. At 2026-06-30
  (balance sheet, 10-K FY2026 `0000080424-26-000103`): property, plant and equipment $25,360M; receivables $6,056M,
  inventories $8,170M and prepaid $2,040M, against payables $16,306M and accrued liabilities $11,091M, so operating working
  capital is **negative $11,131M**; net tangible operating capital about **$14,229M** (about $26,460M if all $12,231M of
  "other noncurrent assets" are counted as operating). Operating income FY2026 $19,748M pre-tax: **about 75% to 139%
  pre-tax** on the tangible capital the business needs. With the purchased goodwill and intangibles ($62,720M, mostly the
  2005 Gillette purchase) put back, as the speakers do when judging the capital allocation "because we paid for it"
  **[M2011-060]**, about **22% pre-tax** on $89.2B. The high tangible return is not made by "a cyclical peak in earnings, a
  monopolistic position, or leverage" **[L1994-009]**: margins were steady through the cost cycle (Q2), shares are high but
  not monopolies, and the tangible return is computed before debt. Part of the negative working capital is supplier credit:
  payables rose from $9,632M (FY2017) to $16,306M (FY2026), 14.8% to 18.7% of sales, and the 10-K describes a supply-chain
  finance programme with supplier payment terms of "60 to 180 days" (supplier-finance note). That is cheap capital lent
  by suppliers; it is weighed again at Q9.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Depreciation and amortization ran $2,714M
  to $3,160M in FY2022 to FY2026 and capital spending $3,062M to $4,409M; the filing does not split maintenance from growth
  (it calls adjusted free cash flow "the cash that the Company is able to generate after taking into account planned
  maintenance and asset expansion", MD&A). The step-up from $3,322M (FY2024) to $4,409M (FY2026) sits mostly in Baby,
  Feminine & Family Care ($979M to $1,520M against D&A of $835M) and Fabric & Home Care ($1,076M to $1,250M against $756M)
  (segment note), and the FY2027 guidance is 4.5% to 5.5% of sales (Exhibit 99.1 `0000080424-26-000093`). My judgment,
  stated as a guess: maintenance is near depreciation, "not inappropriate in most companies to use as a proxy"
  **[M1998-127]**; the excess is capacity and productivity spending whose return is not yet shown. The owner-cash figure in
  Step 0 deducts **all** capital spending, so the guess does not raise the value; the D&A variant is shown beside it.
- **The growth arithmetic and its caps** **[M2001-019]**, **[M1999-067]**. Sales rose from $76,118M (FY2021) to $87,032M
  (FY2026), about 2.7% a year, of which the 10-Ks attribute almost all to price (Q2), and acquisitions were negligible.
  Owner cash grew 5.5% a year from FY2017 ($9,018M) to FY2026 ($14,623M), but only 2.9% a year across the five-year window
  (FY2022 $13,039M to FY2026 $14,623M) and was lower in FY2026 than in FY2021 ($15,044M). Earnings per share grew faster
  than earnings because shares fell (diluted 2,740M FY2017 to 2,423M FY2026, `series_output.txt`), but that is the
  owners' own money returned, not a return on capital added: "we just put way more capital into the business" is the
  opposite case **[M2023-081]**, and here very little capital was put in. The surplus cannot be redeployed inside the
  business at anything like the tangible return; the speakers said exactly this of the razor business: "There’s no way
  they can deploy the money they make in the razor and blade business to keep putting more money in that kind of
  business" **[M2003-123]**.
- **The grade.** This is the first of the 1998 grades in its capital need, "gives you more and more money every year
  without putting up anything to get it, or very little" **[M1998-081]**, with the qualification that over the last five
  years the "more and more" has been slow (2.9% a year) and carried by price rather than volume.
- **WEIGHS FOR.** Little capital goes in, the capital that is in earns a very high tangible return, and the business does
  not need the owners' money to stand still **[M1998-081]**, **[M2014-007]**; against it, the growth the capital buys is
  small, and the capital step-up of FY2025 to FY2026 has not yet shown what it earns. (The "little or no debt" criterion
  is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (`run_py_output.txt`, first-filed
  XBRL vintage of each 10-K, FY2017 `0000080424-17-000047` to FY2026 `0000080424-26-000103`; the FY2026 and FY2025 columns
  read against the filed balance sheet in the FY2026 10-K, and they agree). What moved, and why:
  - **Equity against goodwill and intangibles.** Equity was $55,778M in FY2017 and $54,311M in FY2026, flat, while retained
    earnings rose from $96,124M to $135,852M: the earnings kept in the books were paid out through the treasury, which now
    stands at $143,008M at cost (FY2026 balance sheet). Goodwill and intangibles were $68,886M in FY2017 and $62,720M in
    FY2026, 57% and 50% of total assets; tangible equity is negative ($54,311M less $62,720M). The step down came in
    FY2019 (goodwill $45,175M to $40,273M): an $8.3B pre-tax "Shave Care impairment" of goodwill and the Gillette
    intangible, explained in the FY2019 10-K (`0000080424-19-000050`) as due "in large part to significant currency
    devaluations [...], a deceleration of category growth caused by changing grooming habits, primarily in the developed
    markets, and an increased competitive market environment in the U.S.", and a further $1.3B on the Gillette intangible in
    FY2024 (FY2026 10-K, MD&A). **Contrary evidence for Q2, written down when found** **[M1997-127]**: this is the castle the
    speakers called impossible to knock off **[M2002-051]**, and the company itself wrote down what it paid for it twice;
    the blades share is still stated as "more than 60%" (Q2), so the write-down records a smaller, slower franchise than was
    bought in 2005, not a breached one. It does not reopen Q2, and it is carried to Q6 as a capital-allocation fact.
  - **Cash:** $5,569M (FY2017) to $9,942M (FY2026), of which $8.9B sits in foreign subsidiaries, with no material amount in
    countries with exchange controls and no expected repatriation tax (MD&A, Liquidity) **[L2016-009]**.
  - **Receivables against sales:** $4,594M on $65,058M of sales (7.1%) in FY2017; $6,056M on $87,032M (7.0%) in FY2026.
    Steady.
  - **Inventory against sales:** $4,624M (7.1% of sales) in FY2017; $8,170M (9.4%) in FY2026; days on hand up two days in
    FY2026, "driven primarily by increased safety stock levels and new product initiatives" (MD&A). A slow build, explained;
    watched, not a tell on its own **[M1995-064]**.
  - **Payables:** $9,632M (14.8% of sales) to $16,306M (18.7%): supplier credit stretched under a supply-chain finance
    programme (Q3). Part of the operating cash flow of the decade is this stretch, about $6.7B over nine years; in the
    five-year window it added about $1.4B (FY2022 $14,882M to FY2026 $16,306M), small against $70.4B of owner cash.
  - **Debt:** $31,592M (FY2017, partial tag) to $34,734M (FY2026) on the face of the balance sheet; against owner cash it
    fell from about 3.5 years to 2.4 years. Weighed at Q9.
  - **What the figures cannot say:** whether the $62.7B of purchased goodwill and brands will earn its cost; the FY2019 and
    FY2024 write-downs say part of it did not.
- **The real costs.** Depreciation is a real cost **[R1996-023]**, **[L2015-004]**, and the owner-cash figure deducts all
  capital spending, more than depreciation. Stock pay ($476M to $562M a year) is deducted **[L2015-003]**, **[L2021-003]**.
  Restructuring recurs: the company states an "ongoing level of restructuring activities of approximately $250 - $500
  million before tax" every year, plus $1.2B after tax in the limited-market programme (FY2024 to the first quarter of
  FY2025, Argentina and Nigeria), plus $903M after tax in FY2026 under a two-year plan with the rest in FY2027 (10-K MD&A
  and Note 3). These are costs "that should properly be attributed to a number of years" **[L1998-031]**, and "we do not ask
  you to forget about those costs" **[M1999-023]**: about 67% of the FY2026 charges are cash, and that cash is inside
  operating cash flow, so owner cash already bears them. Pensions: funded status of the pension plans is $(296)M and of the
  other retiree plans $3,432M at 2026-06-30, minimum pension funding $573M over three years (Notes; contractual commitments);
  not a hidden cost of size **[M2003-110]**.
- **EBITDA in the filer's own mouth:** no instance found (text search of the FY2026 10-K, the FY2026 results release, the
  Q3 FY2026 10-Q and the proxy for "EBITDA": zero). **[M2002-026]** does not bite.
- **Adjusted earnings.** The company features "Core EPS" beside GAAP EPS; the release headline gives GAAP diluted EPS
  ($6.62, +2%) first and Core ($6.89, +1%) beside it (Exhibit 99.1). Core excludes only the restructuring above the stated
  ongoing level and the $261M Glad gain, and the difference is $0.27 a share (10-K reconciliation); the exclusion has now
  recurred in FY2024, FY2025 (the Argentina tail), FY2026 and the FY2027 guidance ($0.13 to $0.17 a share), so "non-core"
  restructuring is in practice a recurring cost, and Core is the figure on which management is paid (10-K: "also used in
  assessing the achievement of management goals for at-risk compensation"). "a management that regularly attempts to wave
  away very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**: this weighs against,
  mildly, because GAAP leads and the gap is small; it is not confusion.
- **The make-the-numbers habit.** Guidance is given every year (FY2027: organic sales 1% to 3%, Core EPS "in-line to three
  percent", capital spending, free-cash productivity, buyback and dividend sums; Exhibit 99.1), and the proxy records that
  "The Company met its going-in guidance ranges" for FY2026 and sets pay targets at the guidance midpoints (DEF 14A,
  `0001193125-26-372211`). A pattern of consistently reaching declared targets **[L2002-041]** is not shown by one year
  inside a 0% to 4% range; and no second tell from the list (reserves that move, prepaid or deferred accounts building,
  profits on both sides of a contract) was found in the statements read. Under the two-tell CONVENTION it is a weighing
  against, not a STOP.
- **What the accounts say of management's character:** clear statements, GAAP first, the write-downs taken and explained,
  the restructuring quantified in advance **[M1994-018]**.
- **VERDICT on confusion: IN** (the accounts are clear, the cash and the income agree: adjusted free cash flow of 100% of
  earnings in FY2026 and 87% in FY2025, MD&A). **WEIGHS slightly AGAINST** otherwise: recurring "non-core" restructuring,
  pay on Core EPS, and the annual guidance. The recast earnings fed to Q7 are owner cash after all capital spending, stock
  pay and the cash restructuring, five-year mean **$14,087M** (Step 0) **[M2012-034]**, **[L2021-003]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the yardsticks and the reading tests carry the
weight here, and the after-the-sale test does not apply.
- **The two yardsticks** **[M1994-008]**. *How well they run the business, against the hand dealt:* the hand is a set of
  leading brands in slow categories; against the same hand dealt to Unilever, Colgate, Kimberly-Clark, Clorox and Church &
  Dwight, P&G earned the highest and steadiest operating margin and the most owner cash per dollar of sales over five years
  (Q2 competitor row), and passed through a cost spike in two years (Q2). Against that, organic volume was flat for five
  years and share fell in five categories in FY2026 (Foundations). *How they treat the owners:* the business has returned
  more than its owner cash every year of the window (dividends $10,232M plus buybacks $5,028M in FY2026 against owner cash
  of $14,623M; cash flow statement, `0000080424-26-000103`), and the share count has fallen (Q3). The two travel together
  here as the row says they usually do **[M1994-009]**.
- **The people.** Shailesh Jejurikar, chief executive from 2026-01-01 and chairman from 2026-08-01, "joined P&G in 1989"
  and ran Fabric and Home Care among other businesses; Jon Moeller, his predecessor, served 38 years (8-K Exhibit 99.1,
  `0000080424-26-000094`). The company states a "develop-from-within model for staffing most of our senior leadership
  positions" (10-K Item 1). Careers spent inside one company are the nearest public evidence of loving the business rather
  than the money **[M2000-098]**; they are not proof of it.
- **The tells of dishonesty, read for** (the proxy, the 10-K, the release):
  - *Reports that dance* **[M1995-111]**: none found. The industry's key figures (volume, price, mix, foreign exchange,
    share by category, including share losses) are reported segment by segment every year, and the bad ones are named
    ("due to competitive activity", "market contraction") (10-K MD&A).
  - *Numbers obscured on purpose* **[M2003-029]**: none found (Q4).
  - *Fixed on the stock price* **[M2004-067]**: the pay plan's relative-TSR multiplier and business-unit "Operating TSR"
    point the managers at shareholder return (proxy), weighed at Q6 Part B; nothing beyond that found.
  - *Serial issuance* **[L2014-015]**: the reverse; shares outstanding fell every year of the window (Q3).
  - *How they talk about mistakes* **[L2024-003]**: the FY2019 and FY2024 Gillette write-downs were taken and explained in
    plain words, with "an increased competitive market environment" named among the causes (Q4); the FY2026 release calls
    the year "foundation building" and does not use the word mistake. Neither a confession nor a dodge.
  - *The letter's voice* **[M2007-083]**, **[M1998-038]**: the 10-K's strategy text ("irresistible superiority", "constructive
    disruption", "five key vectors") is the standardized jargon the speakers call a turnoff **[M1998-038]**. It weighs
    against, slightly; it is not dishonesty.
- **Integrity, applied on doubt** **[M2013-088]**: no doubt arises on the documents read. No tell found beyond the jargon,
  which goes to ability and candour of style, not to honesty.
- **Ability, weighed** **[M1999-104]**: the business ranks above the manager here, "The really great business is one that
  doesn’t require good management" **[M1996-037]**, and "there are some businesses so good that they’ll easily stand a lot
  of folly in the managerial suite" **[M1995-110]**. The new chief executive has no record as chief executive yet (six
  months). The succession was internal and orderly (proxy; 8-K), which answers the succession question for now
  **[L2011-001]**.
- **VERDICT on integrity: IN. Ability WEIGHS FOR**, modestly: a record of margin and cash leadership against the same hand
  dealt to rivals, offset by five flat volume years and a new, untried chief executive.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[M1998-033]**, **[R1995-009]**: almost nothing is retained. In FY2022 to FY2026 the company paid
  $47,185M of dividends and $33,890M of buybacks (cash flow statements; `series_output.txt`) against $70,433M of owner cash
  (Step 0); debt was about flat. The business cannot use its surplus internally at its own high return (Q3, **[M2003-123]**),
  and paying it out is what the rows prescribe for such a business: "a company that expects to regularly earn more than it
  can profitably employ in its business, should be paying out dividends" **[M2004-089]**. The dividend has been paid 136
  years and raised 70, at a stated discretion that reviews "dividend yields, profitability and cash flow expectations and
  financing needs" (10-K Item 5): "clear, consistent and rational" **[L2012-015]**. This half weighs FOR.
- **Buybacks** **[L1999-023]**, **[L2011-003]**: a fixed sum each year, "approximately $5 billion in fiscal year 2026",
  "financed through a combination of operating cash flows and issuance of debt" (10-K Item 5), and "approximately $5
  billion" again for FY2027 (Exhibit 99.1); no price is named above which the buying stops **[L2016-002]**. The average
  prices paid, from the statements of shareholders' equity (10-K FY2026): **$157.29** (FY2024, 31.877M shares for
  $5,014M), **$169.04** (FY2025, 38.552M for $6,517M), **$150.40** (FY2026, 33.437M for $5,029M); the last quarter
  averaged $147.46 (Item 5). Under the CONVENTION, a buyback with no stated price weighs against unless the prices paid sit
  at or below the bottom of the Q7 range; the test is run at Q7 and recorded here. **Recorded after Q7:** the range is
  $104 to $131 a share, and every year's average price paid ($157, $169, $150) sits **above the top** of it, not at or
  below the bottom; "If you’re repurchasing shares above a rationally calculated intrinsic value, you are harming your
  shareholders" **[M1996-013]**. The buyback **weighs AGAINST**.
  The Core EPS growth on which management is paid (Part B) rises with any buyback at any price, which is the incentive the
  rows warn of: "dilution by itself is a negative and buying back your stock at too high a price is another negative. So
  it has to be related to valuation" **[M2016-049]**.
- **Issuance and deals** **[L2014-012]**: no share issuance beyond employee plans; no all-stock deal in the window, so the
  one STOP of Part A **[L2009-019]** does not arise. The large deal of record is Gillette (2005), on whose purchased
  goodwill and brand $8.3B (FY2019) and $1.3B (FY2024) were written off (Q4); Buffett sat on Gillette's board **[M2018-033]** and
  the 2005 letter said of Gillette's earlier Duracell purchase that "what Gillette received in business value in this acquisition was not
  equivalent to what it gave up" **[L2005-012]**. That is history, not this management. The pending purchase is Thorne,
  "a premium wellness and supplement brand", for $3.8B in cash (10-K MD&A), about a quarter of one year's owner cash; its
  value given against value got cannot be judged from the filing, which states only the price.
- **Part A WEIGHS AGAINST** (settled after Q7): the payout is right in kind and the dividend weighs for, but about two-fifths
  of the cash returned in the window, $33.9B of $81.1B, bought stock above the top of the value range at a fixed sum with no price
  named, part of it financed with debt.

**Part B: the pay, the board and the owners** (proxy DEF 14A, `0001193125-26-372211`).
- **Pay tied to what the person controls** **[M2003-019]**: the annual bonus (STAR) is 70% business-unit results on six
  measures, organic sales growth, operating profit growth, free-cash productivity, **value share**, an "Operating TSR" and
  internal controls, and 30% total-company organic sales and Core EPS against targets set at the midpoint of the published
  guidance. The unit measures are mostly within the manager's reach, and value share is the moat measured **[M2010-030]**.
  The long-term plan (PSP) pays on three-year relative organic sales growth, Core EPS growth, constant-currency core
  operating profit growth and free-cash productivity, multiplied by three-year **relative total shareholder return**. The
  TSR multiplier is a stock-price "lottery ticket" whose value "is totally out of the control of the person whose behavior
  we would like to affect" **[L1996-018]**; Core EPS rewards buybacks at any price (above) and excludes the recurring
  "non-core" restructuring (Q4).
- **Options** **[L1994-021]**, **[M1997-043]**: half of the long-term grant is stock options and RSUs (the CEO's FY2026
  award: $14.0M long-term, half PSP, half options and RSUs); options at a fixed strike with no step-up for retained
  earnings, the "royalty on money that you left with me". The dividend conflict of a fixed-price option **[M2003-018]**,
  **[L2005-014]**: no instance found in the proxy read of the plan's being described in those terms.
- **The sums.** Chief executive total for FY2026 $18,976,742 (summary compensation table), against $15.3B returned to
  owners; "any compensation sins are generally of minor importance compared to the sin of having somebody that’s mediocre
  running a huge company" **[M2007-006]**. Targets are set by peer-group median through an outside consultant (Meridian)
  **[L2005-015]**, **[M2004-016]**.
- **The board** **[L2014-026]**: from 2026-08-01 the chief executive is also chairman, with an independent lead director
  in place since 2021 (8-K `0000080424-26-000094`; proxy). The independent directors are paid a $120,000 retainer and a
  $220,000 grant of RSUs a year, must hold six times the retainer, and most of them hold **only granted RSUs and no shares
  bought** (beneficial ownership table: for several independent directors the only entry is RSUs) **[L2019-008]**,
  **[L2002-033]**.
- **The owners as partners.** Annual earnings guidance with pay keyed to it ("we don’t give out earnings guidance. We
  think it’s silly" is Berkshire's rule, applied by inversion **[M2022-054]**, **[L2019-006]**); a compensation discussion
  that runs from page 37 to page 88 of the proxy (its own page references) **[M2009-087]**.
- **Part B WEIGHS AGAINST**, mildly: pay partly on stock-price and per-share figures that buybacks lift, options without
  a step-up, a combined chair, directors owning grants rather than purchases, and guidance; against it, unit pay on
  controllable measures including share, and sums small against the owners' cash.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[R1996-018]**, as a range
**[L2000-024]**. Construction by the CONVENTION (Q7, with the four PG specifics); arithmetic in `value.py`, output in
`value_output.txt`. *(The arithmetic was first computed while Q2 to Q4 were open, headed "COMPUTATION - NOT A CLEARANCE"
in the script (operator rule 3); it entered this file only now, with Q1 to Q4 IN.)*

- **Cash input:** five-year mean of owner cash after every real cost, **$14,087M** (Step 0; all capital spending deducted;
  the D&A variant is $14,746M). Interest is paid inside operating cash flow, so this is cash to the equity; the ESOP
  preferred is counted as converted (2,391.1M shares) and its dividend is therefore not deducted.
- **Growth shown**, on aggregate owner cash (not per share, the first specific): FY2022 $13,039M to FY2026 $14,623M,
  **2.9% a year**. **Capped by Q3**: it is below the discount rate and traces to no absurdity **[M1997-095]**,
  **[M1999-067]**; it is consistent with what the business shows elsewhere (sales about 2.7% a year FY2021 to FY2026, nearly
  all price; volume flat). The base year is not a poor one picked for effect **[L2005-003]**: FY2022 was the cost-squeeze
  year, and FY2021 ($15,044M) was higher than FY2026, so a window ending at FY2021's level would show less growth, not
  more. The ten-year record (FY2017 $9,018M to FY2026, 5.5% a year, with businesses sold in the early years) is shown as a
  sensitivity only; the CONVENTION carries the growth "the business has actually shown over those years", and the five
  years show 2.9%.
- **Ten years, then no real growth** (zero nominal, the third specific), discounted throughout at **5.66%**.
- **Thorne** ($3.8B cash, pending): not in the owner-cash figures; at no return it would cost $1.59 a share, at a fair
  return about nothing. It does not move the box and is not adjusted.

| case | value, $M | per share (2,391.1M) | expected return at $145.94, after tax |
|---|---|---|---|
| no growth (bottom) | 248,880 | **$104.09** | 4.04% |
| central, 1.45% for ten years | | $116.78 | 4.55% |
| 2.91% for ten years (top, shown growth) | 313,328 | **$131.04** | 5.11% |
| D&A variant, no growth to 2.91% | 260,534 to 328,000 | $108.96 to $137.18 | 4.23% to 5.33% |
| sensitivity: 5.52% (the ten-year record) | 385,374 | $161.17 | 6.20% |
| what the price implies at 5.66% | | $145.94 | 4.27% growth for ten years |

- **Value range: $104 to $131 a share against $145.94.** Width about 1.26 to 1, far inside the three-to-one CONVENTION, so
  the range is narrow enough to conclude from **[L2000-025]**; it is narrow because the business is steady, which is the
  one thing a great castle gives the valuer **[M1999-104]**.
- **The price against the range.** The price is **above the top**. The expected return on owner cash at the price is
  **4.0% to 5.1% a year after corporate tax** (no growth to the shown growth). Converted at P&G's own effective tax rate of
  20.8% (10-K FY2026 MD&A, Income Taxes), the CONVENTION floor of about 10% pre-tax **[L2002-020]**, **[M2003-149]** is
  **7.9% after tax**, and the expected return at the price is **about 5.1% to 6.5% pre-tax**. Even the ten-year record's
  5.5% growth gives 6.2% after tax (about 7.8% pre-tax). To return the floor at this price, owner cash would have to grow
  about **9.1% a year for ten years**, three times what it has shown and more than three times what sales have shown.
  Under the fourth specific, a price above the top of the range closes OUT through the floor: "there’s just a point at
  which we drop out of the game" **[M2003-149]**.
- **The other side's case, stated** **[M2016-055]**: a wonderful business "at a fair price" is worth more than a fair
  business at a wonderful price **[M2003-040]**, and the speakers counted refusing to pay up for the outstanding business
  as their costliest category **[M1997-083]**; "you probably should stretch a little" for the business that can reinvest
  at high returns **[M2013-059]**. But this business cannot reinvest its surplus at high returns (Q3), and the stretch here
  is not a little: the price sits 11% above the top of the range and 40% above its bottom, at a return below the long
  bond. "You can turn any investment into a bad deal by paying too much" **[M2019-015]**.

**Reported at the owner's request (not a rule change; COMPUTATION — NOT A CLEARANCE, since the file closes at this STOP):**
- **Value range:** $104 to $131 a share (D&A variant $109 to $137).
- **Fair price** (the price at which the central case, 1.45% growth for ten years, returns the floor of 7.9% after tax,
  about 10% pre-tax): **about $83**. At the top case (2.9% growth) the floor is met at **about $92**. No price inside the
  range ($104 to $131) meets the floor even in the top case, so the fair-price band lies wholly below the range.
- **Cheap price** (owner cash with **no growth at all** returns the floor; below it the case "ought to just kind of scream"
  **[M1996-084]**): **about $74**. The price is about 2.0 times the cheap price and 1.8 times the fair price.

- **VERDICT: OUT.** Valued, with a narrow range, and the price above its top: the expected return at the price (about 5%
  to 6.5% pre-tax) is below the floor of about ten percent **[M2003-149]**, **[L2002-020]**, and nowhere near a price that
  would "scream" **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- **NOT REACHED as a clearance** (the file closed OUT at Q7). Recorded for the record only: the 30-year Treasury at 5.66%
  beats the 4.0% to 5.1% after-tax expected return on owner cash at the price in every case of the range; only the
  ten-year-record sensitivity (6.2% after tax) clears it, by about half a point, which "wouldn’t tempt you"
  **[M2007-099]**. The name would be "taken out of the filter" by the bond **[M1997-089]**. The ranking against holdings was not done
  (blind rule).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- **NOT REACHED** (closed at Q7). Facts gathered on the way, for the record, not weighed: total debt $34,490M, of which
  **$11,357M is due within one year** (largely commercial paper), backed by $8.0B of undrawn bank facilities "without
  cross-default or ratings triggers", ratings Aa3 / AA- stable (10-K FY2026 MD&A, Liquidity and Contractual Commitments);
  current liabilities exceed current assets by $12.5B; pre-tax earnings plus interest over interest, the speakers' coverage
  measure **[L2012-002]**, about 24 times in FY2026 ($20,377M + $877M over $877M); supplier finance with terms of 60 to 180
  days (Q3). The short maturities of size are the item a Q9 reading would weigh first against **[L2014-023]** and
  **[L2010-020]**.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- **NOT REACHED.** What the draft would have the buyer do: nothing. Inaction is the default **[M1996-006]**; "You wait for
  the fat pitch" **[M2003-070]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- **NOT REACHED** (not asked by the operator; the file closed at Q7). For the record: detergents, diapers, razors and
  toothpaste are none of the named businesses **[M2008-011]**.

---
## THE BOX
**OUT, at Q7.** Q1 IN, Q2 IN (a standing castle, narrowly as to widening), Q3 weighs for, Q4 IN on confusion and weighs
slightly against, Q5 IN on integrity, Q6 weighs against (buybacks above value, pay on per-share and stock-price measures);
the value range is **$104 to $131 a share against $145.94**, the price above the top, the expected return about 5% to 6.5%
pre-tax against the floor of about ten. Fair price (COMPUTATION) about **$83** (about $92 in the top case); cheap price
(COMPUTATION) about **$74**. **What would reverse it:** a price at or below about $83 (central case) to $92 (top case) with
the castle unchanged, or owner cash shown growing near 9% a year, which nothing in the filings suggests.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      template copy and the research folder were made before the first tool ran; commits: Step 0, Q1, Q2, Q3, Q4, Q5, Q6,
      Q7, close.
- [x] Every v5 id resolves (`ids.py --file` over this run file: none missing); every filing fact has its accession; no
      number without a row or a filing; the XBRL-transcribed series are marked as transcription.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED and their notes are
      record, not clearance. One disclosure: `value.py` was written and run while Q2 to Q4 were open; its header says
      "COMPUTATION - NOT A CLEARANCE" (operator rule 3), it was committed with the Q1 commit, and its figures entered this
      file only at Q7. A partial order breach in Q6 follows the CONVENTION: the buyback test needs the Q7 range and was
      recorded back at Q6 after Q7.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash flow less stock pay
      less all capital spending, cross-checked to the filed FY2026 cash flow statement; the sovereign from the US Treasury,
      dated; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: in the Foundations, in Q1, in Q2 (pricing,
      retailer, share losses, **[M2016-080]**), and at Q4 (the Gillette write-downs, found there and carried back to Q2).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; rows of every
      year admitted.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The growth input's endpoints are not fixed.** The Q7 CONVENTION carries "the growth the business has actually shown
over those years" but does not say how it is measured: end-point to end-point inside the five-year window gives 2.9%
(FY2022 to FY2026), FY2021 to FY2026 gives a decline, and the ten-year record gives 5.5%; I used the window's end points and
showed the ten-year rate as a sensitivity. Here the box does not move (all three cases are OUT), but for a name nearer the
line the choice decides it. (2) **Convertible preferred.** The template says to read the charter note before adding
classes but not what to do with a convertible preferred paid the common dividend; I counted the ESOP preferred as
converted (2,391.1M shares) and did not deduct its dividend, the consistent pair; deducting the dividend and using the
cover count gives nearly the same value per share, but the rule should say which. (3) **The pre-tax floor against after-tax
owner cash.** The floor is stated pre-tax and owner cash is after tax; no conversion is prescribed. I used the company's
own effective rate (20.8%); the row itself translates its 10% pre-tax at the corporate rate of its day **[L2002-020]**, and
the HUBB run read for form did as I did, so the practice may be uniform, but it is unwritten. (4) **The timing
convention of the ten-year sum is not fixed.** My script, checked against the HUBB run's published case, gives $20,116M
where that run gives $20,148M (0.2% apart); the CONVENTION does not say whether the first year's cash is the five-year mean
or the mean grown one year, or whether cash arrives at year-end. Immaterial here, but two analysts will not match to the
dollar. (5) **The owner's "fair" and "cheap" prices are not in the framework**, and "central case" is not defined; I took
the midpoint of the two growth ends (1.45%) and showed the top case beside it. (6) **Q6 before Q7.** The buyback test needs
the Q7 range, so Q6 cannot close in order; the CONVENTION's "recorded back at Q6" works but means a WEIGHING is left
open across a STOP. **Tool defects:** none found in `tools/run.py`, `Screens/cover_shares.py` or `tools/sources.py` for
this name (share count, OCF, capex, stock pay and D&A all agreed with the filed statements). My own `peers.py` left an empty
cache file on a cut-off EDGAR transfer and failed on re-read; it was fixed in the research folder with retries (the error
log is `peers_err.txt`).
