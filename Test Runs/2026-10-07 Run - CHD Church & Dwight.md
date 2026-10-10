# Company Run — Church & Dwight Co., Inc. (NYSE: CHD) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended to 2026-10-07). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` (operator rule 10). Business: household and personal care
brands (ARM & HAMMER, OXICLEAN, BATISTE, WATERPIK, THERABREATH, HERO, TOUCHLAND, TROJAN, FIRST RESPONSE, NAIR, ORAJEL,
XTRA, ZICAM) and a Specialty Products Division (sodium bicarbonate, animal nutrition). No rename or merger; portfolio
changes in the window: VMS (VITAFUSION, L'IL CRITTERS) sold 2025-12-31; FLAWLESS, SPINBRUSH and WATERPIK showerheads exited
in 2025; TOUCHLAND bought 2025-07-16; MISS MOUTH'S MESSY EATER bought in 2026.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared at the start.** (1) The git status shown to this session at start listed an untracked folder
`Test Runs/_research 2026-09-26 CHD/` with file names (a 2025 exhibit, a 2026 proxy, a 2026 10-Q). That folder belongs to an
earlier run on this company; it was not opened, listed or searched, and nothing in it is used. Its existence says only that the
name was run before; its box is unknown to this analyst. (2) The recent-commit subjects shown at start name boxes for ATR,
ACNB, ACLS and AMAT (other companies); not used. (3) The memory index loaded at start mentions "57 gate-clearers, nothing
buyable" and holding reviews owed in general terms; it names no company and is not used. Nothing else was seen.
(4) *Added after the close:* the `git log` printed to confirm the closing commit showed other analysts' commit subjects
for BMI and CB runs of the same day (boxes and figures in the subjects). Seen after this run's box was written; not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $96.54 (close 2026-10-06, the quote printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $1 par, **237,203,907** shares (10-Q for the
  period ended 2026-06-30, filed 2026-07-31, accession `0001193125-26-327567`; cover as of 2026-07-29;
  `python Screens/cover_shares.py CHD`). Cross-check: the same 10-Q's equity statement shows 293.7M issued less 56.6M
  treasury = 237.1M at 2026-06-30, agreeing to rounding. No 8-K or prospectus after that 10-Q issues shares (the only later
  8-K is the earnings release of 2026-07-31, `0001193125-26-326749`). The Touchland founder's $50.0M of shares vest 50% at each
  of the first and second anniversaries of 2025-07-16 (10-K FY2025, `0001193125-26-048139`); immaterial to the count.
