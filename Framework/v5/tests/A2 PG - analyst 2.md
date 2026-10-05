# A2 PG - analyst 2. The Procter & Gamble Company (NYSE: PG), run under the v5 drafts. 2026-10-04.

Re-test of reproducibility after the correction pass of 2026-10-05. Binds nothing; changes no verdict of record. Run under
`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md` and `Framework/v5/DRAFT - THE FRAMEWORK v5.md`.
The operator does not hold PG: Q11 is not answered; Q12 is. Working files: `Framework/v5/tests/_work_A2r2_PG/`.

**Documents read (every filing fact below carries one of these accessions).**

| Short name | Document | Filed | Accession |
|---|---|---|---|
| 10-K FY26 | PG Form 10-K, fiscal year ended 2026-06-30 (`pg-20260630.htm`) | 2026-08-04 | 0000080424-26-000103 |
| 10-K FY25 | PG Form 10-K, fiscal year ended 2025-06-30 | 2025-08-04 | 0000080424-25-000076 |
| 10-K FY23 | PG Form 10-K, fiscal year ended 2023-06-30 | 2023 | 0000080424-23-000073 |
| Proxy 26 | PG DEF 14A (`pg-20260826.htm`) | 2026-08-28 | 0001193125-26-372211 |
| CL 10-K | Colgate-Palmolive Form 10-K, year ended 2025-12-31 (`cl-20251231.htm`) | 2026-02-23 | 0000021665-26-000006 |
| XBRL | SEC companyfacts for CIK 0000080424, FY2022 and FY2023 annual values, each tagged to its 10-K (FY22: 0000080424-22-000064; FY23: 0000080424-23-000073) | | |

---

## 0. Step 0

| Item | Value | Source |
|---|---|---|
| Price | **$144.91**, close 2026-10-02 | `tools/sources.py` `price('PG')`, an aggregator: **live quote only, flagged** |
| Shares, cover | **2,324,433,060** common (single class on the cover; dei count as of 2026-07-31) | `Screens/cover_shares.py PG`, from 10-K FY26 cover, 0000080424-26-000103 |
| Market cap | **about $336.8 billion** (144.91 x 2,324.4M) | arithmetic; `tools/run.py PG` arithmetic line agrees (336.83B) |
| Dilution note | Diluted weighted shares FY26 2,422.5M (convertible Class A ESOP preferred, options); on that count the price is about $351B | 10-K FY26 Note 6 / XBRL `WeightedAverageNumberOfDilutedSharesOutstanding`, 0000080424-26-000103 |
| Sovereign (USD, the earnings currency) | **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026 | issuing authority, as given in the brief; `tools/run.py` arithmetic line prints the same figure and date |

Cross-check of tool against filing (operator rule 4): `tools/run.py` FY26 operating cash flow 19,556, capex 4,409, D&A 3,160,
stock pay 524 ($ millions) each equal the filed Consolidated Statement of Cash Flows, 10-K FY26 p. 42, 0000080424-26-000103.
Per Part VII, only `run.py`'s arithmetic lines were read; its v4 ids, its v4 floor line and its "still owed" list were ignored.

---

## 1. The foundations

A share is a business **[M1997-109]**: PG is read as a whole business whose cash is to be estimated, not a quotation to
be timed **[M2006-077]**. The foundation that bears hardest is **margin of safety**: "if you have to actually do it on —
with pencil and paper, it’s too close to think about" **[M1996-084]**, with the arithmetic deferred to Q7 **[M1997-126]**.
Macro is kept out **[M2000-094]**: tariffs, FX and the Middle East appear in the 10-K's risk factors and are not used as a
forecast. The analyst's habits: write the contrary evidence down at once **[M1997-127]** and destroy the previous
conclusion **[M2016-054]**; the familiarity of the name is the hazard here, so the share losses and the lagging return
are written into Q2 and Q5 below, not left out. The index fork **[M2008-055]** is assumed passed (the operator runs the
questions). The CONVENTION falsifier is not written, because no purchase follows (the run closes at Q7).

## 2. The standing rule

Owning PG need not put the buyer at risk of ruin: nothing in the question requires borrowed money, and the rule forbids it
**[L2014-005]**, **[M2012-081]**, **[L2023-005]**. The rule binds the buyer's financing and sizing, not the target; no
position is taken here.

