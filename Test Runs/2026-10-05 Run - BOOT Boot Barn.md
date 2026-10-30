# Company Run — Boot Barn Holdings, Inc. (NYSE: BOOT) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched under a blind rule that forbids
opening `PORTFOLIO.md`; the analyst does not know whether the operator holds this name. **Contamination declared:** the
recent commit subjects visible at session start name other runs' boxes (MBUU, among others); none names BOOT. No other
`Test Runs/` file about Boot Barn was opened (a directory listing filtered on "boot" returned nothing before the file
was copied). The analyst's general memory of Boot Barn (a fast-growing western retailer, a CEO who left in late 2024)
predates the run and is set aside; every fact below is from a filing read today.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $123.43 (close 2026-10-05, Yahoo Finance chart endpoint via `tools/sources.py`; **aggregator, live quote
  only, flagged** under operator rule 5). `tools/run.py` printed $121.82 earlier in the session; the difference is
  intraday and immaterial. Recent path, same source: $152.60 on 2026-09-08, $142.84 on 2026-09-14, $128.37 on
  2026-09-15 (the day of the Goldman Sachs fireside chat announced in the 8-K of 2026-09-14), $120.47 on 2026-09-30.
  Two-year high in the series about $201 (2025-12-03).
- **Shares by class** from the latest filing's cover: **30,284,844** common, $0.0001 par, one class (10-Q for the
  quarter ended 2026-06-27, filed 2026-07-29, accession `0001104659-26-088262`; `python Screens/cover_shares.py BOOT`).
- **Market cap:** 30.285M × $123.43 = **$3,738M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2026 (52 weeks ended 2026-03-28), filed 2026-05-14, accession `0001104659-26-061346`.
  - 10-Q for the quarter ended 2026-06-27, filed 2026-07-29, accession `0001104659-26-088262`.
  - DEF 14A for the 2026 annual meeting (2026-08-26), filed 2026-07-16, accession `0001104659-26-084071`.
  - 8-Ks: 2024-10-28 `0001558370-24-013745` (CEO resignation); 2025-05-05 `0001558370-25-006307` (CEO appointed);
    2026-01-05 `0001104659-26-000612` (executive chairman reverts); 2026-05-14 `0001104659-26-061169` (FY2026
    results, Ex. 99.1); 2026-07-29 `0001104659-26-088137` (Q1 FY2027 results, Ex. 99.1; revolver amendment No. 6);
    2026-08-27 `0001104659-26-102449` (2026 equity plan, vote results); 2026-09-14 `0001104659-26-107497`
    (quarter-to-date sales update, Ex. 99.1).
  - Older 10-Ks and the IPO prospectus for the history: listed where used (Q2, Q4).
- **One figure cross-checked against the filed statement:** operating cash flow FY2026 **$304,903K** in the 10-K's
  cash-flow summary (MD&A, Cash Position and Cash Flow, `0001104659-26-061346`) against $305M in `tools/run.py`'s
  XBRL line: agrees. Net income FY2026 $225,880K (10-K statement of operations) agrees with the XBRL vintage.
- `python tools/run.py BOOT`, arithmetic lines only (its "OE" labels, yields and any rule text are not used; Part VII):

  | FY end | OCF | SBC | D&A | capex |
  |---|---|---|---|---|
  | 2024-03-30 | 236 | 13 | 50 | 119 |
  | 2025-03-29 | 148 | 11 | 62 | 148 |
  | 2026-03-28 | 305 | 16 | 79 | 179 |

  ($ millions.) Known defects checked against the filing: the share count is the 2026-07-24 cover count (no split since
  the IPO found in the filings read); stock pay FY2025 of $11.0M is net of a **$6.7M net benefit** from the former
  CEO's forfeited awards (10-K FY2026 MD&A, SG&A paragraph), so it understates the run rate; OCF contains no securities
  purchases (the company holds cash only); the debt column is not used (no funded debt; leases treated at Q9). The
  owner-cash recast is done at Q4 from the filed cash-flow statements, not from these lines.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. **A share is a business:** the test is whether one would be content to own it "if
