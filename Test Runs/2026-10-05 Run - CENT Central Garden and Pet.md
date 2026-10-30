# Company Run: Central Garden & Pet Company (NASDAQ: CENT voting, CENTA non-voting): 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: `Test Runs/_TEMPLATE - Company Run.md`,
copied to this dated file before any fetch. Every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP
that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Working folder:
`Test Runs/_research 2026-10-05 CENT/` (fetch helper, arithmetic script `compute.py` and its output `compute_output.txt`, the
`tools/run.py` output `runpy_output.txt`, the filings as text, the competitor filings under `peers/`, the cited ledger rows).

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so whether
the operator holds CENT or CENTA is unknown to this analyst.

**Contamination declared.** (1) A directory listing of `Test Runs/` showed the file names of other companies' 2026-10-05 runs,
research passes and holding reviews (names only; none opened; none concerns this company). (2) The session context showed five recent
commit subjects with verdicts on PENN (OUT at Q2), YELP (TOO HARD at Q1), ROCK (TOO HARD (WORK) at Q2), ENR (OUT at Q2) and a
session-state commit. Seen, not used; ENR is a consumer-products supplier to the same retailers, so the ENR subject is the one most
likely to steer, and it is named for that reason. (3) The project memory index names "five holding reviews" without names; the
listing in (1) showed holding-review file names that did not include CENT. Nothing about CENT was seen before this run.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** CENT (voting) **$39.70**; CENTA (non-voting) **$34.20**; both quotes of 2026-10-05 from the aggregator in
  `tools/sources.py` (Yahoo chart endpoint), **aggregator, live quote only, flagged** (operator rule 5). The non-voting class trades
  about 14% below the voting class for an identical economic claim (charter terms below).
- **Shares by class** from the cover of the latest 10-Q (period 2026-06-27, filed 2026-08-06, accession `0000887733-26-000022`),
  `python Screens/cover_shares.py CENT`: Common Stock (CENT) 9,650,221; Class A Common Stock (CENTA) 51,340,003; Class B Stock
  1,602,374 (unlisted). **Charter note read before adding:** Class A's "preferences and relative rights [...] are identical to common
  stock in all respects, except that the Class A common stock generally has no voting rights"; Class B is "identical to common stock
  in all respects except" its vote (the lesser of ten votes per share or 49% of votes cast), stock-dividend class and transfer limits,
  and "is convertible into one share of common stock" (10-K FY2025, Note on capital stock, accession `0000887733-25-000041`). The three
  classes are one economic claim: **62,592,598 shares** combined. (`tools/run.py` printed 63.8M, a weighted diluted average, and a stale
  2013 balance-sheet count of 12.2M; neither is used.)