---

## 3. The questions, in order

### Q1. CAN I UNDERSTAND IT? STOP.

**The test as the draft states it:** "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**, **[M2000-037]**; identify the key variables and how predictable they are
**[M1998-044]**; do the past statements tell me the future ones **[M2008-033]**; can I name the winner, not just the
industry **[M2012-067]**; is the forecast about customers or technology **[M2017-019]**, **[M2023-030]**.

**Applied.** PG sells daily-use consumables in five segments: Fabric & Home Care 35% of FY26 net sales, Baby, Feminine &
Family Care 24%, Beauty 19%, Health Care 14%, Grooming 8% (10-K FY26, MD&A Overview, 0000080424-26-000103). The key
variables, in the Coca-Cola form "unit case sales and shares outstanding" **[M1998-040]**, are unit volume, price/mix and
the share count; the 10-K reports each every year (FY26: volume 0%, price +1%, FX +2%, net sales +3% to $87.0 billion;
FY25: volume 0%, price +1%; FY23: volume -3%, price +9%; 10-K FY26, FY25, FY23 net sales driver tables). The forecast is
about consumer behaviour (detergent, diapers, razors, toothpaste), not technology **[M2017-019]**. The winner is named:
PG reports leadership positions, e.g. blades and razors "more than 60%", fabric care "over 35%" in its markets, baby care
"more than 30%" (10-K FY26, MD&A, Organization Design). The 10-K itself names channel change (social commerce, AI search,
retailer media) as the threat to execution, which is a customer and channel question, not a product-technology one.
The speakers name this very case as easier than a bank: "it’s much easier to come to a conclusion on something like
Coca-Cola or Procter & Gamble than it is [...] to make a decision on whether to own bank A" **[M2009-060]**. Doubt test
**[M2002-092]**: none about where the economics sit in ten years (daily-use, branded, scale-distributed, low growth).

**Verdict: IN.** The ten-year economics are foreseeable from the filings and turn on consumer behaviour **[M2012-065]**,
**[M2017-019]**, **[M2009-060]**.

### Q2. WHY IS THE CASTLE STILL STANDING? STOP.

**The test as the draft states it:** "why is that castle still standing? And what’s going to keep it standing [...] five,
10, 20 years from now" **[M1995-038]**; the money test **[M2011-015]**, **[M1997-103]**; pricing power **[M2005-020]**,
**[M2005-017]**; share of mind and volume **[M1997-099]**, **[M1999-054]**; asked for by name **[M2023-073]**; brand
against retailer **[M2001-090]**, **[M2019-041]**; widening or narrowing **[M1999-108]**, **[L2005-010]**; ask the
competitors **[M2017-091]**. OUT only for a castle "shown on the evidence to be filling in"; TOO HARD for one whose future
cannot be judged **[M2000-019]**, **[M2006-013]**.

**What keeps it standing.** "The might of their brand names, the attributes of their products, and the strength of their
distribution systems" **[L1993-021]**: PG spent $10.2 billion on advertising in FY26 and $2.1 billion on R&D (10-K FY26,
Note 1), sells in about 180 countries (Item 1), and holds the shares above. The products are asked for by name
**[M2023-073]**, **[M2002-091]**. The money test **[M2011-015]**: an entrant with a large sum would face the same retailers,
the same shelf and the incumbents' advertising scale; the rows' own Gillette form, "they can’t knock off Gillette"
**[M2002-051]**, is a statement of exactly this business (Grooming, 8% of sales).

**Pricing power, the passing-through test.** In FY23 PG raised price 9% against a 3% fall in unit volume (10-K FY23, net
sales drivers, 0000080424-23-000073), carrying a cost wave through to customers as **[M2005-017]** describes; since then
price has been +1% a year with volume flat (10-K FY25, FY26). That is pass-through, not the business-school case
**[M2000-085]**.