the market closed for five years" **[M1997-109]**; for a retailer that question is about the stores' trade ten years out,
not about the quote. **The market serves:** the price fell from $152.60 (2026-09-08) to $120.47 (2026-09-30) while the
company was reporting a 17.7% sales increase for the June quarter and guiding the September quarter to the high end of
its range (8-Ks `0001104659-26-088137`, `0001104659-26-107497`); the quotation "doesn’t tell us anything. It just tells
us prices." **[M2006-077]**, so the fall is neither a reason to buy nor evidence against the business. **Who is paid to
tell you:** the 8-K of 2026-09-14 is a conference schedule with a quarter-to-date sales line attached; the company gives
quarterly and annual guidance (Ex. 99.1 of `0001104659-26-088137`), and the two conferences it announced are hosted by
brokers (Goldman Sachs, Piper Sandler); "you do not get impartial advice from Wall Street" **[M2020-037]**. No macro view enters **[M2000-094]**;
what counts is "the average profitability of the business over time and how strong its competitive mode is" **[M2015-016]**.
**Contrary evidence, written down as found** **[M1997-127]**, looking for "what’s wrong" and "what you’re missing"
**[M2025-013]**, in the order met:
1. The filings say the business is not fashion-driven ("neither the western nor the work component of our business has
   been meaningfully impacted by fashion trends", 10-K FY2026 MD&A) while same store sales rose **53.7%** in FY2022 and
   fell **6.2%** in FY2024 (10-Ks `0001558370-22-008393`, `0001558370-24-008176`). The FY2022 10-K explains the surge by
   the COVID-depressed prior year and closed stores, not by fashion. The words and the record do not sit easily together.
2. Against my own doubt about the step-up: average sales per comparable store were $4,194K (FY2022), $4,190K (FY2023),
   $4,081K (FY2024), $4,116K (FY2025), $4,186K (FY2026); the post-2022 level has held four years through a down year,
   where a fad would have been expected to fall back toward the FY2021 level of $2,602K.
3. Against the doubt again: loyalty members who bought in the prior three years were 4.3M (FY2020), 5.8M (FY2022), 8.4M
   (FY2024), 10.8M (FY2026) (10-Ks); per store about 16.6K (FY2020) and 20.0K (FY2026). The customer base did not shrink
   after the boom.
4. For the doubt: the cost of every new store has risen faster than its trade. Net cash investment per new store was
   $670K at the IPO (prospectus `0001047469-14-008690`), $0.8M from FY2018 to FY2021, $1.2M (FY2022), $1.4M, $1.5M, $1.7M
   (FY2025 and FY2026), with the three-year payback target unchanged.
5. For the doubt: the operating income added since FY2022 is small against the capital added (computed below: about
   $41M of added operating income on about $695M of added net tangible operating assets, FY2022 to FY2026).
6. Against the doubt: Academy Sports, a pandemic-boom retailer, gave back most of its margin step (operating margin 13.4%
   in its fiscal 2021 to 8.5% in fiscal 2025); Boot Barn's fell from 17.4% to 11.9% and rose again to 13.3%.
7. For the doubt: same store sales are decelerating again: +7.2% (FY2026), +4.7% (Q1 FY2027), guidance of flat to +2.0%
   for Q2 FY2027 with retail stores at -1.0% to +1.0%; fiscal July "came in slightly below our expectations"; fiscal
   August +2% (8-Ks `0001104659-26-088137`, `0001104659-26-107497`).

## THE STANDING RULE
Bought for cash, with no borrowed money, and sized so that a fall of half or more "and be comfortable with it"
**[M2020-022]** changes nothing for the buyer, the purchase cannot ruin the buyer; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, and nothing here is bought "for what we don’t have and don’t need" **[M2012-081]**.
The standing rule is met by the buyer's conduct, whatever the questions conclude.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**; understanding is "a reasonable fix on about
  what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; "where the
  business will be in 10 years" **[M2000-037]**.
- **What the business is, from the 10-K FY2026 (`0001104659-26-061346`).** 539 leased stores in 49 states at 2026-03-28
  (577 by 2026-09-14), averaging 11,400 selling square feet; boots 46% of sales, apparel 37%, the rest hats, accessories
  and gifts; western styles about 75%, work about 25%; men's about 60%; e-commerce 10.4% of sales. Exclusive brands
  (Cody James, Shyanne, Idyllwind, Hawx and others) 40.8% of sales, with "higher merchandise margins than the third-party
  brands"; top three suppliers about 25% of sales. "more than four times as many stores as our nearest direct
  competitor"; target of about 1,200 domestic stores. Founded 1978; grown by building stores and by buying rival chains
  (RCC, Baskins, Sheplers in 2015) and rebranding them.
- **The key variables and how predictable they are** **[M1998-044]**: (a) sales per store; (b) the number of stores and
  what each new one costs and earns; (c) merchandise margin, driven by the exclusive-brand mix; (d) occupancy and store
  labour. (b), (c) and (d) have a long, legible record in the filings. (a) is the variable that moved most: average
  sales per store $2,602K in FY2021 and $4,194K in FY2022, a 61% step in one year, flat in dollars since.
- **Do the statements tell the future ones** **[M2008-033]**: for the mechanics, yes. No funded debt, no acquisitions
  since FY2020, goodwill unchanged at $197.5M since FY2020, no adjusted-earnings presentation in the 10-K, a plain
  cash-flow statement. The economic dynamics are understood in the sense of **[M2011-014]**: buy boots and jeans from
  vendors or make them under its own labels, sell them through leased boxes; the open matter is the moat and the "ease
  of entry" that **[M2011-014]** names, which is Q2's.
- **Customers, not technology** **[M2017-019]**, **[M2023-030]**: the forecast is of consumer behaviour, of the kind the
  rows say can be projected.
- **The doubt, stated.** The narrated warning is retail: "it’s easy to sort of think you understand retail, and then
  subsequently find out you don’t" **[M2014-052]**; and "if you have doubts about something being into your circle of
  competence, it isn’t." **[M2002-092]**. My doubt is not about what this business does or how its figures are made; it
  is about whether the per-store trade of 2022 to 2026 and the competitive position behind it will hold for ten years.
  That is the castle question, which Q2 owns; Q1's routing sends a business to TOO HARD here only when "its industry
  changes fast", and boots, work wear and leased stores do not.
- **VERDICT: IN.** The economics of a specialty boot and work-wear retailer can be read from its filings and the key
  variables named **[M1998-044]**, **[M2012-065]**; the doubt is carried to Q2 and written there, not dissolved.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they? How much do they depend on the
genius of the lord in the castle?" **[M1995-038]**. Competitors "will repeatedly assault any business "castle" that is
earning high returns" **[L2007-004]**.

**Filing facts, test by test.**
1. **Key factors and their permanence** **[M1995-038]**. The 10-K names scale (four times the nearest specialty rival),
   supplier terms ("In many cases, we are one of the largest accounts of our suppliers"), the exclusive brands (40.8% of
   sales; about 10% in FY2015 `0001047469-15-005099`, 13.5% FY2018, 22.0% FY2020, 28.3% FY2022, 37.7% FY2024), the loyalty
   file (10.8M members; "The majority of our sales are made to these customers"), and site selection. These are real and
   have widened for a decade. Their permanence over ten to twenty years is the question; nothing in the filings shows the
   See's kind of fact, reasons for buying "virtually unchanged" for decades **[L1996-028]**: one year moved trade per
   store by 61%.
2. **Would it stand without the lord?** The rows put retail on the wrong side of this test by name: "In retailing, to
   coast is to fail." **[L1995-008]**; "retailing is a good case of a business where you have to stay smart" **[M1995-040]**;
   "Buying a retailer without good management is like buying the Eiffel Tower without an elevator." **[L1995-006]**.
   The filing fact in its favour: the chief executive resigned to "pursue a different opportunity" effective 2024-11-22 (8-K
   `0001558370-24-013745`); the chief digital officer became interim and then permanent CEO on 2025-05-05 (8-K
   `0001558370-25-006307`); same store sales were +5.5% in FY2025 and +7.2% in FY2026 under him. The castle did not
   stumble when the lord left, which is evidence, though over eighteen months only.
3. **The money test** **[M2011-015]**: could a well-funded attacker take it? A new store costs about $1.7M net (10-K
   FY2026); about $1B would build some 600 boxes; 59% of sales are third-party brands any retailer can stock, and the
   rows' warning is that "you can create another airline" **[M2013-054]**. What a new chain could not buy quickly: the
   exclusive-brand programme, the supplier terms and the loyalty file. On the public record, attackers exist: Tecovas,
   Inc. (private; western boots, direct and its own stores) filed Forms D reporting equity sold of $14,999,899 (first sale
   2020-02-07, `0001686840-20-000001`), $35,000,000 (2021-12-30, `0001686840-22-000001`) and $9,999,990 (2025-06-17,
   `0001686840-25-000002`), revenue "Decline to Disclose". Cavender's (private, family-owned) files nothing found in an
   EDGAR full-text search for "Cavender" (2019 to 2026); its store count and economics are not on the primary record.
   Tractor Supply sells clothing and footwear inside a "Clothing, Gift & Décor" category that is 10% of its $15.5B of
   sales from 2,602 stores (10-K FY2025, `0000916365-26-000014`); Academy Sports reports footwear sales of $1,201.5M
   including "Work and western boots" (10-K FY2025, `0001817358-26-000031`). Why "are there no new entrants into the
   field?" **[M2000-077]** is not the question here: there are entrants, and whether they are taking anything cannot be
   read from filings because the specialty ones are private. "one competitor is frequently enough to ruin a business"
   **[M2012-108]**.
4. **Pricing power** **[M2005-020]**, **[M2000-031]**. Gross margin 30.2% (FY2017) to 38.1% (FY2026); merchandise margin
   rate up 90 bp (FY2020), 90 bp (FY2021), 270 bp (FY2022), down 70 bp (FY2023, freight), up 160 bp (FY2024), 130 bp
   (FY2025), 80 bp (FY2026), the stated causes being exclusive-brand mix, full-price selling, buying scale and freight.
   This is mix and scale more than price on the same goods; a monthly promotional calendar is described in the 10-K.
   Weighs for.
5. **Unit volume and share of mind** **[M1999-054]**, **[M1997-099]**. Same store sales: +17.5% (FY2012), +11.9%, +6.7%,
   +7.3% (FY2015), -0.1% (FY2016, oil regions), +0.3%, +5.2%, +10.0%, +5.0%, +3.1% (FY2021), +53.7% (FY2022), -0.1%, -6.2%
   (FY2024), +5.5%, +7.2% (FY2026), +4.7% (Q1 FY2027), guided flat to +2.0% (Q2 FY2027). The IPO prospectus shows 19
   positive quarters beginning with the quarter ended December 2009 at +1.0%; the quarters of the 2008 to 2009 recession
   are not printed (the chart starts there and the text gives no annual figure), so the run of positive comparisons
   began after them. Average sales per comparable store flat in dollars for four years ($4.19M, $4.19M, $4.08M, $4.12M,
   $4.19M), which is a fall in real terms.
6. **The low-cost position** **[M2018-043]**: against independents, scale buying; against Tractor Supply, no. Boot Barn's
   operating margin was below Tractor Supply's in every year FY2017 to FY2021 and above it in every year since (table
   below); the change came with the demand step, not with a change in cost position shown in the filings.