- **Market cap:** $2,203M with each class at its own price (Class B at the CENT price, into which it converts); $2,485M if all were
  valued at $39.70; $2,141M at $34.20.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (fiscal year to 2025-09-27, filed 2025-11-26, `0000887733-25-000041`): business,
  risk factors, MD&A, statements, segment and capital-stock notes. 10-Q Q3 FY2026 (to 2026-06-27, `0000887733-26-000022`): MD&A,
  balance sheet, subsequent events. Proxy DEF 14A filed 2025-12-22 (`0001140361-25-046376`): voting, ownership, pay, related parties.
  8-Ks: 2025-11-12 credit agreement (`0001193125-25-277476`); 2026-02-18 director and bonuses (`0001193125-26-057026`); 2026-07-27
  TRIXIE purchase (`0001193125-26-316953`); 2026-08-05 Q3 results (`0000887733-26-000019`); 2026-09-22 retirement of the Garden
  president (`0001193125-26-397048`). For the fifteen-to-twenty-year span, the segment notes and MD&A of the 10-Ks for FY2008
  (`0001193125-08-244611`), FY2010 (`0001193125-10-265032`), FY2012 (`0001193125-12-501706`), FY2013 (`0001193125-13-470429`),
  FY2015 (`0001193125-15-399914`), FY2016 (`0001628280-16-021764`), FY2019 (`0000887733-19-000016`), FY2021 (`0000887733-21-000016`),
  FY2022 (`0000887733-22-000017`), FY2023 (`0000887733-23-000017`), FY2024 (`0000887733-24-000029`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, **$332,506 thousand**
  on the filed cash-flow statement (10-K FY2025, `0000887733-25-000041`), against $332.5M in the `tools/run.py` table. Agrees. Total
  assets $3,625,643 thousand on the filed balance sheet against $3,626M in the tool's table. Agrees.
- **`tools/run.py CENT` arithmetic lines only** (the tool still prints v4 material; none of it is used, Part VII). Owner cash (OCF
  less stock pay less capital spending) by year, from the filed cash-flow statements, USD millions:

| FY | OCF | stock pay | capex | D&A | owner cash (capex basis) | acquisitions paid |
|---|---|---|---|---|---|---|
| 2016 | 151.4 | 8.4 | 27.6 | 40.0 | 115.4 | 69.0 |
| 2017 | 114.3 | 11.1 | 44.7 | 42.7 | 58.5 | 103.9 |
| 2018 | 114.1 | 11.6 | 37.8 | 47.2 | 64.7 | 91.2 |
| 2019 | 205.0 | 14.7 | 31.6 | 50.8 | 158.7 | 41.2 |
| 2020 | 264.3 | 19.0 | 43.1 | 55.4 | 202.2 | 0.0 |
| 2021 | 250.8 | 23.1 | 80.3 | 74.7 | 147.4 | 820.5 |
| 2022 | -34.0 | 25.8 | 115.2 | 80.9 | -175.0 | 0.0 |
| 2023 | 381.6 | 28.0 | 54.0 | 87.7 | 299.6 | 0.0 (a business sold for 20.0) |
| 2024 | 394.9 | 20.6 | 43.1 | 90.8 | 331.2 | 60.2 |
| 2025 | 332.5 | 21.1 | 41.4 | 84.9 | 270.0 | 3.3 |

  Five-year mean (FY2021-25): **$174.6M** on the capex basis, $157.6M on the D&A basis. Ten-year mean: $147.3M. Ten-year sums: owner
  cash $1,472.7M; acquisitions $1,189.3M; buybacks $481.0M; capex $518.8M against D&A $655.1M (D&A includes intangible amortization;
  amortization of intangibles ran about $26M a year in FY2025, from the 10-Q's nine-month $18.9M). The OCF figures are after cash
  interest paid ($57.7M in FY2025) and include interest earned on the cash pile ($24.9M in FY2025), and after operating-lease payments.
  Stock pay is resolved: $21.1M in FY2025, the only stock-pay line on the statement.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own Central "if the market closed for five years" **[M1997-109]**; the question is what
the pet and garden businesses will earn, never what the quote does. The market serves and does not instruct: the same cash claim is
quoted at $39.70 with a vote and $34.20 without one, and the gap says nothing about the business; "It just tells us prices."
**[M2006-077]**. Who is paid to tell you: the filer features "non-GAAP" operating income, "adjusted EBITDA" and "organic net sales"
in every report read; the GAAP figures are used here. The analyst's habits govern: hunt "what you’re missing" **[M2025-013]**, and use
the competitors' own filings "to possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence**, written down at once, as the row asks: "write it down in the first 30 minutes" **[M1997-127]**. Against the business, in the order found: (1) the five largest customers
took 54% of FY2025 sales, and the filer writes that these retailers "are more capable of resisting price increases and can demand
lower pricing" (10-K FY2025, risk factors); (2) Home Depot 37%, Walmart 29% and Lowe's 14% of Garden sales, 80% of the segment through
three buyers; (3) FY2022: "volume declines were only partially offset by increased prices" (10-K FY2022, `0000887733-22-000017`);
(4) FY2024: a $12.8M intangible impairment in Pet "due primarily to changing market conditions resulting from the decline in demand
for durable products and increased international competition" and a grass-seed inventory write-down of about $20M after market
prices fell; (5) consolidated operating margin between 2.4% and 8.4% in every year FY2006 to FY2025 except FY2008, a loss after $430M
of impairments ($403M of goodwill); (6) organic stagnation: net sales $1,621.5M in FY2006 and $1,650.7M in FY2015; (7) Garden segment
margin a fraction of Scotts' U.S. Consumer margin in every year compared (competitor row, Q2); (8) loss of distribution of product
lines in FY2025 and again in FY2026; (9) the business has been built by acquisition: $1,189M paid in ten years, $820.5M of it in FY2021
at the pandemic peak, and now a €340M to €400M purchase of TRIXIE pending. For the business, written as found: (a) Pet segment
operating margin held between 8.9% and 12.8% for nineteen years through the pandemic boom and the unwind; (b) leading niche brands
(Nylabone, Kaytee, Pennington, Amdro, Ferry-Morse); (c) margins rose in FY2025 and the first nine months of FY2026 (operating margin
10.7% against 10.5%), with the low-margin pet distribution business contributed to a partnership in April 2026; (d) capital spending
below depreciation for three years; (e) owner cash positive in nine of ten years.

## THE STANDING RULE
A purchase of CENT or CENTA paid in cash, unlevered and sized within the buyer's means puts the buyer at no risk of ruin; the rule binds
the buyer's financing: "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**, and
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this name requires otherwise.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning
  power and competitive position will look like in five or 10 years" **[M2012-065]**, i.e. "where the business will be in 10 years"
  **[M2000-037]**.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**): (1) U.S. demand for pet supplies and lawn-and-garden consumables (dog
  chews and treats, flea and tick, small-animal and bird food, grass seed, fertilizer and pest control): slow-moving household habits,
  no technology in the product; (2) commodity input costs (millet, milo, sunflower, grass seed, chemical ingredients): not predictable
  year to year but bounded and passed along, with lags, in both directions (10-K FY2025, risk factors); (3) weather in the garden season
  (64% of Garden sales in two quarters); (4) the terms set by five retailers and the shift of the pet channel online (Amazon is a top-five
  customer). Variables (1) to (3) are "things that are important and knowable" **[M2006-076]** in the sense the rows ask: the filer
  itself cites an outside industry forecast (Freedonia) for garden sales, so the insiders do write the forecast down, unlike the field
  where they would say "That’s too hard." **[M2000-105]**. The forecast is about "what their prospective customers will do in the
  future" **[M2017-019]**, not about technology.
- **Routing.** No fast-changing technology; not a financial institution; not a holding company (two operating segments, both read).
  Variable (4), whether the company keeps its terms with the retailers, is the competitive-position question and belongs to Q2.
- **Doubt recorded.** "it’s easy to sort of think you understand retail" **[M2014-052]**: Central is a supplier to retail, not a
  retailer, and the doubt bears on its position (Q2), not on whether its economics can be pictured. "if you have doubts about something
  being into your circle of competence, it isn’t." **[M2002-092]**: I have no doubt that the demand, the costs and the channel can be
  pictured ten years out; the doubt is about who keeps the margin, which is Q2's question by the routing fixed in Q1.
- **VERDICT: IN.** The economics of a supplier of pet and garden consumables to U.S. mass retail can be pictured ten years out; the
  winner question is asked next.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**; a moat is what "protects excellent returns on invested capital" against the
competitors that "repeatedly assault" it **[L2007-004]** (that row's words). The question starts from the attacker, and "most moats
aren’t worth a damn" **[M1995-038]**.

**The record first: twenty years of the filer's own segment tables** (10-Ks listed in Step 0; operating income after depreciation,
amortization and the filer's facility-closure charges):

| FY | net sales $M | consolidated op. margin | Pet op. margin | Garden op. margin |
|---|---|---|---|---|
| 2006 | 1,621.5 | 8.4% | 12.8% | 7.2% |
| 2007 | 1,671.1 | 5.9% | 10.6% | 5.9% |
| 2008 | 1,705.4 | loss ($403M goodwill, $27M asset impairments); 6.2% before them | n/m | n/m |
| 2009 | 1,614.3 | 7.8% | 12.3% | 8.8% |
| 2010 | 1,523.6 | 7.2% | 11.6% | 7.8% |
| 2011 | 1,628.7 | 5.2% | 9.1% | 6.4% |
| 2012 | 1,700.0 | 4.4% | 9.4% | 5.3% |
| 2013 | 1,653.6 | 2.4% | 10.8% | 1.1% |
| 2014 | 1,604.4 | 3.5% | 10.4% | 5.4% |
| 2015 | 1,650.7 | 5.5% | 11.0% | 7.9% |
| 2016 | 1,829.0 | 7.1% | 11.1% | 9.4% |
| 2017 | 2,054.5 | 7.6% | 10.6% | 10.8% |
| 2018 | 2,215.4 | 7.6% | 10.5% | 10.9% |
| 2019 | 2,383.0 | 6.4% | 8.9% | 10.2% |
| 2020 | 2,695.5 | 7.3% | 10.2% | 11.3% |
| 2021 | 3,303.7 | 7.7% | 11.0% | 9.9% |
| 2022 | 3,338.6 | 7.8% | 11.1% | 10.5% |
| 2023 | 3,310.1 | 6.4% | 10.5% | 8.6% |
| 2024 | 3,200.5 | 5.8% | 11.1% | 6.0% |
| 2025 | 3,129.1 | 8.0% | 12.0% | 10.7% |

Sales doubled, but the growth was bought: sales were flat for the nine years FY2006 to FY2015 and the doubling since came with $1,189M
of acquisitions in FY2016-25 and a $196M share issue in FY2018 (5,550,000 Class A shares at $37.00, 10-K FY2019). In no year of twenty
did the consolidated margin reach 8.5%. That is the record of a business whose returns are contested, not protected.

**The castle tests, each with its filing fact.**
1. **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]**. The filer names its attackers and concedes the size: "Mars, Inc., Spectrum Brands and the J.M. Smucker Co." in pet,
   "Scotts Miracle-Gro, Spectrum Brands and S.C. Johnson" in garden, "some of which are more established in their industries and have
   substantially greater revenue and resources than we do" (10-K FY2025, risk factors). It names a second attacker the money test does
   not need: imports. The FY2024 impairment of durable-pet intangibles cites "increased international competition"; the rows warn
   against "a product that can be shipped in from abroad very easily" **[M2007-116]**. Failing answer for the durables (cushions, beds,
   aquatics); not shown either way for the consumables.
2. **Pricing power, and the agony before a rise.** "a prayer session before you raise your prices a penny" **[M2005-020]**; "would
   sales fall off a cliff?" **[M2005-019]**. The filed answers: in FY2022, "Generally, in both operating segments, volume declines were
   only partially offset by increased prices we implemented in response to high inflation" (10-K FY2022); FY2023 and FY2024 sales fell
   again on volume. When costs fall the price follows them down: after grass-seed market prices collapsed, a write-down of about $20M,
   and "We can provide no assurance as to [...] our ability to maintain pricing with our retailers in the context of declining costs"
   (10-K FY2025). The rows grant that "the businesses with strong competitive positions manage to pass through increases in raw material
   costs" **[M2005-017]**, and Central did pass through the 2021-22 increases; but the volume left, which is the reverse of the strong
   form, "charge more for a product and maintain or increase market share" **[M2000-031]**. Failing answer.
3. **Unit volume and share of mind.** Volume fell in FY2022, FY2023 and FY2024 in both segments by the filer's own words; it rose in
   the first nine months of FY2026 on "new private label business and new retailer listings" (10-Q Q3 FY2026). Unit declines are not
   by themselves a fail ("it will have unit declines over a period of time" **[M2015-066]** was said of a business
   still judged very good), but here the volume gains are listings granted by retailers, and listings were also lost ("the loss of distribution
   of two product lines" FY2025; "the distribution loss of a product line" FY2026). The share of mind that "ask[s] for you by name" is not
   shown: the rows' own test is better margins "if they ask for you by name" **[M2023-073]**, and Central's gross margin was 28.6% to
   31.9% in FY2023-25 (10-K FY2025), the operating margins above.
4. **The low-cost position.** In a product with commodity traits "being the low-cost producer is all-important" **[L2000-017]**, and
   "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. The filer claims "the advantage of efficient,
   low-cost manufacturing" in Garden (10-K FY2025). The competitor row below does not support the claim: Scotts' U.S. Consumer segment
   earned between 1.8 and 3.6 times Central's Garden margin in every year compared, and fourteen times it in FY2013. In bird feed and grass seed the input market sets the price,
   "he determined our profit, because we looked at his price every day" **[M2023-079]**. Not shown to be the low-cost producer.
5. **The brand against the retailer.** "the retailer is going to use all the pressure they’ve got" **[M2015-038]**; when the shopper
   trusts the store as much as the label, "the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]**; "the brand is our protection against the intermediaries making all the money" **[M2019-041]**. The filer: "some
   retailers are increasing their emphasis on private label products [...] we could lose sales if key retailers replace our branded
   products with private label product manufactured by others" (10-K FY2025), and Central itself makes private label for those retailers
   (about 15% of FY2019 sales, "approximately 10% to 15%" in FY2021, 10-K FY2019 and FY2021). A company that supplies the store brand
   that competes with its own brand has told us where the brand stands. Failing answer at the retailer; the consumer side not shown.
6. **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the low bid"
   **[M2017-009]** is the passing form. Central's customer of record is the retailer, five of them buy 54%, and they "can demand lower
   pricing"; the failing form is the customer who does not care from whom it buys, "most insureds don't care from whom they buy"
   **[L2004-003]**. Failing answer.
7. **Ask the competitors.** Both name Central, as one among many: Scotts lists "Central Garden & Pet Company" among its "Primary
   competitors" beside Spectrum, Bayer, Enforcer, Kellogg Garden, Oldcastle and others, in a market where "our products compete against
   private-label as well as branded products" (all six Scotts 10-Ks read, e.g. FY2025 `0000825542-25-000022`); Spectrum names Central in
   each of its four 10-Ks read. Neither ranks it or singles it out. *(A first draft of this line said no competitor named Central; a
   search of the downloaded filings for "Central Garden" found the mentions, and the line was corrected before the run closed.)* The
   competitors' own sentence puts private label in the field beside the brands; "one competitor is frequently enough to ruin a business"
   **[M2012-108]**, and here the retailer's own label is one of them.
8. **Widening or narrowing?** "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Pet durables narrowed
   (impairments FY2019 and FY2024; U.K. operations wound down FY2025); pet distribution was handed to a partnership in April 2026 after
   $474M of FY2025 sales; Garden recovered from FY2013's 1.1% to 10.7% under a cost programme. The recent gains are cost cuts and exits
   ("Cost and Simplicity"), the work of "eliminating unnecessary costs" **[L2005-010]** that the rows credit, but no row says cost-cutting
   in a contested field is a moat, and the twenty-year record shows the gains given back before (FY2006 8.4%, FY2013 2.4%).
9. **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**: one large buyer moving a category to its store brand or to an importer;
   the online channel (where Amazon and Chewy decide placement) taking share from the specialty stores Central has served; commodity
   swings. Each has already happened to a part of the business in the record.

**The competitor row** (same metric where the filings allow; they do not allow exactly the same one, and the differences are stated):

| FY | Central Garden op. margin | Scotts U.S. Consumer segment profit margin | Central Pet, op. income + segment D&A | Spectrum GPC segment adj. EBITDA | Central Garden, op. income + segment D&A | Spectrum H&G segment adj. EBITDA |
|---|---|---|---|---|---|---|
| 2010 | 7.8% | 19.0% (Global Consumer) | | | | |
| 2011 | 6.4% | 16.8% (Global Consumer) | | | | |
| 2012 | 5.3% | 13.3% (Global Consumer) | | | | |
| 2013 | 1.1% | 16.1% (Global Consumer) | | | | |
| 2014 | 5.4% | 19.6% | | | | |
| 2015 | 7.9% | 20.5% | | | | |
| 2016 | 9.4% | 22.9% | | | | |
| 2017 | 10.8% | 24.1% | 12.6% | 18.0% | 11.6% | 26.4% |
| 2018 | 10.9% | 23.5% | 12.7% | 16.7% | 11.9% | 21.5% |
| 2019 | 10.2% | 23.1% | 11.2% | 16.4% | 11.4% | 20.8% |
| 2020 | 11.3% | 24.1% | 12.5% | 17.9% | 12.4% | 20.3% |
| 2021 | 9.9% | 22.7% | 12.9% | 18.8% | 12.2% | 20.4% |
| 2022 | 10.5% | 19.4% | 13.2% | 14.3% | 13.1% | 14.7% |
| 2023 | 8.6% | 16.0% | 12.7% | 16.7% | 11.6% | 13.5% |
| 2024 | 6.0% | 16.5% | 13.5% | 18.8% | 9.2% | 15.7% |
| 2025 | 10.7% | 19.1% | 14.2% | 18.0% | 13.9% | 16.0% |

Sources: Scotts Miracle-Gro 10-Ks FY2010 (`0000950123-10-108803`), FY2013 (`0001546380-13-000032`), FY2016 (`0001546380-16-000078`),
FY2019 (`0001546380-19-000034`), FY2022 (`0001546380-22-000035`), FY2025 (`0000825542-25-000022`), segment tables ("Segment Profit"
excludes amortization, impairment and restructuring, which flatters it against Central's figure by a point or two; FY2010-13 is the
Global Consumer segment, which included Europe). Spectrum Brands 10-Ks FY2019 (`0000109177-19-000050`), FY2022 (`0000109177-22-000034`),
FY2025 (`0000109177-25-000043`), segment tables ("Segment Adjusted EBITDA" excludes depreciation, amortization, stock pay and
restructuring; Central's column adds back segment D&A only, so Central still carries its facility-closure charges: FY2024 adds back to
14.6% Pet and 10.7% Garden). Central's Pet segment carried the low-margin pet distribution business ($474M of FY2025 sales) until April
2026; without it the Pet margin is higher (non-GAAP Pet operating margin 15.8% for the first nine months of FY2026, 10-Q Q3 FY2026),
which brings Central's pet consumables near Spectrum's pet margin, not above it. Channels: Chewy's net sales rose from $4,846.7M (fiscal
year to 2020-02-02) to $12,601.5M (to 2026-02-01), operating income $254.3M in the last year (XBRL companyfacts transcription, latest
10-K `0001766502-26-000034`); Petco's net sales peaked at $6,255.3M (to 2024-02-03) and fell to $5,961.5M (to 2026-01-31), with an
operating loss of $1,180.3M in the peak year (XBRL transcription, latest 10-K `0001193125-26-106114`). Petco's sales have fallen since its
FY2023 peak and the online gatekeepers are growing; Central's response was to exit distribution.

**Reading.** Over the whole span Central earned roughly half of Scotts' garden margin and less than Spectrum's in both categories, in
every year compared; its consolidated margin never reached 8.5% in twenty years; its customers are five retailers who say what they will
pay and who buy Central's private label too; prices rose only with lost volume and fell when costs fell. Against it stands a pet
consumables franchise of steady, average margins. Nothing in the record answers "why is that castle still standing?" **[M1995-038]**
with a reason that protects excellent returns: the returns were never excellent, and the filer's own words name who holds the pricing
power. This is not a castle whose future cannot be judged, the case for "it’s just too risky. We don’t know how to valuate that"
**[M2000-019]**; it is a business whose position is judged, on twenty years of its own and its competitors' filings, to be open: the
industries where there are "just never going to have barriers to entry" **[M2012-106]**, and a supplier whose buyer sets the terms.
The nearest alternative reading, TOO HARD (WORK) on whether the pet consumables brands hold share of mind with consumers, is rejected:
the deciding party at the shelf is the retailer, and the filings already answer how the retailers treat Central (price resistance,
private label, listings lost and won). The rows also say a low price does not reopen this: "What you can’t do is turn any investment into
a good deal by paying little" **[M2019-015]**, and marginal businesses bought cheap "are the wrong foundation" **[L2014-009]**.
- **VERDICT: OUT.** The castle is shown open on the evidence (the filer's statements on retailer pricing power and private label;
  volume lost to price in FY2022; price given back with costs in FY2024; margins below both named competitors in every year compared;
  twenty years of consolidated margins of 2.4% to 8.4%). Of the three boxes, "in, out, and too hard" **[M2006-013]**, the box is OUT. The
  run closes here.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING. **NOT REACHED** (closed at Q2).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? **NOT REACHED as a judgment** (closed at Q2). The balance sheets are read here as record,
because the template asks for eight to ten years of them in Step 0 when the file closes before Q4: "balance sheets over an 8 or 10 year
period before I even look at the income account" **[M2025-032]**. Filed balance sheets, fiscal year-ends, USD millions (`tools/run.py`
transcription checked against the FY2025 and FY2016 filed statements for assets, equity, goodwill and cash):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,212 | 553 | 93 | 201 | 362 | 231 | 96 | 395 | 161 |
| 2018 | 1,907 | 952 | 482 | 276 | 428 | 281 | 152 | 692 | 363 |
| 2020 | 2,339 | 1,077 | 653 | 392 | 440 | 290 | 135 | 694 | 511 |
| 2021 | 3,117 | 1,222 | 426 | 385 | 685 | 369 | 134 | 1,185 | 646 |
| 2022 | 3,282 | 1,334 | 177 | 377 | 938 | 546 | 543 | 1,186 | 755 |
| 2023 | 3,379 | 1,451 | 489 | 333 | 838 | 546 | 497 | 1,188 | 859 |
| 2024 | 3,553 | 1,556 | 754 | 326 | 758 | 551 | 473 | 1,190 | 960 |
| 2025 | 3,626 | 1,583 | 882 | 325 | 722 | 555 | 448 | 1,192 | 1,015 |

