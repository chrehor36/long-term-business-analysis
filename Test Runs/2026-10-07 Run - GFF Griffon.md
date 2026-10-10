# Company Run — Griffon Corporation (NYSE: GFF) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatch.** Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (operator rule 10). The lock in
`Screens/_daily/` was present and held by the dispatching session before the first fetch (its text: "interactive v5 re-runs
batch 5", written 2026-10-07 12:22). Working folder `Test Runs/_research 2026-10-07 GFF/`; raw filings under its `cache/`
(ignored). Run file copied from the template before any fetch.

**Contamination, declared and not used.** (1) The session context showed the repository's git status and recent commit
subjects: research folders of other companies (AYI, BDC, CHD, ARCB and others) and the subjects of the CTAS, ECL, EFX and
EPAC runs of the v5 re-run batch 4, with their Q7 alert prices. None names Griffon. (2) The memory index loaded with the
session says the queue holds "57 gate-clearers, nothing buyable" and that holding reviews are owed; it names no ticker.
(3) The lock text says this dispatch is a v5 re-run batch, and the dispatching message says earlier Griffon run files exist;
neither their dates, boxes nor contents were seen. No `Test Runs/` listing was made, no other run file, holding review,
`PORTFOLIO.md`, register or reading list was opened or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $94.51, the close of 2026-10-06 (Yahoo Finance chart endpoint through `tools/sources.py`; an aggregator, a
  live quote only, flagged under operator rule 5). The intraday quote at 12:16 EDT on 2026-10-07 was $93.08; the close of
  2026-10-06 is used as the dated price. 52-week range on the same feed $65.01 to $108.57.
- **Shares by class** from the latest filing's cover: one class, common stock $0.25 par, **45,294,716** shares outstanding at
  2026-07-31 (10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0001628280-26-053536`;
  `python Screens/cover_shares.py GFF`). Check: the 10-Q balance sheet shows 45,477 thousand common shares outstanding at
  2026-06-30 (issued 84,746 thousand less treasury), the difference being the 1.29 million shares repurchased in the nine
  months and the July purchases; basic weighted shares for the quarter 43,970 thousand exclude unvested restricted shares,
  diluted 45,148 thousand. No 8-K filed after the 10-Q (`0001628280-26-054906`, `-055203`, `-055694`;
  `0000930413-26-002595`) reports an issuance or a tender. The cover count is used.
- **Market cap:** 45.295M × $94.51 = **$4,281M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-06 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025 (year to 2025-09-30), filed 2025-11-19, `0001628280-25-053242`, as originally filed (two segments).
  - **8-K of 2026-08-07, `0001628280-26-054906`, Exhibit 99.1**: the FY2025 10-K items 1, 1A, 1C, 2, 7, 7A and 8 recast
    with the AMES businesses as discontinued operations and one reportable segment (auditor's consent and dual-dated
    opinion, Grant Thornton, "November 19, 2025 except for [...] August 7, 2026"). This is the filed statement of the
    business Griffon now is, and is the primary source for FY2023 to FY2025.
  - 10-Q for the quarter ended 2026-06-30, `0001628280-26-053536` (continuing operations; subsequent events).
  - 8-Ks: 2026-06-11 `0000930413-26-001842` (AMES North America joint venture closed; Australasia sale signed);
    2026-08-04 `0001628280-26-052181` (Australasia closed; Term Loan B repaid; pro forma statements, Ex. 99.2);
    2026-08-11 `0001628280-26-055694` and 2026-08-19 `0000930413-26-002595` (USD 800M 6.25% notes due 2034; notice of
    redemption of all 5.75% notes due 2028; revolver extended to 2031); 2022-02-18 `0000930413-22-000240` (contested
    annual meeting); 2023-01-09 `0000930413-23-000045` (Voss cooperation agreement); 2024-02-20 `0000930413-24-000626`
    (repurchase of Voss's shares); 2022-10-06 `0000050725-22-000072` (strategic review, by-law change).
  - Proxy: DEF 14A filed 2026-01-09, `0000930413-26-000074`.
  - Earlier 10-Ks for the cycle: FY2024 `0000050725-24-000152`, FY2023 `0000050725-23-000055`, FY2022
    `0000050725-22-000090`, FY2021 `0000050725-21-000068`, FY2019 `0000050725-19-000077`, FY2018
    `0000050725-18-000075`, FY2017 `0000050725-17-000060`, FY2016 `0000050725-16-000166`, FY2013
    `0000930413-13-005414`, FY2010 `0001047469-10-009877`.
  - **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 as originally
    filed, $357,440 thousand (consolidated cash-flow statement, `0001628280-25-053242`), equals the $357.4M `tools/run.py`
    printed from XBRL; stock pay $25,483 thousand and capital spending $52,435 thousand also match. The recast continuing
    figure is $307,794 thousand (`0001628280-26-054906`, Ex. 99.1).
- `python tools/run.py GFF` arithmetic lines only (saved at `cache/run_py_output.txt`): its owner-earnings table is the
  **consolidated, pre-recast** series including AMES (FY2023 $327.0M, FY2024 $284.8M, FY2025 $279.5M on the capex basis;
  five-year mean $177.6M). AMES has since left the group, so these lines describe a company that no longer exists and are
  not used for the range; the continuing-operations series is built at Q4 from the recast statements. Its ten-year balance
  sheets are used at Q4. Nothing it prints as a rule, an id or a verdict is used (Part VII, the tooling).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own Griffon "if the market closed for five years"
**[M1997-109]**, which turns on garage doors, not on the 2026 reshaping that has moved the quote. The market serves and does
not instruct: "It just tells us prices." **[M2006-077]**; the stock has run from about $65 to above $100 in a year on the
portfolio actions, and nothing in that move is evidence about the business. Margin of safety: "if you have to actually do
it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro enters: the housing turnover and
rate cycle is read only as it shows in Griffon's own volumes and prices **[M2000-094]**. Who is paid to tell you: the
company features "adjusted EBITDA" and "adjusted earnings per share", and the bankers and the private-equity buyer
(ONCAP) were on the other side of the AMES transactions; "you do not get impartial advice from Wall Street" **[M2020-037]**.
**Contrary evidence, written down as found** **[M1997-127]**: (i) before 2020 Clopay earned segment EBITDA margins of about
14%, and in 2008 to 2010 between about 1% and 5%; the 31% margin of FY2023 to FY2025 is new, and the business has not
been through a housing collapse at it. (ii) The Hunter Fan purchase of January 2022 ($845M) has been written down by
$80.0M (FY2023) and $243.6M (FY2025, the whole remaining goodwill and part of the trademark). (iii) The AMES exit came
partly in paper: of North America's consideration, $161.1M is a 10% pay-in-kind second-lien loan to the buyer and the rest
a 43% minority stake; of Australasia's, a USD 48.6M PIK note and a 49% stake. (iv) Shareholders' equity has fallen to
$129M at 2026-06-30 against $1.27B of debt, after buybacks of $1.0B at cost since 2022. (v) Say-on-pay failed in February
2022 (34% for) and the President and COO lost his board seat to an activist's nominee.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered and sized within the buyer's means, puts the buyer at
no risk of ruin from this name: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]** is the buyer's rule and is not engaged by a stock bought for cash, with which "Never risk permanent loss of
capital." **[L2023-005]** is kept by sizing; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business now is.** After June to July 2026 Griffon is one reportable segment: Clopay (residential sectional
  garage doors under Clopay, IDEAL and Holmes; commercial sectional and rolling steel doors under Clopay, Cornell and
  Cookson) and Hunter Fan (ceiling and industrial fans) (recast 10-K, Item 1, `0001628280-26-054906`). FY2025 continuing
  revenue $1,795.4M: residential repair and remodel $956.7M (53%), commercial $702.8M (39%), residential new construction
  $136.0M (8%), the split "contains certain management assumptions" (Note 17). About 95% of revenue is in the United
  States. Clopay manufactures in Troy and Russia, Ohio, Mountain Top, Pennsylvania and Goodyear, Arizona and ships through
  57 distribution centres; it is "currently the exclusive supplier of residential and commercial garage doors to Home Depot
  and Menards" and serves over 3,000 independent installing dealers (Item 1). Hunter Fan's products are made by contract
  manufacturers, chiefly in China, and sold against retailers' house brands (Hampton Bay, Harbor Breeze) (Items 1, 1A).
  Beside the operating business Griffon holds non-operating claims from the AMES exit: 43% of Veritage Brands (carried at
  $118.6M) and a $161.1M 10% PIK second-lien loan to it, due 2029-12-09 (8-K `0000930413-26-001842`); 49% of the AMES
  Australasia joint venture (USD 20.9M) and an AUD 69.3M (USD 48.6M) PIK note (10-Q, subsequent events).
- **The key variables** "trying to identify the key variables in that particular business, and evaluating how predictable
  they were first" **[M1998-044]**: (1) the price Clopay can hold over steel, labour and freight, in an industry of a few
  national makers; (2) the volume of door replacement and remodelling, which follows the age of the housing stock and
  existing-home turnover; (3) the retail channel, where two customers are exclusive and their loss "would have a material
  adverse effect" (Item 1); (4) commercial construction and replacement. The product changes slowly: a galvanised-steel
  sectional door, made by Clopay since 1964; the electronics (openers) are bought from third parties (Item 1). No variable
  is a technology forecast **[M1999-063]**.
- **Do the past statements tell me the future ones?** **[M2008-033]**. For volume and for the industry's shape, yes: the
  demand drivers are physical and slow. For the margin, the statements show a break: Clopay's segment EBITDA margin was
  about 1% to 5% in 2008 to 2010, about 14% in 2017 to 2019, 17% in 2020 to 2021, 27% in 2022 and 31% to 32% in 2023 to
  2025 (segment tables, accessions at Step 0; figures at Q2). Whether that break lasts is the castle question and is
  Q2's, by the routing **[M1998-008]**: Q1 asks whether the economics can be foreseen at all, and they can be put in
  terms whose answer is knowable from filings, not a forecast insiders would refuse to write down **[M2000-105]**.
- **Hunter Fan** is a consumer import business exposed to tariffs and retailers' private labels (Item 1A), a smaller and
  harder part; by the business-of-parts convention (Q2) it does not decide: on the recast figures it carried about $211M of
  FY2025's $1,795M revenue and roughly 5% of its EBITDA (derived at Q2). The non-operating AMES claims are investments, read
  at Q4 and Q7; neither is more than half of, or the largest part of, five-year operating profit.
- **Doubt test** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**:
  the deciding part is a manufactured building product with physical demand, sold through dealers and two home centres;
  I understand "the economic dynamics of the industry" **[M2011-014]**: few national makers, distribution and lead times,
  steel cost, the retail channel. The doubt is about the level of margin, which is a castle doubt, not a circle doubt.
- **VERDICT: IN.** The deciding part's ten-year economics turn on knowable, slow variables **[M2006-076]**, **[M1995-051]**;
  "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]** depends on whether the post-2022 margin holds, which Q2 asks.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (business of parts, Q2 CONVENTION). Griffon now reports one segment with two reporting units, Clopay and
Hunter Fan (recast Note 17, `0001628280-26-054906`). Hunter is not reported separately; its size is derived: FY2025
continuing revenue $1,795.4M less the former Home and Building Products segment (Clopay) $1,584.2M (original FY2025 10-K,
`0001628280-25-053242`) leaves about $211M for Hunter; continuing adjusted EBITDA $461.8M against Clopay's segment
adjusted EBITDA $494.6M less corporate overhead of about $58M leaves roughly $25M for Hunter (a derivation, not a filed
figure). "lumping them together [...] impedes analysis" **[L2008-005]**, so they are read apart.

| part | share of five-year operating profit | castle | decides |
|---|---|---|---|
| Clopay (garage and rolling steel doors) | above 90% (derived; FY2021 to FY2025 segment adjusted EBITDA $181.0M, $412.7M, $510.9M, $501.0M, $494.6M) | read below | **yes** (more than half) |
| Hunter Fan (fans, contract-made in Asia) | under 10% (derived), and impaired twice | open on the evidence: retailers' house brands, tariffs, $80.0M trademark impairment FY2023, $243.6M goodwill and trademark impairment FY2025 (recast Item 7); "a product that can be shipped in from abroad very easily" **[M2007-116]** | no; carried to Q7 as an ordinary business at no growth |
| AMES claims (43% of Veritage, $161.1M PIK loan; 49% of the Australasia venture, USD 48.6M PIK note) | none in operating profit | not a castle of Griffon's; minority stakes in businesses Griffon chose to leave | no; investments, valued at Q7 |

The file closes on Clopay. **[M2023-031]** stays open against the parts reading (the framework's note).

**Clopay over the cycle, from the filer's own segment tables** (Clopay alone: CBP to FY2010, HBP from FY2017; FY2011 to
FY2016 Clopay was reported inside a segment with AMES and is not separable; dollars in millions):

| FY | revenue | segment EBITDA (filer's measure) | margin | price and mix, as the filer states it | segment EBIT on year-end segment assets |
|---|---|---|---|---|---|
| 2008 | 435.3 | 10.2 | 2.3% | | loss (operating loss $17.4M incl. $12.9M goodwill impairment) |
| 2009 | 393.4 | 3.1 | 0.8% | "favorable shift in mix" while volume fell | negative (operating loss $11.3M on assets $169.3M) |
| 2010 | 389.4 | 19.4 | 5.0% | | about 3% |
| 2017 | 568.0 | 81.8 | 14.4% | | 34% (EBIT 70.4 on 204.7) |
| 2018 | 698.0 | 100.3 | 14.4% | +10%; CornellCookson bought June 2018 for $180M | 21% |
| 2019 | 873.6 | 120.2 | 13.8% | +5% | 18% |
| 2020 | 927.3 | 153.6 | 16.6% | | |
| 2021 | 1,041.1 | 181.0 | 17.4% | +8% | 25% |
| 2022 | 1,506.9 | 412.7 | 27.4% | **+47%**, volume −2% | 54% |
| 2023 | 1,588.5 | 510.9 | 32.2% | +8%, volume −3%, "reduced material costs" | |
| 2024 | 1,588.6 | 501.0 | 31.5% | flat; residential volume up, commercial down | 66% |
| 2025 | 1,584.2 | 494.6 | 31.2% | +2%, volume −2% | 62% |
| 9M FY2026 (continuing, incl. Hunter) | 1,357.5 | 331.8 (company adjusted EBITDA) | 24.4% | +6%, volume −3% | |

Sources: FY2010 10-K `0001047469-10-009877` (2008 to 2010); FY2019 10-K `0000050725-19-000077` (2017 to 2019, segment
assets, D&A); FY2022 10-K `0000050725-22-000090` (2020 to 2022, assets 2021 and 2022); FY2024 10-K
`0000050725-24-000152` and FY2023 10-K `0000050725-23-000055` (2023 price and volume); FY2025 10-K
`0001628280-25-053242` (2023 to 2025, assets 2024 and 2025); 10-Q `0001628280-26-053536`. Segment assets include the
CornellCookson goodwill and intangibles from 2018 (goodwill $191.3M), so the returns on tangible capital are higher than
the last column. Segment EBITDA excludes corporate overhead and stock pay; it is the filer's own measure, used here only
to compare the part with itself over time. The 2010 revenue is derived from the filer's statement that it fell $4.0M from 2009; the 2010 return uses the 2009 segment assets, since the 2010 figure includes AMES, bought that September.

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent.* Clopay is "the largest manufacturer and marketer of garage doors and rolling steel doors
   in North America", the exclusive garage-door supplier to Home Depot (40 years) and Menards (over 30), with over 3,000
   installing dealers and 57 distribution centres giving quick-ship service (recast Item 1). Scale, distribution and the
   two retail accounts are the factors; none depends on "the genius of the lord in the castle" **[M1995-038]**.
2. *The money test.* The test is whether a well-funded attacker could take it **[M2011-015]**. One has tried: Nucor, the
   largest US steelmaker, bought C.H.I. Overhead Doors in June 2022 for about $3.0B, "approximately 13x C.H.I.’s estimated
   trailing twelve-month EBITDA" (Nucor 8-K Ex. 99.1, `0001193125-22-151808`), and Rytec for $565M in July 2024, saying it
   intends "to grow CHI’s business by gaining further market share" (Nucor FY2022 10-K, `0001564590-23-002793`) and to put
   its own paint lines and sales channels behind it (FY2025 10-K, `0001193125-26-071575`). "one competitor is frequently
   enough to ruin a business." **[M2012-108]** Against this: since 2022 Clopay's margin has not fallen.
3. *Pricing power and the agony before a rise.* Price and mix rose 10% (2018), 5% (2019), 8% (2021), 47% (2022), 8% (2023),
   2% (2025) and 6% (nine months of 2026), and in 2023 the margin rose further on "reduced material costs": the price was
   held when steel fell. That is what the row asks to be observed, "the price behavior" **[M2005-020]**; and **[M2005-017]**
   describes the strong position as the one that will "pass through increases in raw material costs". But volume fell in
   2022, 2023, 2025 and 2026, and no filing gives Clopay's share of industry units, so the stronger form, to "charge more for
   a product and maintain or increase market share" **[M2000-031]**, is not shown.
4. *Unit volume and share of mind.* Volume fell 2% (2022), 3% (2023), 2% (2025) and 3% (nine months of 2026); no industry
   unit figure is in Griffon's filings. Not shown either way.
5. *The low-cost position.* Clopay "manufactures exclusively in the United States" and is the largest; C.H.I. (Nucor) claims
   "industry-leading fulfillment times" and has a steelmaker behind its input cost; Clopay claims "industry leading lead
   times". Which is the low-cost producer is not shown in any filing read.
6. *The brand and the retailer.* The Clopay name is sold under Home Depot's roof as its exclusive door; the risk the rows
   name is that "the value of having the brand moves over to the retailer from the product itself" **[M2001-090]**; the
   10-K says the loss of either retailer "would have a material adverse effect". Home Depot was about 10% of continuing
   revenue in FY2023 and under 10% in FY2024 and FY2025 (Note 17).
7. *Widening or narrowing, and what could destroy it.* What destroyed the returns once is in the table: in 2008 to 2010 the
   same castle earned 1% to 5% margins and lost money at the operating line. "Fixed costs are high [...] and that's bad news
   when unit volume heads south." **[L2006-009]** describes what the filing says of 2009 ("the sharp decline in volume, and
   the resultant unfavorable impact on absorption of fixed operating expenses", FY2010 10-K).

**The competitor row** (same kind of metric, the competitors' own filings):

| rival | metric | figures | accession |
|---|---|---|---|
| C.H.I. Overhead Doors (Nucor since 2022) | price paid; EBITDA multiple; net tangible operating assets acquired | $3.0B at about 13x TTM EBITDA (so about $230M EBITDA, mid-2022); receivables, inventory, other current assets, plant and other assets less current and other liabilities about $189M | `0001193125-22-151808`; `0001564590-23-002793` (purchase allocation) |
| Masonite (doors, not garage doors; same home-centre channel; acquired by Owens Corning, consummated May 2024; last 10-K FY2023) | North American Residential adjusted EBITDA margin | 2015 11.3%; 2018 13.9%; 2021 19.1%; 2022 20.2%; 2023 19.6% | `0000893691-16-000072`; `0000893691-19-000016`; `0000893691-24-000011`; 8-K `0001193125-24-138587` |
| Overhead Door (Wayne Dalton), owned by Sanwa Holdings | not an SEC filer | flagged; Sanwa reports in Japan | none |
| Chamberlain (openers; a complement more than a rival) | private | flagged | none |
| Amarr (ASSA ABLOY), Raynor, Haas | not SEC filers; not named in the brief, named here as other national makers from general knowledge, unverified in any filing read | flagged | none |
| Stanley Black & Decker (former AMES rival) | tools segment profit margin | 2018 14.2%; 2019 15.2%; 2020 17.8%; 2024 9.0%; 2025 10.1% | `0000093556-21-000008`; `0000093556-26-000009` |
| Toro (former AMES rival) | Residential segment earnings (EBIT from 2024) margin | 2018 9.9%; 2019 9.9%; 2020 13.8%; 2024 7.9%; 2025 4.2% | `0000737758-20-000029`; `0000737758-25-000115` |
| AMES itself (CPP segment; Hunter inside it 2022 to 2025) | segment EBITDA margin | 2017 8.3%; 2019 9.1%; 2021 9.4%; 2022 7.4%; 2023 4.6%; 2024 7.0%; 2025 9.1% | Griffon 10-Ks at Step 0 |

Read together: the one garage-door rival with a filed price (C.H.I.) shows the same very high return on tangible capital at
the 2022 peak that Clopay shows; the best-documented adjacent door maker (Masonite) shows the same step-up through the
inflation, smaller (about 11% to 14% before, about 20% after). The tools business Griffon left earned less than either
tools rival over most of the span; that part is gone, and Griffon's remaining exposure to it is the PIK loans and the
minority stakes.

**The field's returns over the last full cycle, judged in words.** In the 2008 to 2010 housing collapse Clopay's returns
were nil to negative; mid-cycle (2017 to 2021) they were good, about 18% to 34% pre-tax on segment assets including acquired
goodwill; since 2022 they have been extraordinary, above 50%, and have held through four fiscal years of falling volume,
with price raised again in FY2025 and FY2026. The field is not one of ordinary returns over the cycle, so the OUT for a
standing castle that protects only ordinary returns does not apply. Nor is the castle shown open: no filing read shows
Clopay losing a channel, a customer or margin to C.H.I. or anyone else.

**The deciding fact.** What the castle protects across a cycle is not settled by the record. The pre-2020 Clopay protected
good mid-cycle returns and nothing in a collapse; the post-2022 Clopay earns about twice the margin, and that level is a
**change for the better** that has been tested by a falling-volume stretch but not by a full cycle, peak to peak or trough
to trough, and not by a downturn like 2009. "the railroads were a terrible business for decades and decades and decades
and then they got good." **[M2017-026]** says such changes happen; the framework credits one only on the evidence of a full
cycle in which the price behaviour held (Q2, CONVENTION of 2026-10-06), and the falling-volume years since 2022 are half
of one. Whether the doubled margin is a lasting change in the industry's structure (fewer national makers, a steelmaker
owning a rival, price discipline learnt in the inflation) or a peak that a recession and an attacker with money will take
back is knowable in part from records not yet read (the main rivals' own reports across 2008 to 2025, industry shipment
data against Clopay's volume, Clopay's price against steel cost), and is the work of a research pass. Until then, "it’s
just too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**, and the box is "too
hard" **[M2006-013]**, not OUT.

**VERDICT: TOO HARD (WORK).** Deciding part: Clopay. The castle stands and is not shown open; the level of return it
protects across a full cycle turns on a change for the better (the 2022 margin step from about 14% to 17% to about 31%)
that the framework credits only on a full cycle, which the record does not yet contain. Cause WORK: the question is
"important and knowable" in the sense of **[M2006-076]**, and part of its evidence (rivals' cycle records, industry
volumes, price against steel) is on the public record and not read. Research-pass steps 1 and 2 are at the end of this
file; they are not run. Q3 to Q12 are NOT REACHED; figures after this point are COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance-sheet reading and the recast owner cash, done to supply the reporting figures, are under AFTER
THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH. STOP.
NOT REACHED. The two reporting figures the brief asks for are computed under AFTER THE STOP as COMPUTATION, NOT A
CLEARANCE; they are no verdict and carry no entry language (operator rule 3).

## Q8 — BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US. WEIGHING.
NOT REACHED.

## Q10 — THE FAT PITCH. WEIGHING.
NOT REACHED.

## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE.
NOT REACHED. (Garage doors, commercial doors and fans; none of the businesses the question names.)

---
## THE BOX
**TOO HARD (WORK), decided at Q2** on Clopay, the deciding part: the castle stands and is not shown open, but the return it
protects across a full cycle turns on the 2022 margin step (Clopay segment EBITDA margin about 14% to 17% before, about 31%
since), a change for the better not yet tested by a full cycle. Q7 not reached; for the record the COMPUTATION range is
$69.70 to $109.58 a share (all-equity basis, central) against $94.51. **Integrity facts recorded, not judged** (Part VII):
the failed say-on-pay vote and the contested election of February 2022, the retention payments of the strategic review,
the CEO who is also Chairman, adjusted EBITDA in the bonus plan and in guidance. Research-pass steps 1 and 2 are below.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found* **[M1997-127]**; *no verdict; the box is unchanged (operator rule 2).*

**Bearing on Q3 (capital needed).**
- Continuing capital spending $31.4M (FY2023, before $11.9M of real-estate proceeds), $50.3M (FY2024, including new
  distribution warehouses), $41.7M (FY2025), $23.7M in nine months of FY2026, guided $50M for FY2026; depreciation about
  $21M to $24M a year (D&A $35.5M, $35.9M, $38.5M less filed amortization $14.6M, $14.3M, $14.6M) (recast statements;
  8-K Ex. 99.1 of 2026-08-05, `0001628280-26-052927`). Clopay's segment EBIT on year-end segment assets: 18% to 34%
  (2017 to 2021), 54% to 66% (2022 to 2025) (Q2 table). Revenue of the continuing business fell from $1,871.2M (FY2023)
  to $1,795.4M (FY2025); the nine months of FY2026 rose 3% on price.
- Hunter Fan: bought January 2022 for $845M, financed chiefly by an $800M Term Loan B; goodwill recognised $250.7M (FY2023
  10-K); trademark impaired $80.0M (FY2023); "the remaining goodwill" $136.6M and a further $107.0M of trademark impaired in
  FY2025 (recast Item 7). The difference between $250.7M and $136.6M was written off before FY2025; the unit split of the
  FY2022 consumer-segment impairment ($342.0M goodwill, $175.0M trademarks, FY2022 10-K) was not read.

**Bearing on Q4 (the accounts). COMPUTATION, NOT A CLEARANCE.**
- *The balance sheets first, ten year-ends* (consolidated, first-filed XBRL through `tools/run.py`, read against the filed
  statements of FY2025, FY2022 and FY2019; USD millions):

  | year-end | equity | goodwill | intangibles | cash | receivables | inventory | long-term debt | retained earnings |
  |---|---|---|---|---|---|---|---|---|
  | 2017 | 399 | 319 | 205 | 48 | 208 | 299 | 968 | 480 |
  | 2018 | 474 | 439 | 371 | 70 | 281 | 398 | 1,108 | 551 |
  | 2019 | 478 | 437 | 357 | 72 | 264 | 442 | 1,094 | 569 |
  | 2020 | 700 | 443 | 355 | 218 | 348 | 414 | 1,037 | 608 |
  | 2021 | 807 | 426 | 350 | 249 | 295 | 473 | 1,033 | 670 |
  | 2022 | 478 | 336 | 762 | 120 | 362 | 669 | 1,561 | 344 |
  | 2023 | 315 | 328 | 635 | 103 | 312 | 507 | 1,460 | 282 |
  | 2024 | 225 | 329 | 619 | 114 | 313 | 425 | 1,516 | 461 |
  | 2025 | 74 | 193 | 488 | 99 | 291 | 441 | 1,404 | 479 |
  | 2026-06-30 (10-Q, continuing; AMES in held-for-sale) | 129 | 191 | 347 | 110 | 202 | 186 | 1,260 | n/r |

  What moved and why: equity rose to $807M by 2021 on retained earnings and the August 2020 offering of 8.7M shares
  ($178.2M net; FY2021 10-K `0000050725-21-000068`), then fell to $74M in 2025 through the FY2022 impairments ($517.0M), two
  $2.00 special dividends (July 2022, May 2023), and buybacks that took treasury stock from $420M (2022) to $1,044M (2025);
  the 2025 figure also carries the $243.6M Hunter impairment. Goodwill and intangibles jumped with Hunter in 2022 and have
  been written down since. Long-term debt rose $528M with Hunter and has been paid down since 2022. Inventory rose to $669M
  in 2022 (the supply-chain year) and was worked down. The continuing receivables ($197M) and inventories ($172M) at
  2025-09-30 are about 11% and 10% of continuing revenue; at 2026-06-30 both are higher ($202M, $186M) in the seasonal
  build the MD&A describes, and prepaid and other current assets rose from $42M to $55M. What the figures say: a business
  that throws off cash, and a capital structure run with thin book equity since the buybacks. What they do not say: the
  value of the AMES claims ($350.1M at carrying, none of it cash yet) or the level of margin through a downturn.
- *Owner cash, continuing operations as recast* (OCF less stock pay less all capital spending; USD millions): FY2023
  $262.2M, FY2024 $231.5M, FY2025 $241.9M; twelve months to 2026-06-30 $230.3M (FY2025 less nine months of FY2025 plus
  nine months of FY2026, 10-Q). Before interest, after tax at the filer's 27.2% adjusted rate: $334.9M, $304.8M, $309.5M,
  $293.8M. Stock pay $39.2M, $25.6M, $24.2M, TTM $28.0M is deducted every year.
- *EBITDA in the filer's own mouth and the recurring charges.* "Adjusted EBITDA" heads every release and the annual
  outlook (FY2026: revenue $1.8B, adjusted EBITDA $458M, 8-K `0001628280-26-052927`), is "a significant performance
  metric in our annual management incentive bonus plan" (recast Item 7), and the company's "free cash flow" is OCF less
  capex with stock pay not deducted. "Strategic review - retention and other" was excluded from adjusted results in four
  successive years (continuing: $9.7M FY2022 consolidated, $15.9M FY2023, $9.1M FY2024, $2.6M FY2025), with proxy expenses
  of $7.0M (FY2022) and $2.7M (FY2023). Annual guidance is given. These are the habits the framework records at Q4 and
  carries to Q5; not weighed here. Of adjusted figures the rows say a management that "regularly attempts to wave away
  very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**.
- No sign was found in the statements read of prepaid or deferred accounts building out of line, reserves moving, or
  profits on both sides of a contract; the auditor (Grant Thornton since 2006) gave a clean opinion with one critical audit
  matter, the Hunter trademark impairment.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- February 17, 2022 annual meeting (8-K `0000930413-22-000240`): say-on-pay failed, 17,361,455 for and 33,983,871
  against; a nominee of Voss Capital (H. C. Charles Diao) was elected with 36,755,237 votes while the company's nominee
  Robert F. Mehmel, President and COO, received 19,993,094; shareholders approved declassifying the board and a 25%
  special-meeting threshold. Proxy expenses $7.0M (FY2022).
- January 8, 2023: cooperation agreement with Voss; Voss's CIO appointed to the board, its slate withdrawn, standstill
  (8-K `0000930413-23-000045`). February 20, 2024: the company bought Voss's 1,500,000 shares privately at $65.50, "a 3.7%
  discount" to the prior close of $68.04, with a two-year standstill and voting commitment; the Voss director resigned
  (8-K `0000930413-24-000626`).
- Strategic review announced May 16, 2022, concluded April 20, 2023 with no transaction; retention payments charged in
  FY2022 to FY2025 (above). Kramer's employment agreement amended April 28, 2022 and November 14, 2022 (during the review)
  and restated May 8, 2024 (DEF 14A `0000930413-26-000074`).
- Ronald J. Kramer: CEO since April 2008 and Chairman since January 2018; formerly President of Wynn Resorts (2002 to
  2008); owns 2,630,251 shares (5.6%); FY2025 total pay $17,515,575, 305 times the median employee; say-on-pay in March
  2025 approved by about 89.7% of votes cast (proxy). A CEO who is also Chairman is the case **[L2014-026]** names.
- The 2026 proxy discloses a related-person transaction policy and **no** related-person transaction (section
  "Certain Relationships and Related Person Transactions", read in full). No instance found in the 2026 proxy of dealings
  between the company and the Chairman and CEO beyond his employment terms; earlier proxies were not read for this.
- The FY2026 Q1 grant: 531,456 restricted shares to four senior executives (target 177,152) vesting on return on invested
  capital and relative total shareholder return, with a two-year post-vesting hold (10-Q, Note on stock pay).

**Bearing on Q6 (money and owners).**
- Buybacks (shares; average price; source 10-Ks and 10-Q): August 2011 to September 2017, 20.4M shares at $12.81; FY2016
  3.55M at $15.86; FY2017 0.13M at $17.06; FY2019 37,500 at $9.92; FY2020 an offering of 8.7M shares instead ($178.2M
  net, about $20.48 each); FY2021 and FY2022 none; FY2023 4.14M at $36.39; FY2024 4.77M at $57.52 (including Voss's
  1.5M at $65.50); FY2025 1.90M at $70.99; nine months of FY2026 1.29M at $80.48 (the June quarter at $85.00).
  Authorisations name sums, not prices ($400M added November 2024; $193.8M left at 2026-06-30). The rows on a programme that
  never states a price: such announcements "almost never refer to a price above which repurchases will be eschewed"
  **[L2016-002]**. Against the COMPUTATION range below (bottom $69.70 a share, central basis), the FY2023 and FY2024 average
  prices sit below the bottom, FY2025 about at it, and FY2026 above it. Not weighed.
- Dividends: regular $0.09 a quarter (2022) raised to $0.22 (from December 2025); special $2.00 in July 2022 and May 2023.
- Deals: CornellCookson (June 2018, $180M) into Clopay; Hunter (January 2022, $845M, impaired as above); Telephonics sold
  June 2022 for $330M (FY2022 10-K); the plastics business sold in 2018 (FY2022 10-K, "We divested our specialty plastics
  business in 2018"; the price was not read in this run); AMES North America into Veritage Brands (June 9, 2026: $100M
  cash, a $161.1M 10% PIK second-lien loan due 2029-12-09, 43% equity carried at $118.6M; loss $26.6M); AMES Australasia
  (July 31, 2026: AUD 258M, USD 180.9M, cash, an AUD 69.3M PIK note, 49% equity carried at USD 20.9M; estimated gain
  about $123M); AMES U.K. closed with $25.9M of charges. The PIK loans rank behind Veritage's first-lien lenders and carry
  covenants of up to 4.90x total funded debt to adjusted EBITDA (8-K `0000930413-26-001842`).

**Bearing on Q7 (the reporting figures). COMPUTATION, NOT A CLEARANCE.** Script and output:
`Test Runs/_research 2026-10-07 GFF/q7_computation.py`, `q7_output.txt`.
- *Window.* The business Griffon now is has filed statements for three fiscal years only (FY2023 to FY2025, recast); FY2021
  and FY2022 were never recast and Hunter was bought inside FY2022 with no filed pre-acquisition record. **CONVENTION of
  this run:** the base is the mean of the three recast years, the TTM to June 2026 shown beside; rationale: the literal
  five-year window can only be built for a company (with AMES) that no longer exists, and Q7's specific (c) values a
  merger on the combined companies' own averages, which here are the recast years. The literal window is shown beside:
  `tools/run.py`'s five-year consolidated mean $177.6M (with AMES, after interest), $69.52 a share at no growth on the
  equity-only basis.
- *Base:* $316.4M a year before interest (all-equity), $245.2M after interest (equity-only). *Growth shown* FY2023 to
  FY2025: −3.9% a year on both; by specific (b) the decline makes the bottom and no growth the top. No year is called
  aberrational by the filer, so specific (a) does not move the base; the doubt about the margin level is Q2's and is why
  the file is closed.
- *Specific (e).* The filing allows a maintenance guess: depreciation (D&A less filed amortization) against capital
  spending; growth spending above depreciation averaged $19.0M a year. The central range's top is the maintenance-only,
  no-growth case ($335.4M), its bottom the all-spending case at the shown decline; the growth spending has bought no growth
  in the window, so "growth can destroy value" is the reading, not an error.
- *Net debt* $983.5M: $1,164.4M at 2026-06-30 (gross debt $1,274.8M incl. finance leases, less cash $110.4M; 10-Q) less the
  AUD 258M (USD 180.9M) Australasia cash received 2026-07-31, a subsequent event the 10-Q states. The 10-Q also states the
  Term Loan B was repaid ($285M) from those proceeds and the revolver, which leaves net debt unchanged. The August 2026
  notes exchange (USD 800M 6.25% 2034 notes; all 5.75% 2028 notes called) was filed after the 10-Q and moves the cost, not
  the amount. Operating leases left out. The AMES claims ($350.1M at carrying) are not cash or securities and are left out
  of the central figure, shown beside.
- *Tax:* the company's own tax; the adjusted effective rate is about 27%, no carryforward that runs out inside ten years
  was found; no shelter adjustment.
- **(a) VALUE RANGE, central (all-equity basis, specifics (b) and (e)): $69.70 to $109.58 a share** (whole business
  $4,141M to $5,946M less net debt; width 1.44 to 1). Equity-only beside: $70.36 to $103.42. With the AMES claims at
  carrying: add $7.73 a share to every figure. Literal window beside: $69.52 (equity-only, no growth).
- **(b) FAIR PRICE: $42.32 a share** (central, all-equity basis): the price at which the cash stream midway between the
  range's two ends (whose value at the 5.64% sovereign is the midpoint, $89.64) earns 10%, after the company's own tax,
  ten years then no growth. Equity-only figure beside: **$49.98**. With the AMES claims at carrying: $50.05 and $57.71.
  Against the price of $94.51 the central stream is expected to return about 5.4% a year (equity-only 5.2%), below the
  sovereign's 5.64%. No cheap price is reported (Part VII, The owner's price).
- Hunter Fan, by the parts convention an open part at no growth, is inside the aggregate; its decline is part of the
  negative growth shown and is not separated.

**Bearing on Q8.** The expected return at the price on the central stream (about 5.4%) is below the 30-year Treasury
(5.64%). Not weighed.

**Bearing on Q9 (debt and exposures).**
- After August 2026: USD 800M 6.25% senior unsecured notes due 2034; a $500M secured revolver extended to August 2031
  (SOFR + 1.75%); the 2028 notes called; Term Loan B repaid (8-Ks `0001628280-26-052181`, `0000930413-26-002595`).
  Leverage by the credit agreement 2.2x net debt to EBITDA at 2026-06-30 (release); pre-tax earnings to interest in FY2025,
  before the $243.6M impairment, about 4.4x ((83.2 + 243.6 + 95.7) / 95.7; the coverage form of **[L2012-002]**).
- Concentrations: Home Depot and Menards exclusive; Home Depot about 10% of FY2023 revenue. Credit exposure to Veritage
  (PE-controlled, second lien, PIK) and to the Australasia venture. Pension plans frozen. Hunter's tariff exposure.

---
## RESEARCH PASS (TOO HARD (WORK)): STEPS 1 AND 2, WRITTEN, NOT RUN
*Part VII; CONVENTION in its form. Step 3 (the reading) and step 4 (the close) are for a later session; each step is
committed before the next.*

**Step 1.** "What do I not know that I need to know?" **[M1999-129]** The deciding question: is Clopay's post-2022 margin
(about 31%, from about 14% to 17%) a durable change in the field that the castle will protect through a downturn, or a
peak an attacker and a recession will take back? It splits into:
1. Has Clopay's price held in every year of the current falling-volume stretch? *Knowable* (Griffon's filings).
2. Has Clopay kept its share of industry units while raising price? *Knowable in part* (industry shipment statistics are
   published by the trade association; Griffon gives only volume percentages).
3. Did the main rival that files anywhere (Sanwa's North America segment, Overhead Door) show the same step-up since 2022
   and the same collapse in 2008 to 2010? *Knowable* (Sanwa's annual reports, outside EDGAR).
4. Will the new margin survive the next housing recession? *Not knowable before it happens*: no reading supplies a cycle
   that has not occurred; recorded under refinement (c) as unanswerable from primary documents, the close to be decided on
   1 to 3 **[M2006-076]**.

**Step 2.** For each knowable question: the evidence, where it is, the span, and the single fact that closes OUT, the
reading being "to possibly reject your original hypothesis" **[M1998-144]**.

| # | evidence and source | span fixed now | the one fact that closes OUT |
|---|---|---|---|
| 1 | Griffon 10-K and 10-Q MD&A, price and mix and volume lines (residential and commercial doors) | FY2022 to the latest filed quarter at the time of the reading | any filed period in which Griffon reports **unfavorable price** (negative price and mix) for doors |
| 2 | Door and Access Systems Manufacturers' Association published shipment statistics (aggregator, flagged) against Griffon's stated volume changes | calendar 2022 to 2026 | industry sectional-door unit shipments ran **5 points or more above** Clopay's cumulative volume change over the span (a share loss of that size while raising price) |
| 3 | Sanwa Holdings annual reports / securities reports, North America segment (Overhead Door) operating margin | FY2007 to FY2025 (Sanwa's fiscal years) | Sanwa North America's latest operating margin is **at or below its own FY2015 to FY2019 average** (the step-up is Clopay's alone, so the leading rival has room and reason to take it back) |

**How step 4 closes.** OUT on any one of the three facts, the STOP re-answered OUT. If none is found, the castle's price
behaviour has held through the falling-volume years and field-wide; the framework still credits a change for the better
only on a full cycle (Q2), and question 4 cannot be answered from documents, so on the text as it reads the pass would
close **TOO HARD (NATURE)** on question 4, not IN, unless a full housing downturn has by then been filed and the price held
through it (then IN, and the run continues from Q3). The pass never closes TOO HARD (WORK) a second time **[M2008-086]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits after Step 0 to Q1, after Q2, and at the close, with a pathspec of the run file and research folder only.
- [x] Dispatched to an analyst: the brief allowed the per-question commits, and the lock in `Screens/_daily/` was present
      and held by the dispatching session ("interactive v5 re-runs batch 5") throughout; the fold is the dispatcher's.
      A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no listing of `Test Runs/` was
      made; what was seen by accident (commit subjects and research-folder names of other companies in the session's git
      status; the memory index line; the lock text) is declared under Contamination at the top and was not used.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids; every M/L/R id in `principle_ledger_v5.csv`; every quoted fragment
      beside an id found in that row, apostrophes and double quotes normalised); every filing fact carries its accession;
      numbers without a filing are labelled as derived (Hunter's share; C.H.I.'s EBITDA from the stated multiple).
- [x] The order was kept; Q2's STOP closed the file; nothing after it is a clearance; Q7's figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay and all capital spending deducted; no net-income proxy); the sovereign
      from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations line and Q2); facts for later questions are under AFTER THE
      STOP; the integrity flag is in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its pre-recast consolidated owner-earnings series was shown
      as the literal window only.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded below).
- [ ] Not done: the plastics sale price (2018) and the FY2022 consumer impairment's split by unit were not read; earlier
      proxies were not read for related-party dealings; Sanwa, ASSA ABLOY, Chamberlain and Raynor have no SEC filings, so
      the garage-door competitor row rests on one rival's purchase price (C.H.I.) and an adjacent door maker (Masonite).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The full-cycle convention routes to WORK a question no work can answer.** Q2 says a change for the better is
credited only on a full cycle "until then the file is TOO HARD (WORK) on that question". A research pass can read rivals,
shipments and price lines, but it cannot read a downturn that has not happened; on the text, the pass then closes TOO HARD
(NATURE), so the WORK label promises a cure the pass cannot deliver. Here the stretch since 2022 is a long falling-volume
leg with price held, half a cycle; the framework does not say whether half a cycle with field-wide evidence ever counts.
I applied the text (WORK now, the likely NATURE close written into step 4). (2) **Q2 credits the castle on old economics
but Q7 values on the window.** Had Q2 been answered IN on the pre-2022 economics (good mid-cycle returns, a standing
castle), Q7's five-year average would have credited the very change Q2 declined to credit, since the filer calls no year
aberrational and specific (a) waits on the filer's own word. The framework does not say whether an uncredited change at Q2
must be removed from the Q7 base. (3) **A window for a company remade by divestiture.** The five-year window cannot be
built for Griffon as it now is: the recast covers three years and the acquisition inside the window (Hunter) has no filed
pre-acquisition record. Specific (c) covers mergers and deals after the window, not a recast that shortens the record; I
confessed a CONVENTION (three recast years). (4) **Claims received in a divestiture.** PIK loans and minority stakes
received as sale consideration are neither "cash and securities" for net debt nor equity-method income with dividends
received; the framework gives them no place in the range. I left them out of the central figure and showed them at
carrying beside. (5) **The fair price's "midpoint".** Part VII defines the fair price as the price at which "the midpoint
of the range earns the floor"; a midpoint is a value, not a cash stream. I took the stream midway between the two ends
(whose value at the sovereign is the midpoint) and discounted it at 10%; another analyst might discount the midpoint's
implied perpetuity, which gives a different figure. (6) **The brief's error.** The canonical brief and the dispatching
message: the message calls it "the 2023 activist contest"; the filed record shows the contest went to a vote on February 17,
2022 (Voss Capital's nominee elected over the President and COO; say-on-pay failed), and 2023 brought only a settlement
(the cooperation agreement of January 8, 2023, before any vote). It also lists Masonite as a garage-door rival: Masonite
describes itself as a maker of "interior and exterior doors and door solutions" and its FY2023 10-K never uses the word
"garage" (`0000893691-24-000011`), so it is an adjacent comparison only; and it names the
two segments as current, when since June 2026 Griffon reports one segment, the consumer segment being discontinued.