**Same-metric competitor comparison (from the competitor's own filing).**

| Metric | PG, FY ended 2026-06-30 (10-K FY26, 0000080424-26-000103) | Colgate-Palmolive, FY ended 2025-12-31 (CL 10-K, 0000021665-26-000006) |
|---|---|---|
| Operating margin, GAAP | 22.7% | 16.2% (21.3% on Colgate's own non-GAAP basis) |
| Gross margin, GAAP | 50.2% | 60.1% |
| Organic sales growth | +1% | +1.4% |
| Unit volume | 0% | -0.4% |
| Share in its head-to-head category | oral care "nearly 30%" global, unchanged | toothpaste 41.3% global, down 0.4 points |

Read: PG earns a GAAP operating margin above the strongest single-category peer while spending more of sales on
marketing; both incumbents hold their volume flat and gain price slowly. The castle is standing for both, and the
attacker in the filings is not a new entrant with a better product but "competitive activity" and the retailer.

**Widening or narrowing.** The evidence runs against widening in FY26. The 10-K reports global share down in Beauty (-0.3
points), Grooming (-0.4), fabric care (-0.4), Baby, Feminine & Family Care (-0.2) and North America family care (-0.7),
up in Health Care (+0.4) and home care (+0.3); volume declines in North America are repeatedly put "due to competitive
activity"; gross margin fell 100 basis points with 120 of decline from unfavourable mix (10-K FY26, Segment Results).
Grooming goodwill is carried "net of $7.9 billion accumulated impairment losses" and the Gillette indefinite-lived brand
was impaired $1.3 billion in FY24 (10-K FY26, Note 4): the notch **[L1995-023]** in the one franchise the rows quote
by name. Walmart is about 16% of sales and the top ten customers about 43% (Item 1), the retailer pressure of
**[M2001-090]** and the lesson of **[M2019-041]**. The speakers' own reading of this group is the same: "The packaged good
business, the Procter & Gambles and so forth of the world — General Mills — they’re all weaker than they used to be at
their peak" **[M2016-080]**, beside "Procter & Gamble’s not going to go away" **[M2010-015]**.

**Judgment.** Weaker than at its peak, losing fractions of a point in several categories, but not shown "on the evidence to
be filling in": volume is held, leadership shares are intact, GAAP margin is above its nearest peer's, and the business
throws off about $14 billion a year of owner cash (Q7). A slow loss of notches is "slow change" that "can lull you to
sleep" **[M2014-038]**, so it is carried forward as a weight on "how sure" at Q7 and as the falsifier a purchase would
have had to write (share in fabric care and baby care, read each 10-K), not as an OUT.

**Verdict: IN.** The castle stands on brand, scale and distribution **[L1993-021]**, **[M1995-038]**, **[M2010-015]**;
the narrowing **[M2016-080]**, **[L1995-023]** is recorded and carried, and does not meet the draft's OUT standard of a
castle shown to be filling in **[M2011-015]**.

### Q3. HOW MUCH CAPITAL MUST GO IN? WEIGHING.

**Test:** what it earns on the capital it needs, "return on tangible assets" **[M2011-060]**, **[M2010-090]**; what must
be reinvested to stand still and to grow **[L1999-024]**, **[M2000-144]**; read a high return for "a cyclical peak in
earnings, a monopolistic position, or leverage" **[L1994-009]**, **[M1998-017]**.

**Arithmetic from the filing** ($ millions, 10-K FY26 balance sheet, 0000080424-26-000103): net PP&E 25,360 + receivables
6,056 + inventories 8,170 + prepaid 2,040 - payables 16,306 - accrued 11,091 = about 14,200 of net tangible operating
capital (about 26,500 if all 12,231 of other noncurrent assets are added). FY26 operating income 19,748 is a pre-tax return
of roughly 75% to 140% on it. Not from leverage or shrunken equity: the figure is on operating assets, not on book equity
**[M1998-017]**. Not a cyclical peak: operating income FY22 to FY26 ran 17,813 / 18,134 / 18,545 / 20,451 / 19,748
(XBRL and 10-K FY26).

**Reinvestment.** Capex FY22 to FY26 summed 17,722 against D&A of 14,424, an excess of about 3,300 over five years, while
operating income rose about 1,900 (XBRL; 10-K FY26 cash flow statement). Capex has run above depreciation since FY24 (FY26
4,409 against 3,160), so depreciation is not a safe proxy for maintenance here **[M1998-127]**; with volume flat, the
excess is read as mostly maintenance and productivity, not growth. The business cannot use what it earns: FY22 to FY26 it
paid $47.2 billion in dividends and $33.9 billion in buybacks against $76.3 billion of net earnings (XBRL, each year's
10-K). That is the business "that gives you more and more money every year without putting up anything to get it, or very
little" **[M1998-081]**, without the "more and more": growth is slow.

**Verdict: WEIGHS FOR.** Very high returns on the tangible capital the business needs **[M2011-060]**, **[M1998-081]**,
with little incremental capital and little growth to put it in.

### Q4. DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion, otherwise WEIGHING.

**Test:** confusion or suspicion stops **[M1995-063]**, **[M2003-029]**; otherwise recast to earnings "after interest,
taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**, and read the tells **[M1995-064]**.

**Confusion: none.** The statements are plain; Deloitte's opinion is unqualified, with one critical audit matter (the
Gillette brand impairment test) disclosed (10-K FY26, auditor's report). Balance sheet over years **[M2025-032]**:
inventories rose 7.5 billion to 8.2 billion with sales up 3%, explained in MD&A (safety stock, new products); no
prepaid or deferred build-up out of line **[M1995-064]**.

**The real costs.** Stock pay 524 is subtracted from operating cash flow **[L2015-003]**. Restructuring is incurred every
year: 659, 1,114 and 1,230 before tax in FY24, FY25 and FY26, on top of an "ongoing" level of $250 to $500 million that PG
calls normal (10-K FY26, Note 3). The cash part is already inside operating cash flow; the owner-cash figure at Q7 takes
it in full.

**The tells.** PG features "Core EPS", which removes "incremental restructuring" charges incurred in each of the last
three years, and pays its executives on it (10-K FY26 non-GAAP reconciliation; Proxy 26, PSP and STAR metrics). The rows:
"to tell owners year after year, "Don't count this," when management is simply making business adjustments that are
necessary, is misleading" **[L2016-007]**; "a management that regularly attempts to wave away very real costs by
highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**. The make-the-numbers habit is absent:
FY26 guidance was 0-4% organic growth and 0-4% Core EPS growth and was met at the low end (Proxy 26, CD&A), and Core EPS
grew 1% against a published "mid-to-high single digits" algorithm (10-K FY26, MD&A). Under the two-tell CONVENTION of
Q4 **[L2002-041]**, **[M1994-018]**, one tell without the habit is a weight, not suspicion.

**Verdict: WEIGHS AGAINST** (no STOP). The accounts are clear and recast easily, but the company features, and pays on,
an adjusted figure that sets aside restructuring incurred every year **[L2016-007]**, **[L2016-006]**.

### Q5. WHO RUNS IT? STOP on integrity, WEIGHING on ability.

**Integrity (the STOP).** Tests: the proxy, "how they treat themselves versus how they treat the shareholders"
**[M1994-009]**; reports that tell "the things that we would want to know about" **[M1998-036]**; the named tells
**[M2003-029]**, **[M2013-088]**. Read: the 10-K reports its own share losses category by category and says "due to
competitive activity", and prints a performance graph showing PG's five-year total return (100 to 123) behind the S&P 500
Consumer Staples Index (100 to 145) (10-K FY26, Item 5); that is the bad news told **[M1998-036]**. Related-person
transactions are two employed spouses, disclosed and approved (Proxy 26); hedging and pledging are prohibited; the CEO
must own eight times salary and all NEOs exceed their requirement (Proxy 26). Stock pay is expensed. No tell from the
draft's list was found. For a marketable stock "the yardsticks and the reading tests carry the weight" **[M2007-081]**.

**Ability (the WEIGHING).** The record against the hand dealt **[M1994-008]**: diluted EPS FY22 to FY26 $5.81 to $6.62
(XBRL, 10-K FY26), about 3.3% a year; total return behind the staples index over five years (10-K FY26, Item 5). The chief
executive, Shailesh Jejurikar, became CEO on 2026-01-01 and Chairman since (10-K FY26 executive officers; Proxy 26); his
record as CEO is nine months, as COO 2021 to 2025 (10-K FY26). "we don’t like banjo hitters" **[M1996-038]** cuts neither
way on so short a tenure. The business needs little genius **[M1996-037]**.

**Verdict: IN on integrity** (no tell found **[M2013-088]**, **[M1998-036]**); **UNDECIDED on ability**: a new chief
executive and a company record that trails its peer index **[M1994-008]**.

### Q6. WHAT WILL THEY DO WITH THE MONEY AND WITH THE OWNERS? WEIGHING.

**Part A, the money.**
- *Retention test* **[M1998-033]**, **[R1995-009]**, **[M2010-097]**: PG retains almost nothing. FY22 to FY26 retained
  earnings after dividends of about $29.1 billion went, with more, into $33.9 billion of buybacks (XBRL). The forward
  question "Can you keep using all of the capital you generate" **[M2010-097]** is answered by the company's own conduct:
  it cannot, and pays out, as **[M2004-089]** says a company should. Dividend raised 70 consecutive years (10-K FY26,
  Item 5): clear and consistent **[L2012-015]**.
- *Buybacks* **[L1999-023]**, **[L2016-002]**: the FY26 programme was a fixed sum, "approximately $5 billion", with no stated
  price, "financed through a combination of operating cash flows and issuance of debt" (10-K FY26, Item 5, note 3). Under
  the CONVENTION for a buyback with no stated price, the prices paid are read against the bottom of the Q7 range: FY26
  treasury purchases 5,029 for 33.4 million shares, about $150 a share; May to June 2026 average $147.46 (10-K FY26,
  statement of equity; Item 5). The Q7 range below is about $105 to $135 a share; the purchases sit above its top.
  Repurchases "only make sense if the shares are bought at a price below intrinsic value" **[L2016-002]**.
- *Deals*: Thorne, $3.8 billion, announced 2026-08-04 (10-K FY26, Recent Developments), about 1% of market value; the Glad
  stake sold for $476 million. No all-stock deal by an undervalued acquirer: the one STOP of Part A **[L2009-019]** is not
  triggered; no serial issuance **[L2014-015]** (share count falling).

**Part B, pay, board, owners** (Proxy 26, 0001193125-26-372211).
- Chairman and CEO combined in Mr. Jejurikar from 2026; an independent Lead Director: "I've seen how hard it is to replace
  a mediocre CEO if that person is also Chairman" **[L2014-026]**.
- Pay is set at "the median [...] of comparable positions in the compensation peer group, regressed for revenue size",
  advised by Meridian: the ratchet of **[M2012-095]**, **[L2005-015]**, **[M2004-016]**.
- Paid on Core EPS growth, organic sales growth relative to peers, core operating profit, free cash flow productivity and
  a relative TSR multiplier: largely within management's control **[M2003-019]**, but Core EPS excludes restructuring (Q4).
- Stock options with 10-year terms at the grant-date price, no step-up for retained earnings **[L1994-021]**,
  **[M1997-043]**; FY26 long-term award to the CEO $14 million.
- For: ownership eight times salary for the CEO, six times retainer for directors **[L2019-008]**; no hedging or pledging;
  clawback beyond the Dodd-Frank minimum.

**Verdict: WEIGHS AGAINST.** Payout policy is right for a business that cannot use its earnings **[M2004-089]**, but the
fixed-sum buyback runs at prices above the value range **[L2016-002]**, and the board structure and benchmarked pay are
the forms the rows warn of **[L2014-026]**, **[M2012-095]**.

### Q7. WHAT IS IT WORTH ... HELD AS A RANGE; AND IS THE PRICE SO FAR BELOW IT THAT IT NEEDS NO PENCIL? STOP.

Reached: Q1 and Q2 are IN, Q5 is IN on integrity, Q3, Q4 and Q6 are weighed and carried.

**How much cash** **[L2000-021]**, **[R1996-018]**, **[M1998-080]**: owner cash = operating cash flow - stock pay - all
capex **[L2021-003]**, **[L2015-004]**, **[M2014-068]** ($ millions; FY24-FY26 10-K FY26 cash flow statement, FY22-FY23
XBRL tagged to their 10-Ks):

| FY | OCF | stock pay | capex | owner cash |
|---|---|---|---|---|
| 2022 | 16,723 | 528 | 3,156 | 13,039 |
| 2023 | 16,848 | 545 | 3,062 | 13,241 |
| 2024 | 19,846 | 562 | 3,322 | 15,962 |
| 2025 | 17,817 | 476 | 3,773 | 13,568 |
| 2026 | 19,556 | 524 | 4,409 | 14,623 |
| **five-year average** | | | | **14,087** |

All capex is taken, not D&A, because capex has exceeded depreciation since FY24 with volume flat (Q3), and the draft
asks conservative inputs **[M2004-055]**. (With D&A in place of capex the average is 14,746; shown below, it does not move
the box.) The five-year average is the CONVENTION's base **[L2005-003]**.

**Shown growth.** Owner cash FY22 to FY26: 13,039 to 14,623, about 2.9% a year compounded (net sales 2.1% a year, 80,187 to
87,032; 10-K FY26, XBRL). Aggregate, not per share, because the value is set against the whole market capitalisation.
Below the 5.63% rate, so the cap of Q3 does not bind **[M1997-095]**, **[M1999-067]**.

**The range** (CONVENTION of Q7: ten years at shown growth, then no real growth, discounted throughout at the long
government rate **[M1996-025]**, **[L2000-021]**; two ends **[L2000-024]**, **[L1999-027]**):
- no-growth end: 14,087 / 5.63% = **about $250 billion** (about $108 a cover share, $103 a diluted share);
- shown-growth end: 2.9% for ten years, then flat = **about $315 billion** (about $136 a cover share, $130 diluted).
- Sensitivity, D&A instead of capex: about $262 to $330 billion. Still below the price.

**How sure, how soon.** Width top to bottom is about 1.26 to 1, far inside the three-to-one CONVENTION line, so the range is
not TOO HARD **[L2000-025]**: the stream is steady and the castle stands (Q2), with the narrowing carried as a reason not to
use more than the shown growth. Cash arrives evenly, year by year.

**Price against range.** Price **$336.8 billion ($144.91)** sits **above the top** of the range. The growth the price implies
at 5.63% over ten years, then flat, is about 3.7% a year against 2.9% shown. **The floor CONVENTION**: expected return at the
price is about 4.2% owner-cash yield with no growth, about 5.3% a year as the rate that equates the shown-growth stream to
the price, and about 7.1% if read as yield plus shown growth (4.2 + 2.9); all three are below
"about ten percent pre-tax", "a point at which we drop out of the game" **[M2003-149]**, **[L2002-020]**, **[M1994-004]**.
Not a screamer: no reading of the figures puts the price below the bottom, let alone far below it **[M2009-005]**,
**[M1996-084]**.

**Verdict: OUT.** "Valued, but the price does not clear the floor: stop" **[M2003-149]**; the price is above the value
range, not below it **[L2013-012]**.

### Q8. IS IT BETTER THAN THE ALTERNATIVES? STOP.

NOT REACHED. (For the record only: at about 5% expected return the name would also lose to the 5.63% bond **[M1997-089]**.)

---

## 4. Q9 and Q10

NOT REACHED.

### COMPUTATION — NOT A CLEARANCE

Q9 arithmetic, for the record only: total debt $34.1 billion (11,296 current + 22,842 long-term), cash $9.9 billion;
pre-tax coverage (20,377 + 877) / 877 = about 24 times, on the rows' definition "pre-tax earnings/interest"
**[L2012-002]**; current liabilities exceed current assets by $12.5 billion, carried by commercial paper backed by an
undrawn $8.0 billion facility with no rating triggers (10-K FY26, balance sheet and Liquidity, 0000080424-26-000103).
No weighing is recorded.

## 5. Q11 and Q12

**Q11:** not answered (the operator does not hold PG).

**Q12, the newspaper test. WEIGHING** (PG is not a named business: no casino, tobacco or loading scheme **[M2007-018]**,
**[M2005-097]**, **[M2013-015]**). Test: "if a story were written by an unfriendly but intelligent reporter [...] they would
have no problem with their neighbors, their family reading it" **[M2008-011]**; "We don’t want to make our money selling
things that are bad for people" **[M2021-059]**. Read: the only Item 3 matter is a U.K. emissions-permit lapse, self-reported,
penalty under $2 million (10-K FY26, Item 3); Note 13 reports no material litigation. Perfection is not asked
**[M2021-012]**. **WEIGHS FOR**: nothing in the filings read would embarrass an owner. Recorded after the Q7 close as the
brief asked; it reopens nothing.

---

## 6. The box

**OUT, decided at Q7.** Value about **$250 to $315 billion** (about $105 to $135 a share), how much: about $14 billion a year
of owner cash; how sure: steady, range width about 1.3 to 1; how soon: evenly, year by year; at the 5.63% long government
rate. Price **$336.8 billion ($144.91)**, above the top of the range; expected return about 5%, below the ten-percent floor
CONVENTION **[M2003-149]**. Not so far below value that it needs no pencil: it is above value **[M2009-005]**.

## 7. Self-audit

- [x] **Every id resolves.** All 112 distinct bold ids in this file were extracted from the finished file and checked
  against `principle_ledger_v5.csv` by an exact `^ID,` grep; none missing. The P&G rows found by a text search of the
  ledger (M2006-052, M2007-006, L2007-015, M2009-060, M2010-015, M2016-080) were read in full; three are cited.
- [x] **Every filing fact has an accession** (the table at the top; each fact names its document).
- [x] **No number without a row or a filing.** The 10% floor, the five-year base, the ten-year term and the three-to-one
  width are the draft's confessed CONVENTIONs at Q7; the two-tell line and the no-price buyback reading are its CONVENTIONs at
  Q4 and Q6. Arithmetic (ratios, sums, the range) is mine from filed figures and is shown.
- [x] **No file outside the whitelist was opened by me.** Opened: the protocol, the v5 draft, `principle_ledger_v5.csv`,
  `tools/sources.py` (function list only), the outputs of `tools/run.py PG` and `Screens/cover_shares.py PG`, SEC EDGAR
  filings, and my working folder. Declared: `CLAUDE.md`, `Framework/OPERATOR-PROTOCOL.md` and the auto-memory index were
  loaded into the session by the harness before the task began (the second is on the whitelist; the first is the project
  map and carries no verdict on PG; the memory index carries none either). A directory listing of `Framework/v5/` showed
  file names only. No file under `Test Runs/` or `Screens/` was read; `cover_shares.py` was run, not read.
- [x] **`run.py` read for arithmetic only**; its printed v4 ids and v4 floor ignored (Part VII).
- [x] **Order kept; the first STOP stopped the run.** Q1 IN, Q2 IN, Q3/Q4/Q6 weighed, Q5 IN on integrity, Q7 OUT; Q8 to Q10
  NOT REACHED; the Q9 figures are under COMPUTATION — NOT A CLEARANCE.
- [x] No em dashes in my own prose; quoted rows and the protocol's heading keep theirs.
- [x] No position taken or recommended. Nothing committed.

## 8. What in the draft was wrong or unclear

The Q7 range CONVENTION leaves the growth input and the price-above-range case open in ways that would let two analysts
differ. It says to carry owner cash "at the growth the business has actually shown" but not whether that growth is
aggregate or per share: for PG, aggregate owner cash grew about 2.9% a year and owner cash per diluted share about 4.1%,
because buybacks shrink the count; the per-share figure set against a whole-company price double-counts the buyback, so I
used aggregate, but nothing in the draft says so. It also says "owner cash after every real cost" without saying whether
capex enters in full or only its maintenance part (Q3 asks for a maintenance guess; the Q7 CONVENTION does not take it); I
used all capex and showed the D&A variant. The two closes besides IN are "TOO HARD" (range wider than three to one) and
"OUT" (price "inside it or just below its bottom"); the commonest case for a quality name, a price above the top, is not
named, and I closed it OUT through the floor CONVENTION and the "does not clear the floor" stop. Finally, the floor is an
"expected return at the price" with no stated way to compute it (yield plus growth, or the discount rate that equates the
range's cash stream to the price); here both readings (about 7% and about 5.3%) fall below ten percent, so the box does not
depend on it, but a closer name would. Smaller: the protocol closes the run at the first failed STOP while the brief asked
for Q12, so I answered Q12 after the close and said so.