What the figures say: (1) equity rose $1,030M in nine years, of which $196M was new stock (FY2018) and the rest retained earnings net of
$481M of buybacks; but goodwill and intangibles rose $676M over the same years, so tangible equity rose only from $226M to $580M, and
debt tripled from $395M to $1,192M (notes of 2028, 2030 and 2031 at 4.125% to 5.125%; nothing drawn on a $600M asset-based revolver to
2030). Growth was bought with borrowed and issued money, and the purchases sit on the balance sheet as goodwill. (2) Inventory is the
swing: $440M in 2020, $938M in 2022 (OCF that year was negative, $-34.0M), back to $722M in 2025; inventory to sales went from 19.8%
(2016) to 28.1% (2022) to 23.1% (2025). The FY2023-25 cash flows were flattered by about $319M of working-capital release, and FY2022
was depressed by the build: the five-year owner-cash mean washes most of this out, no single year can be used. (3) Receivables stayed
near 10% to 11% of sales throughout. (4) Cash of $882M (and $997M at June 2026) is not idle in the plan: TRIXIE (€340M at closing, up to
€60M of earn-out, and a put on the remaining 20% after three years) is pending (8-K `0001193125-26-316953`). (5) History the balance
sheet records: $403M of goodwill written off in FY2008 and $7.7M in FY2013 "due to its continuing poor performance" (10-K FY2013), the
price of an earlier acquisition programme. (6) The recurring "one-time": facility-closure and exit charges in FY2023, FY2024, FY2025 and
every quarter of FY2026 read, which the filer excludes from "non-GAAP" results; the rows call telling owners year after year to ignore
them, "when management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**. Recorded for a future
run; not judged here.