- **Market cap:** 237.204M x $96.54 = **$22,900M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 2026-10-06
  (`python tools/sources.py`, issuing authority). About 82% of sales are in the U.S. (10-K FY2025).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0001193125-26-048139`); 10-K FY2024
  (`0000950170-25-019801`), FY2023 (`0000950170-24-015810`), FY2022 (`0000950170-23-003066`), FY2021
  (`0001564590-22-005528`), FY2020 (`0001564590-21-006669`), FY2019 (`0001564590-20-004956`), FY2017
  (`0001564590-18-002984`), FY2016 (`0001564590-17-002326`); 10-Q Q2 2026 (`0001193125-26-327567`); proxy DEF 14A filed
  2026-03-19 (`0001193125-26-115994`); 8-Ks of 2025-07-18 (credit agreement, `0001193125-25-161241`), 2025-12-05
  (board tenure limits removed, `0001193125-25-309753`), 2025-12-09 (VMS sale, `0001193125-25-312870`); and the ten
  fourth-quarter earnings releases FY2016 to FY2025 (exhibit 99.1 to the 8-Ks `0001564590-17-001054`,
  `0001564590-18-001296`, `0001564590-19-001888`, `0001564590-20-002837`, `0001564590-21-003212`,
  `0001564590-22-002820`, `0000950170-23-001741`, `0000950170-24-010091`, `0000950170-25-011420`,
  `0001193125-26-030474`). Stripped texts in the working folder.
- **One figure cross-checked against the filed statement:** cash from operations FY2025 **$1,215.4M** in the 10-K's
  statement of cash flows and MD&A (`0001193125-26-048139`) against 1,215 printed by `tools/run.py`; also net sales FY2025
  $6,203.2M in the segment note against the XBRL figure. Both agree.
- `python tools/run.py CHD` arithmetic lines only (output saved as `run_py_output.txt` in the working folder), with the
  longer series pulled from the same XBRL facts by `series.py` and checked against the filed cash-flow statements of
  FY2025 and FY2023:

| FY | Cash from ops | Stock pay | Capex | D&A | Owner cash (OCF - stock pay - capex) | Acquisitions paid | Divestiture proceeds |
|---|---|---|---|---|---|---|---|
| 2016 | 655.3 | 16.0 | 49.8 | 107.6 | 589.5 | 305.3 | - |
| 2017 | 681.5 | 18.1 | 45.0 | 125.4 | 618.4 | 1,260.0 | - |
| 2018 | 763.6 | 23.3 | 60.4 | 141.1 | 679.9 | 49.8 | - |
| 2019 | 864.5 | 20.8 | 73.7 | 176.4 | 770.0 | 475.0 | - |
| 2020 | 990.3 | 21.5 | 98.9 | 189.7 | 869.9 | 512.7 | 7.0 |
| 2021 | 993.8 | 23.7 | 118.8 | 219.1 | 851.3 | 556.0 | - |
| 2022 | 885.2 | 32.3 | 178.8 | 219.0 | 674.1 | 546.8 | - |
| 2023 | 1,030.6 | 63.6 | 223.5 | 225.2 | 743.5 | 0.0 | - |
| 2024 | 1,156.2 | 59.2 | 179.8 | 239.1 | 917.2 | 19.9 | 6.6 |
| 2025 | 1,215.4 | 58.0 | 122.4 | 247.4 | 1,035.0 | 656.0 | 160.3 |

  USD millions. Five-year average owner cash 2021 to 2025, all capex deducted: **$844.2M** (run.py prints 844). On the D&A
  basis the five-year average is 779 (run.py). Stock pay is complete as tagged: run.py found no other stock-pay line,
  no securities inside operating cash, no intangible or software payments beside capex. Not in the table: the Touchland
  earnout ($159.0M owed for 2025, paid in 2026 with $180.5M of business-acquisition liabilities paid in H1 2026, 10-Q) and
  the 2026 MISS MOUTH'S purchase ($300.0M cash plus $25.0M deferred, 10-Q).

## THE FOUNDATIONS (not a gate)
A share of CHD is a share of a brand portfolio: the test is whether it could be owned "if the market closed for five years"
**[M1997-109]**, which turns the run toward what the brands earn and what the managers buy with the cash, not toward the
quote. The quote is information only: "It just tells us prices." **[M2006-077]**. The foundation that bears hardest here is
**who is paid to tell you**: every fourth-quarter release from FY2016 to FY2025 headlines figures that "EXCEED OUTLOOK" and
leads with organic and adjusted figures (the releases listed in Step 0), and the company's own 10-K strategy section says
it "will continue to focus on core growth" with stated long-term targets; the analyst reads the filed statements first and
the company's framing last, and does not "ask the barber whether you need a haircut" **[M2011-083]**. The analyst's habit:
look for "what’s wrong in things" **[M2025-013]**. The index fork is not engaged: this is a run of record for an operator
who runs the questions.
**Contrary evidence, written down as found** **[M1997-127]**:
1. Three acquired businesses failed inside the decade: FLAWLESS (bought 2019 for $475.0M; $411.0M intangible impairment in
   2022; exited 2025), VITAFUSION and L'IL CRITTERS (VMS; $357.1M impairment in 2024; sold 2025-12-31 for $160.3M with a
   further $58.5M pre-tax loss), and WATERPIK (bought 2017 for $1,024.6M; showerheads exited 2025; the trade name's fair value
   down to 117% of its $644.7M carrying value, "reflecting falling sales, rising competition"; 10-K FY2025). SPINBRUSH's
   intellectual property was transferred "for nominal" consideration (10-K FY2025, Note 8).
2. The 10-K FY2025 says "e-commerce significantly reducing the barriers for even small competitors to quickly introduce new
   brands and products directly to consumers", and the growth brands bought in the decade (THERABREATH, HERO, TOUCHLAND) were
   themselves small attackers that took the lead in their niches; the same door is open to the next attacker.
3. Walmart is about 23% of net sales in each of 2023 to 2025 and the top four customers about 44% (10-K FY2025); retailers
   are named as pushing private label "primarily in the stain fighters, diagnostic kits and oral analgesics categories".
4. Organic growth was 0.7% in FY2025 and Consumer Domestic declined 0.5% organically (release of 2026-01-30).

## THE STANDING RULE
The buyer's conduct, not the target's: a part-interest in CHD bought with the operator's own money, unlevered and sized so
that no fall in the quote forces a sale, puts nothing the buyer has and needs at risk; borrowed money would, and is ruled out
**[L2014-005]**, **[M2012-081]**. Nothing in this run asks the buyer to give an option or accept a call on his cash
**[M2004-065]**. Passes, as the buyer's rule; it says nothing of the business.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- **The parts first** (Q1's holding-company paragraph, extended 2026-10-06 to operating segments; a part "matters" when it
  carries more than half of five-year operating profit). Segment income from operations 2021 to 2025, from the segment notes
  of the 10-Ks FY2023 (`0000950170-24-015810`) and FY2025 (`0001193125-26-048139`): Consumer Domestic 908.4, 499.1, 929.7,
  684.9, 920.8 = **3,942.9 (85.4%)**; Consumer International 135.3, 46.2, 104.2, 83.1, 116.2 = 485.0 (10.5%); SPD 35.4, 52.5,
  23.5, 39.1, 40.6 = 191.1 (4.1%); total 4,619.0. Consumer Domestic decides; the other two do not, and both are
  understandable on their face (the same brands abroad; sodium bicarbonate and dairy feed additives from an integrated
  trona supply at Green River).
- **The key variables** **[M1998-044]**: for Consumer Domestic, (1) unit volume and price/mix of the brands in the stores,
  against private label and small online entrants; (2) the terms the large retailers extract (Walmart about 23% of sales,
  top four about 44%); (3) input costs (surfactants, diesel, resin, tariffs) and whether price passes them through; and
  (4) what the company pays for the brands it buys, since six of seven power brands were bought ("Since 2001, we have
  acquired six of our seven “power brands.”", 10-K FY2025 MD&A). The first three are consumer and retail behaviour, the kind
  the rows say can be projected: "we know what we think we can project out in terms of consumer behavior and threats to a
  business" **[M2023-030]**; the forecast is about customers, not technology **[M2017-019]**. The fourth is a use of the
  money and belongs to Q3 and Q6, not to understanding.
- **Do the past statements tell the future ones?** **[M2008-033]** For the deciding part, yes: ten years of segment and
  bridge data read for this run show the same mechanics every year (volume, price/mix, acquired lines, exited lines), a
  gross margin between 41.9% and 45.8% in every year 2016 to 2025, and the one large disturbance (2021 to 2023 inflation)
  visible and explained in the filings. Laundry detergent, cat litter, baking soda, condoms, depilatories, toothpaste and
  mouthwash will be bought in ten years by the same kinds of households through the same kinds of stores.
- **Would the insiders write it down?** **[M2000-105]** The company writes down a ten-year frame for its core in its own
  filing (ARM & HAMMER from a $2 billion to a $3 billion brand; oral care from $1 billion to $1.5 billion; 10-K FY2025),
  which is the opposite of the "too hard" answer the row describes. That is the seller's projection and is not used as
  evidence of the outcome **[M2011-083]**; it is used only as evidence that the industry's insiders treat the forecast as
  writable.
- **How far off could I be?** **[M2011-084]** Narrow on the household core; wide on the trend brands (dry shampoo, acne
  patches, hand sanitizer, water flossers), where three bought brands failed inside the decade (Foundations, contrary
  evidence 1). That width is a question of the castle (Q2) and of what the cash is spent on (Q6), not of whether the
  economics can be seen.
- **Doubt test** **[M2002-092]**: the doubt this analyst has is about the durability of the newer brands and the price paid
  for them, not about whether the business can be understood; it is carried to Q2 and Q6. Retail is the narrated case of
  thinking one understands **[M2014-052]**; CHD is a supplier to retail, not a retailer, and its exposure to the retailer is
  carried to Q2 as a castle test.
- **VERDICT: IN.** The deciding part, Consumer Domestic, is a portfolio of household and personal care brands whose ten-year
  economics turn on consumer and retailer behaviour that the filings show year by year **[M2012-065]**, **[M2023-030]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. The deciding part is Consumer Domestic (Q1, 85.4% of five-year segment
income); the file closes on it.

**The parts table** (section B; segment income from operations, 10-Ks FY2023 `0000950170-24-015810` and FY2025
`0001193125-26-048139`):

| Part | Share of 2021-2025 operating profit | Castle | Decides |
|---|---|---|---|
| Consumer Domestic | 3,942.9 of 4,619.0 = 85.4% | judged below | **yes** (more than half) |
| Consumer International | 485.0 = 10.5% | the same brands abroad; organic growth 9.0% (2023), 9.6% (2024), 5.5% (2025) per the releases | no |
| Specialty Products | 191.1 = 4.1% | sodium bicarbonate from its own trona-fed plants, against Cargill, Solvay, Genesis Alkali/WE Soda and Huber-Natural Soda (10-K FY2025); commodity-like | no; carried to Q7 at no growth if open |

**Consumer Domestic over the cycle** (segment notes of the 10-Ks FY2017, FY2019, FY2021, FY2023, FY2025; the net-sales
bridges in each MD&A; USD millions):

| Year | CD net sales | CD gross margin | CD operating margin as reported | before the named impairment or exit charge | CD volume | CD price/mix |
|---|---|---|---|---|---|---|
| 2016 | 2,677.8 | 48.9% | 22.9% | 22.9% | | |
| 2017 | 2,854.9 | 48.3% | 22.7% | 22.7% | 4.6% | (3.2%) |
| 2019 | 3,302.6 | 47.7% | 21.4% | 21.4% | (0.2%) | 4.2% |
| 2020 | 3,767.6 | 47.8% | 23.5% | 23.5% | 8.9% | 1.8% |
| 2021 | 3,941.9 | 45.6% | 23.0% | 23.0% | (0.3%) | 3.9% |
| 2022 | 4,131.0 | 43.4% | 12.1% | 22.0% (FLAWLESS $411.0) | (5.9%) | 6.8% |
| 2023 | 4,571.2 | 46.8% | 20.3% | 20.3% | 1.0% | 4.7% |
| 2024 | 4,732.3 | 48.2% | 14.5% | 21.4% (VMS $327.4) | 2.8% | 0.7% |
| 2025 | 4,774.8 | 46.7% | 19.3% | 20.2% (exits $45.6) | 0.0% | (0.5%) |

**The castle tests, each with its filing fact.**
1. *What keeps it standing* **[M1995-038]**. The 10-K's own answer is the brand list: ARM & HAMMER (the trademark used
   since 1867; the number one baking soda "in terms of consumer recognition"), TROJAN (number one condom), NAIR (number
   one depilatory), ORAJEL (number one oral pain relief), BATISTE (the world's number one dry shampoo), THERABREATH
   (number one alcohol-free mouthwash), HERO (number one acne patch), TOUCHLAND (number one hand sanitizer), WATERPIK
   (number one water flosser), FIRST RESPONSE (number two pregnancy test). Rankings are by IRI dollar share. **No
   brand-level sales, share percentages or profits are disclosed** beyond "approximately 70% of our net sales and
   profits" for the seven power brands and ARM & HAMMER called a "$2 billion brand" (10-K FY2025).
2. *Would it stand without the lord?* The household core has stood through a change of chief executive in the decade read
   (the earlier releases quote Matthew Farrell, the 2026 release Rick Dierker). Nothing in the brands depends on one person.
3. *The money test* **[M2011-015]**. For the old household brands the decade answers no: Henkel entered U.S. premium
   laundry and bought Sun Products (10-K FY2016), P&G and private label press on laundry, and Consumer Domestic held its
   gross margin. For the niche personal-care brands the answer is **yes, and cheaply**: THERABREATH, HERO and TOUCHLAND
   each took first place in its niche as a small entrant, which is why CHD bought them, and the 10-K FY2025 says
   e-commerce is "significantly reducing the barriers for even small competitors to quickly introduce new brands". The
   rows: "usually if something can gain competitive advantage very quickly, you have to worry about them losing it
   quickly, too" **[M2002-050]**. The filings show it happening: VMS (both brands "number one leading brands in their
   respective categories", 10-K FY2021) impaired in 2024 for "significant product competition coming from new category
   entrants, including private label"; FLAWLESS ("the number one women’s electric hair removal system", 10-K FY2021)
   impaired in 2022 and exited in 2025; WATERPIK losing to "value-branded products".
4. *Pricing power and the agony before a rise* **[M2005-020]**, **[M2005-017]**. The full inflation cycle is in the
   record: Consumer Domestic took price/mix of 3.9%, 6.8% and 4.7% in 2021 to 2023 (about 16% compounded) against volume of
   (0.3%), (5.9%) and 1.0%; volume then grew 2.8% in 2024; segment gross margin fell from 47.8% (2020) to 43.4% (2022) and
   was back to 48.2% in 2024. The costs were passed through and the customers came back, which is what "the businesses
   with strong competitive positions manage to pass through increases in raw material costs" describes **[M2005-017]**.
   Against it: 2025 Consumer Domestic price/mix was (0.5%), and the 10-K says laundry is "subject to significant price
   competition" and that the company "may need to reduce the prices for some of our products".
5. *Unit volume and share of mind* **[M1997-099]**. Consumer Domestic volume over 2021 to 2025 compounded to about
   (2.6%) while price/mix compounded to about 16%: volume, the rows' preferred evidence, was flat to down across the cycle
   in the deciding part. The company reports share gains in "four of our eight power brands" in 2025 (release of
   2026-01-30), which is half.
6. *The low-cost position.* About one-third of consumer revenue is in "value" brands (34% in 2025, 10-K FY2025), led by
   ARM & HAMMER and XTRA laundry. No filing read compares CHD's laundry cost with P&G's or private label's; the integrated
   sodium bicarbonate supply (Green River trona) is the one named cost edge, and it reaches the baking-soda lines, not
   liquid detergent. Not shown either way.
7. *The brand against the retailer* **[M2015-038]**, **[M2001-090]**. Walmart about 23% of net sales in each of 2023 to
   2025, the top four customers about 44% (10-K FY2025); retailers "have discontinued or reduced distribution of some of
   our products" to push their own private label in "stain fighters, diagnostic kits and oral analgesics" (OXICLEAN,
   FIRST RESPONSE, ORAJEL). The speakers' own narrated error is this one: "we did underestimate, not what the consumer is
   doing so much, but what the retailer is" **[M2019-041]**.
8. *Would the customer still choose it over the low bid?* For ARM & HAMMER baking soda and TROJAN, a decade of price rises
   at stable margins says yes. For WATERPIK the filing says no ("more customers choosing value brands amid inflation").
   For value laundry the brand is itself the lower bid against the premium leader; its customer is the price-sensitive one.
9. *Ask the competitors.* Not available on the public record beyond the competitors the 10-K names. S.C. Johnson is private
   and **not an SEC filer**; Henkel, Reckitt, Haleon and Unilever report abroad and were not read; flagged.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Consumer Domestic operating margin before the named charges
   ran 22.7% to 23.5% in 2016 to 2021 and 20.2% to 21.4% in 2023 to 2025, about two points narrower, while the mix moved
   toward higher-margin acquired brands; gross margin ended the cycle where it began. Narrowing slightly in the aggregate;
   sharply in the three exited parts; widening in THERABREATH and HERO by the company's account.
11. *What could destroy it* **[M2000-014]**: the retailer (test 7), the small online entrant (test 3), and price competition
   in laundry, the largest single business.

**The competitor row**, ten fiscal years each, from the companies' own XBRL filings (`comp_margins.txt`,
`comp_tangible.txt`, `comp_averages.txt` in the working folder). EBIT is operating income as filed; for Clorox, which
tags no operating income, income before tax plus interest expense. Tangible assets are total assets less goodwill and
intangibles. Last-year accessions: CHD `0001193125-26-048139`, PG `0000080424-25-000076` (FY June 2025), CLX
`0000021076-25-000039` (FY June 2025), CL `0000021665-26-000006`, KMB `0001628280-26-007567`.

| Company | Years | Gross margin avg | Operating margin avg (min) | EBIT / tangible assets avg (min to max) | Goodwill + intangibles / assets, last |
|---|---|---|---|---|---|
| CHD | 2016-2025 | 44.6% | 18.0% (11.1%) | 40.2% (22.7% to 49.6%) | 69% |
| Procter & Gamble | FY2016-FY2025 | 49.6% | 20.7% (8.1%) | 27.9% (10.8% to 33.2%) | 51% |
| Clorox | FY2016-FY2025 | 43.0% | 14.4% (4.4%) | 28.5% (8.2% to 45.0%) | 32% |
| Colgate-Palmolive | 2016-2025 | 59.5% | 21.2% (16.1%) | 37.9% (27.7% to 46.2%) | 29% |
| Kimberly-Clark | 2016-2025 | 33.9% | 15.0% (11.5%) | 19.8% (15.5% to 25.3%) | 11% |

*Added after Q7, before the run closed:* two U.S. filers that the 10-K FY2025 names as competitors and the brief did not
list, read the same way for the years they file (`comp_margins.txt`, `comp_tangible.txt`): **Kenvue** (10-Ks from 2023;
last `0001944048-26-000030`), gross margin 55.4% to 58.1%, operating margin 11.9% to 17.9%, EBIT on tangible assets 22.2% to
32.3%, goodwill and intangibles 67% to 70% of assets, the one rival as acquisition-built as CHD; **Edgewell Personal Care**
(FY September 2019 to 2025; last `0001628280-25-052765`), operating margin 4.3% to 11.4%, EBIT on tangible assets 6.3% to
16.5%: a brand portfolio in the same aisles earning ordinary returns, which shows that the category alone does not
protect returns and that CHD's results are its own. Kimberly-Clark, which the brief lists, is not among the competitors
the 10-K names; its tissue and diaper categories barely overlap CHD's, and its row is kept as a field reference only.

**The field's returns over the last full cycle** (section C), judged in words: the field earns high pre-tax returns on
the tangible capital it uses, through the 2021 to 2023 inflation as well as before and after it, with Clorox the one
that fell hard in the trough; CHD sits at the top of the field on that measure, above P&G and Colgate on average. These are
not ordinary returns **[L2007-004]**. What the measure leaves out is that 69% of CHD's assets are purchased goodwill and
trade names, the highest share in the field; the return on what was paid for the brands is Q3's question.

**Judgment.** The castle of the deciding part stands, on the evidence of a full cycle in which price rose by about 16%,
customers came back, and gross margin returned to its starting level **[M2005-020]**, **[M2005-017]**, **[L1995-022]**, and
of returns on tangible capital at the top of a field that itself earns well **[L2007-004]**. It is not one castle but a row
of small ones. The old household ones (ARM & HAMMER, TROJAN, NAIR, ORAJEL) have stood for decades. The newer personal-care
ones were built quickly by small attackers, and three of the decade's purchases were crossed within a few years
**[M2002-050]**; a portfolio that keeps its growth by buying the latest winner comes close to "A moat that must be
continuously rebuilt" **[L2007-005]**, which the framework sends OUT only "where the evidence shows the rebuilding
failing". Here the rebuilding failed in three parts and held in the aggregate. Flat volume across the cycle and the
retailer at 23% weigh against **[M2019-041]** and are carried to Q7 (the growth input) and Q9. No row about one named
company is used to decide this (the CONVENTION of 2026-10-07).
- **VERDICT: IN**, on the deciding part, Consumer Domestic, with the evidence against written above and carried forward
  **[M1995-038]**, **[M2005-020]**, **[L2007-004]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The rows judge the business on "the capital actually needed in the business" **[M2010-090]**, on "return on tangible
assets", and judge the capital allocation with the goodwill put back, "because we paid for it" **[M2011-060]**; the
question for growth is "what we earn on that incremental $130 million over time" **[M2001-019]**.

- **The capital the business needs.** Pre-tax operating income on tangible assets averaged 40.2% over 2016 to 2025 and ran
  42% to 50% in every year without a large impairment (Q2 competitor row). Capital spending was 1.2% to 3.8% of sales
  (45.0 in 2017, 223.5 in 2023, 122.4 in 2025); depreciation of plant was 59.7 to 89.7 a year (statements of cash flows,
  10-Ks FY2017, FY2019, FY2021, FY2023, FY2025). Capital spending ran above depreciation by 50.4, 111.8, 150.7, 96.6 and 32.7
  in 2021 to 2025 (442.2 in all), the excess going to capacity; the business that needs plant is a small one. On this
  measure it is the first kind the rows name, "more and more money every year without putting up anything to get it, or
  very little" **[M1998-081]**.
- **Maintenance, the stated guess** **[M2000-144]**, **[L1999-024]**: the filings give no maintenance figure. The guess
  here is depreciation of plant, 68.4 to 89.7 in 2021 to 2025, which the rows allow as the proxy in most companies
  **[M1998-127]**; the rest of capital spending (88.4 a year on average) is growth spending. Intangible amortization (121.1 in
  2025) is the write-off of purchase prices, not a cost of staying in place, and is handled at Q7 by deducting the purchases
  themselves.
- **What the added capital earned.** The business's added capital in the decade was not plant; it was purchases. Cash paid
  for businesses 2016 to 2025 was **4,381.5** (305.3, 1,260.0, 49.8, 475.0, 512.7, 556.0, 546.8, 0.0, 19.9, 656.0), less 173.9
  of divestiture proceeds, plus the TOUCHLAND earnout of 159.0 owed for 2025: about **4,367 net**. Over the same decade
  owner cash before interest (owner cash plus after-tax interest; 2016 at that year's 35.0% effective rate, 2025 at 23.0%)
  rose from about 607 to about 1,090, an increase of about **483 a year**. Crediting the whole increase to the purchases,
  including the organic growth of the brands owned in 2015, the purchases earned at most **about 11% after tax** on what was
  paid; the true figure is lower by whatever the 2015 portfolio would have grown on its own (organic growth averaged about
  4% a year over the decade, Q2). With goodwill put back as the row requires **[M2011-060]**, the whole business earns
  about 1,078 of operating income (2025) on about 5,800 of capital (equity 4,002 plus long-term debt 2,205 less cash 409 at
  2025-12-31), about **18.6% pre-tax, about 14% after the 2025 tax rate**.
- **The write-offs inside that record.** FLAWLESS: 475.0 paid in 2019; 411.0 written off in 2022; exited in 2025. VMS: bought
  before the window; 357.1 written off in 2024; sold for 160.3 at a further 58.5 loss. WATERPIK: 1,024.6 paid in 2017;
  showerheads exited; trade name at 117% of carrying value. SPINBRUSH: transferred for nominal consideration. About a
  third of the decade's acquisition money (FLAWLESS and WATERPIK, 1,500 of 4,382) went into brands that are now written off
  or flagged by the filer's own impairment test.
- **The growth arithmetic** **[M2001-019]**, **[L2007-010]**: the base business is the "great" savings account, high
  returns and little added capital; the money it throws off is redeployed at the rate of the purchases, which on the
  decade's record is nearer the "good" account, an attractive but not extraordinary rate, with three losses inside it.
  Rising earnings show nothing by themselves **[M2023-081]**: most of the rise in CHD's earnings came with the purchases.
- **WEIGHS: UNDECIDED.** FOR on the capital the business itself needs, among the lowest in its field and earning returns
  on tangible assets at the top of it **[M2010-090]**, **[M1998-081]**; AGAINST on the added capital, which went into
  purchased brands at a decade's after-tax return of at most about 11% on the price, with three write-offs **[M2011-060]**,
  **[M2001-019]**. The "little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]**, eight year-ends from `tools/run.py` (first-filed XBRL; accessions in
`run_py_output.txt`), read against the filed statements of the 10-Ks FY2019, FY2021, FY2023 and FY2025 and the 10-Q of
2026-06-30 (USD millions):

| Year-end | Assets | Equity | Goodwill | Trade names and intangibles | Cash | Receivables (% of sales) | Inventory (% of sales) | Long-term debt | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 6,069 | 2,454 | 1,993 | 2,274 | 317 | 345 (8.3%) | 383 (9.2%) | 1,509 | 3,833 |
| 2019 | 6,657 | 2,668 | 2,080 | 2,750 | 156 | 356 (8.2%) | 417 (9.6%) | 1,810 | 4,237 |
| 2020 | 7,414 | 3,020 | 2,230 | 3,110 | 183 | 399 (8.1%) | 495 (10.1%) | 1,812 | 4,786 |
| 2021 | 7,996 | 3,233 | 2,274 | 3,494 | 241 | 406 (7.8%) | 535 (10.3%) | 1,611 | 5,366 |
| 2022 | 8,346 | 3,490 | 2,427 | 3,432 | 270 | 422 (7.9%) | 647 (12.0%) | 2,600 | 5,525 |
| 2023 | 8,569 | 3,855 | 2,432 | 3,302 | 344 | 527 (9.0%) | 613 (10.4%) | 2,202 | 6,012 |
| 2024 | 8,883 | 4,361 | 2,433 | 2,888 | 964 | 601 (9.8%) | 613 (10.0%) | 2,205 | 6,320 |
| 2025 | 8,912 | 4,002 | 2,628 | 3,512 | 409 | 593 (9.6%) | 535 (8.6%) | 2,205 | 6,768 |
| 2026-06-30 (10-Q) | | 4,348 | 2,650 | 3,743 | 255 | 597 | 602 | 2,206 + 49.9 short | 7,040 |

What the figures are saying **[M2025-032]**: (1) **goodwill and trade names exceed equity in every year**, by 1,813 in
2018 and 2,138 in 2025: tangible equity is negative, and the balance sheet is a record of brands bought, the money for
them having come from retained earnings and debt; (2) retained earnings rose by about 2,935 from 2018 to 2025 while equity
rose by about 1,548, the difference going mostly to buybacks (treasury stock 2,784.8 at 2025-01-01 and 3,648.6 at
2026-06-30, 10-Q equity statement); (3) inventory swelled to 12.0% of sales in the 2022 supply squeeze and is back to 8.6%,
receivables drifted up from about 8% to about 9.6% of sales, neither out of line with the trend of sales **[M1995-064]**;
(4) debt rose by about 1,000 in 2022 for the HERO purchase and has been flat at 2,205 since 2024; (5) the trade names
carry the risk the income account does not show: the WATERPIK trade name alone is 644.7 at 117% cover. What they don't
say: brand-level profits, and whether the purchased names will hold their value. What they can't say: what the next
purchase will cost.

**The real costs.**
- *Depreciation*: plant depreciation 89.7 against capital spending 122.4 in 2025; capital spending ran above
  depreciation in each of 2021 to 2025 (Q3). Owner cash at Q7 deducts all capital spending in one case and plant
  depreciation in the other.
- *Stock pay*: 58.0 in 2025, 59.2 in 2024, 63.6 in 2023, about 5% to 9% of owner cash; deducted in owner cash
  **[L2015-003]**, **[L2021-003]**. The TOUCHLAND founder's $50.0M of shares and the HERO restricted stock ($61.5M) are
  purchase price paid as pay; the company's adjusted EPS excludes the "acquisition-related restricted stock amortization"
  ($0.08 a share in each of 2024 and 2025, 10-K FY2025), which is a real cost taken out.
- *The recurring one-time items* **[L1998-031]**, **[L2016-007]**: FLAWLESS impairment 411.0 (2022); VMS impairment 357.1
  (2024); exit charges 45.6, VMS sale loss 58.5 and TOUCHLAND earnout and stock 30.5 (2025); and in the other direction
  FLAWLESS earnout liabilities released into income of 93.7 (2020) and 98.0 (2021) when the bought business missed its
  targets (statements of cash flows, 10-K FY2021). Five of the six years 2020 to 2025 carry a large acquisition-related
  item. These are the write-offs of money already spent on purchases; Q7 deducts the purchases themselves, so the items
  are not added to owner cash a second time.
- *EBITDA in the filer's mouth*: the revolving credit agreement's one covenant is "Consolidated EBITDA to Interest Expense"
  of at least 3.75 (8-K of 2025-07-18); the impairment notes speak of "EBITA margins". No EBITDA is featured as earnings in
  the releases read.
- *Taxes*: effective rates 19.8% to 23.0% in 2021 to 2025, below statutory federal plus state in part through stock-option
  exercise benefits ("lower stock option benefits" raised the 2025 rate, 10-K FY2025); no carryforward that runs out
  inside ten years was found.

**The habits carried to Q5** (section A of the gaps case: weighed here, judged at Q5).
- *Targets made or beaten* **[L2002-041]**: the headline of every fourth-quarter release read, FY2016 to FY2025, says the
  quarter's figures "EXCEED OUTLOOK" (FY2018: sales and cash flow "EXCEED", EPS "MEET"). Ten of ten.
- *Guidance*: every release gives the next year's outlook for organic sales and adjusted EPS (e.g. "2026 OUTLOOK OF ORGANIC
  SALES GROWTH OF 3-4% and ADJUSTED EPS GROWTH OF 5-8%", release of 2026-01-30).
- *The adjusted figure featured* **[L2016-006]**: the FY2025 release leads with "Adjusted EPS $3.53" beside reported
  $3.02; the 10-K's own MD&A highlights give "Excluding these charges diluted net earnings per share in 2025 was $3.53".
  The exclusions are disclosed and reconciled, including the favourable ones (the 2020 adjusted EPS of $2.83 sat below
  the reported $3.12 because the earnout release was taken out), so the adjustment runs both ways.
- These are habits of presentation, a WEIGHING against **[M1994-018]**; none is confusion or suspicion in the statements.

**Confusion or suspicion?** None found. The segment notes, the net-sales bridges, the impairment notes (with discount
rates, growth assumptions and the cover ratio for WATERPIK) and the cash-flow statements reconcile with one another and
across years. The disclosure of the WATERPIK cover falling from 135% to 117% is the kind of bad news told plainly that the
rows count as a plus **[M1994-018]**. Inventories and receivables move with sales **[M1995-064]**.
- **VERDICT on the accounts: IN (no confusion, no suspicion) **[M1995-063]**; WEIGHS AGAINST** on the presentation habits
  carried to Q5 **[L2002-041]**, **[L2016-006]**, and on the record of purchase write-offs that the adjusted figures leave
  out **[L2016-007]**. The recast earnings for Q7: owner cash after stock pay and capital spending (Step 0 table), with the
  purchases deducted as capital spending.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: "how well they run the business" against "the hand they were dealt", and how they treat the owners
**[M1994-008]**; read from "the proxy statements" **[M1994-009]** and the reports **[M1998-036]**. A marketable part-interest,
so the reading tests carry the weight; there is no seller and no after-the-sale test.

**The people.** Richard A. Dierker, chief executive since Matthew Farrell's retirement on 2025-04-01 (chief financial officer
from January 2016 to March 2025, so the decade's purchases and releases were made on his watch as well; proxy
`0001193125-26-115994`); an independent Board Chairman, Ravichandra Saligram, since October 2025,
before that independent Lead Director. An orderly succession from inside, with the chair separated from the chief
executive.

**Integrity: the record read.**
- *The habits carried from Q4.* Ten of ten fourth-quarter releases headline that figures "EXCEED OUTLOOK"; outlooks are
  given every year; adjusted EPS leads the release. Read with the rest of the record, the habit is one of framing, not of
  making the numbers: the company **missed** its 2025 outlook ("2025 OUTLOOK: 3 to 4% NET SALES GROWTH", release of
  2025-01-31; actual 1.6%) and said so, and the Q4 2025 release states organic growth "lower than the Company’s outlook of
  approximately 1.5%". The annual incentive plan recorded the miss in pay: net sales target $6,148M, actual "as adjusted"
  $6,013M, rating 0.49 of a possible 2.2 (proxy, 2025 Annual Incentive Plan table). The pattern **[L2002-041]** of
  consistently reaching declared targets is therefore not present; the headline habit is a lesser thing, and the rows treat
  preoccupation with presentation as "a negative" short of exclusion **[M1994-018]**.
- *The pay figures differ from the reported ones.* The incentive plan scores "Diluted Earnings Per Share" at an actual of
  $3.57 against reported $3.02 and the release's adjusted $3.53, and cash from operations at $1,225M against the reported
  $1,215.4M. Each adjustment is described as "as adjusted" in the proxy; the reconciliation of the plan figures to the filed
  figures is not given line by line in the pages read. Recorded; it does not raise doubt about honesty, it weighs on Part B
  of Q6 (pay on figures the managers help define).
- *Bad news told plainly.* The impairment notes give the WATERPIK trade name's fall in cover from 135% to 117% with the
  discount rate and growth assumptions, and the VMS impairment with its causes ("significant product competition coming from
  new category entrants, including private label"). That is the owner being told what he would want to know **[M1998-036]**.
- *How mistakes are spoken of* **[L2024-003]**: the word "mistake" does not appear in the 10-K FY2025, the proxy, or the
  FY2024 and FY2025 releases (text search). The three failed purchases are described as a decision "to reposition our
  portfolio" that "enables us to devote greater focus to our portfolio’s faster growing value and premium product lines"
  (10-K FY2025). The facts are disclosed; the word is avoided. Weighs against, mildly.
- *Owners as partners* **[M2004-067]**: no disclosable related-person transactions in 2025; no director or officer shares
  pledged; clawback policy; double-trigger change-in-control vesting (proxy). The board removed its director term limits on
  2025-12-04 (8-K `0001193125-25-309753`), keeping the age-75 retirement rule.
- *Litigation and investigations*: the 10-K FY2025 Legal Proceedings section describes only ordinary-course matters
  (product liability, consumer class actions, employment, antitrust, environmental) with no matter named as material. No
  investigation of the company's accounts or conduct was found in the filings read.
- **Integrity verdict: IN.** No tell of dishonesty in the record read; the habits carried from Q4 are habits of
  presentation, and the record shows targets missed and reported, which is the opposite of the tell the rows name
  **[L2002-041]**. No doubt of the kind that closes the file **[M2013-088]**.

**Ability: the weighing.**
- *Running the business against the hand dealt* **[M1994-008]**: organic sales growth of 3.2%, 2.7%, 4.3%, 4.4%, 9.6%, 4.3%,
  1.4%, 5.3%, 4.6% and 0.7% in 2016 to 2025 (the releases), against a field in which Clorox's tangible return fell to 8.2%
  and Kimberly-Clark's operating margin to 11.5% in the same inflation (Q2 row); margins restored by 2024. The operating
  record is good.
- *Capital allocated over time* **[M1994-008]**: three of the decade's purchases failed and were exited (Q3); the WATERPIK
  purchase, the largest at $1,024.6M, is flagged by the company's own impairment test. Weighs against, and is Q6's subject.
- **Ability: WEIGHS FOR** on operations, **AGAINST** on the record of purchases, carried to Q6.
- **VERDICT on integrity: IN; ability WEIGHS FOR (operations) and AGAINST (capital allocation).**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *Where the money went, 2016 to 2025* (statements of cash flows; XBRL series checked against the 10-Ks FY2025 and FY2023):
  owner cash 7,749 in all (Step 0 table); purchases of businesses 4,381.5 (less 173.9 of divestiture proceeds); buybacks
  3,250.1 (400.0, 400.0, 200.0, 250.0, 300.0, 500.0, 0, 300.1, 0, 900.0); dividends 2,381.3; option-exercise proceeds of
  about 730 came back in. Long-term debt rose from 693.4 at 2016-12-31 (10-K FY2016) to 2,205 (the 2017 notes of 1,425.0
  financed WATERPIK). The stated policy is to keep buying: "pursue strategic acquisitions", and to take
  international sales "from $1 billion to $2 billion" "with a focus on M&A" (10-K FY2025). Since 2025-12-31 a further
  $300.0M plus $25.0M deferred went to MISS MOUTH'S MESSY EATER, a brand with about $80.0M of 2025 sales (10-Q of
  2026-06-30), about 4 times sales.
- *The retention test* **[R1995-009]**, **[M1998-110]**: over the five years 2021 to 2025 the company kept about $8.04 a
  diluted share of earnings after dividends (net income less dividends each year over the diluted count: 2.32, 0.65,
  1.98, 1.25, 1.84). The quote went from $87.23 (2020-12-31) to $83.85 (2025-12-31) (aggregator closes, flagged): **the
  market-value leg fails over the five years**, about $3.38 lost against $8.04 kept. Over the ten years 2016 to 2025 the
  quote rose from $44.19 to $83.85 against about $16 a share kept, and the leg passes; much of that rise came from a higher
  multiple of the same cash (the owner-cash yield at the 2016 quote was higher than today's), which the rows warn the
  market leg alone can mislead on **[R2009-002]**.
- *Buybacks* **[L1999-023]**, **[L2011-003]**, **[L2016-002]**: no price above which purchases stop is stated in any filing
  read. Part of the buying is under an "evergreen share repurchase program" whose stated purpose is "to reduce or eliminate
  dilution associated with issuances of Common Stock under our incentive plans" (10-K FY2025): buying to cover option
  issuance, which the rows rule out as a reason **[M2014-008]**: "It’s got nothing to do with preventing dilution"
  **[M2016-049]**. The prices paid in 2025: $95.71 (ASR, May to August, $300.0M), $92.81 (August and September, $300.0M),
  $83.59 (November and December, $300.0M); in 2023 3.3M shares for $300.1M (about $90.9); in 2021 at prices from $82.40 (October, Item 5 table, 10-K FY2021) to a year-end quote of $102.50.
  **The CONVENTION test** (a programme with no stated price is read by the prices paid against the bottom of the Q7
  range, run when Q7 is reached and recorded here): the Q7 range below is $56.49 to $65.75 a share on the default pair and
  $65.75 to $78.93 on the organic pair; **every 2025 purchase price sits above the top of both**. Weighs against.
- *Issuance and deals* **[M1995-001]**, **[L2014-012]**: no all-stock deal; the one STOP of Part A **[L2009-019]** is not
  engaged. Stock used in deals is small (HERO restricted stock $61.5M, TOUCHLAND founder shares $50.0M). Value given against
  value got, in the decade: FLAWLESS 475.0 for a business written down by 411.0 in three years and exited; WATERPIK 1,024.6
  for a business whose showerheads were exited and whose trade name now sits at 117% cover; VMS written off and sold. A
  post-mortem against the projections **[L2014-013]** is not published; the exits are presented as repositioning (Q5).
- *Dividends*: 287.2 in 2025, about 28% of 2025 owner cash, raised every year (4.2% for 2026, 10-K FY2025). Clear and
  consistent.
- **Part A: WEIGHS AGAINST.** The cash the business throws off goes first to purchases whose decade record includes three
  failures (Q3), and second to buybacks with no stated price, partly to offset option dilution, at prices above every Q7
  range; the five-year retention leg fails.

**Part B: the pay, the board and the owners.**
- *The proxy* **[M1994-009]** (`0001193125-26-115994`): chief executive pay $9.80M in 2025 (Dierker, first year in role),
  the predecessor $12.28M in 2024 and $11.22M in 2023; option awards are the largest part (2025: $5.31M of options). The
  annual plan scores five measures at 20% each: net sales, gross margin, diluted EPS "as adjusted", cash from operations
  and qualitative "Strategic Initiatives"; 2025 paid at 1.25 (114% of opportunity). The long-term plan is options and
  performance units on relative total shareholder return, with three-year cumulative cash from operations added from 2026.
- *Tied to what the person controls* **[M2003-019]**: net sales, gross margin and cash from operations are under the
  managers' control; relative TSR is the market's verdict, not theirs. The net-sales target was scored on a figure
  "as adjusted" ($6,013M against reported $6,203.2M), which appears to take out the TOUCHLAND purchase; a plan that does
  not pay for bought sales is the better kind.
- *Options* **[L1994-021]**, **[M1997-043]**, **[M2003-018]**: ten-year fixed-price options vesting at three years
  (proxy), with no step-up for retained earnings; the company pays a dividend of about 1.3% of the price and buys back
  stock, and the option holder "benefits from retained earnings and benefits not at all from dividends" **[M2003-018]**.
  The proxy does not name the dividend conflict.
- *The board*: independent chair since October 2025; fully independent audit, compensation and governance committees;
  directors paid about $280,000 to $346,250 a year, mostly in stock; an independent compensation consultant is engaged,
  which the rows count against **[M2004-016]**; director term limits removed in December 2025.
- *Owners*: executive ownership guidelines of 6 times salary for the chief executive; no pledged shares; no related-person
  transactions in 2025; outlooks given every year (Q4, Q5).
- **Part B: WEIGHS AGAINST, mildly.** Ordinary large-company pay: fixed-price options with no step-up, a market-relative
  long-term measure, a consultant, and figures "as adjusted"; offset by an independent chair and a sales measure that does
  not reward purchases.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate **[L2000-021]**, **[M1996-025]**, credited "for whatever net cash is left every year"
**[M1998-080]**, with the question "are you going to have to put more cash into after you buy it?" **[M2014-068]**. The
construction is the framework's CONVENTION (Q7, the range, its four and six specifics, the floor, whose tax, the basis);
arithmetic in `q7.py`, output in `q7_output.txt`, in the working folder.

**Inputs** (USD millions; Step 0 table and the filed statements):
- *Basis*: all-equity **[L2017-004]**. Owner cash before interest = owner cash plus net interest after the company's own
  effective tax (2021 to 2025: 43.7, 70.9, 76.5, 53.2, 55.2). Net debt at the latest filed date, 2026-06-30 (10-Q
  `0001193125-26-327567`): short-term borrowings 49.9 plus long-term debt 2,206.3 less cash 254.8 = **2,001.4**; no finance
  leases found; operating leases left out; the 10-Q states no subsequent event that adds debt. Net debt already contains the
  2026 cash paid for MISS MOUTH'S ($300.0M) and the TOUCHLAND earnout, so those are not deducted again; MISS MOUTH'S is
  credited at nothing, its earnings not yet filed (specific (c)).
- *Tax*: the company's own, no conversion (Whose tax). Effective rates 19.8% to 23.0%; no carryforward or credit that runs
  out inside ten years was found.
- *Five-year window 2021 to 2025*: owner cash before interest after all capital spending averages **904.1**; after plant
  depreciation only (the maintenance guess, Q3) **992.5**. Net purchases of businesses average **322.4** a year (556.0,
  546.8, 0.0, 13.3, 495.7, net of divestiture proceeds).
- *Growth shown* (on the aggregate cash, not per share): owner cash before interest after all capital spending went from
  895.0 (2021) to 1,090.2 (2025), **5.06%** a year. Organic sales growth as the filer reports it, 2021 to 2025 (4.3%, 1.4%,
  5.3%, 4.6%, 0.7%), compounds to **3.24%** a year. Both are below the 5.64% discount rate; no cap binds (specific (f)).
- *Specific (a), cycles*: the filer does not call 2021 or 2025 aberrational; the window holds the 2022 inflation trough,
  two purchases and the VMS sale, so the ten-year whole-cycle variant (2016 to 2025) is shown beside it, as the brief asks.

**The cases**, ten years at the growth then no growth, discounted at 5.64%:

| Case | Cash a year | Growth | Enterprise value | Per share (less 2,001.4 net debt, 237.204M shares) | Expected return at the price |
|---|---|---|---|---|---|
| A. No growth, maintenance spending only | 992.5 | 0% | 17,598 | **$65.75** | 3.99% |
| B. Total growth credited, all capital spending and net purchases deducted (the default pair) | 581.7 | 5.06% | 15,402 | **$56.49** | 3.60% |
| C. Organic growth credited, purchases left out (the organic pair, shown beside) | 904.1 | 3.24% | 20,724 | **$78.93** | 4.73% |
| Whole cycle A (2016-2025) | 872.6 | 0% | 15,472 | $56.79 | 3.50% |
| Whole cycle B | 406.3 | 6.71% | 12,268 | $43.28 | 2.93% |
| Whole cycle C | 827.1 | 4.02% | 20,169 | $76.59 | 4.62% |

The expected return is the rate at which each case's cash stream equals the enterprise value at the price, $22,900M of
market value plus 2,001.4 of net debt = 24,901.

**The finding inside the range** (specific (e)): the growth case with the purchases paid for (B) is worth **less** than
the no-growth case (A), in the window and over the whole cycle: the decade's purchases bought growth worth less than its
cost at the long rate. The rows: "growth can destroy value if it requires cash inputs in the early years of a project or
enterprise that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**.
By specific (e) the no-growth case is then the top of the range and the growth case the bottom; the inversion is the
finding, not an error.

**Value range:** **$56.49 to $65.75** a share on the default pair (width 1.16 to 1; with the organic pair beside, $65.75 to
$78.93; whole-cycle variant $43.28 to $56.79, organic beside $56.79 to $76.59), against **$96.54**.
- **Closes:** the range is far narrower than three to one, so not TOO HARD. The price sits **above the top of every range
  built**, including the most generous (organic growth credited, the purchases ignored, $78.93). By the floor CONVENTION a
  price above the top of the range closes OUT: the expected return at the price is **3.6% to 4.7%** on the all-equity basis
  (equity-only 3.5% to 4.8%), against a floor of about ten percent **[M2003-149]**, **[M1994-004]**, **[L2002-020]**, and
  below the 5.64% long bond itself. "So, there’s just a point at which we drop out of the game." **[M2003-149]**. No pencil
  is needed to see it; the case is not close in the buyer's favour **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** the price at which the midpoint of the range earns the
  floor, read in this run as the price at which the mean of the two end cases' cash streams yields 10% (a CONVENTION of
  this run, confessed below under "What in the framework was wrong or unclear"), after the company's own tax:
  **$29.83 a share on the all-equity basis** (default pair; organic pair beside, $36.26); **equity-only $35.17** (default;
  organic $41.86), owner cash after interest against the market value. The all-equity figure is the central one. No cheap
  price is reported.
- **Buyback test recorded back at Q6**: every 2025 repurchase price ($83.59 to $95.71) sits above the top of the range.
- **VERDICT: OUT.** Valued, narrow range, price above it; the expected return at the price is below the floor
  **[M2003-149]**, **[L2013-012]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**: value range **$56.49 to $65.75** a share on the default pair (all-equity, five-year window; organic pair
beside $65.75 to $78.93; whole-cycle variant $43.28 to $56.79) against **$96.54** (2026-10-06, aggregator); expected return
at the price 3.6% to 4.7%, below the floor of about ten percent **[M2003-149]**. Q1 IN, Q2 IN (Consumer Domestic decides),
Q3 UNDECIDED, Q4 accounts IN and weighs against, Q5 integrity IN, Q6 weighs against. Reporting figures: value range as
above; fair price **$29.83** a share all-equity (equity-only $35.17). No integrity facts are left unjudged (Q5 was reached
and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged; operator rule 2.)* **[M1997-127]**
- **Q8, the bond.** The 30-year Treasury par yield was 5.64% on 2026-10-06 (`tools/sources.py`); the expected returns
  computed at Q7 at the price are 3.6% to 4.7% on the all-equity basis and 3.5% to 4.8% equity-only.
- **Q9, debt and exposures** (10-Q `0001193125-26-327567`; 8-K `0001193125-25-161241`; 10-K FY2025): senior notes of
  $425.0M due 2027-08-01 (3.15%), $400.0M due 2031 (2.3%), $500.0M due 2032 (5.6%), $400.0M due 2047 (3.95%), $500.0M due
  2052 (5.00%); commercial paper $49.9M at 2026-06-30; cash $254.8M. An unsecured $2.0B revolving credit facility to
  2030-07-17 with one covenant, Consolidated EBITDA to interest expense of at least 3.75. 2025 operating income $1,077.6M
  against interest expense $95.2M, about 11 times. Customer concentration: Walmart about 23% of net sales, top four about
  44%, with orders "based primarily upon individual sales orders rather than long-term contracts" (10-K FY2025). The
  10-K names product liability and consumer class actions as ordinary-course exposures; none is named as material.
  The WATERPIK trade name ($644.7M) sits at 117% of carrying value, a non-cash exposure to a further write-down.
- **Q12.** The products are household cleaning and laundry, oral care, baking soda, cat litter, condoms, lubricants and
  vibrators (TROJAN), pregnancy tests, depilatories, acne and cold remedies, hand sanitizer, and animal-feed additives. None
  is among the businesses the framework names (casinos, tobacco, distributor-loading schemes, gambling dressed as investing,
  promotion on a borrowed reputation).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits a6e223a0 (Step 0 to the standing rule), 1020fe6c (Q1), 20c82b23 (Q2), 7eacedc4 (Q3), e7873d61 (Q4),
      bed8b3dd (Q5), e38c1bc9 (Q6), ebe553b3 (Q7), and the close.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; a lock file was present in
      `Screens/_daily/` at the start (held by the dispatching session, not written or touched here); the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared
      under CONTAMINATION at the top: the name of an earlier CHD research folder in the starting git status, commit subjects
      for four other companies, and a general memory line. None used.
- [x] Every v5 id resolves (checked by `check_ids.py` in the working folder against `principle_ledger_v5.csv`); every
      filing fact has its accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 NOT REACHED; nothing after it is
      a clearance.
- [x] Owner cash after every real cost (stock pay and all capital spending, with the maintenance case beside and the
      purchases of businesses deducted in the default pair), never a net-income proxy (operator rule 5); the sovereign
      from the issuing authority (US Treasury); aggregator quotes flagged (the price and the historical closes used at Q6).
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, and each question); the facts found
      for later questions are under AFTER THE STOP. No integrity facts are left unjudged.
- [x] No row dated after the anchor is cited (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-earnings figures were recomputed from the
      filed cash-flow lines.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the closing commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The fair price is defined in words that admit two readings.** "The price at which the midpoint of the range earns the
floor" could mean the midpoint value re-priced at 10%, or the cash stream midway between the two end cases discounted at
10%. This run used the second: the mean of the two end cases' cash streams, discounted at 10% for ten years and then
perpetually at no growth (a CONVENTION of this run; rationale: it is the only reading in which "earns the floor" is an
expected return on a price, as the floor rows speak of it). (2) **Specific (e)'s inversion meets specific (c)'s pair with
no rule for which end is the range.** For a serial buyer the default pair (purchases deducted, total growth credited)
gives a growth case worth less than no growth; (e) then makes the no-growth case the top. But the no-growth case
deducts no purchases, while this company's own record shows its portfolio losing three brands in a decade without them;
whether "standing still" for a brand buyer includes some buying is not said. The run reported both pairs and the
whole-cycle variant, and the close does not depend on the choice (the price is above every case). (3) **The parts rule
stops at the segment.** Consumer Domestic is a row of brands with very different castles (decades-old household names and
three-year-old trend brands, three of which failed); the filer reports no brand profits, so section B decides on a
segment that averages strong and weak castles, and Q2's verdict is the average's. (4) **Q2 test 9 ("ask the
competitors") cannot be run from the public record** for a part-interest; the run said so. (5) **The growth shown is an
end-to-end rate** and is sensitive to the end years (2021 to 2025: 5.06%; 2016 to 2025: 6.71%). **The brief's error:** it
names Kimberly-Clark as a competitor, which the CHD 10-K does not name and whose categories (tissue, diapers) barely touch
CHD's, and omits Kenvue and Edgewell Personal Care, U.S. SEC filers that the 10-K names; the run read those two and kept
Kimberly-Clark as a field reference only. A lesser one: the brief told the analyst that earlier CHD runs exist, a fact
about the name's history that the blind rule otherwise keeps from the analyst.