7. **The brand in the customer's mind** **[M2015-038]**, **[M2001-090]**. Boot Barn is a retailer pulling value from its
   vendors' brands to its own: "three of our five top selling brands were exclusive brands" (10-K FY2026). Where the
   retailer is trusted "as much as" the brand, "the value of having the brand moves over to the retailer" **[M2001-090]**.
   Weighs for. Against: the largest western brand on its shelves also sells direct, and the filings do not show what
   share of the vendor's trade Boot Barn is.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. For the 59% of sales that are third-party
   brands the same boot is sold elsewhere; what holds the customer is breadth, fit, in-stock and service, which the
   10-K describes and does not measure. For the 41% exclusive, the customer has no like-for-like low bid. Unanswered from
   the filings.
9. **Ask the competitors** **[M1999-130]**: not possible from the public record; the 10-K names no competitor, and the
   proxy's peer group (Buckle, Caleres, DBI, Genesco, Tractor Supply, Wolverine, Zumiez) contains no western specialist.
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**, **[M2000-075]**. Widening: exclusive-brand share,
    merchandise margin, loyalty members, e-commerce same store sales (+15.3% FY2026). Narrowing: trade per store flat in
    dollars; the cost of a new store up from $0.8M (FY2021) to $1.7M against sales per store up about 61%; the return on
    the capital added since the FY2022 peak low (Q3 computation below).