**Share-count note** (for any future Q6): in February 2024 the company paid a stock dividend of one Class A share for every four shares
of all classes, accounted for as a split; all earlier Class A and per-share figures were restated (10-K FY2024). Adjusted for it,
diluted shares were about 63.9M in FY2016 and 63.8M in FY2025: ten years of buybacks ($481M) offset the 2018 issue and the stock pay,
and per-share owner cash grew at the aggregate rate. The dividend was paid in non-voting shares, which keeps the founder's vote intact
as the share count grows.

## Q5: WHO RUNS IT? **NOT REACHED.** Recorded from the proxy (`0001140361-25-046376`), not judged: the founder William E. Brown, 84,
Chairman, CEO 1980-2003 and 2007-2013, holds 1,600,459 Class B, 1,386,792 common and 1,432,565 Class A shares: 7.1% of the economic
interest and 56.3% of the vote. Chief executive Nicholas Lahanas since fiscal 2025, total reported pay $1,905,762 before an annual bonus
(pay ratio 40 to 1). A related-party payment of $266,000 to an entity 80% owned by Mr. Brown (Diamond Fork) in FY2025.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? **NOT REACHED.** (Buybacks of $148.4M in FY2025 at an average near $32 a share,
against an authorization that names no price; no dividend ever paid; the acquisition record is in Q4's reading.)
## Q7: WHAT IS IT WORTH? **NOT REACHED** as a judgment. The owner's requested figures are given below as computation only.
## Q8: BETTER THAN THE ALTERNATIVES? **NOT REACHED.**
## Q9: COULD IT RUIN US? **NOT REACHED.** (Pre-tax earnings plus interest over interest, FY2025: ($216.8M + $57.7M) / $57.7M, about
4.8 times; no maturity before February 2028; the criterion "Businesses earning good returns on equity while employing little or no debt" **[R1997-001]** is not applied.)
## Q10: THE FAT PITCH? **NOT REACHED.**
## Q12 (optional): PROUD OF HOW THE MONEY IS MADE? **NOT REACHED.** (Pet supplies, seed, fertilizer and pest control: none of the
businesses Q12 names.)

