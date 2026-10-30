# Company Run — Costco Wholesale Corporation (NASDAQ: COST) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked by this analyst. *(Filled at the fold by the dispatching session, 2026-10-06: not held; `PORTFOLIO.md` lists COST only in the opportunity set, from the v4.1 run of 2026-08-30.)* The dispatch brief's blind rule forbids opening
`PORTFOLIO.md` and forbids trying to learn whether anyone holds or wants this name; the template line asks for exactly that
check. The conflict is recorded under WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR, and the dispatching session fills this
line at the fold.

**Dispatched run (operator rule 10).** Brief received 2026-10-06, following `Screens/_daily/_dispatch_brief.md` without
departure. Lock `Screens/_daily/_overnight.lock` observed present at 16:53 on 2026-10-06, written by the dispatching
session. Per-question pathspec commits of this file and `Test Runs/_research 2026-10-06 COST/` only.

**CONTAMINATION, declared.** A directory listing of `Test Runs/` made at the start of the session (to confirm this file
did not already exist) showed two file names about this company: a run of 2026-08-30 under v4.1 and an addendum of
2026-09-01 whose title mentions finance-lease additions in the COST and HD runs. Neither was opened, searched or used; the
treatment of finance-lease principal below follows the dispatch brief's own description of `tools/run.py` (which lists
finance-lease principal among the alternates) and the filed cash-flow statement, not the addendum. `tools/run.py` prints
v4 material (a "yield", a "growth the price assumes" line and "points over the sovereign"); only its arithmetic lines were
used (Part VII). One more sighting, after the run was written: the `git log` printed at the final commit showed the
subject line of a commit by the dispatching session (a1b5b41b) naming T2 re-run results for four tickers, a PBH re-run
closed OUT at Q7, a blind-run clause added to the template's position note and a change of the brief's reply line to
two figures. The subject line was read; the commit's files were not opened; nothing in it was used in this run, which
was already complete through Q7 when it appeared. Nothing else on the blind list was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $935.68 (live quote 2026-10-06, printed by `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $.005 par, 443,478,804 shares as of
  2026-05-27 (10-Q for the quarter ended 2026-05-10, filed 2026-06-03, accession `0000909832-26-000051`;
  `python Screens/cover_shares.py COST`). Checked against issued less treasury: the balance sheet shows 443,514,000
  shares "issued and outstanding" at 2026-05-10 and no treasury stock (repurchased shares are retired under the Washington
  Business Corporation Act, 10-K Note 1). Later filing: the 8-K of 2026-09-24 (`0000909832-26-000084`, exhibit 99.1)
  shows 443,266,000 issued and outstanding at 2026-08-30; no prospectus or issuance since the 10-Q. 443.479M used.
- **Market cap:** $414,954M (443.479M × $935.68).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for fiscal 2025, the 52 weeks ended 2025-08-31, filed 2025-10-08, accession
  `0000909832-25-000101` (the latest 10-K on file; the fiscal 2026 10-K for the year ended 2026-08-30 is **not yet filed**
  as of 2026-10-06; the full-year fiscal 2026 statements are furnished unaudited and "Subject to Reclassification" in the
  8-K of 2026-09-24, `0000909832-26-000084`, exhibit 99.1, and are used below as the latest cycle, flagged as such); the
  10-Q for the 12 weeks ended 2026-05-10 (`0000909832-26-000051`); the proxy, DEF 14A filed 2025-12-04
  (`0000909832-25-000159`); 8-Ks of 2026-01-21 (`0000909832-26-000016`, annual meeting votes), 2026-07-08
  (`0000909832-26-000060`, June sales and dividend) and 2026-09-24; and, for the span, the 10-Ks for fiscal 2016
  (`0000909832-16-000032`, filed 2016-10-12), fiscal 2019 (`0000909832-19-000019`, filed 2019-10-11) and fiscal 2022
  (`0000909832-22-000021`, filed 2022-10-05). **One figure cross-checked against the
  filed statement:** net cash provided by operating activities, fiscal 2025, $13,335M, as printed by `tools/run.py` from
  XBRL and as printed on the consolidated statement of cash flows, 10-K page 41. Match. Also matched: additions to
  property and equipment $5,498M and stock-based compensation $860M on the same statement.
- `python tools/run.py COST` arithmetic lines only (USD millions, fiscal years ended late August or early September):

| FY | OCF | SBC | capex | finance-lease principal | D&A | owner cash, capex basis | owner cash, D&A basis |
|---|---|---|---|---|---|---|---|
| 2021 | 8,958 | 665 | 3,588 | 67 | 1,781 | 4,638 | 6,512 |
| 2022 | 7,392 | 724 | 3,891 | 176 | 1,900 | 2,601 | 4,768 |
| 2023 (53 wks) | 11,068 | 774 | 4,323 | 291 | 2,077 | 5,680 | 8,217 |
| 2024 | 11,339 | 818 | 4,710 | 136 | 2,237 | 5,675 | 8,284 |
| 2025 | 13,335 | 860 | 5,498 | 147 | 2,426 | 6,830 | 10,049 |
| 2026 (8-K, unaudited) | 15,825 | 924 | 6,435 | 91 | 2,674 | 8,375 | 12,227 |

  Owner cash, capex basis = OCF less stock pay less all capital spending (additions to property and equipment plus
  finance-lease principal, the "other capital payment" the tool lists as an alternate and which the filed cash-flow
  statement puts in financing). Five-year average FY2021 to FY2025: **$5,085M** (capex basis), $7,566M (D&A basis). The
  tool's three-year window (FY2023 to FY2025) averages $6,062M on the same basis; the window spread is part of the range.
  SBC resolved every year from `ShareBasedCompensation`, complete (the only stock pay is RSUs; Note 7). The FY2021 and
  FY2022 lines were read from the XBRL facts and the fiscal 2022 10-K's cash-flow statement, since the tool printed only
  three years in detail. All six fiscal years' figures are in `Test Runs/_research 2026-10-06 COST/q7_arith.py`.

## THE FOUNDATIONS (not a gate)
A share is a business: the question asked of Costco is what its members will do and what it will earn ten years out, not
when the quote moves, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. The
market serves: the quote carries no instruction about value, "It just tells us prices" **[M2006-077]**, and the price
here ($936) is read against what the filings say the cash is, not against what the price has done. Margin of safety: if
the decision "with pencil and paper" is "too close to think about" **[M1996-084]**, it is not taken; the arithmetic at
Q7 is kept for the reporting figures, not to clear a close call. No macro enters: "macro conclusions are — just never
enter into the discussion" **[M2000-094]**; inflation enters only as the business's freedom to price, read at Q2 from the
2022 gross-margin record. Who is paid to tell you: this name is the one the speakers themselves praised by name, and one
of them sat on its board, so the praise rows are commentary with "a dog in this fight" **[L2009-015]** and are weighed
below only where the filings say the same thing; "don’t ask the barber whether you need a haircut" **[M2011-083]**. The
analyst's habits: write the contrary evidence down at once **[M1997-127]**; look "for what’s wrong in things because
that’s part of investing – looking at what you’re missing" **[M2025-013]**; "What do I not know that I need to know?"
**[M1999-129]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the worldwide renewal rate has slipped,
90% at the end of fiscal 2022 to 89.8% at fiscal 2025 to 89.7% at the third quarter of fiscal 2026, and U.S. and Canada
from 93% to 92.3% to 92.2% (10-K FY2022 p.5; 10-K FY2025 p.5; 10-Q Q3 FY2026 p.22), which the company attributes to
memberships sold online renewing "at a slightly lower rate on average"; (2) gross margin fell 65 basis points in fiscal
2022 (11.13% to 10.48%) as costs were absorbed rather than passed on (10-K FY2022, MD&A, Gross Margin); (3) share repurchases have been
made at $505, $695, $958 and $945 a share (FY2023 to the first 36 weeks of FY2026) under a program that names no price,
and the share count has not fallen in ten years (438M to 443M); (4) the one-year performance hurdle on executive RSUs is a
3% rise in net sales or a 2% rise in pre-tax income, in a business that grew sales 8% and pre-tax income 11% that year
(proxy p.15); (5) the owner-cash yield at the price is about 1.6% on fiscal 2025 and 2.0% on fiscal 2026 (Step 0 table
against $414,954M); (6) the fiscal 2026 10-K is not filed, so the latest full year rests on an unaudited release; (7) a
False Claims Act investigation into prescription-drug claims has been open since January 2023 (10-K FY2025 Note 10);
(8) the speakers' own warning that retail is the field where one most easily thinks one understands and does not
**[M2014-052]**. *(This line asked for a pre-committed falsifier until 2026-10-05; that CONVENTION was removed under the
v5 scope directive.)*

## THE STANDING RULE
Owning a part-interest in Costco in cash, unlevered and sized within what the buyer can lose without being forced to sell,
puts the buyer at no risk of ruin from the buyer's own conduct: "We are never going to risk what we have and need for what
we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**;
the holder must be "prepared, when you buy a stock, to have it go down 50 percent — or more — and be comfortable with it"
**[M2020-022]**, which at a price of some 60 times fiscal 2025 owner cash is the live case, not the remote one. The
target's own debt and exposures are Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it, applied to the filings.** "can I understand it?" **[M1995-051]**, where understanding
  is "a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]** and "a
  reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**. The business is one thing done in 939 places: a paid membership that admits the holder to warehouses
  selling fewer than 4,000 stock-keeping units at a gross margin the company holds at about 11% of sales, with the profit
  coming from the fee and from volume (10-K FY2025 pp.3 to 5: "offering low prices on a limited selection of
  nationally-branded and private-label products in a wide range of categories will produce high sales volumes and rapid
  inventory turnover", enabling it "to operate profitably at significantly lower gross margins (net sales less merchandise
  costs) than most other retailers"). The three geographic segments run "generally the same" operating model (10-K FY2025
  p.24), so understanding one is understanding all.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (i) paid members, 47.6M (FY2016), 53.9M
  (FY2019), 65.8M (FY2022), 81.0M (FY2025), 82.9M at Q3 FY2026 (10-Ks FY2016 p.5, FY2019 p.5, FY2022 p.5, FY2025 p.5;
  10-Q p.22); (ii) the renewal rate, 88% worldwide and 90% U.S. and Canada in FY2016, 88% and 91% in FY2019, 90% and 93%
  in FY2022, 89.8% and 92.3% in FY2025 (same pages); (iii) the fee, $55 to June 2017, $60 to August 2024, $65 from
  2024-09-01 (10-Ks FY2016 p.5, FY2019 p.5, FY2025 p.26); (iv) comparable sales, which the company says is "the most
  important driver of our profitability" (10-K FY2025 p.23), 8% in FY2025 and 6.6% in FY2026 excluding gasoline and
  currency, with "increases of 5% in shopping frequency and approximately 1% in average ticket" in FY2025 (10-K FY2025
  p.26; 8-K 2026-09-24); (v) the warehouse count, 715 (FY2016) to 914 (FY2025) to 939 at 2026-09-24, with "up to 35 new
  warehouses, including five relocations, in 2026" planned (10-K FY2025 p.29; 8-K 2026-09-24); (vi) gross margin and
  SG&A as a share of sales, 11.35% and 10.40% in FY2016, 11.02% and 10.04% in FY2019, 10.48% and 8.88% in FY2022, 11.12%
  and 9.25% in FY2025, 11.09% and 9.15% in FY2026 (10-Ks and the 8-K; the FY2026 ratios computed from the release's net
  sales $297,247M, merchandise costs $264,279M and SG&A $27,190M). Each of these has moved slowly and in one direction for
  a decade, and the past statements do tell what the future ones will look like **[M2008-033]**: the members, the fee and
  the renewal rate together set membership fee revenue a year ahead (the fee is deferred and recognized ratably over the
  membership year; deferred membership fees $2,854M at FY2025 and $3,006M at FY2026 are next year's fee income already
  collected), and the warehouse count sets the floor under net sales. For Coca-Cola the speakers reduced the forecast to
  "unit case sales and shares outstanding" **[M1998-040]**; for Costco it reduces to paid members, renewals and
  warehouses, and shares outstanding have been flat at 438M to 443M for ten years.
- **Is the forecast about customers or about technology?** **[M2017-019]**, **[M2023-030]**. About customers: the
  question is whether 83M households will keep paying $65 to $130 a year to shop in a warehouse. The technology in the
  filings is e-commerce at 7% of net sales and digitally enabled sales at 10% (10-K FY2025 p.4), growing about 20% a
  year on the company's comparable measure (8-K 2026-09-24) from a small base; it is a channel the company runs, not a
  substitute arriving from outside, and the warehouse is the thing the member pays for. Change is the enemy of the
  forecast, "We view change as more of a threat into the investment process than an opportunity" **[M1999-063]**, and
  the record above shows little of it in the economics: the gross margin has sat between 10.5% and 11.4% of sales for
  every one of the ten years read.
- **The speakers' own warning, faced.** "it’s easy to sort of think you understand retail, and then subsequently find out
  you don’t" **[M2014-052]**; "In retailing, to coast is to fail" and "a retailer must stay smart, day after day"
  **[L1995-008]**. These weigh at Q2 (would it stand without the lord) rather than here, because the understanding
  question is whether the economics ten years out can be foreseen, and the same speaker names this company as the one a
  reader can understand: "You can understand Walmart. That doesn’t mean whether you decide whether the price — what the
  price should be — but you understand Walmart. You can understand Costco." **[M2002-092]**. That row is a speaker's view
  of this very name and is not the evidence; the evidence is the ten-year stability of the six variables above, which is
  what the row's test asks for. Doubt about the perimeter would put it outside, "if you have doubts about something being
  into your circle of competence, it isn’t" **[M2002-092]**; on the filings read, there is none about what this business
  is or what drives it. Where I could be off **[M2011-084]**: in the renewal rate and the fee, which together could be a
  point or two lower a decade out if the online cohort renews worse; that is a quantity, not a change of kind.
- **Routing.** No fast-moving technology puts the ten-year economics out of reach **[M1998-008]** by the routing fixed
  under Q1; no bank, no holding company; the three segments share one model, so the business-of-parts paragraph does not
  split it (the U.S. segment carries 66% of five-year operating income and decides in any case; see Q2).
- **VERDICT: IN.** The economics ten years out are foreseeable within a narrow band from six slowly moving variables the
  filings report every year **[M2000-037]**, **[M2012-065]**, **[M1998-044]**; the forecast is about what members do, not
  about technology **[M2017-019]**; and the company is named by the speakers as one a reader can understand
  **[M2002-092]**, a view the filings bear out. Filing fact: paid members 47.6M to 82.9M over ten years with the fee
  raised twice and the renewal rate within two points of where it started (10-Ks FY2016 to FY2025; 10-Q Q3 FY2026).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question starts from the attacker: "all moats are subject to attack in a capitalistic system" and "most moats aren’t
worth a damn" **[M1995-038]**. Costco is named in the rows as one of the two examples of the low-cost producer's castle,
"a formidable barrier such as a company's being the low-cost producer (GEICO, Costco)" **[L2007-004]**; that is a
speaker's view of this name, written in 2007, and it is weighed here only as far as the filings of 2016 to 2026 show the
same thing. Each castle test, with its filing fact:

1. **What keeps it standing, and how permanent is it?** **[M1995-038]**. The reason the member comes is price on a
   narrow list of goods, and the reason that reason lasts is a cost structure the member funds: the fee is the profit, so
   the goods can be sold near cost. Membership fees were $5,323M against operating income of $10,383M in FY2025 (51%),
   $2,646M against $3,672M in FY2016 (72%) and $5,907M against $11,685M in FY2026 (51%) (10-K FY2016 Item 8; 10-K FY2025
   p.37; 8-K 2026-09-24). The company states the mechanism as policy: "We do not focus in the short-term on maximizing
   prices charged, but instead seek to maintain what we believe is a perception among our members of our “pricing
   authority” – consistently providing the most competitive values" (10-K FY2025 p.23), which is the conduct the rows
   name as keeping a low-cost moat: "Our goal, however, is not to widen our profit margin but rather to enlarge the price
   advantage we offer customers" **[L1996-016]**. The gross margin held between 10.48% and 11.35% of sales for ten years
   while SG&A fell from 10.40% to 9.15% (Q1 table), so the whole of the decade's efficiency went to the member or to the
   operating margin, never to the gross margin.
2. **Would it stand without the lord?** **[L2007-006]**, **[M1996-037]**. The chief executive changed in January 2024
   (Jelinek to Vachris) and the chief financial officer in 2024 (Galanti to Millerchip, from Kroger) (10-K FY2025 p.8;
   proxy, Pay Versus Performance); operating income rose 14%, 12% and 13% in the three fiscal years across the change (10-K FY2025
   p.37; 8-K 2026-09-24). The retailer's warning is real, "a retailer must stay smart, day after day" and "In retailing,
   to coast is to fail" **[L1995-008]**, and the filings show the staying-smart is institutional rather than personal:
   "Most officers have over 25 years of service with the Company" (10-K FY2025 p.8); employee retention 94% for those
   with a year's service (p.6); a stated policy "not to seek to minimize their wages and benefits" (p.24). The speaker's
   row on the company's "extreme meritocracy" **[M2011-063]** is a director's view and is not relied on.
3. **The money test: could a well-funded attacker take it?** **[M2011-015]**, **[M1997-103]**. The attacker with the
   most money has been in the field for 43 years: Walmart opened its first Sam's Club in 1983 (WMT 10-K FY2026,
   `0000104169-26-000055`, p.6). Sam's Club U.S. net sales were $58.0B in Walmart's fiscal 2015 and $93.0B in fiscal
   2026, on 599 to 601 clubs throughout, with operating income of $915M (fiscal 2018), $1,642M (fiscal 2020), $2,259M
   (fiscal 2022) and $2,442M (fiscal 2026), 1.5% to 3.1% of sales (WMT 10-Ks filed 2017-03-31 `0000104169-17-000021`,
   2020-03-20 `0000104169-20-000011`, 2023-03-17 `0000104169-23-000020`, 2026-03-13). Over the same span Costco's U.S.
   warehouses went from 501 to 629 and U.S. segment revenue from $122,142M (FY2020) to $200,046M (FY2025) (10-K FY2022
   Note 11; 10-K FY2025 Note 11). The best-funded rival has held its club count flat for a decade while the target added
   128 clubs in the same country; "why are there no new entrants into the field? [...] Normally, if you’ve got a
   profitable business, you know, a dozen people want to go into it" **[M2000-077]**. BJ's, the third club, has 263
   clubs, 8 million members and $500M of fee income against Costco's 81 million paid members and $5.3B (BJ 10-K FY2025,
   `0001531152-26-000007`, pp.7 to 8). One competitor can be enough to ruin a business **[M2012-108]**; this one has had
   two for forty years.
4. **Pricing power, and the agony before a rise** **[M2005-020]**. The fee went from $55 to $60 in June 2017 and to $65
   on 2024-09-01 (10-Ks FY2016 p.5, FY2019 p.5, FY2025 p.26). In the year of the last rise membership fee revenue grew
   10% with "approximately 40%" of the growth from the fee increase, paid members rose from 76.2M to 81.0M, and the
   renewal rate moved from 92.3% and 89.8% at FY2025 to 92.2% and 89.7% at Q3 FY2026 (10-K FY2025 pp.5, 26; 10-Q
   p.27). "Anytime you can charge more for a product and maintain or increase market share against wellentrenched,
   well-known competitors, you have something very special in people’s minds" **[M2000-031]**. The other side of the
   test, pricing past the moat **[M2001-088]**, is what the 2022 margin shows the company declining to do: it absorbed
   cost inflation (gross margin down 65 basis points, "holding prices steady despite cost increases instead of passing
   the increases on to our members", 10-K FY2022 MD&A) and recovered the margin over the next three years.
5. **Unit volume and share of mind** **[M1999-054]**, **[M1997-099]**. Paid members 47.6M to 82.9M in ten years;
   shopping frequency up 5% in FY2025 with comparable sales ex gasoline and currency of 8% in FY2025 and 6.6% in FY2026
   (10-K FY2025 p.26; 8-K 2026-09-24); total cardholders 148.5M at Q3 FY2026 (10-Q p.22). Volume is up, not down, in
   every year read, including the inflation years. *Contrary fact, written down:* the worldwide renewal rate is 0.3 of a
   point below its FY2022 level and the U.S. and Canada rate 0.8 below (Q1), which the company attributes to online
   sign-ups; small, but the direction is down.
6. **The low-cost position** **[L1996-015]**, **[M2018-043]**. Costco's SG&A was 9.25% of net sales in FY2025 and 9.15%
   in FY2026; Sam's Club's operating expenses were 11.4% of its net sales in Walmart's fiscal 2026 and BJ's SG&A 15.0%
   ($3,154M on $20,958M) in BJ's fiscal 2025 (10-K FY2025 p.27; 8-K 2026-09-24; WMT 10-K FY2026 p.41; BJ 10-K FY2025,
   consolidated statement of operations). Costco carries this cost advantage while paying "better than the industry
   average for much of our workforce" (10-K FY2025 p.24), an average U.S. hourly rate of about $32 (p.6). The cost is
   measured against the competitor, not in absolute terms **[M2001-013]**, and on the competitors' own filings the
   target's operating cost per dollar of sales is two to six points below the two rivals in its own format. "if you can
   offer somebody a good product cheaper than the other guy then everybody practically has to buy it" **[M2024-013]**.
7. **The brand in the customer's mind** **[M2008-075]**, **[M2015-038]**. The brand here is the retailer's, and the rows
   say the retailer can hold it: "to the extent that people trust Costco or Walmart more than they — or as much as — they
   trust the brand, then the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]**. The filings give the fact without the number: Kirkland Signature products "generally carry higher
   margins than national brand products and represent a growing portion of our overall sales" (10-K FY2025 pp.7, 10);
   the company gives no private-label share, where BJ's reports 27% and PriceSmart 28.1% (BJ 10-K FY2025 p.7; PSMT 10-K
   FY2025, `0001041803-25-000060`, p.5). *Written down as missing.*
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. The customer here is choosing the low bid,
   and that is the point: the moat is being the low bid at a quality the member trusts, the low-cost producer's version
   of the test, "Low costs permit low prices, and low prices attract and retain good policyholders" **[L1996-015]**.
   Members paid the fee a year ahead ($3,006M deferred at FY2026) and 73.6% of net sales came from Executive members who
   pay double (10-K FY2025 p.5).
9. **Ask the competitors** **[M1999-130]**, **[M2017-022]**. From their own filings: BJ's names "Costco Wholesale
   Corporation and Sam’s Clubs" as its club competitors (BJ 10-K FY2025 p.10); Walmart's Sam's Club discussion names no
   rival and in fiscal 2026 began "combining the Sam's Club U.S. supply chain function with Walmart U.S. to streamline
   operations" (WMT 10-K FY2026 p.9); Kroger and Target each put Costco in the peer group of their performance graphs
   (KR 10-K FY2025 `0001104659-26-037723`; TGT 10-K FY2025 `0000027419-26-000016`). The filings cannot answer the
   silver-bullet question; the nearest the record gives is that the rival with the most money has stopped building clubs.
10. **Widening or narrowing?** **[M1999-108]**, **[L2005-010]**. Sales per warehouse for the 715 warehouses open in 2016
    or before rose from $159M in FY2016 to $287M in FY2025, and a warehouse opened in 2025 starts at $192M where one
    opened in 2018 started at $116M (10-K FY2025 p.22, the ten-year sales-per-warehouse table); Executive penetration of
    sales went from 71% (FY2022) to 73.6% (FY2025); comparable e-commerce sales grew 16%, 16% and 21% in the last three
    years (10-K FY2025 p.26; 8-K 2026-09-24). On the filings the moat widened over the decade.
11. **What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]**, **[L2006-008]**. Written
    down: (a) online grocery and general merchandise from Amazon and Walmart, whose filings show Walmart U.S. e-commerce
    at $99.6B and Sam's Club e-commerce at $15.0B (16% of its sales) in fiscal 2026 (WMT 10-K FY2026 Note 11) and Amazon
    running "online and physical stores" with Prime as "a membership program" (AMZN 10-K FY2025, `0001018724-26-000004`,
    pp.3, 4); against this, the target's own digital sales grow about 20% a year and its warehouse traffic grew 5% in
    FY2025, so the evidence to date is the channel added, not the warehouse replaced; (b) a labor-cost squeeze, since the
    company pays above the field by policy and 5% of employees are unionized (10-K FY2025 p.6); the SG&A ratio has
    nonetheless fallen for a decade; (c) tariffs, which the company says are "more likely to adversely impact rather than
    improve our results" (10-K FY2025 p.24); FY2026 instead carried IEEPA refunds, "partial reinvestment of those refunds
    in increased member values" (8-K 2026-09-24); (d) the slow slip in renewal rates (test 5); (e) the test the rows set,
    would the business be started today against its substitutes **[L2006-008]**: the two newest entrants in the format,
    BJ's at 263 clubs and PriceSmart at 56, are both still building clubs (BJ 10-K FY2025 p.8; PSMT 10-K FY2025 p.1).
- **The competitor row** (operating income over total assets, the filers' own XBRL, fiscal years as each files them;
  computed in `Test Runs/_research 2026-10-06 COST/peer_returns.py`):

| company (accession of latest 10-K) | OI / total assets, FY2016 | FY2020 | FY2025 | operating margin FY2025 | span |
|---|---|---|---|---|---|
| Costco (`0000909832-25-000101`) | 11.1% | 9.8% | 13.5% | 3.8% | 9.8% to 13.5% |
| Walmart, whole (`0000104169-26-000055`) | 11.4% | 8.9% | 10.5% | 4.2% | 8.4% to 12.1% |
| Sam's Club U.S. segment (same) | n/a (segment assets $17,186M in FY2026; OI $2,442M, 14.2%) | | | 2.6% | 1.5% to 3.1% margin |
| BJ's (`0001531152-26-000007`) | n/a (negative tangible equity, LBO goodwill $1,104M) | 11.9% | 10.9% | 3.8% | 6.7% to 12.0% |
| Target (`0000027419-26-000016`) | 13.0% | 12.8% | 8.6% | n/a | 7.2% to 16.6% |
| Kroger (`0001104659-26-037723`) | 9.4% | 5.7% | 3.8% | 1.3% | 3.8% to 10.5% |
| PriceSmart (`0001041803-25-000060`) | 12.5% | 7.4% | 10.2% | n/a | 7.4% to 14.8% |
| Amazon (`0001018724-26-000004`) | 5.0% | 7.1% | 9.8% | 11.2% | 2.6% to 11.2% (AWS inside; not comparable) |

- **The parts table** (five-year operating income FY2021 to FY2025, 10-K FY2022 Note 11 and 10-K FY2025 Note 11):

| part | share of five-year operating profit | castle | decides |
|---|---|---|---|
| United States | 66.8% ($28,225M of $42,283M) | the tests above, on U.S. facts | yes (more than half) |
| Canada | 17.5% ($7,384M) | same model, 110 warehouses, 94 owned | no |
| Other International | 15.8% ($6,674M) | same model, 175 warehouses in twelve countries, 119 owned | no |

  The company says the segments run "generally the same" model and that certain international operations have "less or
  no direct membership warehouse competition" (10-K FY2025 p.24). The file closes on the U.S. part, and the other parts
  are not lumped in by accident **[L2008-005]**; their castle is the same one on the same evidence.
- **The field's returns over the last full cycle**, judged in words. The field (the table) earns ordinary returns on
  total assets, around 4% to 12% for the grocers and general merchants and 1% to 4% margins for the two rival clubs; a
  castle that did not protect "excellent returns on invested capital" **[L2007-004]** would close OUT under section C's
  convention (a standing castle that protects only ordinary returns). Costco's returns are not
  ordinary: 11% to 13.5% on total assets with no net debt, and 30% to 43% pre-tax on tangible equity for ten years
  (peer_returns.py), because the capital is lent by the members and the vendors, "We often sell inventory before we are
  required to pay for it" (10-K FY2025 p.3), accounts payable $19,783M against inventory $18,116M at FY2025 (p.39). A
  thin margin "only works in terms of return on capital if you turn your equity extraordinarily fast" **[M2017-096]**,
  and the filings show that it does. The return has been stable across the inflation of 2021 to 2023 and the chief
  executive's change, so no change for the better is being credited early; the castle has stood the whole cycle.
- A castle shown open closes OUT **[M2011-015]**; a castle whose future cannot be judged closes TOO HARD **[M2000-019]**.
  Neither applies on the evidence: the best-funded attacker has stood still, the fee was raised with retention held, unit
  volume grows, and the cost gap to the rivals in the same format is on their own filings.
- **VERDICT: IN.** The castle is the low-cost position in an essential category, the moat the rows call "terribly
  important" **[M2018-043]** and "all-important" in a commodity-like product **[L2000-017]**, held by a company whose
  stated policy is to pass the cost advantage on rather than keep it **[L1996-016]**, and shown on ten years of its own
  and its rivals' filings to be widening **[M1999-108]**. The U.S. part decides and passes; the other two parts share
  its castle. The contrary facts (renewal slip, private-label share undisclosed, the online channel) are recorded and do
  not show the moat filling in **[M1995-038]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible capital, "forget about goodwill"
  **[M2011-060]**. Goodwill is $994M, all from one purchase in fiscal 2020 (10-K FY2025 Note 1), and intangibles are
  immaterial. The capital the business needs, at 2025-08-31: property and equipment $31,909M plus inventory $18,116M,
  receivables $3,203M and other current assets $1,777M, less the liabilities the members and vendors fund (accounts
  payable $19,783M, accrued salaries $5,205M, accrued member rewards $2,677M, deferred membership fees $2,854M, other
  current liabilities $6,589M), is about $17,900M (10-K FY2025 p.39). Operating income of $10,383M on that is about 58%
  pre-tax; on total assets less cash and investments ($61,815M) it is 16.8%; pre-tax income on tangible equity, 37% in
  FY2025 and between 30% and 43% in every year of the decade (peer_returns.py). None of the three flatterers the rows
  name applies, "a cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]**: the return has held
  through the cycle, two rivals share the format, and net cash exceeds debt. Nor is equity kept low by buybacks
  **[M1998-017]**: repurchases totalled $4,940M over FY2016 to FY2025 against $27,577M of dividends (XBRL cash-flow
  series; 10-K FY2025 p.41), and equity rose from $12,079M to $29,164M.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. The filing does not split maintenance
  from growth: "Our primary requirements for capital are acquiring land, buildings, and equipment for new and remodeled
  warehouses, information systems, and manufacturing and distribution facilities. In 2025, we spent $5,498 on capital
  expenditures, and it is our current intention to spend $6,000 to $6,500 during fiscal 2026" (10-K FY2025 p.29; actual
  FY2026 $6,435M, 8-K 2026-09-24). Depreciation and amortization was $2,426M in FY2025 and $2,674M in FY2026, so capital
  spending ran at 2.3 to 2.4 times depreciation. **The maintenance judgment, stated as a guess the filing allows:**
  depreciation is "not inappropriate in most companies to use as a proxy for required capital expenditures"
  **[M1998-127]** and it is the proxy here, with two reasons it may understate: remodels of existing warehouses are
  inside capex and not separately disclosed, and 725 of 914 warehouses sit on owned land ($10,323M of land, 10-K FY2025
  Note 1, p.44) which does not depreciate and is bought anew for each warehouse. The growth outlay is therefore about
  $3,100M in FY2025 (capex less D&A), for 24 net new warehouses, depots, a fourth-quarter remodel program and systems;
  the company gives no cost per warehouse. The spending is not compulsory to stand still **[M1998-128]**, **[M1997-016]**:
  the sales-per-warehouse table shows the existing fleet growing sales at about 7% a year with no new land.
- **What the added capital earns** **[M2001-019]**. From FY2020 to FY2025 net property and equipment rose from $21,807M
  to $31,909M (XBRL, `PropertyPlantAndEquipmentNet`) while net working capital funded by vendors was unchanged
  (inventory up $5,874M, payables up $5,611M), and operating income rose from $5,435M to $10,383M (10-K FY2022, Item 8;
  10-K FY2025 p.37). That is about $4,950M of added pre-tax operating income on about $10,100M of added capital, roughly
  49% pre-tax, though part of the income growth came from the existing warehouses' comparable sales rather than from the
  new capital; even halved, it is "a very satisfactory rate" **[M1998-081]**. The rows' second-best business is the one
  that "also gives you more and more money. It takes more money, but the rate at which you invest — reinvest — the money
  to get that growth is a very satisfactory rate" **[M1998-081]**; Costco is that business, not the first-best, since the
  land and buildings for each new warehouse must be bought, "decent returns on the incremental sums they invest"
  **[L2009-012]** being plainly met. Rising earnings alone would prove nothing **[M2023-081]**; here the return on the
  added capital is itself high.
- **The growth arithmetic and its caps** **[M1997-095]**, **[M1999-067]**. Revenue grew 8.9% a year FY2021 to FY2025,
  operating income 11.5%, owner cash on the capex basis 10.2% on its endpoints (Step 0; q7_arith.py). Carried ten years
  at 10.2% the owner cash reaches about $13.4B on sales of perhaps $650B at the sales rate shown, a sum Walmart already
  reports today ($706B, WMT 10-K FY2026 p.6), so the trace does not "bump into absurdities" **[M1999-067]** inside the
  ten-year horizon; carried forever it would, and Q7 carries it ten years then flat. Inflation: the business "retains
  its earning power in real dollars" largely without added capital **[M2005-049]** on the 2021 to 2023 evidence, where
  the margin dipped and recovered with no change in the capital intensity.
- **WEIGHS FOR:** high returns on the tangible capital the business needs, held for a decade without leverage or buybacks
  flattering them **[M1995-047]**, **[L1994-009]**, and a satisfactory return on the sums added to grow **[M1998-081]**,
  **[L2009-012]**; the one qualification is that growth needs land and buildings at about 2.3 times depreciation, which
  Q7 deducts in full. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten years of them, before the income account** **[M2025-032]** (USD millions, fiscal
  year-ends; `tools/run.py` table from first-filed XBRL, read against the filed statements of the 10-Ks for fiscal 2016,
  2019, 2022 and 2025 and the unaudited FY2026 balance sheet in the 8-K of 2026-09-24):

| FY end | assets | equity | goodwill | cash + ST inv. | receivables | inventory | payables | debt (LT + current) | retained earnings | shares (M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 33,163 | 12,079 | 0 | 4,729 | 1,252 | 8,969 | 7,612 | 5,161 | 7,686 | 438 |
| 2017 | 36,347 | 10,778 | 0 | 5,779 | 1,432 | 9,834 | 9,608 | 6,659 | 5,988 | 437 |
| 2018 | 40,830 | 12,799 | 0 | 7,259 | 1,669 | 11,040 | 11,237 | 6,577 | 7,887 | 438 |
| 2019 | 45,400 | 15,243 | 53 | 9,444 | 1,535 | 11,395 | 11,679 | 6,823 | 10,258 | 440 |
| 2020 | 55,556 | 18,284 | 988 | 13,305 | 1,550 | 12,242 | 14,172 | 7,609 | 12,879 | 441 |
| 2021 | 59,268 | 17,564 | 996 | 12,175 | 1,803 | 14,215 | 16,278 | 7,491 | 11,666 | 442 |
| 2022 | 64,166 | 20,642 | 993 | 11,049 | 2,241 | 17,907 | 17,848 | 6,557 | 15,585 | 443 |
| 2023 | 68,994 | 25,058 | 994 | 15,234 | 2,285 | 16,651 | 17,483 | 6,458 | 19,521 | 443 |
| 2024 | 69,831 | 23,622 | 994 | 11,144 | 2,721 | 18,647 | 19,421 | 5,897 | 17,619 | 443 |
| 2025 | 77,099 | 29,164 | 994 | 15,284 | 3,203 | 18,116 | 19,783 | 5,788 | 22,650 | 443 |
| 2026 (8-K) | 89,045 | 35,803 | n/s | 21,301 | 3,959 | 19,324 | 22,591 | 6,162 | 28,591 | 443 |

  What moved and why. Equity fell in 2017, 2021 and 2024, each the year of a special dividend ($7, $10 and $15 a share;
  10-K FY2025 Note 6 for 2024's $6,655M) and rose every other year; retained earnings went from $7,686M to $28,591M while
  $30,035M of dividends and $5,788M of repurchases were paid out over the eleven years (XBRL cash-flow series; 8-K
  2026-09-24), so the earnings are real enough to have been paid away and still to have tripled the equity. Goodwill
  appeared once, $988M in fiscal 2020, and has not moved: no acquisition habit. Cash and short-term investments exceed
  debt in every year from 2019 and by $15,139M at FY2026; debt itself is flat at $5B to $7B against sales that rose from
  $116B to $297B, so leverage fell by two-thirds. Receivables against total revenue drifted from 1.05% (2016) to 1.16%
  (2025) and 1.31% (2026); they are vendor rebates, card incentives and pharmacy receivables (Note 1, p.43), and the
  drift is small but is written down. Inventory against net sales fell from 7.7% (2016) to 6.7% (2025) and 6.5% (2026),
  with one bulge to 8.0% in 2022 that unwound the next year, so inventories do not "look out of line, you know, with
  sales" **[M1995-064]**; payables rose faster than inventory and now exceed it (109% at FY2025, 85% in 2016), which is
  the vendor-funded model in the figures. Deferred membership fees ($2,854M to $3,006M) and accrued member rewards
  ($2,677M to $3,037M) are the members' money held ahead of service, a liability that grows with the business and costs
  nothing. What the figures "don’t say and what they can’t say" **[M2025-032]**: the balance sheet carries land at cost
  ($10,323M), bought over forty years, and the lease notes add $2,668M of operating and $1,479M of finance lease
  liabilities with 20 and 25 year remaining terms (Note 5), so the fixed-asset base is understated against replacement and
  the lease obligations sit mostly off the face. The share count is flat at 437M to 443M for ten years: repurchases
  (1.3M, 1.0M and 0.9M shares in FY2023 to FY2025) roughly match RSU releases (1.5M, 1.3M and 1.1M; statement of equity,
  p.40), a fact carried to Q6.
- **The real costs.** Depreciation ($2,426M FY2025) is "almost always" a true cost **[L2015-004]** and is taken in full;
  buildings depreciate over 5 to 50 years and equipment over 3 to 20 (Note 1, p.44). Stock pay is RSUs only, $860M
  expensed in SG&A with no options outstanding (Note 7), so no earnings here leave out "all forms of compensation"
  **[L2021-003]**; the dilution is computed, not waved off **[M2014-004]**: 818,000 RSUs in the diluted count on 444M
  shares (Note 9). Restructurings: none in the three years. The one large special item, $391M of charter-shipping lease
  impairments in fiscal 2023, was charged to merchandise costs and left in GAAP earnings with no "adjusted" figure beside
  it (Note 1, p.45), which is the opposite of "wave away very real costs by highlighting "adjusted per-share earnings""
  **[L2016-006]**. Pensions: none, "The Company does not maintain a pension plan or post-retirement medical plan for any
  employee" (proxy p.15); defined-contribution cost $1,061M expensed (Note 1, p.48). Taxes at 25.1% effective, cash taxes
  paid $2,917M against a $2,719M provision (p.41), with the foreign tax credit carryforwards nearly fully reserved
  ($390M against a $554M valuation allowance, Note 8), so no shelter runs out inside ten years. U.S. inventories are on
  LIFO with a $142M charge in 2025 (Note 1, p.43), a conservative choice. Self-insurance liabilities of $1,878M are
  "not discounted" (p.45).
- **EBITDA in the filer's own mouth:** no instance in the 10-K, the 10-Q, the proxy or the fiscal 2026 release (a text
  search of each for "EBITDA"); the release reports GAAP net income and names the one unusual item, "a non-recurring
  benefit of $0.15 per diluted share from IEEPA tariff refunds received in the quarter, less partial reinvestment of
  those refunds in increased member values" (8-K 2026-09-24), which is the clear speech the rows ask for, a management
  that does "explain to you in clear terms what’s going on" **[M1994-018]**. The two supplemental measures are
  comparable sales excluding gasoline and currency and "net sales adjusted for changes in foreign currencies", both
  labelled "not a substitute for net sales presented in accordance with U.S. GAAP" (10-K FY2025 p.23; proxy Appendix A,
  p.35); the word "guidance" occurs in the 10-K and 10-Q only as "accounting guidance";
  neither is an earnings figure.
- **The make-the-numbers habit, weighed here and carried to Q5.** The filings carry no earnings guidance (no instance
  found in the 10-K, 10-Q, proxy or the four 8-Ks read). The risk factor "We believe that the price of our stock
  currently reflects high market expectations for our future operating results" (10-K FY2025 p.16) is a warning, not a
  number to hit. What is recorded against: the one-year hurdles for executive RSUs, a 3% rise in net sales or a 2% rise
  in pre-tax income, were "exceeded" in a year of 8% and 11% growth, and the cash-bonus targets came in at "101.3% of
  the pre-tax profit target" and "100.3% of the sales target" (proxy pp.15 to 16); targets met every year, as
  **[L2002-041]** warns, though these are internal plan targets, not declared public numbers. Weighs against lightly
  here; judged at Q5 and Q6.
- **What the accounts say of management's character** **[M1995-064]**: conservative inventory accounting, every cost
  expensed, no adjusted earnings, no acquisitions to hide behind, and the equity statement reconciling exactly to the
  cash paid out. Nothing confuses **[M1995-063]** and nothing raises suspicion **[M1995-065]**.
- **VERDICT on the accounts: IN; WEIGHS FOR.** The recast earnings fed to Q7, "regular pretax earnings" **[M2012-034]**
  after "interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**: net income $8,099M
  (FY2025) and $9,226M (FY2026, unaudited); owner cash after all capital spending $6,830M and $8,375M, and after
  depreciation only $10,049M and $12,227M (Step 0 table), the difference being the growth outlay of Q3. One caution for
  Q7: operating cash flow includes interest income on the cash pile ($469M in FY2025, 10-K p.28), so the owner cash
  carries about $350M after tax that belongs to the net cash and not to the warehouses; it is small against the total and
  is noted rather than removed.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet, "We read annual reports. We read about competitors. We read
about the industries they’re in" **[M2007-081]**; what follows is from the 10-K, the proxy and the 10-Q.
- **The two yardsticks** **[M1994-008]**. How well they run it: the record against the hand dealt is Q2 and Q3, a decade
  of widening the cost gap, raising the fee twice without losing the member, and growing operating income 11.5% a year
  with no acquisitions and no leverage. How they treat the owners: dividends raised every year and three special
  dividends in the decade; no stock issued; no guidance; a 10-K that tells the owner the stock "currently reflects high
  market expectations" (p.16) and names the renewal slip and its cause (p.26), the inverse of the report that dances
  **[M1995-111]**. The two yardsticks run the same way, as the rows say they tend to **[M1994-009]**.
- **The proxy, read for how they treat themselves against the owners** **[M1994-009]**. Chief executive total pay
  $13,932,597 for fiscal 2025, of which $12,036,800 is performance RSUs, salary $1,183,270 and cash bonus $600,000
  (proxy p.19); the other named officers $5.2M to $7.5M, two of them carrying sign-on bonuses ($4,008,615 for the CFO in
  2024 and $3M for the CIDO in 2025) for coming from Kroger and Mondelez (pp.19 to 20). No options; RSUs vest over five
  years with long-service acceleration, and the chief executive's own award "is not subject to accelerated vesting prior
  to termination for long service" (p.15). No compensation consultant: "The Committee has authority under its charter to
  engage compensation consultants but did not use any" (p.13), the practice the rows prefer **[M2004-016]**. No
  change-in-control agreements; severance for the chief executive 1.5 times salary and target bonus, about $2.7M (p.23).
  Ownership requirements seven times salary for the chief executive and $1M for directors, all in compliance (pp.10, 17).
  Pay ratio 283 to 1, 210 to 1 against full-time employees (p.25). Beneficial holdings: chief executive 52,258 shares,
  chairman 56,689, all 23 directors and officers 460,270 shares, about $430M at the price (p.12), small against $415B
  but large against the holders' salaries. Related persons: one officer's three brothers and another's son employed at
  $113,000 to $251,000 (p.28), disclosed. Say-on-pay passed with 251.4M for and 34.4M against (8-K 2026-01-21). Nothing
  here is the manager treating himself ahead of the owners; the sums are modest for a $415B company and the structure is
  plain enough to read in a dozen pages, not a hundred **[M2009-087]** (the proxy is 35 pages).
- **The tells of dishonesty, checked against the filings.** Too good to be true **[M2002-028]**: the opposite; the risk
  factors and MD&A undersell. Reports that dance **[M1995-111]**: none found; the 2023 charter-lease impairment and the
  2026 tariff refund were each named in one sentence with the amount. Fixed on the stock price **[M2004-067]**,
  **[M2014-010]**: no guidance, no adjusted figure, no repurchase program sized to prop the stock (buybacks $0.7B to $0.9B
  a year against $1.3B to $9.0B of dividends). Taking credit **[M1998-167]**: the 10-K attributes the warehouses'
  productivity "largely to the commitment and efficiency of our employees" (p.6). Owners as patsies **[L2001-002]**: no
  insider selling into a promotion is suggested by the filings; the share count is flat and the owners have been paid
  $30B in cash. What they talk about **[M2007-090]**: the MD&A talks about members, renewal, frequency and the fee.
- **Integrity facts in the filings, written down.** (a) A Civil Investigative Demand of January 2023 from the U.S.
  Attorney, Western District of Washington, in "a False Claims Act investigation concerning whether the Company presented
  or caused to be presented to the federal government for payment false claims relating to prescription medications"
  (10-K FY2025 Note 10, p.61), open for nearly three years with no charge, no accrual and no further disclosure in the
  10-Q; (b) the opioid multidistrict litigation, in which most claims against the company have been "resolved or
  dismissed" (10-Q Note 8); (c) five pixel-tracker privacy class actions and two Washington Attorney General demands
  (Note 10, p.60; Birdwell dismissed with prejudice March 2026, 10-Q); (d) California wage-and-hour and PAGA actions;
  (e) a PFAS labelling class action on Kirkland Signature wipes; (f) two class actions on Kirkland Signature tequila
  labelled "100% de Agave" (10-Q Note 8); (g) four class actions of March 2026 seeking refunds of IEEPA tariffs passed on
  in prices (10-Q Note 8); (h) an EPA FIFRA matter settled "for an immaterial amount" (Note 10, p.61). The company
  believes none "either alone or in the aggregate, will have a material adverse effect" (p.61). None is an accounting
  matter and none alleges conduct by the officers; (a) is the one with a government integrity dimension and it is
  recorded here as an open fact the analyst cannot judge from the filing, not as a doubt about the people. Applied on
  doubt alone **[M2013-088]**: the filings read raise none about the honesty of the accounts or the officers.
- **Love of the business, and the same after being paid** **[M2000-098]**. The chief executive, 60, has been an
  executive officer since 2016 and held regional, real-estate and merchandising posts from 2010 (10-K p.8), and
  "Most officers have over 25 years of service" (p.8): people who stayed through many pay cheques. The two outside
  hires (finance and digital) are the exception and are recent.
- **Ability, what it shows in.** A long record, not a promise **[M1996-038]**, **[M2005-039]**: the chief executive was
  promoted from within and the results continued (Q2 test 2). Facing reality **[M2000-153]**: the 10-K states the slip in
  renewal, the 2022 margin, the tariff exposure and the stock's expectations without softening. Focus **[L1996-033]**:
  one format, one acquisition in a decade, growth by opening warehouses. Knowing the limits **[L2014-027]**: the
  company buys land and builds at 24 to 30 warehouses a year rather than faster, and has gone from one warehouse in
  China in 2019 to seven in 2025 (10-K FY2019 Note 1; 10-K FY2025 p.3), a pace that tests a market before it commits. The habit carried from Q4: the internal RSU and bonus targets are set low (a 3%
  sales rise or 2% pre-tax rise earns the whole RSU grant) and were met at 101.3% and 100.3%; read with the rest of the
  record (no public guidance, GAAP-only reporting, cash paid out) this is a bar set too low rather than numbers made,
  "a lousy manager will always suggest an arrangement like that" **[M2004-097]** weighs at Q6 Part B; it is not an
  integrity doubt. Succession: "Who besides you" **[M2014-059]** was answered in 2024 from inside, and the board "has
  oversight responsibility for executive-officer succession planning" (proxy p.10).
- **VERDICT on integrity: IN** (no tell found; no doubt raised by the accounts, the proxy or the record **[M2015-047]**,
  **[M2013-088]**). **Ability WEIGHS FOR**: a management that has kept a retailer smart "day after day" **[L1995-008]**
  for a decade across a succession, read from a candid report and a plain proxy **[M1994-009]**, **[M2007-083]**; the
  one mark against, a low performance bar, is carried to Q6.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Over FY2021 to FY2025 the company earned $32,609M, paid
  $19,721M in dividends and $3,214M in repurchases, and so kept about $9,674M (XBRL cash-flow series; 10-K FY2025 p.41).
  Market value: the proxy's own five-year figure shows $100 invested at the end of fiscal 2020 worth $293.59 at the end
  of fiscal 2025 against $173.48 for the S&P Retail Select Index (proxy p.25), a rise of about $265B in market value for
  $9.7B retained. Intrinsic value, since the market leg alone misleads **[R2009-002]**: operating income rose $4,948M
  pre-tax over the span on about $10,100M of added capital (Q3), so each dollar kept added well over a dollar of earning
  power at any sane multiple. Forward: "Can you keep using all of the capital you generate, effectively, for a very long
  time?" **[M2010-097]**: no, and the company does not pretend to; it keeps what 24 to 35 warehouses a year can use and
  returns the rest. Passes on both legs.
- **Dividends and the use of cash.** The ordinary dividend was raised from $1.16 to $1.30 (April 2025) and to $1.47
  (April 2026) a quarter (10-K Note 6; 10-Q Note 5); special dividends of $7 (2017), $10 (fiscal 2021) and $15 (fiscal
  2024) a share returned $3,904M, $5,748M and $9,041M in those years (XBRL `PaymentsOfDividends`; 10-K FY2025 Note 6).
  This is the rows' rule in action: "a company that expects to regularly earn more than it can profitably employ in its
  business, should be paying out dividends" **[M2004-089]**, and the policy, a rising quarterly dividend plus a special
  when cash builds, has been "clear, consistent and rational" **[L2012-015]** for a decade. Cash is a residual
  **[M1995-057]**: $21,301M of cash and investments at FY2026 against $6,162M of debt and $6.4B of annual capital
  spending, held in "direct U.S. government and government agency obligations" and money funds (10-K p.31), not reached
  for yield and not spent on "something marginal simply because we are long on cash" **[L1993-007]**.
- **Buybacks.** The program is a $4,000M authorization of January 2023 expiring January 2027 with $1,359M remaining at
  2026-05-10 (10-Q Note 5); it names no price **[L2016-002]**. Shares were bought at average prices of $504.68 (FY2023),
  $695.29 (FY2024), $957.66 (FY2025) and $945.46 (first 36 weeks of FY2026) (10-K Note 6; 10-Q Note 5). **The test the
  convention sets, run at Q7 and recorded back here:** the bottom of the Q7 range is $203 a share on the operating cash
  and $224 with net cash (Q7); every purchase was made at two to four times the bottom of the range, so the programme
  with no stated price weighs against on the prices actually paid **[L2016-002]**, **[L1999-023]**. The pattern is the
  one the rows rule out by name: repurchases of 1.3M, 1.0M and 0.9M shares against RSU releases of 1.5M, 1.3M and 1.1M
  (statement of equity, 10-K p.40), a share count flat for ten years, which is buying "to cover options" rather than
  bargain-seeking **[M2014-008]**, and "It’s got nothing to do with preventing dilution [...] it has to be related to
  valuation" **[M2016-049]**. The sums are small ($0.7B to $0.9B a year against $1.3B to $9.0B of dividends) and the
  needs of the business come first (capex is funded from operations with cash left over, **[L2016-003]**), so the harm
  is a few hundred million dollars a year, not a policy of propping; but it is "no favor at all" **[M2014-008]**.
- **Issuance and deals.** One acquisition in the decade, for about $1,000M in cash in fiscal 2020 (goodwill $988M, 10-K
  Note 1); no shares issued for it; no stock deals, so the one STOP in Part A **[L2009-019]** does not arise, and no
  serial issuance **[L2014-015]**. Value given against value got **[M1995-001]** on that purchase cannot be judged from
  the filings, which do not report it separately; it is 1% of a year's cash flow.
- **WEIGHS FOR on retention and dividends, AGAINST on the buyback:** the earnings kept have earned far more than a
  dollar per dollar **[R1995-009]** and the surplus is paid out as the rows prescribe **[M2004-089]**, while the small
  repurchase programme buys at prices far above the range to offset stock pay **[M2014-008]**, **[L2016-002]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the RSU hurdle and the cash bonus are set on net sales and
  pre-tax income adjusted for currency, which the officers control, not on the stock price, "merit badges, not lottery
  tickets" **[L1997-022]**; the $100,000 environmental and social component is all-or-nothing on quantitative metrics
  (proxy p.16). Against: the bar. A 3% sales or 2% pre-tax rise in a business that has grown 8% to 11% a year is a bar a
  chimpanzee clears, "it’s silly to have something that starts at 10 percent or 15 percent" when the business earns
  35 **[M2004-097]**; the full grant was earned every year shown. No step-up for retained earnings is needed since there
  are no options **[M1997-043]**; RSUs carry no dividends until delivered (10-K Note 1), so no royalty on money kept
  from the owners. The plan is designed by the committee without a consultant and the awards to the other officers "were
  based on the recommendations of Mr. Vachris" (p.16), the beneficiary's hand near the switch **[M1998-066]** but with
  the chief executive's own award set by the committee alone. Upside only? Severance is 1.5 times salary and target
  bonus and there is no change-in-control agreement (p.23), so the downside is the owners' downside.
- **The board** **[M2007-120]**. Every director but the chief executive is independent under the Nasdaq standard (eight
  of the nine serving, and the new nominee); a non-executive chairman, a director since 1988
  and chairman since 2017 (proxy pp.4, 7, 9), so the chief executive does not also chair **[L2014-026]**; four meetings
  a year with full attendance (p.11). Director pay $37,000 cash plus $270,000 in RSUs (p.10), fees that are not "a very
  important part of a director’s wellbeing" **[M2009-086]** for the former chief executives and investors on this board;
  a $1M ownership requirement, met (p.10); directors' holdings "Includes RSUs outstanding" (p.12), so how much was bought
  "with their savings" **[L2019-008]** the proxy does not say. Succession: done from inside in 2024 and overseen by the
  board (p.10) **[L2011-001]**. A shareholder proposal for a greenwashing audit drew 4.1M votes for and 279.7M against
  (8-K 2026-01-21).
- **The owners as partners.** No guidance, no quarterly "number" to hit **[L2018-003]**, **[M2016-002]**; the same
  information to all in the 10-K and the monthly sales releases (8-K 2026-07-08); a dividend policy that returns what
  the business cannot use; a 10-K written in the company's own words with the bad news in it, "tell us the bad news
  immediately" **[M1998-039]**. The owners' money: matched charitable contributions for employees are capped (proxy
  p.15); no political giving is disclosed.
- **WEIGHS FOR**, with one mark against: pay is tied to controllable results and designed without consultants, the
  board is independent with a separate chairman and owns shares, and the owners are told the truth and paid the surplus
  **[M2003-019]**, **[M2004-016]**, **[L2014-026]**, **[L2018-003]**; against, a performance bar set where the business
  cannot miss it **[M2004-097]**, which is "generally of minor importance compared to the sin of having somebody that’s
  mediocre running a huge company" **[M2007-006]**, and that sin is not present.

## Q7 — WHAT IS IT WORTH? STOP.
- **How much cash, how sure, how soon, at the long government rate** **[L2000-021]**, **[M2009-004]**. The cash is Q4's
  recast owner cash, "whatever net cash is left every year" **[M1998-080]** after all capital spending, averaged over
  FY2021 to FY2025 so that no single year sets the base: **$5,085M** (Step 0 table; capex basis), with the
  depreciation-basis variant of $7,566M beside it. How sure: as sure as the rows describe for the businesses they say
  need little margin, "we don’t think we need a huge margin of safety because we don’t think we’re going to be wrong
  about our assumptions in any material way" **[M2007-022]**; the stream has grown in every year but one of the six read
  and is funded by members a year ahead. How soon: now, and growing. The rate: the 30-year Treasury, 5.66% at
  2026-10-05, "use the government bond rate" **[M1996-025]**, with no risk premium stacked in **[M1996-024]**,
  **[M1998-151]**; certainty is handled in the cash estimate and the discount demanded at purchase **[M1997-126]**, not
  in the rate.
- **The range (the CONVENTION construction).** Growth shown on the aggregate owner cash over the window, endpoints
  $4,638M (FY2021) to $6,830M (FY2025): 10.2% a year. The endpoint check **[L2005-003]**: neither endpoint is the
  aberrant year (the trough is FY2022 at $2,601M, inside the window, and the FY2021 figure sits mid-range), so the rate
  is not a base-year artifact; it is below the 11.5% of operating income and above the 8.9% of revenue over the same
  years, and Q3 found no absurdity inside ten years. Carried ten years at 10.2% and then flat, at 5.66%:
  - no growth: $89,837M, **$203 a share** on the operating cash; $224 with net cash of $9,479M (cash $14,161M and
    investments $1,123M less debt $5,805M at 2025-08-31);
  - shown growth: $200,742M, **$453 a share**; $474 with net cash;
  - top over bottom 2.23, narrower than the three-to-one that would make it TOO HARD;
  - depreciation-basis variant (owner cash after depreciation only, the earning power if the company stopped growing;
    shown growth on that series 11.5%): $301 to $746 a share, $323 to $767 with net cash;
  - growth capped at the sovereign, the stricter reading of the Q3 cap (my reading, stated as such): $317 a share.
  All in `Test Runs/_research 2026-10-06 COST/q7_arith.py` and its output file.
- **The whole-cycle variant** (the brief asks for one where the window holds a boom or a trough; FY2021 was the
  pandemic year and FY2022 the inventory trough). Window FY2022 to FY2026, the last year from the unaudited release:
  average $5,832M; but the endpoints run from the trough ($2,601M) to the high ($8,375M) and give 34% a year, "a base
  year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**, so the
  variant is carried at the sovereign-capped rate: $232 to $364 a share on the operating cash, $266 to $398 with the
  FY2026 net cash of $15,139M. It sits inside the range of record and does not move the verdict.
- **Value range: $203 to $453 a share** (operating cash; $224 to $474 with net cash) **against $935.68.** The price is
  twice the top of the range of record, 1.2 times the top of the most generous variant (depreciation basis with net
  cash, $767), and 4.2 times its bottom. The expected return at the price, the stream against today's market value less
  net cash, is 1.25% a year on the no-growth stream and 3.0% on the shown-growth stream (q7_arith.py), both below the
  5.66% bond and far below the floor. For the five-year-average owner cash to return the floor at today's price it would
  have to grow 29.7% a year for ten years (q7_arith.py), a rate the business has never shown in any year of the window
  and that would carry sales past a trillion dollars.
- **The floor (CONVENTION): about ten percent pre-tax**, "we don’t want to buy equities where our real expectancy is
  below 10 percent" **[M2003-149]**, applied to owner cash after the company's own income tax with no conversion
  (section E): the effective rate was 25.1% against a 21% federal statutory rate (10-K Note 8), and no carryforward or
  credit shelters the figure (the foreign tax credit carryforwards are reserved), so nothing is priced separately. Below
  the floor "there’s just a point at which we drop out of the game" **[M2003-149]**; at 1% to 3% this name is three
  points below the bond, not ten.
- **Closes: OUT.** A price above the top of the range closes OUT through the floor convention, the expected return at
  the price being below the minimum; it is the same close as a price inside the range, and it needs no pencil in the
  other direction: "If you have to carry it out to three decimal places, it’s not a good idea" **[M2008-068]**, and
  here the first decimal says the price is double the value. The rows' own warnings both apply and point the same way:
  the costliest errors were "being reluctant to pay up a little for a business I knew was really outstanding"
  **[M1997-083]**, and "you can pay too much for a wonderful business. [...] the business does not know how much you paid
  for it" **[M2019-013]**. Sixty times owner cash and forty-five times net income is not "a little". The speaker's own
  remark that this stock "at about 12 or 13 times earnings" was "a ridiculously low value" **[M2018-050]** was made of a
  price a quarter of today's multiple and is cited only to mark the distance.
- **Fair price (a reporting figure, never a verdict; Part VII):** the price at which the midpoint of the range earns
  the floor, computed as the midpoint of the two end streams discounted at 10%: **$173 a share on the operating cash
  (equity plus net debt basis, here net cash) and $195 a share on the equity** (net cash $9,479M at FY2025 added; with
  the FY2026 net cash of $15,139M the equity figure is $207). Tax treatment: owner cash after the company's own income
  tax at its 25.1% effective rate, no conversion to the holder's tax. On the depreciation basis the same construction
  gives $274 and $296. No cheap price is reported.
- **VERDICT: OUT** at Q7. The business is understood, the castle stands and the accounts and people pass; the price
  does not clear the floor by a wide margin **[M2003-149]**, **[M2007-095]**, and "What you can’t do is turn any
  investment into a good deal by paying little" has its mirror here: nor can a good business be turned into a good
  investment by paying anything **[M2019-015]**, **[M2019-013]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED. The file closed at Q7. The one fact the bond filter would have used is recorded under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are recorded under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED as a question; one fact is recorded under AFTER THE STOP.

---
## THE BOX
**OUT**, decided at **Q7**: value range $203 to $453 a share on the operating cash ($224 to $474 with net cash) against a
price of $935.68; the expected return at the price is 1% to 3% against a 5.66% long bond and a floor of about ten
percent. Q1 to Q6 all passed (Q1 IN, Q2 IN, Q3 FOR, Q4 IN and FOR, Q5 IN and FOR, Q6 FOR with the buyback against). Not
TOO HARD: the range is narrower than three to one and the business is as knowable as any the rows describe. Integrity
facts recorded, not judged: the open False Claims Act investigation of January 2023 (Q5), recorded there as an open
fact and found to raise no doubt on the filings read; it is flagged here so that a later run reads it first.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(A STOP closed the file at Q7.)* Written down, not weighed; no verdict; the box unchanged (operator rule 2)
**[M1997-127]**.
- **Q8.** The 30-year Treasury pays 5.66% (US Treasury, 2026-10-05). The owner-cash yield at the price is 1.6% on
  FY2025 and 2.0% on FY2026 (Step 0; 8-K 2026-09-24).
- **Q9.** Debt: Senior Notes of $1,000M at 3.000% due May 2027, $1,250M at 1.375% due June 2027, $1,750M at 1.600% due
  April 2030, $1,000M at 1.750% due April 2032, plus $684M of the Japan subsidiary's Guaranteed Senior Notes; $2,250M
  matures in fiscal 2027 and is shown as current at FY2026 (10-K FY2025 Note 4, p.52; 10-Q Note 4; 8-K 2026-09-24).
  Cash and short-term investments $21,301M at 2026-08-30 against total debt $6,162M; interest expense $145M against
  pre-tax income $12,251M in FY2026 (8-K 2026-09-24), 84 times covered on "pre-tax earnings/interest" terms. Bank
  credit facilities $1,220M, "immaterial" drawn; letters of credit $224M (10-K p.30). Leases: operating $2,668M and
  finance $1,479M present value, 20 and 25 year remaining terms, $1,094M more signed and not commenced (Note 5). No
  collateral calls: the forward foreign-exchange contracts' credit-risk features "were immaterial" (Note 1, p.47);
  notional $1,184M. Self-insurance liabilities $1,878M, not discounted, with a captive insurer in a reinsurance program
  under which the company "retains its primary obligation to the participants for prior activity" if it leaves (Note 1,
  pp.45 to 46). Concentration: the U.S. and Canada are 86% of net sales and 84% of operating income, and California 26%
  of U.S. net sales (10-K p.9). The one-event exposures named by the filing are the self-insured catastrophe property
  risk ("we still bear a significant portion of the risk", p.13) and the Washington and California headquarters and
  systems (p.15). Litigation and investigations: Q5's list. Of the "little or no debt" criterion **[R1997-001]**, the
  filing shows net cash of $15,139M.
- **Q10.** No position is taken. The owner's sizing question does not arise on a name closed OUT at Q7.
- **Q12.** Foods and sundries includes "liquor, and tobacco" (10-K p.4) and gasoline is 10% of net sales (p.4). For a
  marketable stake the rows own what they would not run **[M2005-096]**; recorded, not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied at 16:54 on 2026-10-06, before `tools/run.py`,
      `cover_shares.py`, `sources.py` or any EDGAR request); written question by question; committed after each
      question with a pathspec of this file and the research folder only (commits 7b33c420, d539311d, 20f8e8be,
      d104ae75, and the Q7 commit that follows).
- [x] Dispatched to an analyst: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present
      before the first fetch, written by the dispatching session; the fold into the register is the dispatcher's
      (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Two file names about this
      company were seen in a directory listing and are declared under CONTAMINATION at the head of this file; neither was
      opened or used. The POSITION NOTE is left for the dispatcher for the same reason.
- [x] Every v5 id resolves: 375 candidate ids were checked against `principle_ledger_v5.csv` before writing (none
      missing) and `Test Runs/_research 2026-10-06 COST/check_citations.py` re-checks every id and every quoted fragment
      in this file against its row. Every filing fact carries its accession at Step 0 and its page or note in the text.
- [x] The order was kept; Q1 to Q6 passed in order; the first STOP that failed, Q7, closed the run; nothing after it is
      a clearance.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending including finance-lease principal),
      never a net-income proxy; the sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations line and each question); the facts for
      later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited: this is a live run anchored today, so none applies.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 "yield", "growth the price assumes" and
      "points over the sovereign" lines were ignored and are declared under CONTAMINATION.
- [x] `python tools/check_framework.py` PASS before each commit.
- **Honest marks against this run.** (1) The fiscal 2026 10-K is not filed; the FY2026 figures are from an unaudited
  release and the five-year window of record is FY2021 to FY2025 for that reason. (2) The private-label share, the cost
  of a new warehouse and the maintenance share of capital spending are not in the filings and are stated as absences or
  guesses. (3) Page numbers were verified mechanically against the stripped filing text and may be off by one where a
  paragraph breaks across a page. (4) The competitor row uses operating income over total assets because the rivals'
  tangible equity is negative (BJ's) or carries unrelated businesses (Amazon, Walmart); a cleaner common metric is not
  available from the filings. (5) The speakers' praise of this company by name was excluded from the evidence and used
  only to mark distance; the analyst nonetheless read those rows before the filings, and cannot prove they did not
  colour the reading.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. **First**, the growth-shown convention at Q7 measures growth on the endpoints of the aggregate owner cash,
and owner cash in a retailer swings with inventory: the window of record gave 10.2% and the window one year later gave
34%, from the same business, because the later window starts at the FY2022 trough. The convention needs a rule for the
endpoints (the framework's own **[L2005-003]** supplies the principle but no procedure); this run used the window whose
endpoints were not aberrant and carried the other at the sovereign cap, stating both. **Second**, the five-year average
as the base understates a business that grows 10% a year by about two years of growth (the average sits near the FY2023
figure, $5,085M against $6,830M for FY2025 and $8,375M for FY2026); the growth carry compensates only in part, and the
convention does not say whether the average or the latest year is the base when the series is monotonic. The verdict
here does not turn on it (the price is double the range top on any base), but a closer case would. **Third**, the Q3
cap, "no rate that runs past the discount rate", is ambiguous for the ten-years-then-flat construction: the shown rate
of 10.2% exceeds the 5.66% discount rate but is not carried forever, so no infinity arises; this run read the cap as
the absurdity test and showed the stricter capped figure beside it. **Fourth**, the template's POSITION NOTE asks the
analyst to "check `PORTFOLIO.md`" while the dispatch brief's blind rule forbids opening it; the brief should say the
dispatcher fills that line, or the template should carry a blind-run form of it. One more, for the record: the brief's
"Reply with" asks for "the three reporting figures" in the canonical text and "the two reporting figures" in the brief as
sent; two are defined (the value range and the fair price), and two are reported.