11. **What could destroy, modify or reduce it** **[M2000-014]**. The company's own risk factor: "a general trend in
    consumer preferences away from boots and other western or country products". The FY2022 step came in one year, and
    the row warns that "if something can gain competitive advantage very quickly, you have to worry about them losing it
    quickly, too" **[M2002-050]**; "slow change can be much harder to perceive" **[M2014-038]**.

**The competitor row** (operating income ÷ net sales, from each company's filed 10-Ks via XBRL company facts; BOOT
fiscal years end late March, TSCO December, ASO late January and labelled by the year the fiscal year begins; whole
spans, not one year):

| Year | BOOT | TSCO | ASO |
|---|---|---|---|
| 2017 | 6.0% | 9.5% | |
| 2018 | 6.8% | 8.9% | 2.7% |
| 2019 | 8.3% | 8.9% | 3.7% |
| 2020 | 8.7% | 9.4% | 7.4% |
| 2021 | 9.7% | 10.3% | 13.4% |
| 2022 | 17.4% | 10.1% | 13.2% |
| 2023 | 14.0% | 10.2% | 11.0% |
| 2024 | 11.9% | 9.9% | 9.1% |
| 2025 | 12.5% | 9.5% | 8.5% |
| 2026 | 13.3% | | |
| **Mean of the span** | **10.9%** (FY2017 to FY2026) | **9.6%** (2017 to 2025) | **8.6%** (2018 to 2025) |

Accessions: BOOT 10-Ks listed in Step 0 and Q4; TSCO `0000916365-18-000031` through `0000916365-26-000014`; ASO
`0001817358-21-000059` through `0001817358-26-000031`. Gross margins over the same spans: BOOT 30.2% to 38.1%, TSCO
34.2% to 36.4%, ASO 28.6% to 34.8%. Cavender's, Tecovas and Ariat's own stores: private, no figures on the primary
record (flagged). Over the whole span Boot Barn earns somewhat more on sales than the rural general retailer and the
sporting-goods chain; before the step it earned less than the rural retailer, and after it more.

**Reading.** The castle is not shown open: it has stood for decades, it consolidated its rivals, its exclusive-brand
and margin record has widened for ten years, its customer file has grown through the post-boom hangover, and it kept
more of its boom than the sporting-goods comparison did. So the file does not close OUT **[M2011-015]**. But the
question asked is what keeps it standing "five, 10, 20 years from now" **[M1995-038]**, and on the evidence read I
cannot judge it: the trade per store that the present economics rest on arrived in one year and has not grown since;
the specialty attackers are private and unmeasurable from filings; the rows name retail as the field where the castle
depends on the lord and where "Your competitor is always copying and then topping whatever you do" **[L1995-008]**; and
"Leadership alone provides no certainties" **[L1996-031]**. Where the moat is "tenuous in any way", "We don’t know how
to valuate that, and therefore we leave it alone." **[M2000-019]**. The routing: a castle whose future cannot be judged
closes TOO HARD **[M2006-013]**.