---
## COMPUTATION - NOT A CLEARANCE
*Written at the owner's request after the Q2 STOP closed the file. No entry language; none of it reopens Q2 (operator rule 3).*

**(a) VALUE RANGE, by the Q7 CONVENTION.** Base: five-year mean owner cash after every real cost, **$174.6M** (OCF less stock pay less
all capital spending, FY2021-25; the D&A variant $157.6M; the maintenance judgment: management guides capital spending of $50M to $60M
for the next year, 10-K FY2025, above the $41.4M spent, so the capex basis is the better basis, not the generous one). Carried ten years
at the shown growth, then at zero nominal growth, discounted at 5.66%. The ends: no growth and shown growth.
- No-growth end: $3,086M, **$49.30 a share**. Shown-growth end (4.8% a year, below): $4,513M, **$72.11 a share**. Width 1.46 to 1
  (under the three-to-one TOO HARD line). Against the prices: **CENT $39.70 is 19% below the bottom of the range; CENTA $34.20 is 31%
  below it.** "working with a range of possibilities is the better approach" **[L2000-024]**; price is set against "the bottom boundary of
  our estimate" **[L2013-012]**.
- **The growth input, CONVENTION of this run.** The framework's convention measures shown growth on aggregate owner cash over the five
  years. Here that is meaningless: the window runs from $147.4M through $-175.0M to $270.0M, and an endpoint rate (16.3% a year) is
  exactly what "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]** warns
  of. Used instead: the filer's own five-year average growth in GAAP operating income, 4.8% a year (10-K FY2025, business section), which
  includes the businesses bought for $820.5M in FY2021, so it overstates organic growth; it is below the 5.66% discount rate, so the Q3
  cap is met.
- **Whole-cycle variant** (the five-year window holds abnormal years: the pandemic peak FY2021, the inventory build FY2022 and its
  release FY2023-24). Ten-year mean owner cash, $147.3M: **$41.57 to $60.81 a share**. A working-capital-neutral variant (FY2023-25 OCF
  less the filed working-capital changes, CONVENTION of this run, shown only to bound the base, not used for the fair price below):
  $194.0M, $54.76 to $80.11. The ten-year mean includes years before $1,189M of acquisitions were made, so it understates the present
  business; the working-capital-neutral figure takes the best three years of the cycle, so it overstates it. The five-year mean sits
  between them.

**(b) FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor). Floor: "at least 10% pre-tax returns"
**[L2002-020]**; "a point at which we drop out of the game. And it’s arbitrary." **[M2003-149]** (the Q7 CONVENTION of about ten percent
pre-tax). **Tax treatment:** owner cash is after corporate income tax (OCF is after cash taxes); it is grossed up to a pre-tax equivalent
at the FY2025 effective rate of 24.4% (10-K FY2025) and the pre-tax stream is discounted at 10%. **Central case, CONVENTION of this run:**
the five-year mean carried at half the shown growth (2.4% a year) for ten years, then flat; the midpoint of the range's two growth
inputs. Result: **fair price about $43.46 a share** ($2,720M). Both quotes are below it: CENT $39.70 by 9%, CENTA $34.20 by 21%. At zero
growth the fair price is $36.91 (CENT above it, CENTA below it); at the full shown growth, $51.29. On the whole-cycle ten-year base the
central fair price would be lower, about $36.66 by the same arithmetic scaled to $147.3M (CENT above it, CENTA below it). Pre-tax
owner-cash yield at the price, five-year base: 9.30% at $39.70, 10.79% at $34.20.