**Which cause.** WORK, not NATURE, on the evidence that the deciding sub-questions are "important and knowable"
**[M2006-076]** from primary documents not yet read in full: the filings over a longer run of years (store cohorts,
loyalty counts, the oldest regions' comparisons, the 2008 to 2009 figures if the earlier S-1 filings print them), Tractor
Supply's and Academy's category trends, and Tecovas's and Ariat's public record. The industry's insiders do write this
kind of forecast down: Boot Barn's own 10-K writes a 1,200-store target and a 10% annual unit growth rate, which is not
the "That’s too hard." of **[M2000-105]**. If the pass ends unsure it ends TOO HARD (NATURE) **[M2002-092]**.

- **VERDICT: TOO HARD (WORK).** The castle is visible and not shown to be filling in, but whether it holds the present
  per-store economics for ten to twenty years cannot be judged from the evidence read **[M1995-038]**, **[M2000-019]**,
  **[M2006-013]**. The file closes here. Q3 to Q12 are NOT REACHED; every figure below this line is COMPUTATION.

---
## Q3 to Q12: NOT REACHED
Q3 (capital), Q4 (the numbers), Q5 (who runs it), Q6 (money and owners), Q7 (value), Q8 (alternatives), Q9 (ruin),
Q10 (fat pitch) and Q12 (pride) are NOT REACHED. Nothing below is a clearance or a verdict on any of them.

## COMPUTATION — NOT A CLEARANCE
*Done because the template asks for the balance sheets in Step 0 when the file closes before Q4, and because the owner
asked for the value range, fair price and cheap price. No entry language; operator rule 3.*

### The balance sheets, ten year-ends, read before the income account **[M2025-032]**
From `tools/run.py` (first-filed XBRL vintage) checked against the filed balance sheets of the 10-Ks for FY2017
(`0001558370-17-004692`), FY2019 (`0001558370-19-005281`), FY2021 (`0001558370-21-007103`), FY2023
(`0001558370-23-010209`) and FY2026 (`0001104659-26-061346`). $ millions.

| Year-end | Assets | Equity | Cash | Inventory | Inv ÷ sales | Goodwill + intangibles | Funded debt | Lease liabilities | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| FY2017 | 566 | 180 | 8 | 189 | 30.0% | 258 | 226 (notes 193 + line 33) | (pre-ASC 842) | 38 |
| FY2018 | 588 | 215 | 9 | 211 | 31.2% | 256 | 204 (notes 183 + line 21) | (pre-ASC 842) | 67 |
| FY2019 | 636 | 264 | 17 | 241 | 31.0% | 259 | 174 (notes) | (pre-ASC 842) | 106 |
| FY2020 | 925 | 322 | 70 | 289 | 34.1% | 258 | 239 (notes 109 + line 130) | 196 | 154 |
| FY2021 | 934 | 395 | 73 | 276 | 30.9% | 258 | 110 (notes) | 221 | 213 |
| FY2022 | 1,200 | 600 | 21 | 474 | 31.9% | 258 | 29 (line) | 278 | 405 |
| FY2023 | 1,517 | 776 | 18 | 589 | 35.6% | 258 | 66 (line) | 382 | 576 |
| FY2024 | 1,706 | 944 | 76 | 599 | 35.9% | 257 | 0 | 452 | 723 |
| FY2025 | 2,018 | 1,131 | 70 | 747 | 39.1% | 256 | 0 | 549 | 904 |
| FY2026 | 2,450 | 1,319 | 141 | 845 | 37.5% | 256 | 0 | 773 | 1,130 |

What the figures say, what they do not, what they cannot **[M2025-032]**:
- **Equity was built by earnings, not by issuance.** Equity rose from $180M to $1,319M; retained earnings from $38M to
  $1,130M; paid-in capital from $142M to $263M (stock pay and option exercises). The IPO proceeds ($82.2M) and a $41.3M dividend were
  both in fiscal 2015 (cash-flow statement, 10-K FY2017). Since FY2020 no acquisition, and goodwill is
  unchanged at $197.5M; the $2.0M Sheplers trademark impairment of FY2024 is the only intangible write-down found;
  store impairments were small ($1.2M FY2017, $0.4M FY2021).
- **Debt was paid off and replaced by leases.** Funded debt fell from $226M (FY2017) to zero (FY2024 onward); the $500M
  revolver (amendment of 2026-07-28, 8-K `0001104659-26-088137`) is undrawn. Lease liabilities rose from $196M (FY2020,
  the first year on the balance sheet) to $773M; undiscounted operating lease obligations $950.4M (10-K FY2026). The
  balance sheet carries the stores as a lease debt of about two-thirds of equity.
- **Inventory has grown faster than sales.** Inventory was about 30% to 31% of sales through FY2022 and 35.6% to 39.1%
  since; per store $1.01M (FY2021) against $1.57M (FY2026). The rows say to "look twice" when "inventories look out of
  line, you know, with sales and, particularly, the trend of them" **[M1995-064]**. The company's stated causes are new
  stores, exclusive-brand buying and distribution-centre stock; it reports same-store inventory per store +1.2% at
  2026-06-27 (Ex. 99.1, `0001104659-26-088137`). One tell, read and explained; prepaid and deferred accounts are small
  and not rising ($33.5M prepaid at FY2026). No second tell found.
- **Property grew faster than the store count.** Net property $110M (FY2021, 273 stores, $0.40M a store) to $514M
  (FY2026, 539 stores, $0.95M a store), with the new Store Support Center and distribution automation in it.
- **What they cannot say:** how much of the inventory is slow, and what the trade of the oldest stores is doing.

### Owner cash after every real cost (operator rule 5; never a net-income proxy)
From the filed cash-flow statements (10-Ks FY2017, FY2020, FY2023, FY2026; XBRL for the years between, cross-checked
in Step 0). Stock pay is deducted as a real cost **[L2021-003]**; depreciation as a true cost **[L2015-004]**. $ millions.

| FY | OCF | Stock pay | Capex | Depreciation | **A: OCF − stock pay − capex** | B: OCF − stock pay − depreciation | Net income | Inventory change |
|---|---|---|---|---|---|---|---|---|
| 2017 | 41.2 | 3.0 | 22.3 | 14.6 | 15.9 | 23.6 | 14.2 | -12.8 |
| 2018 | 44.2 | 2.2 | 24.4 | 16.0 | 17.6 | 26.0 | 28.9 | -24.6 |
| 2019 | 63.3 | 2.9 | 27.5 | 18.3 | 32.9 | 42.1 | 39.0 | -27.7 |
| 2020 | 25.3 | 4.9 | 37.2 | 21.2 | -16.8 | -0.8 | 47.9 | -45.6 |
| 2021 | 155.9 | 7.2 | 28.4 | 24.1 | 120.3 | 124.6 | 59.4 | 13.0 |
| 2022 | 88.9 | 9.5 | 60.4 | 27.3 | 19.0 | 52.1 | 192.4 | -198.5 |
| 2023 | 88.9 | 9.7 | 124.5 | 35.9 | -45.3 | 43.3 | 170.6 | -115.2 |
| 2024 | 236.1 | 12.9 | 118.8 | 49.5 | 104.4 | 173.7 | 147.0 | -9.6 |
| 2025 | 147.5 | 11.0 | 148.3 | 62.5 | -11.8 | 74.0 | 180.9 | -148.1 |
| 2026 | 304.9 | 16.1 | 178.6 | 78.7 | 110.2 | 210.1 | 225.9 | -97.4 |
| **5-yr mean FY2022-26** | | | | | **35.3** | **110.6** | 183.4 | |

- A deducts all capital spending (the convention's input); B is the depreciation variant, depreciation "not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**.
- **The maintenance judgment, where the filing allows one** **[M2000-144]**, **[L1999-024]**: the 10-Ks give the net
  cash investment per new store ($1.2M FY2022, $1.4M FY2023, $1.5M FY2024, $1.7M FY2025 and FY2026) and the openings
  (28, 45, 55, 60, 80). Growth investment so estimated: $33.6M, $63.0M, $82.5M, $102.0M, $136.0M. Adding it back to A
  gives owner cash for a business that stopped opening stores of $52.6M, $17.7M, $186.9M, $90.2M, $246.2M, mean
  **$118.7M**. My best guess, stated as a guess: maintenance spending is near the depreciation charge, so B and this
  figure differ by about 7%.
- FY2025 stock pay ($11.0M) is net of a $6.7M benefit from the former CEO's forfeited awards; the run rate is nearer
  $16M (7.1% of FY2026 net income).

### Capital (Q3's material, not a verdict)
Return on net tangible operating assets (inventory + receivables + prepaid − payables − accrued + net property),
operating income before tax, both sides after depreciation; the earnings-after-depreciation against capital-employed
pairing, not mixed with cash measures **[M2014-007]**, **[M2001-019]**:

| FY | Net tangible operating assets | Operating income | Pre-tax return | With lease liabilities added to capital |
|---|---|---|---|---|
| 2017 | 185.5 | 37.8 | 20.4% | |
| 2019 | 207.4 | 64.3 | 31.0% | |
| 2021 | 229.6 | 86.3 | 37.6% | 19.1% |
| 2022 | 411.6 | 258.3 | 62.8% | 37.5% |
| 2023 | 650.8 | 231.8 | 35.6% | 22.5% |
| 2026 | 1,106.3 | 299.1 | 27.0% | 15.9% |

Incremental: FY2017 to FY2021, $48.5M of added operating income on $44.1M of added assets; FY2021 to FY2026, 24.3%;
**FY2022 to FY2026, $40.8M on $694.7M, 5.9%**; FY2023 to FY2026, 14.8%. The low recent figure is partly young stores
(194 net new stores in the last three fiscal years, 10-K FY2026) and partly the FY2022 peak. "whether that’s good or bad
depends on what we earn on that incremental $130 million over time" **[M2001-019]**: on this span, not yet shown.

### Value range, per the Q7 CONVENTION (Part VI): COMPUTATION
Inputs: five-year mean owner cash FY2022 to FY2026; sovereign 5.63%; ten years then zero nominal growth; ends are the
no-growth and the shown-growth cases. **Growth shown** on aggregate owner cash: series A has negative years and no
meaningful rate; series B rose 52.1 to 210.1, 41.7% a year, from a base year depressed by a $198.5M inventory build,
"a breathtaking, but meaningless, growth rate" **[L2005-003]** and an absurdity if carried **[M1999-067]**. The
convention's cap, in Part VI's own words "no rate that runs past the discount rate", is read literally: growth for the
ten years is capped at 5.63% (CONVENTION of this run, confessed: the convention does not say whether a rate above the
discount rate for ten years only is barred; I take its words as written). The row behind the cap speaks of the
perpetual case: "when the compound rate becomes higher than the discount rate, you get into infinite numbers"
**[M1997-095]**. On that reading:

| Owner cash input | No growth | Shown growth (capped 5.63%, 10 years, then 0) | Top ÷ bottom |
|---|---|---|---|
| **A, all capex (the convention's input): $35.3M** | $627M, **$20.7/share** | $980M, **$32.4/share** | 1.56 |
| B, depreciation variant (shown beside): $110.6M | $1,964M, $64.9/share | $3,070M, $101.4/share | 1.56 |
| Maintenance judgment: $118.7M | $2,108M, $69.6/share | $3,295M, $108.8/share | 1.56 |

Sensitivity, not the convention: if growth at the FY2022 to FY2026 sales rate (10.9% a year) were allowed for ten
years, B's top would be $4,656M ($153.8/share), a range of 2.4 to 1.

**VALUE RANGE (convention): $20.7 to $32.4 a share; depreciation variant $64.9 to $101.4; against $123.43.** The price
sits above the top of every convention range. Had Q2 passed, Q7 under the convention would have closed OUT through the
floor (expected return at the price below the minimum), not TOO HARD (every range is under three to one). With
growth at the sales rate the range would contain the price, which also closes OUT under the convention, since the case
would need a calculator and "It should scream at you." **[M2009-005]**.

### Fair price and cheap price, at the owner's request: COMPUTATION
- **Central case (CONVENTION of this run):** owner cash = B, $110.6M (depreciation as the maintenance proxy, which still
  charges the inventory built for new stores), growing 5.63% a year for ten years, then flat. I chose B over A because
  A charges the growth capital of 80 new stores a year against the stream while the capped growth gives that capital
  almost no return, counting the cost of growth without its fruit; I chose it over the maintenance judgment because B
  comes from the filed statements alone.
- **FAIR PRICE: $53.8 a share** ($1,628M): the price at which that stream returns 10% a year, the Q7 floor CONVENTION
  of about ten percent pre-tax ("at least 10% pre-tax returns" **[L2002-020]**; "it’s arbitrary" **[M2003-149]**). The
  10% is applied to cash already after Boot Barn's corporate tax, so it is pre-tax to the buyer; after the buyer's
  own tax at 15% (a long-term capital gains and qualified dividend rate, CONVENTION of this run) it is 8.5%. If the 10%
  is instead read as corporate pre-tax, as **[L2002-020]** translates it to "6�-7% after corporate tax", the
  after-corporate-tax hurdle at Boot Barn's 24.9% FY2026 effective rate is about 7.5% and the fair price would be
  $74.1. The expected return on the central case at $123.43 is about **4.7%** a year, below the 5.63% bond.
  Sensitivities: at 10.9% growth for ten years the fair price is $77.8 and the return at today's price 6.8%; on the
  five-year mean of net income ($183.4M, not owner cash, shown only to bound the case) the fair price is $89.2.
- **CHEAP PRICE: $36.5 a share** ($1,106M). Rule (CONVENTION of this run): the price at which the five-year mean owner
  cash, depreciation variant, with no growth at all, yields the 10% floor ($110.6M ÷ 10%). Below it no growth arithmetic
  is needed to clear the floor, which is what "it ought to just kind of scream at you" **[M1996-084]** asks.
- **Against the price:** $123.43 is 2.3 times the fair price and 3.4 times the cheap price.

### Facts read for questions not reached (recorded for the research file; no verdict)
- **Buybacks** (Q6): $200M authorization of May 2025 with no stated price limit (10-K FY2026 Note 9). FY2026: 286,504
  shares for $50.0M, about **$174.54** a share; Q4 FY2026 68,472 at $182.55; Q1 FY2027 158,451 for $25.0M, about
  **$157.78** (10-Q `0001104659-26-088262`); $125.0M remained at 2026-06-27. Every price paid is above the top of every
  convention range above. "repurchase announcements almost never refer to a price above which repurchases will be
  eschewed" **[L2016-002]**. No repurchases FY2015 to FY2025.
- **Stock pay and dilution** (Q4, Q6): $16.1M FY2026; diluted shares 26.9M (FY2017), 29.5M (FY2021), 30.7M (FY2026); the
  2026 Equity Incentive Plan adds 1,000,000 new shares plus up to 1,088,748 rollover shares (8-K `0001104659-26-102449`).
- **Pay design** (Q6 Part B), DEF 14A `0001104659-26-084071`: annual bonus on "Consolidated EBIT", defined as
  "earnings before income taxes, excluding certain one-time selling, general, and administrative expenses", with no
  charge for capital; performance share units on cumulative three-year earnings per share; CEO total pay $6,661,922 in
  FY2026 (salary $894,231, stock awards $4,100,160, bonus $1,634,211).
- **Guidance** (Q4 tells, Q6): quarterly and annual guidance is given, including earnings per share (Ex. 99.1,
  `0001104659-26-088137`); the 8-K of 2026-09-14 updates the quarter to date. "We don’t give out earnings guidance. We
  think it’s silly." **[M2016-002]** is Berkshire's conduct, read here by inversion only.
- **Succession** (Q5): CEO resigned 2024 for another opportunity; interim CEO from inside, confirmed after a search;
  the chairman served as executive chairman until 2025-12-31 (8-Ks of 2024-10-28, 2025-05-05, 2026-01-05). At the 2026
  annual meeting the chairman drew the most withheld votes of the eight directors (Peter Starrett, 24,048,823 for,
  3,344,860 withheld; next Lisa G. Laube, 2,261,045 withheld; the CEO 271,307 withheld); say-on-pay passed 27,036,041
  to 334,861 (8-K `0001104659-26-102449`).
- **Tariffs** (Q4): $14.7M of tariff refunds booked in cost of goods sold in Q1 FY2027, $17.8M expected for the year
  ($0.46 a share), disclosed and separated by the company in its release, not folded into a recurring margin.

---
## THE BOX
**TOO HARD (WORK), decided at Q2.** The castle (the only national western and work-wear chain, four times its nearest
specialty rival, exclusive brands at 40.8% of sales, a loyalty file of 10.8M buyers) is visible and not shown to be
filling in, so the file does not close OUT; whether it keeps the present per-store economics for ten to twenty years
cannot be judged from the evidence read **[M1995-038]**, **[M2000-019]**, **[M2006-013]**. Q7 was not reached. As
COMPUTATION only: convention value range $20.7 to $32.4 a share (depreciation variant $64.9 to $101.4), fair price
$53.8, cheap price $36.5, against $123.43.

## RESEARCH PASS, STEPS 1 AND 2 (written, not run; Part VII, CONVENTION in its form)
*To be committed before any reading of step 3. Steps 3 and 4 are not run in this session.*

**Step 1. "What do I not know that I need to know?"** **[M1999-129]**, each marked knowable or not **[M2006-076]**.

| # | Question | Knowable? |
|---|---|---|
| R1 | Do new stores opened since FY2022 earn their stated payback (about three years on about $1.7M net), or is the store model's return falling as the cost per store rises faster than its sales? | Knowable in part: the company's furnished supplemental presentations (8-K Ex. 99.2) and the 10-K store-model text |
| R2 | Is the trade of the stores already open holding, or is the flat average sales per comparable store a mix of ramping new stores and falling old ones? | Knowable in part: retail-store (ex e-commerce) same store sales by quarter in the 10-Qs and releases; cohort data are not published |
| R3 | Is a funded specialty attacker reaching a scale that can take Boot Barn's customer (Tecovas, Cavender's, Ariat's own stores)? | Knowable in part: Forms D on EDGAR; store counts only from the companies' own websites (aggregator class, flagged) |
| R4 | Is the merchandise-margin gain pricing power on the same goods, or only mix toward exclusive brands that a rival could copy? | Knowable: the gross-profit paragraphs of the 10-Ks and 10-Qs |
| R5 | How much of today's trade is a western-fashion overlay that came in FY2022 and can leave as fast? | **Not knowable** from primary documents: no filing splits sales by customer type or by the year a customer joined. Recorded and set aside (form (c)); the close is decided on R1 to R4 |
| R6 | How deep did trade fall in the 2008 to 2009 recession? | Knowable if the S-1 of 2014-09-29 (`0001047469-14-007948`) or its amendments print annual same store sales for FY2009 and FY2010; it informs Q7's range, not the castle, so it cannot close the pass by itself |

R5 is the question my doubt rests on most, and it is not knowable. The pass therefore asks whether R1 to R4, which are
knowable, settle the castle without it. If they do not, the pass ends TOO HARD (NATURE) **[M2002-092]**.

**Step 2. For each knowable question: the evidence, its span and source fixed now, and the single fact that would close
the file OUT** **[M1998-144]**.

| # | Evidence; span and source (fixed) | The one fact that closes OUT |
|---|---|---|
| R1 | Boot Barn 8-K Ex. 99.2 supplemental financial presentations dated 2024-10-28 (`0001558370-24-013745`), 2026-05-14 (`0001104659-26-061169`) and 2026-07-29 (`0001104659-26-088137`), and the new-store model sentence of every 10-K FY2018 to FY2026 | The company's own figures show any store class opened in FY2022, FY2023 or FY2024 with an actual or projected payback longer than four years |
| R2 | Retail-store same store sales, excluding e-commerce, for each fiscal quarter Q1 FY2024 to the latest 10-Q filed when step 3 runs (Q2 FY2027, quarter ended 2026-09-26, if filed), from the earnings releases (8-K Ex. 99.1) and the 10-Qs | The sum of the latest four reported quarters' retail-store same store sales is below zero |
| R3 | Tecovas Forms D (`0001686840-20-000001`, `0001686840-22-000001`, `0001686840-25-000002`); store counts on the websites of Tecovas, Cavender's and Ariat as of the reading date (aggregator class, flagged); Tractor Supply's "Clothing, Gift & Décor" share of sales, 10-Ks FY2017 to FY2025 | Any one specialty western rival shown with at least 200 stores, half of Boot Barn's FY2024 count of 400 |
| R4 | Gross-profit paragraphs of the 10-Ks FY2017 to FY2026 and the 10-Qs of FY2027, read for "product margin" as distinct from freight, tariff and occupancy | Any fiscal year in the span in which product margin fell while exclusive-brand penetration rose |

**How step 4 closes.** OUT if any one OUT fact above is found. IN only if no OUT fact is found AND R1 finds a stated
payback of three and a half years or less for the FY2022 to FY2024 classes AND R2's latest four quarters sum above zero;
the run then continues at Q3 from this file. If R1 or R2 proves unanswerable from the named sources, that is recorded
with the search that failed and the close is decided on the rest; any other ending, or any doubt left, is TOO HARD
(NATURE) **[M2002-092]**, never TOO HARD (WORK) a second time **[M2008-086]**. Any capital test in step 3 sets earnings
after depreciation against capital employed, or cash earnings against capital spending, never one against the other;
any margin comparison covers the whole span named, not one year. A held name would need a blind second session; the
analyst does not know whether this one is held (position note above).

**What the analyst expects, written before the reading so that it can be checked:** that R1 to R4 will not produce an
OUT fact, that R1 will be partly unanswerable, and that the pass will most likely end TOO HARD (NATURE) on R5. Had the
castle passed, the computation above says Q7 would have closed OUT at $123.43 under the convention in any case.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each:** the
      dispatch instruction forbids commits in this session; the write-early order was kept on disk (Step 0, then the
      Foundations to Q2, then the computation, then the rest).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; Q3 to Q12 are marked NOT REACHED and every later figure is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, stock pay deducted, never a net-income proxy
      (net income appears only as a labelled bound); the sovereign from the US Treasury; the price flagged as an
      aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (seven items in the Foundations, three of them
      against the analyst's own doubt).
- [x] No row dated after the anchor: the run is dated today, so no point-in-time bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its labels, yields and rule text were not.
- [x] `python tools/check_framework.py` run after writing (result in the session report; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q2 has no rule for a demand step the castle did not cause.** The castle tests ask about the moat, but the economics
   a buyer pays for here rest on a one-year 61% step in trade per store whose cause the filings do not give. Whether it
   belongs to Q1 (the ten-year economics), Q2 (the castle) or Q7 (the width of the range) the text does not settle; I put
   it at Q2 because "how permanent are they?" **[M1995-038]** is a castle question, but a second analyst could pass Q2 on
   the castle and carry the demand question to Q7, where the convention would close OUT.
2. **The Q7 growth cap is ambiguous.** The convention's words, "no rate that runs past the discount rate", can mean no
   perpetual rate above it or no rate above it even for the ten years; the row it rests on speaks of the perpetual case,
   "you get into infinite numbers" **[M1997-095]**. The two readings move the top of
   the range from $101.4 to $153.8 on the depreciation variant. I took the words literally and said so.
3. **The convention's input punishes a growth retailer twice.** Deducting all capital spending charges 80 new stores a
   year against the stream, while the capped growth gives that spending almost no return; the convention's own range
   ($20.7 to $32.4) sits below the no-growth value of the depreciation variant. The convention asks for the
   maintenance judgment where the filing allows one but does not say which input sets the range when the two differ threefold.
4. **The floor convention's "about ten percent pre-tax" does not say pre whose tax.** The 2002 letter means
   corporate tax, "6�-7% after corporate tax" **[L2002-020]**; the 1994 answer applies the rate to "after-tax streams of
   cash" **[M1994-004]**. On owner cash already after the
   company's tax, the two readings move the fair price from $53.8 to $74.1. I applied 10% to the after-corporate-tax
   stream and showed the other.
5. **The research pass's OUT facts must be single facts, but the doubt here is a forecast (R5) no document answers.**
   Form (c) lets an unanswerable question be set aside; when the set-aside question is the one the doubt rests on, the
   form steers the close toward the secondary questions. I flagged this in step 2 rather than resolve it.
6. **The write-early rule says commit after each question; this dispatch forbade commits.** The template has no line
   for that case; I recorded it in the self-audit.