**(c) CHEAP PRICE** (below which no pencil is needed). **Rule, CONVENTION of this run:** half the bottom of the five-year value range,
**about $24.65 a share**. Rationale: the rows' picture of a price needing no pencil is "I didn’t need to know whether it was worth 97
billion or 103 billion if I was buying it at 35 billion" **[M2008-068]**, about a third of value, and the margin is "a big discount from
that present value calculated using the risk-free interest rate" **[M1997-126]**; half the bottom is the gentler of the two and is
applied to the bottom, not the middle. Both quotes are well above it ($39.70 is 61% above; $34.20 is 39% above). By the rows' own test
neither price screams: "It should scream at you." **[M2009-005]**; the arithmetic above needed a calculator.

**What the computation says, plainly.** At these prices CENTA, and to a lesser degree CENT, sit below a range built from Central's own
owner cash at the long government rate, and the non-voting class sits near a 10% pre-tax return on the central case. That is the
arithmetic of a cheap price for an ordinary business. The framework stops before it, at Q2, because the record shows no castle that
keeps that owner cash from being competed away; a price does not cure that, and the owner should read the numbers above as what a
reopening would have to start from, not as a reason to reopen.

---
## THE BOX
**OUT at Q2** (the castle shown open: five retailers set the terms by the filer's own account; volume lost to price in FY2022 and price
given back with costs in FY2024; margins below Scotts and Spectrum in every year compared; consolidated operating margin 2.4% to 8.4% in
every year FY2006-2025 except the FY2008 impairment loss). Not reached: Q3 to Q12. Computation only: value range $49.30 to $72.11 a share
(whole-cycle $41.57 to $60.81) against CENT $39.70 and CENTA $34.20; fair price about $43.46; cheap price about $24.65.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not** written question by question with a commit after each: the run file was written
  in one pass after the reading, and nothing was committed, at the instruction of this session (no commits). Declared, not ticked as met.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment matched inside its row); no
  v4 or E-id is cited; every filing fact carries its accession; every number carries a filing or a CONVENTION label.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after Q2 is a clearance; the computation is headed as one.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending), never a net-income proxy; the sovereign from the
  issuing authority (US Treasury par curve, dated); aggregator quotes flagged. Acquisitions are not deducted from owner cash and are shown
  beside it (see the framework note below).
- [x] Contrary evidence was written down as it was found, "write it down in the first 30 minutes" **[M1997-127]**, in the foundations paragraph, in both directions.
- [x] No row dated after the anchor is cited (this is not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its share count (63.8M weighted) and its stale 2013 count were rejected for
  the cover count.
- [x] `python tools/check_framework.py` run after the file was written: **PASS** (2026-10-05). The run's own check
  (`_research 2026-10-05 CENT/check_ids.py`: no E-ids, every id in the v5 ledger, every quoted fragment inside its row): PASS. Not committed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no rule for a two-segment business whose halves read differently.** The by-parts rule exists only for a holding company at
Q1. Here Garden shows no castle and Pet consumables show an average one; I closed the whole on the evidence that applies to both (the
retailers' terms) and on the consolidated record, but two analysts could split on whether an average pet franchise is enough to send the
file to TOO HARD (WORK). (2) **The Q7 growth input breaks when the five-year window contains a negative year.** The convention measures
shown growth on aggregate owner cash; with FY2022 at $-175M the endpoint rate is 16.3%, "a breathtaking, but meaningless, growth rate" **[L2005-003]**. I substituted the
filer's operating-income growth and confessed it; the framework should say what to use. (3) **Acquisitions are not addressed by the
range convention.** "Deducts all capital spending" is silent on purchases of businesses; at Central they were $1,189M in ten years against
$1,473M of owner cash, so including or excluding them changes the base by most of its size. I excluded them from the base and showed them
beside it. (4) **"Fair price", "central case" and "cheap price" have no definitions in the framework**; each is a CONVENTION of this run,
and a different choice of central growth moves the fair price between $36.91 and $51.29. (5) **The competitor row's "same metric" is not
available**: Scotts reports segment profit before amortization and restructuring, Spectrum segment EBITDA before depreciation, stock pay and
restructuring, Central operating income after all of them; the template should allow "nearest metric, differences stated". (6) **Two
share classes at two prices**: the framework says nothing about which quote to set against value when the economic claims are identical;
both are reported. (7) **The protocol's heading for a computation joins its two halves with an em dash** (operator rule 3), which the
operator's standing rule forbids in output; it is written here with a hyphen. (8) **`tools/run.py` still prints v4 commentary and a
weighted-average share count for a multi-class filer**; both were set aside, as Part VII directs.
